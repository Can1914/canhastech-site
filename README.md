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
