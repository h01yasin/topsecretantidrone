"""
UNIFIED ANTI-DRONE DEFENSE SYSTEM
==================================

Complete integration of 6 detection modules:
1. Computer Vision Detection (YOLOv8)
2. RF Signal Analysis (SDR)
3. Acoustic Detection (Microphone Array)
4. Radar Integration
5. Trajectory Prediction (LSTM)
6. Swarm Detection

Author: AzTU Defense Project Team
Date: March 2026
License: Proprietary
"""

import cv2
import numpy as np
import torch
from ultralytics import YOLO
from scipy import signal
import librosa
from dataclasses import dataclass
from typing import List, Dict, Tuple, Optional
from datetime import datetime
import json
import logging
from collections import deque
import threading
import queue

# Setup logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)


@dataclass
class DroneDetection:
    """Single drone detection from any sensor"""
    id: str
    timestamp: datetime
    position: Tuple[float, float, float]  # x, y, z (meters)
    velocity: Tuple[float, float, float]  # vx, vy, vz (m/s)
    confidence: float  # 0.0 - 1.0
    sensor_type: str  # 'vision', 'rf', 'acoustic', 'radar'
    drone_type: Optional[str] = None
    threat_level: int = 0  # 0-10
    frequency: Optional[float] = None  # For RF detections


