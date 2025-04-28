# Ürün Gereksinimleri Belgesi (PRD)

## Proje Genel Bakış
Bu belge, bir mobil uygulama için FastAPI tabanlı bir backend sisteminin gereksinimlerini özetlemektedir. Backend, kullanıcı yönetimi, batarya veri işleme, loglama ve ayar yönetimi gibi temel hizmetleri sağlayarak sağlam, ölçeklenebilir ve güvenli olacaktır.

## API Çerçevesi ve Sunucu
- **Çerçeve**: FastAPI
- **Sunucu**: Uvicorn
- **Ana URL**: `http://localhost:8000`

## Veritabanı
- **Tür**: PostgreSQL
- **ORM**: SQLAlchemy
- **Tablolar**:
  - **Kullanıcı**: `id`, `email` (benzersiz, zorunlu), `hashed_password`, `is_admin`
  - **BataryaVerisi**: `id`, `timestamp`, `voltage`, `current`, `temperature`, `soc` (Şarj Durumu), `soh` (Sağlık Durumu)
  - **LogGirdisi**: `id`, `timestamp`, `message`
  - **Ayar**: `id`, `key` (benzersiz), `value`
- **Çevresel Değişken**: `DATABASE_URL`

## Kullanıcı Yönetimi ve Kimlik Doğrulama
- **Endpoint'ler**:
  - `POST /users/register`: Kullanıcı kaydı
  - `POST /users/login`: Kullanıcı girişi
- **Şifre Güvenliği**: Şifreleri bcrypt kullanarak hash'le
- **Kimlik Doğrulama**: JWT (JSON Web Token)
  - Token oluşturma ve doğrulama fonksiyonları
  - Token'lar istek başlıklarında 'Bearer' formatında gönderilir

## API Endpoint'leri
- **Kullanıcı İşlemleri**:
  - `/users/register`: Yeni kullanıcı kaydı
  - `/users/login`: Kullanıcı girişi, başarılı girişte JWT token üretimi
- **Batarya Veri İşlemleri**:
  - `/battery`: (POST) Batarya verisi ekleme, (GET) En son batarya verisini çekme
  - `/battery/control`: Batarya veya cihaz kontrol komutlarının alınması
- **Log Yönetimi**:
  - `/logs`: Sistem loglarını döndürme (sayfalı listeleme)
- **Sistem Ayarları**:
  - `/settings`: Ayarların okunması ve güncellenmesi
- **JWT Kimlik Doğrulama**: Tüm korunan endpoint'lerde gereklidir

## Gerçek Zamanlı Veri İletişimi
- **WebSocket Desteği**:
  - Endpoint: `/ws/battery`
  - Bağlantıları kabul et ve gerçek zamanlı batarya verilerini veya kontrol mesajlarını ilet
  - İstemciler JWT token'ını WebSocket üzerinden gönderir (örneğin, URL sorgu parametresi ile)

## Çevresel Ayarlar ve Güvenlik
- **Çevresel Değişkenler**: Bir `.env` dosyası kullan (örneğin, `DATABASE_URL`, `SECRET_KEY`, `ALGORITHM`, `ACCESS_TOKEN_EXPIRE_MINUTES`)
- **CORS Middleware**: Farklı origin'lerden gelen istekleri kabul et (geliştirme aşamasında tüm origin'lere izin verilebilir)
- **HTTP Durum Kodları ve Mesajlar**: Giriş, yetkilendirme ve hata senaryoları için anlamlı kodlar ve mesajlar döndür (örneğin, 401 Yetkisiz, 404 Bulunamadı, 400 Hatalı İstek)

## Dokümantasyon ve Test
- **Dokümantasyon**: FastAPI'nin otomatik oluşturduğu Swagger/OpenAPI dokümantasyonunu kullan (`http://localhost:8000/docs`)
- **Modüler Dosya Yapısı**:
  - Ana dosya: `main.py`
  - Veritabanı bağlantısı: `database.py`
  - Modeller: `models.py`
  - Pydantic şemalar: `schemas.py`
  - CRUD işlemleri: `crud.py`
  - WebSocket işlemleri: `websocket.py`
  - Güvenlik ve konfigürasyon: `core/config.py` ve `core/security.py`
  - API rotaları: `routes/users.py`, `routes/battery.py`, `routes/logs.py`, `routes/settings.py`

## Hata Yönetimi ve Loglama
- **Global Hata Yönetimi**: Hataları global olarak yakala ve uygun hata mesajları döndür
- **Loglama Mekanizması**: Kritik işlemler için loglama yap; örneğin, her hatalı giriş denemesi veya donanımla ilgili bir hata `LogEntry` tablosuna kaydedilsin

## Kod Kalitesi
- Kodun okunabilir, modüler ve sürdürülebilir olmasını sağla. Her modül ve endpoint, bağımsız dosyalarda yer almalı ve tüm sistemi entegre bir şekilde çalışır hale getirmelidir. 