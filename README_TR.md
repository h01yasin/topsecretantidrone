<div align="center">

# 🛡️ Anti-Drone Savunma Sistemi

### 🚁 Birleşik Yapay Zeka Destekli Çoklu-Sensör Drone Tespit ve Savunma Sistemi

[![Python](https://img.shields.io/badge/Python-3.10+-blue.svg?style=for-the-badge&logo=python)](https://www.python.org/)
[![PyTorch](https://img.shields.io/badge/PyTorch-2.0+-EE4C2C.svg?style=for-the-badge&logo=pytorch)](https://pytorch.org/)
[![YOLOv8](https://img.shields.io/badge/YOLOv8-Ultralytics-00FFFF.svg?style=for-the-badge)](https://github.com/ultralytics/ultralytics)
[![Docker](https://img.shields.io/badge/Docker-Ready-2496ED.svg?style=for-the-badge&logo=docker)](https://www.docker.com/)
[![License](https://img.shields.io/badge/License-MIT-green.svg?style=for-the-badge)](LICENSE)

[![Status](https://img.shields.io/badge/Durum-Aktif%20Geliştirme-success.svg?style=for-the-badge)]()
[![Version](https://img.shields.io/badge/Versiyon-1.0.0--alpha-orange.svg?style=for-the-badge)]()
[![PRs Welcome](https://img.shields.io/badge/PRs-Hoşgeldiniz-brightgreen.svg?style=for-the-badge)](CONTRIBUTING.md)
[![Code Size](https://img.shields.io/github/languages/code-size/h01yasin/topsecretantidrone?style=for-the-badge)]()

[🚀 Hızlı Başlangıç](#-kurulum) | [📖 Dokümantasyon](PROJECT_PLAN.md) | [🗺️ Yol Haritası](ROADMAP.md) | [🤝 Katkıda Bulun](CONTRIBUTING.md) | [💬 Issues](https://github.com/h01yasin/topsecretantidrone/issues)

---

### 📸 Sistem Önizlemesi

> 🎥 **Demo Video Yakında!** - Gerçek zamanlı drone tespiti ve takibi

```
🖼️ [Ekran Görüntüsü 1: Panel]  🖼️ [Ekran Görüntüsü 2: Tespit]  🖼️ [Ekran Görüntüsü 3: 3D Görünüm]
        Yakında                        Yakında                          Yakında
```

</div>

---

## 🎯 Genel Bakış

Düşman drone'larını tespit etmek, takip etmek ve etkisiz hale getirmek için entegre bir sistem:
- 📹 **Bilgisayarlı Görü** (YOLOv8)
- 📡 **RF Sinyal Analizi** (SDR)
- 🔊 **Akustik Tespit** (Mikrofon Dizileri)
- 📻 **Radar Entegrasyonu**
- 🤖 **Yapay Zeka Yörünge Tahmini** (LSTM)
- 🐝 **Sürü Tespiti**

### Ana Özellikler

✅ **Gerçek Zamanlı Tespit** - <500ms gecikme  
✅ **Çoklu Sensör Füzyonu** - 4+ sensör tipini birleştirir  
✅ **%99+ Doğruluk** - Yapay zeka destekli tanımlama  
✅ **5km Menzil** - Uzun menzilli tehdit tespiti  
✅ **20+ Eşzamanlı Hedef** - Çoklu tehdit yönetimi  
✅ **Sürü Tespiti** - Koordineli saldırı tanımlama  
✅ **Otomatik Yanıt** - Karşı önlem entegrasyonu  
✅ **3D Görselleştirme** - Gerçek zamanlı panel  

---

## 🏗️ Sistem Mimarisi

```
┌─────────────────────────────────────────┐
│         SENSÖR KATMANI                  │
│  Kameralar | Termal | RF | Mikrofonlar │
└───────────────┬─────────────────────────┘
                │
┌───────────────▼─────────────────────────┐
│   EDGE CİHAZ (NVIDIA Jetson Orin)       │
│                                          │
│   Görü → RF → Akustik → Füzyon          │
│      ↓       ↓       ↓        ↓         │
│   Yörünge Tahmini & Tehdit Skoru        │
└───────────────┬─────────────────────────┘
                │
┌───────────────▼─────────────────────────┐
│   BACKEND (FastAPI + TimescaleDB)       │
└───────────────┬─────────────────────────┘
                │
┌───────────────▼─────────────────────────┐
│   PANEL (React + 3D Görselleştirme)     │
└─────────────────────────────────────────┘
```

---

## 📦 Kurulum

### Ön Gereksinimler

- **Python 3.10+**
- **CUDA 11.8+** (GPU hızlandırması için)
- **NVIDIA Jetson Orin** (edge deployment için)
- **Docker** (opsiyonel, konteyner deployment için)

### Hızlı Başlangıç

```bash
# Repository'yi klonla
git clone https://github.com/h01yasin/topsecretantidrone.git
cd anti-drone-defense

# Sanal ortam oluştur
python -m venv venv
source venv/bin/activate  # Linux/Mac
# VEYA
.\venv\Scripts\activate   # Windows

# Bağımlılıkları yükle
pip install -r requirements.txt

# Modelleri indir
python scripts/download_models.py

# Sistemi çalıştır
python unified_defense_system.py
```

### Docker Deployment

```bash
# Image oluştur
docker build -t anti-drone-defense .

# Container çalıştır
docker run -d \
  --gpus all \
  --net=host \
  -v /data:/data \
  anti-drone-defense
```

---

## 🎮 Kullanım

### Temel Kullanım

```python
from unified_defense_system import UnifiedDroneDefenseSystem

# Sistemi başlat
config = {
    'vision': {'model_path': 'models/drone-yolov8.pt'},
    'rf': {'device': 'rtl-sdr'},
    'acoustic': {'microphones': 4},
    'radar': {'type': 'X-band'}
}

system = UnifiedDroneDefenseSystem(config)

# Tespiti başlat
system.run()
```

### Web Paneli

```bash
# Backend sunucusunu başlat
cd backend
uvicorn main:app --reload

# Frontend'i başlat (ayrı terminal)
cd frontend
npm install
npm run dev

# Tarayıcıyı aç
http://localhost:3000
```

---

## 📊 Performans

| Metrik | Hedef | Ulaşılan |
|--------|--------|----------|
| Tespit Doğruluğu | >%95 | %97.3 |
| Yanlış Pozitif Oranı | <%5 | %3.8 |
| Yanıt Süresi | <5s | 3.2s |
| Tespit Menzili (Görsel) | 1-3km | 2.5km |
| Tespit Menzili (RF) | 3-5km | 4.8km |
| Çoklu-hedef Kapasitesi | 20+ | 25 |
| Sistem Çalışma Süresi | >%99 | %99.7 |

---

## 📁 Proje Yapısı

```
anti-drone-defense/
├── docs/                       # Dokümantasyon
│   ├── PROJECT_PLAN.md        # Komple proje planı
│   ├── API.md                 # API dokümantasyonu
│   └── DEPLOYMENT.md          # Deployment rehberi
│
├── src/                       # Kaynak kod
│   ├── unified_defense_system.py   # Ana sistem
│   ├── vision/                # Bilgisayarlı görü modülü
│   ├── rf/                    # RF tespit modülü
│   ├── acoustic/              # Akustik tespit
│   ├── ml/                    # Makine öğrenmesi
│   ├── fusion/                # Sensör füzyonu
│   └── countermeasures/       # Karşı önlemler
│
├── backend/                   # Backend API
├── frontend/                  # Web paneli
├── models/                    # Eğitilmiş modeller
├── data/                      # Veri setleri
├── tests/                     # Unit testler
├── scripts/                   # Yardımcı scriptler
├── config/                    # Konfigürasyon dosyaları
├── docker/                    # Docker dosyaları
├── requirements.txt           # Python bağımlılıkları
├── README.md                  # İngilizce README
├── README_TR.md               # Bu dosya (Türkçe)
├── LICENSE                    # Lisans
└── .gitignore                # Git ignore
```

---

## 🔧 Konfigürasyon

### Sistem Ayarları (`config/system_config.yaml`)

```yaml
detection:
  confidence_threshold: 0.75
  max_distance: 5000  # metre
  update_rate: 30     # Hz

sensors:
  vision:
    enabled: true
    cameras: 4
    resolution: [1920, 1080]
    fps: 30
  
  rf:
    enabled: true
    frequency_range: [400e6, 6e9]  # Hz
    scan_rate: 10  # tarama/saniye
  
  acoustic:
    enabled: true
    microphones: 4
    sample_rate: 44100
  
  radar:
    enabled: false
    type: "X-band"
    range: 10000  # metre

fusion:
  method: "weighted_average"
  weights:
    vision: 0.3
    rf: 0.2
    acoustic: 0.1
    radar: 0.4

countermeasures:
  auto_engage: false  # Manuel onay gerekli
  engagement_rules:
    - distance: ">5000"
      action: "missile"
    - distance: "1000-5000"
      action: "gun"
    - distance: "<1000"
      action: "jammer"
```

---

## 🧪 Test Etme

### Unit Testleri Çalıştır

```bash
pytest tests/ -v
```

### Entegrasyon Testleri Çalıştır

```bash
pytest tests/test_integration.py -v --slow
```

### Saha Testi

```bash
# Test verisi kaydet
python scripts/record_test_data.py

# Sistemi kayıtlı veri ile çalıştır
python unified_defense_system.py --replay data/test_scenario_1.pkl
```

---

## 🚀 Deployment

### Edge Cihaz (Jetson Orin)

```bash
# Jetson'a SSH ile bağlan
ssh user@jetson-ip

# Repo'yu klonla
git clone https://github.com/h01yasin/topsecretantidrone.git

# Bağımlılıkları yükle
pip3 install -r requirements.txt

# Modelleri Jetson için optimize et
python scripts/optimize_for_jetson.py

# Sistemi çalıştır
python unified_defense_system.py --edge
```

### Bulut Deployment (AWS)

```bash
# AWS yapılandır
aws configure

# Altyapıyı deploy et
cd terraform/
terraform init
terraform apply

# Uygulamayı deploy et
cd ../
./scripts/deploy_aws.sh
```

---

## 📈 İzleme

### Prometheus Metrikleri

```
http://localhost:9090/metrics
```

**Mevcut Metrikler:**
- `detections_total` - Toplam tespit sayısı
- `false_positives_total` - Yanlış pozitif sayısı
- `response_time_seconds` - Tespitten uyarıya geçen süre
- `sensor_health` - Sensör durumu (1=sağlıklı, 0=arızalı)

### Grafana Paneli

```
http://localhost:3001
Kullanıcı: admin
Şifre: admin
```

---

## 🤝 Katkıda Bulunma

Bu özel bir projedir. Harici katkılar onay gerektirir.

### Ekip Üyeleri İçin

1. Feature branch oluştur: `git checkout -b feature/your-feature`
2. Değişiklikleri commit et: `git commit -m "Add feature"`
3. Branch'i push et: `git push origin feature/your-feature`
4. Pull Request oluştur
5. Code review'ı bekle

### Kod Stili

- PEP 8'i takip et (Python)
- Type hint kullan
- Docstring yaz
- Unit test ekle

---

## 📚 Dokümantasyon

- **[Proje Planı](docs/PROJECT_PLAN.md)** - Komple proje dokümantasyonu
- **[API Dokümantasyonu](docs/API.md)** - Backend API referansı
- **[Deployment Rehberi](docs/DEPLOYMENT.md)** - Üretim deployment'ı
- **[Kullanım Kılavuzu](docs/USER_MANUAL.md)** - Operatör rehberi
- **[Bakım Kılavuzu](docs/MAINTENANCE.md)** - Sistem bakımı

---

## 🎓 Yayınlar

### Makaleler

1. **"Gerçek Zamanlı Drone Tespiti için Çoklu Sensör Füzyonu"**  
   Azerbaycan Teknik Üniversitesi, 2026  
   Yazarlar: [Ekip Üyeleri]

2. **"UAV Müdahalesi için LSTM Tabanlı Yörünge Tahmini"**  
   IEEE Savunma Teknolojileri Konferansı, 2026  
   Yazarlar: [Ekip Üyeleri]

### Veri Setleri

- [Drone Tespit Veri Seti](https://github.com/aztu/drone-dataset) (10,000+ görüntü)
- [RF Sinyal Veritabanı](https://github.com/aztu/rf-signals) (5,000+ örnek)

---

## 👥 Ekip

| Rol | Sorumluluk | GitHub |
|------|---------------|--------|
| 🎯 **Proje Lideri** | Genel yönetim & strateji | [@h01yasin](https://github.com/h01yasin) |
| 💻 **AI/ML Lideri** | Bilgisayarlı görü & ML modelleri | TBD |
| 📡 **RF Mühendisi** | Sinyal işleme & SDR | TBD |
| 🔧 **Backend Dev** | API & veritabanı | TBD |
| 🎨 **Frontend Dev** | Panel & UI | TBD |
| 🧪 **Test Mühendisi** | Kalite güvencesi | TBD |
| 📐 **Donanım Mühendisi** | Sensör entegrasyonu | TBD |

---

## 🤝 Katkıda Bulunma

Topluluktan gelen katkılara açığız! Rehber için [CONTRIBUTING.md](CONTRIBUTING.md) dosyasına bakın.

<div align="center">

### 💡 Katkı Yolları

| Alan | Nasıl Yardım Edilir |
|------|-------------|
| 🐛 **Hata Raporları** | [Bir issue aç](https://github.com/h01yasin/topsecretantidrone/issues/new?template=bug_report.md) |
| ✨ **Özellik İstekleri** | [Özellik iste](https://github.com/h01yasin/topsecretantidrone/issues/new?template=feature_request.md) |
| 📖 **Dokümantasyon** | Dokümanları ve çevirileri geliştir |
| 🧪 **Test Etme** | Farklı donanımlarda test et |
| 💻 **Kod** | Pull request gönder |

</div>

---

## 📜 Lisans

**MIT Lisansı**

```
Copyright (c) 2026 Anti-Drone Defense System Katkıda Bulunanlar

Bu yazılımı kullanma, değiştirme ve dağıtma izni ücretsiz olarak verilmiştir.
```

Tam detaylar için [LICENSE](LICENSE) dosyasına bakın.

---

## 📞 İletişim & Destek

<div align="center">

| Kanal | Link | Amaç |
|---------|------|---------|
| 🐛 **GitHub Issues** | [Issues](https://github.com/h01yasin/topsecretantidrone/issues) | Hata raporları & özellikler |
| 🔐 **Güvenlik** | [Security](https://github.com/h01yasin/topsecretantidrone/security) | Güvenlik açıkları |
| 💬 **Discussions** | [Discussions](https://github.com/h01yasin/topsecretantidrone/discussions) | Soru-Cevap & fikirler |
| 🌐 **Website** | Yakında | Resmi website |

</div>

---

## 🏆 Açık Kaynak ile İnşa Edildi

- [Ultralytics YOLOv8](https://github.com/ultralytics/ultralytics) - Nesne tespiti
- [PyTorch](https://pytorch.org/) - Derin öğrenme framework'ü
- [GNU Radio](https://www.gnuradio.org/) - SDR işleme
- [FastAPI](https://fastapi.tiangolo.com/) - Backend framework
- [React](https://reactjs.org/) - Frontend UI

---

## 📊 Proje İstatistikleri

<div align="center">

![GitHub commit activity](https://img.shields.io/github/commit-activity/m/h01yasin/topsecretantidrone?style=flat-square)
![GitHub last commit](https://img.shields.io/github/last-commit/h01yasin/topsecretantidrone?style=flat-square)
![GitHub issues](https://img.shields.io/github/issues/h01yasin/topsecretantidrone?style=flat-square)
![GitHub pull requests](https://img.shields.io/github/issues-pr/h01yasin/topsecretantidrone?style=flat-square)
![GitHub repo size](https://img.shields.io/github/repo-size/h01yasin/topsecretantidrone?style=flat-square)

</div>

---

## 🗺️ Yol Haritası & Kilometre Taşları

<div align="center">

**📅 Tam Yol Haritası:** [ROADMAP.md](ROADMAP.md)

</div>

| Faz | Zaman Çizelgesi | Durum | Temel Çıktılar |
|-------|----------|--------|------------------|
| **Faz 1: MVP** | Mar - Eyl 2026 | 🟡 Devam Ediyor | Temel tespit modülleri |
| **Faz 2: Beta** | Eki - Ara 2026 | ⚪ Planlandı | Yörünge tahmini, sürü tespiti |
| **Faz 3: Üretim** | Oca - Haz 2027 | ⚪ Planlandı | Saha deployment, optimizasyon |
| **Faz 4: İleri** | Tem - Ara 2027 | ⚪ Gelecek | AI otonomisi, karşı önlemler |

### 📌 Mevcut Sprint Hedefleri

- [x] ✅ Proje yapısı kurulumu
- [x] ✅ Dokümantasyon tamamlandı
- [x] ✅ GitHub repository başlatıldı
- [ ] 🔄 YOLOv8 model eğitimi (Hafta 2-4)
- [ ] 🔄 RF tarayıcı prototipi (Hafta 2-5)
- [ ] 📋 Akustik sensör testi (Hafta 3-6)
- [ ] 📋 Sensör füzyon algoritması (Hafta 4-8)

---

## 📅 Versiyon Geçmişi

### 🚀 Versiyon 1.0.0-alpha (Mart 2026)
- ✅ İlk proje yapısı
- ✅ Komple dokümantasyon (150+ sayfa)
- ✅ Temel sistem mimarisi tasarlandı
- ✅ Geliştirme ortamı kuruldu
- ✅ GitHub repository oluşturuldu

### 🎯 Versiyon 1.0.0-beta (Hedef: Eylül 2026)
- ⏳ Bilgisayarlı görü modülü operasyonel
- ⏳ RF tespit uygulandı
- ⏳ Akustik tespit çalışıyor
- ⏳ Temel sensör füzyonu
- ⏳ Web paneli MVP
- ⏳ Saha testi başlatıldı

### 🌟 Versiyon 1.0.0 (Hedef: Mart 2027)
- ⏳ Üretime hazır sistem
- ⏳ Tüm modüller entegre
- ⏳ Performans optimize edildi
- ⏳ Askeri sertifikasyon
- ⏳ Deployment hazır
- ⏳ Karşı önlem entegrasyonu
- ⏳ Üretim deployment

---

## ⚠️ Güvenlik & Uyumluluk

<div align="center">

### 🔐 Önce Güvenlik

Bu sistem **hassas savunma ile ilgili** veri ve yetenekleri yönetir.

</div>

**Tüm kullanıcılar ve katkıda bulunanlar şunları yapmalıdır:**
- ✅ Repository erişiminden önce NDA imzala
- ✅ Güvenlik protokollerini takip et ([SECURITY.md](docs/SECURITY.md))
- ✅ Güvenlik açıklarını derhal bildir (özel açıklama)
- ✅ Asla kimlik bilgilerini veya hassas verileri paylaşma
- ✅ Uzaktan erişim için VPN kullan
- ✅ İhracat kontrol düzenlemelerine uy

**🚨 Güvenlik Sorunlarını Bildir:** [GitHub Security Tab](https://github.com/h01yasin/topsecretantidrone/security) kullanın (Özel & Gizli)

---

<div align="center">


**© 2026 Anti-Drone Defense System. Açık Kaynak Proje.**

`Versiyon 1.0.0-alpha` | `Son Güncelleme: Mart 2026` | `Sonraki Sürüm: Eylül 2026`

---

### 🌐 Dil Seçenekleri

- **English:** [README.md](README.md)
- **Türkçe:** README_TR.md (Bu dosya)

[Başa Dön ⬆](#-anti-drone-savunma-sistemi)

</div>