class UnifiedDroneDefenseSystem:
    """
    Complete anti-drone system integrating all detection modules
    """
    
    def __init__(self, config: Dict):
        logger.info("🚀 Initializing Unified Defense System...")
        
        # Configuration
        self.config = config
        
        # Initialize subsystems
        self.vision_detector = VisionDetector(config.get('vision', {}))
        self.rf_detector = RFDetector(config.get('rf', {}))
        self.acoustic_detector = AcousticDetector(config.get('acoustic', {}))
        self.radar = RadarSystem(config.get('radar', {}))
        self.trajectory_predictor = TrajectoryPredictor()
        self.swarm_detector = SwarmDetector()
        self.fusion_engine = SensorFusion()
        self.countermeasures = CounterMeasureSystem(config.get('counter', {}))
        
        # Tracking state
        self.tracked_drones = {}
        self.threat_history = deque(maxlen=1000)
        self.detection_queue = queue.Queue()
        
        # Threading
        self.running = False
        self.threads = []
        
        logger.info("✅ System Ready!")
    
    def start(self):
        """Start all detection threads"""
        logger.info("👁️  Starting detection system...")
        self.running = True
        
        # Start sensor threads
        self.threads = [
            threading.Thread(target=self._vision_loop, name="VisionThread"),
            threading.Thread(target=self._rf_loop, name="RFThread"),
            threading.Thread(target=self._acoustic_loop, name="AcousticThread"),
            threading.Thread(target=self._radar_loop, name="RadarThread"),
            threading.Thread(target=self._processing_loop, name="ProcessingThread"),
        ]
        
        for thread in self.threads:
            thread.daemon = True
            thread.start()
        
        logger.info("✅ All detection threads started")
    
    def stop(self):
        """Stop all detection threads"""
        logger.info("🛑 Stopping detection system...")
        self.running = False
        
        for thread in self.threads:
            thread.join(timeout=5.0)
        
        logger.info("✅ System stopped")
    
    def _vision_loop(self):
        """Vision detection thread"""
        while self.running:
            try:
                detections = self.vision_detector.detect()
                for det in detections:
                    self.detection_queue.put(det)
            except Exception as e:
                logger.error(f"Vision error: {e}")
    
    def _rf_loop(self):
        """RF detection thread"""
        while self.running:
            try:
                detections = self.rf_detector.scan()
                for det in detections:
                    self.detection_queue.put(det)
            except Exception as e:
                logger.error(f"RF error: {e}")
    
    def _acoustic_loop(self):
        """Acoustic detection thread"""
        while self.running:
            try:
                detections = self.acoustic_detector.listen()
                for det in detections:
                    self.detection_queue.put(det)
            except Exception as e:
                logger.error(f"Acoustic error: {e}")
    
    def _radar_loop(self):
        """Radar detection thread"""
        while self.running:
            try:
                detections = self.radar.scan()
                for det in detections:
                    self.detection_queue.put(det)
            except Exception as e:
                logger.error(f"Radar error: {e}")
    
    def _processing_loop(self):
        """Main processing thread - fuses data and makes decisions"""
        detection_buffer = []
        last_process_time = datetime.now()
        
        while self.running:
            try:
                # Collect detections for 1 second
                timeout = 0.1
                try:
                    det = self.detection_queue.get(timeout=timeout)
                    detection_buffer.append(det)
                except queue.Empty:
                    pass
                
                # Process every second
                if (datetime.now() - last_process_time).total_seconds() >= 1.0:
                    if detection_buffer:
                        self._process_detections(detection_buffer)
                        detection_buffer = []
                    last_process_time = datetime.now()
                    
            except Exception as e:
                logger.error(f"Processing error: {e}")
    
    def _process_detections(self, detections: List[DroneDetection]):
        """Process a batch of detections"""
        logger.info(f"📊 Processing {len(detections)} detections")
        
        # 1. Sensor fusion
        confirmed_threats = self.fusion_engine.fuse(detections)
        logger.info(f"✅ {len(confirmed_threats)} confirmed threats")
        
        # 2. Track drones
        tracked_threats = self._update_tracking(confirmed_threats)
        
        # 3. Detect swarms
        swarm_analysis = self.swarm_detector.analyze(tracked_threats)
        if swarm_analysis['is_swarm']:
            logger.warning(f"⚠️  SWARM DETECTED: {swarm_analysis['count']} drones")
        
        # 4. Predict trajectories
        predictions = self._predict_trajectories(tracked_threats)
        
        # 5. Assess threats
        prioritized_threats = self._assess_threats(predictions, swarm_analysis)
        
        # 6. Engage counter-measures
        if prioritized_threats:
            self._engage_countermeasures(prioritized_threats)
        
        # 7. Log
        self._log_threats(prioritized_threats)
    
    def _update_tracking(self, detections: List[DroneDetection]) -> List[DroneDetection]:
        """Update tracking for detected drones"""
        # Simple tracking - match by proximity
        tracked = []
        
        for det in detections:
            # Find matching tracked drone
            matched = False
            for drone_id, drone in self.tracked_drones.items():
                dist = np.linalg.norm(
                    np.array(det.position) - np.array(drone.position)
                )
                if dist < 100:  # Within 100m, assume same drone
                    # Update tracking
                    drone.position = det.position
                    drone.velocity = det.velocity
                    drone.timestamp = det.timestamp
                    tracked.append(drone)
                    matched = True
                    break
            
            if not matched:
                # New drone
                det.id = f"drone_{len(self.tracked_drones)}"
                self.tracked_drones[det.id] = det
                tracked.append(det)
                logger.warning(f"🆕 NEW DRONE DETECTED: {det.id}")
        
        return tracked
    
    def _predict_trajectories(self, threats: List[DroneDetection]) -> Dict:
        """Predict future paths"""
        predictions = {}
        
        for threat in threats:
            future_path = self.trajectory_predictor.predict(
                current_pos=threat.position,
                velocity=threat.velocity,
                drone_type=threat.drone_type,
                time_horizon=30
            )
            
            predictions[threat.id] = {
                'path': future_path,
                'eta': self._estimate_time_to_target(future_path),
                'impact_zone': self._estimate_impact_zone(future_path)
            }
        
        return predictions
    
    def _assess_threats(self, predictions: Dict, swarm_info: Dict) -> List[Dict]:
        """Prioritize threats"""
        threats = []
        
        for drone_id, pred in predictions.items():
            if drone_id not in self.tracked_drones:
                continue
            
            drone = self.tracked_drones[drone_id]
            threat_score = 0.0
            
            # Distance to target
            distance = np.linalg.norm(drone.position[:2])  # x, y distance
            threat_score += (5000 - distance) / 50  # Closer = higher
            
            # Speed
            speed = np.linalg.norm(drone.velocity)
            threat_score += speed * 2
            
            # Altitude (low = more dangerous)
            altitude = drone.position[2]
            if altitude < 100:
                threat_score += 50
            
            # Swarm bonus
            if swarm_info['is_swarm'] and drone_id in swarm_info.get('members', []):
                threat_score += 100
            
            # ETA
            if pred['eta'] < 60:  # Less than 1 minute
                threat_score += 100
            
            threats.append({
                'drone_id': drone_id,
                'drone': drone,
                'threat_score': threat_score,
                'prediction': pred,
                'priority': self._get_priority_level(threat_score)
            })
        
        # Sort by threat score
        threats.sort(key=lambda x: x['threat_score'], reverse=True)
        
        return threats
    
    def _get_priority_level(self, score: float) -> str:
        """Convert threat score to priority level"""
        if score > 200:
            return 'CRITICAL'
        elif score > 150:
            return 'HIGH'
        elif score > 100:
            return 'MEDIUM'
        else:
            return 'LOW'
    
    def _engage_countermeasures(self, threats: List[Dict]):
        """Engage appropriate counter-measures"""
        for threat in threats[:3]:  # Top 3 threats only
            if threat['priority'] in ['CRITICAL', 'HIGH']:
                logger.warning(f"⚠️  ENGAGING THREAT: {threat['drone_id']}")
                logger.warning(f"   Priority: {threat['priority']}")
                logger.warning(f"   Threat Score: {threat['threat_score']:.1f}")
                
                drone = threat['drone']
                distance = np.linalg.norm(drone.position[:2])
                
                # Select counter-measure based on distance
                if distance > 5000:
                    self.countermeasures.launch_missile(drone.position)
                elif distance > 1000:
                    self.countermeasures.engage_gun(drone.position)
                elif distance > 500:
                    if drone.frequency:
                        self.countermeasures.jam_signal(drone.frequency, 100)
                else:
                    self.countermeasures.fire_net(drone.position)
    
    def _estimate_time_to_target(self, path: np.ndarray) -> float:
        """Estimate time until drone reaches target (0, 0, 0)"""
        if len(path) == 0:
            return float('inf')
        
        # Find when path crosses target zone (within 100m)
        for i, pos in enumerate(path):
            if np.linalg.norm(pos[:2]) < 100:
                return i  # seconds
        
        return float('inf')
    
    def _estimate_impact_zone(self, path: np.ndarray) -> Tuple[float, float]:
        """Estimate where drone will land"""
        if len(path) == 0:
            return (0.0, 0.0)
        
        # Last predicted position
        return (path[-1][0], path[-1][1])
    
    def _log_threats(self, threats: List[Dict]):
        """Log threats to history"""
        for threat in threats:
            self.threat_history.append({
                'timestamp': datetime.now().isoformat(),
                'drone_id': threat['drone_id'],
                'priority': threat['priority'],
                'threat_score': threat['threat_score'],
                'position': threat['drone'].position
            })
    
    def get_status(self) -> Dict:
        """Get current system status"""
        return {
            'active': self.running,
            'tracked_drones': len(self.tracked_drones),
            'total_threats': len(self.threat_history),
            'threads_alive': sum(t.is_alive() for t in self.threads),
        }


