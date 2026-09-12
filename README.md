# CanhasTech — web sitesi

Saf siyah, Linear/Apple tarzı çok sayfalı statik site. Bağımlılık yok; herhangi bir statik sunucuda çalışır.

| Sayfa | Dosya |
|---|---|
| Ana sayfa (Hub) | `index.html` |
| Has Rep — VBT sistemi & kullanım kılavuzu | `hasrep.html` |
| City Diamond | `citydiamond.html` |
| Cagriaslanfit | `cagriaslanfit.html` |
| Cemil Has Medikal | `cemilhasmedikal.html` |
| TBI Athletics | `tbiathletics.html` |
| Has Contract | `hascontract.html` |

Ortak stil ve davranış: `site.css`, `site.js`.

## Yerelde açma
Dosyaya çift tıklamak yeterli; ya da:
```bash
python3 -m http.server 8080
```
ve http://localhost:8080

## GitHub Pages ile yayın
Repo → Settings → Pages → Source: `main` / root. Site `https://<kullanıcı>.github.io/<repo>/` adresinde yayınlanır.

## SEO & performans
`efeunalmedia-lab/efeunal-website-seo` skill setine göre uygulandı:
- Her sayfada benzersiz `<title>`, `meta description`, `canonical`, Open Graph / Twitter kartları
- JSON-LD: `Organization` (ana sayfa), `Product` (Has Rep), `WebPage` + `BreadcrumbList` (proje sayfaları)
- Semantik yapı: tek `h1`, `h2/h3` hiyerarşisi, `<main>`, `aria-labelledby` bölümler
- `sitemap.xml`, `robots.txt`
- Core Web Vitals: font `preconnect` + `display=swap`, hero görseli `fetchpriority="high"` + `preload`, kart görselleri `loading="lazy"`, `width/height` ile CLS 0, `site.js` `defer`, mobilde hafifletilmiş blur
- Sayfalar `build.py` ile üretilir: `python3 build.py`

## Yapılandırma (build.py başında)
- `WEB3FORMS_KEY` — https://web3forms.com adresinde e-posta girip alınan access key; iletişim formu bu anahtarla `info@canhastech.com`'a düşer.
- `WHATSAPP` — sağ alttaki WhatsApp düğmesinin numarası (ülke koduyla, örn. `905321234567`).
Değiştirdikten sonra `python3 build.py` çalıştırın.
