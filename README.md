# Özen Metalurji: yeni web sitesi

Özen Metalurji (ozenmetalurji.com.tr) için hazırlanmış, SEO, AEO ve GEO uyumlu kurumsal site.

- **Canlı önizleme (GitHub Pages):** `https://kocistrasit.github.io/ozen-metalurji/`
- **WordPress teması (Natro'ya yüklenecek):** [`wordpress/ozen-metalurji-tema.zip`](wordpress/ozen-metalurji-tema.zip)
- **Rakip analizi:** [`docs/RAKIP-ANALIZI.md`](docs/RAKIP-ANALIZI.md)

> Önizleme **arama motorlarına kapalıdır**: her sayfada `noindex, nofollow` etiketi var ve `robots.txt` tüm siteyi `Disallow: /` ile kapatır. WordPress temasında da "Önizleme modu" varsayılan olarak açıktır.

## İçerik (22 sayfa)

Ana sayfa · Hakkımızda · Tesislerimiz ve Makine Parkuru · Kalite ve Laboratuvar · Üretim Süreci · Sektörler ·
Döküm Hizmetleri (+6: alüminyum kum, alüminyum kokil, pirinç, bronz, zamak, anot) · SSS · Bilgi Merkezi (+4 rehber) · İletişim ve Teklif · KVKK · 404

Bilgiler eski siteden (tarihçe, makine parkuru, adresler, telefonlar), Google Haritalar kayıtlarından ve Döküm Makina'nın XRF haberinden alındı. Görseller eski sitenin ürün galerisinden indirilir (`scripts/gorselleri-indir.sh`).

## Natro'da WordPress'e kurulum

1. Natro panelinden WordPress kurun (PHP 7.4 veya üstü).
2. WordPress yönetiminde **Görünüm > Temalar > Yeni ekle > Tema yükle** adımlarıyla `ozen-metalurji-tema.zip` dosyasını yükleyip **Etkinleştir**'e basın.
3. Tema etkinleştiğinde otomatik olarak şunları yapar:
   - 22 sayfayı doğru adres yapısıyla oluşturur (ör. `/hizmetler/bronz-dokum/`),
   - Ana sayfayı ayarlar ve kalıcı bağlantıları `/%postname%/` yapar,
   - Örnek "Sample Page" ve "Hello World" içeriklerini çöp kutusuna taşır,
   - **Önizleme modunu açar** (site Google'a kapalı kalır).
4. Teklif formu e-postaları `info@ozenmetalurji.com.tr` adresine gider. Natro'da e-postaların güvenilir ulaşması için bir SMTP eklentisi (ör. *WP Mail SMTP*) ile kurumsal e-posta hesabını tanımlamanız önerilir.

### Yayına alırken (Google'a açma)

1. **Ayarlar > Özen Metalurji** ekranında **"Önizleme modu"** kutusunu kaldırıp kaydedin.
   Bu adım `noindex` etiketini kaldırır, `robots.txt` dosyasını açar (yapay zekâ botlarına da izin verir) ve `/wp-sitemap.xml` site haritasını etkinleştirir.
2. SSL'i (HTTPS) Natro panelinden açın.
3. Google Search Console'a siteyi ekleyip `https://www.ozenmetalurji.com.tr/wp-sitemap.xml` adresini gönderin.
4. Eski sitedeki adresleri yeni sayfalara 301 ile yönlendirin (`.htaccess`):

```
Redirect 301 /tr/hakkimizda /hakkimizda/
Redirect 301 /tr/vizyonumuz /hakkimizda/
Redirect 301 /tr/misyonumuz /hakkimizda/
Redirect 301 /tr/degerlerimiz /hakkimizda/
Redirect 301 /tr/kalite-politikamiz /kalite-ve-laboratuvar/
Redirect 301 /tr/makine-parkurumuz /tesislerimiz/
Redirect 301 /tr/urunlerimiz /hizmetler/
Redirect 301 /tr/iletisim /iletisim/
Redirect 301 /tr/ /
```

> SEO eklentisi (Yoast veya Rank Math) kurulursa sayfa başlığı ve açıklaması eklentiye bırakılır. Şema (JSON-LD) yine tema tarafından verilir; bu durumda eklentinin kendi şema çıktısını kapatmanız önerilir.

## Geliştirme

Tüm içerik `src/` klasöründe tek kaynaktan üretilir:

```bash
python3 src/build.py            # dist/ (önizleme) + wordpress/ozen-metalurji/ (tema) + zip
BASE=/ python3 src/build.py     # yerelde kök dizinden önizleme için
```

| Dosya | İçerik |
| --- | --- |
| `src/data.py` | Firma bilgileri (adres, telefon, makine parkuru, hizmetler). Bilgiyi değiştirmek için tek yer. |
| `src/pages_*.py` | Sayfa metinleri, SSS'ler, tablolar |
| `src/schema.py` | JSON-LD yapısal veri |
| `src/ui.py` | Üst menü, alt bilgi, harita kartları ve diğer bileşenler |
| `src/assets/` | CSS, JS, logo, favicon, paylaşım görseli |
| `src/wp/` | WordPress tema dosyaları (functions.php vb.) |

`main` dalına her gönderimde GitHub Actions eski siteden eksik görselleri indirir, siteyi üretir, güncel temayı depoya yazar ve önizlemeyi GitHub Pages'te yayınlar.