# =====================================================
# 1. VISION DETECTOR
# =====================================================

class VisionDetector:
    """Computer vision based drone detection using YOLOv8"""
    
    def __init__(self, config: Dict):
        self.config = config
        
        # Load YOLO model
        model_path = config.get('model_path', 'yolov8n.pt')
        self.model = YOLO(model_path)
        
        # Cameras
        self.cameras = []
        for cam_config in config.get('cameras', []):
            try:
                cap = cv2.VideoCapture(cam_config['source'])
                if cap.isOpened():
                    self.cameras.append({
                        'capture': cap,
                        'position': cam_config.get('position', (0, 0, 10)),
                        'fov': cam_config.get('fov', 90)
                    })
                    logger.info(f"📹 Camera {cam_config['source']} initialized")
            except Exception as e:
                logger.error(f"Failed to open camera {cam_config['source']}: {e}")
        
        if not self.cameras:
            logger.warning("⚠️  No cameras available, using dummy data")
    
    def detect(self) -> List[DroneDetection]:
        """Detect drones in camera feeds"""
        detections = []
        
        for idx, cam in enumerate(self.cameras):
            ret, frame = cam['capture'].read()
            if not ret:
                continue
            
            # Run YOLO detection
            results = self.model(frame, conf=0.7, verbose=False)
            
            for box in results[0].boxes:
                x1, y1, x2, y2 = box.xyxy[0].cpu().numpy()
                confidence = float(box.conf[0])
                
                # Estimate 3D position (simplified)
                position_3d = self._pixel_to_3d(
                    (x1 + x2) / 2, (y1 + y2) / 2,
                    cam['position'],
                    cam['fov'],
                    frame.shape
                )
                
                # Estimate velocity (would need tracking in real system)
                velocity = (0.0, 0.0, 0.0)
                
                detection = DroneDetection(
                    id=f"vision_{idx}_{datetime.now().timestamp()}",
                    timestamp=datetime.now(),
                    position=position_3d,
                    velocity=velocity,
                    confidence=confidence,
                    sensor_type='vision'
                )
                
                detections.append(detection)
        
        return detections
    
    def _pixel_to_3d(self, px: float, py: float, cam_pos: Tuple,
                     fov: float, frame_shape: Tuple) -> Tuple[float, float, float]:
        """Convert pixel coordinates to 3D position (simplified)"""
        # This is a simplified version - real implementation needs camera calibration
        height, width = frame_shape[:2]
        
        # Assume distance based on pixel size (rough estimate)
        distance = 1000  # meters (would calculate from object size)
        
        # Convert pixel to angle
        angle_x = (px / width - 0.5) * fov
        angle_y = (py / height - 0.5) * fov
        
        # Convert to 3D
        x = cam_pos[0] + distance * np.sin(np.radians(angle_x))
        y = cam_pos[1] + distance * np.cos(np.radians(angle_x))
        z = cam_pos[2] + distance * np.tan(np.radians(angle_y))
        
        return (x, y, max(z, 0))


# =====================================================
# 2. RF DETECTOR
# =====================================================

class RFDetector:
    """Radio Frequency signal detection"""
    
    def __init__(self, config: Dict):
        self.config = config
        
        # Known drone frequencies (Hz)
        self.drone_signatures = {
            'DJI': [2.4e9, 5.8e9],
            'Shahed-136': [433e6, 915e6],
            'Generic': [900e6, 1.2e9, 2.4e9, 5.8e9]
        }
        
        # SDR initialization (simulated for now)
        self.sdr_available = False
        try:
            # from rtlsdr import RtlSdr
            # self.sdr = RtlSdr()
            # self.sdr_available = True
            logger.info("📡 RF detector initialized (simulated)")
        except Exception as e:
            logger.warning(f"⚠️  SDR not available: {e}")
    
    def scan(self) -> List[DroneDetection]:
        """Scan RF spectrum for drone signals"""
        detections = []
        
        # Simulated detection for demonstration
        # In real system, would scan frequencies and detect signals
        
        return detections


# =====================================================
# 3. ACOUSTIC DETECTOR
# =====================================================

class AcousticDetector:
    """Microphone array for sound-based detection"""
    
    def __init__(self, config: Dict):
        self.config = config
        
        # Microphone initialization (simulated)
        logger.info("🔊 Acoustic detector initialized (simulated)")
        
        # Load drone sound signatures
        self.drone_sounds = {}
    
    def listen(self) -> List[DroneDetection]:
        """Listen for drone sounds"""
        detections = []
        
        # Simulated detection
        # In real system, would analyze audio from microphone array
        
        return detections


# =====================================================
# 4. RADAR SYSTEM
# =====================================================

class RadarSystem:
    """Radar for drone tracking"""
    
    def __init__(self, config: Dict):
        self.config = config
        logger.info("📻 Radar system initialized (simulated)")
    
    def scan(self) -> List[DroneDetection]:
        """Radar scan"""
        detections = []
        
        # Simulated detection
        # In real system, would interface with radar hardware
        
        return detections


# =====================================================
# 5. TRAJECTORY PREDICTOR
# =====================================================

class TrajectoryPredictor:
    """Predict drone future path using physics and ML"""
    
    def __init__(self):
        # In real system, would load trained LSTM model
        logger.info("🎯 Trajectory predictor initialized")
    
    def predict(self, current_pos: Tuple, velocity: Tuple,
                drone_type: Optional[str], time_horizon: int) -> np.ndarray:
        """Predict future trajectory"""
        # Simple physics-based prediction
        path = []
        pos = np.array(current_pos)
        vel = np.array(velocity)
        
        for t in range(time_horizon):
            # Simple constant velocity model
            # Real system would use LSTM + physics
            pos = pos + vel
            path.append(pos.copy())
        
        return np.array(path)


# =====================================================
# 6. SWARM DETECTOR
# =====================================================

class SwarmDetector:
    """Detect coordinated drone swarms"""
    
    def __init__(self):
        self.swarm_threshold = 3
        logger.info("🐝 Swarm detector initialized")
    
    def analyze(self, drones: List[DroneDetection]) -> Dict:
        """Check if drones are coordinated"""
        if len(drones) < self.swarm_threshold:
            return {'is_swarm': False}
        
        # Check formation (simplified)
        positions = np.array([d.position for d in drones])
        
        # Calculate position variance
        variance = np.var(positions, axis=0).sum()
        
        # Low variance = tight formation = potential swarm
        is_swarm = variance < 100000  # within 300m of each other
        
        if is_swarm:
            return {
                'is_swarm': True,
                'count': len(drones),
                'members': [d.id for d in drones],
                'formation_type': 'cluster',
                'threat_level': 'CRITICAL'
            }
        
        return {'is_swarm': False}


# =====================================================
# SENSOR FUSION
# =====================================================

class SensorFusion:
    """Combine data from multiple sensors"""
    
    def fuse(self, detections: List[DroneDetection]) -> List[DroneDetection]:
        """Fuse multiple sensor readings"""
        if not detections:
            return []
        
        # Simple fusion - cluster by proximity
        confirmed = []
        used = set()
        
        for i, det1 in enumerate(detections):
            if i in used:
                continue
            
            # Find nearby detections
            cluster = [det1]
            for j, det2 in enumerate(detections):
                if i != j and j not in used:
                    dist = np.linalg.norm(
                        np.array(det1.position) - np.array(det2.position)
                    )
                    if dist < 200:  # Within 200m
                        cluster.append(det2)
                        used.add(j)
            
            # If multiple sensors agree, high confidence
            if len(cluster) >= 2:
                fused = self._fuse_cluster(cluster)
                confirmed.append(fused)
        
        return confirmed
    
    def _fuse_cluster(self, cluster: List[DroneDetection]) -> DroneDetection:
        """Fuse a cluster of detections"""
        # Weighted average
        weights = {
            'vision': 0.3,
            'rf': 0.2,
            'acoustic': 0.1,
            'radar': 0.4
        }
        
        total_weight = sum(weights.get(d.sensor_type, 0.1) for d in cluster)
        
        avg_pos = sum(
            np.array(d.position) * weights.get(d.sensor_type, 0.1)
            for d in cluster
        ) / total_weight
        
        # Use best velocity estimate (usually radar)
        best_vel = cluster[0].velocity
        for d in cluster:
            if d.sensor_type == 'radar':
                best_vel = d.velocity
                break
        
        return DroneDetection(
            id=f"fused_{cluster[0].timestamp.timestamp()}",
            timestamp=datetime.now(),
            position=tuple(avg_pos),
            velocity=best_vel,
            confidence=min(0.95, np.mean([d.confidence for d in cluster]) + 0.2),
            sensor_type='fused',
            drone_type=cluster[0].drone_type
        )


# =====================================================
# COUNTER-MEASURE SYSTEM
# =====================================================

class CounterMeasureSystem:
    """Execute counter-measures against threats"""
    
    def __init__(self, config: Dict):
        self.config = config
        logger.info("🛡️  Counter-measure system initialized")
    
    def launch_missile(self, target: Tuple):
        """Fire missile at target (simulated)"""
        logger.critical(f"🚀 MISSILE LAUNCH: Target {target}")
        # In real system, would interface with missile launcher
    
    def engage_gun(self, target: Tuple):
        """Engage gun/laser system (simulated)"""
        logger.warning(f"🔫 GUN ENGAGED: Target {target}")
        # In real system, would aim and fire
    
    def jam_signal(self, frequency: float, power: float):
        """RF jamming (simulated)"""
        logger.warning(f"📡 JAMMING: {frequency/1e6:.1f} MHz @ {power}W")
        # In real system, would transmit interference
    
    def fire_net(self, target: Tuple):
        """Net gun to capture drone (simulated)"""
        logger.warning(f"🕸️  NET LAUNCHED: Target {target}")
        # In real system, would fire net gun


# =====================================================
# MAIN FUNCTION
# =====================================================

def main():
    """Run the unified defense system"""
    
    # Configuration
    config = {
        'vision': {
            'model_path': 'yolov8n.pt',  # Will download if not present
            'cameras': [
                {'source': 0, 'position': (0, 0, 10), 'fov': 90},
            ]
        },
        'rf': {
            'device': 'rtl-sdr',
        },
        'acoustic': {
            'microphones': []
        },
        'radar': {
            'type': 'simulated'
        },
        'counter': {
            'enabled': True
        }
    }
    
    # Create system
    system = UnifiedDroneDefenseSystem(config)
    
    # Start detection
    system.start()
    
    logger.info("=" * 60)
    logger.info("🛡️  UNIFIED ANTI-DRONE DEFENSE SYSTEM ACTIVE")
    logger.info("=" * 60)
    logger.info("Press Ctrl+C to stop")
    logger.info("=" * 60)
    
    try:
        # Run indefinitely
        import time
        while True:
            time.sleep(10)
            status = system.get_status()
            logger.info(f"📊 Status: {status}")
    
    except KeyboardInterrupt:
        logger.info("\n🛑 Shutdown requested")
        system.stop()
        logger.info("✅ System stopped successfully")


if __name__ == "__main__":
    main()
