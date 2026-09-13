# Builds the CanhasTech multi-page prototype from shared fragments.
import os
OUT=os.path.dirname(os.path.abspath(__file__))

FONTS='<link rel="preload" as="font" type="font/woff2" href="fonts/Geist-500-latin.woff2" crossorigin><link rel="preload" as="font" type="font/woff2" href="fonts/Geist-400-latin.woff2" crossorigin><link rel="stylesheet" href="fonts/fonts.css">'
SITE='https://canhastech.com/'
WEB3FORMS_KEY='18ddeacb-67bd-46c4-a1a2-361990c1e6a5'   # web3forms.com adresinden alınan access key
WHATSAPP='905537621914'                 # ülke koduyla, boşluksuz
import json
def seo_head(page,title,desc,jsonld=None,preload=None,image='og-canhastech.jpg'):
    url=SITE+('' if page=='index.html' else page)
    m=f'''<meta name="description" content="{desc}">
<link rel="canonical" href="{url}">
<meta name="robots" content="index,follow,max-image-preview:large">
<meta name="theme-color" content="#000000">
<link rel="icon" href="favicon.ico" sizes="32x32"><link rel="icon" type="image/png" sizes="32x32" href="favicon-32.png"><link rel="apple-touch-icon" href="apple-touch-icon.png"><link rel="manifest" href="manifest.json">
<meta property="og:type" content="website"><meta property="og:site_name" content="CanhasTech"><meta property="og:locale" content="tr_TR">
<meta property="og:title" content="{title}"><meta property="og:description" content="{desc}"><meta property="og:url" content="{url}"><meta property="og:image" content="{SITE}{image}">
<meta name="twitter:card" content="summary_large_image"><meta name="twitter:title" content="{title}"><meta name="twitter:description" content="{desc}"><meta name="twitter:image" content="{SITE}{image}">'''
    if preload:m+=f'\n<link rel="preload" as="image" href="{os.path.splitext(preload)[0]}.webp" type="image/webp" fetchpriority="high">'
    if jsonld:m+='\n<script type="application/ld+json">'+json.dumps(jsonld,ensure_ascii=False)+'</script>'
    return m
ORG={"@context":"https://schema.org","@type":"Organization","name":"CanhasTech","alternateName":"Can Has Tech","url":SITE,"logo":SITE+"canhastech-logo.png","email":"info@canhastech.com","address":{"@type":"PostalAddress","addressLocality":"İzmir","addressCountry":"TR"},"description":"İhtiyaca göre özel web siteleri ve mobil uygulamalar geliştiren yazılım, donanım ve yapay zekâ stüdyosu.","parentOrganization":{"@type":"Organization","name":"HAS Software Technologies","url":"https://hassoftware.com.tr"}}
def crumbs(name,page):
    return {"@context":"https://schema.org","@type":"BreadcrumbList","itemListElement":[{"@type":"ListItem","position":1,"name":"CanhasTech","item":SITE},{"@type":"ListItem","position":2,"name":"Ekosistem","item":SITE+"#projeler"},{"@type":"ListItem","position":3,"name":name,"item":SITE+page}]}

MARK='''<svg width="0" height="0" style="position:absolute" aria-hidden="true"><defs>
<linearGradient id="silverG" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#FFFFFF"/><stop offset=".55" stop-color="#C8CBD0"/><stop offset="1" stop-color="#6E7076"/></linearGradient>
<symbol id="ct" viewBox="0 0 120 100">
  <path d="M68 31A32 32 0 1 0 68 79" fill="none" stroke="url(#silverG)" stroke-width="13"/>
  <path d="M40 61A14 14 0 1 0 54 44" fill="none" stroke="#fff" stroke-width="1.5" opacity=".5"/>
  <path d="M30 70 84 16" stroke="url(#silverG)" stroke-width="8" stroke-linecap="round"/>
  <path d="M72 6h30v30l-9-9-9 9-12-12 9-9z" fill="#E6E8EB"/>
  <path d="M94 36h11v60H94V74H66V64l28-28zm0 16L80 64h14z" fill="#9A9DA3"/>
  <rect x="37" y="46" width="14" height="14" rx="2" fill="#000" stroke="#fff" stroke-width="1.5"/>
  <path d="M40 46v-3M44 46v-3M48 46v-3M40 60v3M44 60v3M48 60v3M37 49h-3M37 53h-3M37 57h-3M51 49h3M51 53h3M51 57h3" stroke="#fff" stroke-width="1.2"/>
</symbol></defs></svg>'''

PROJECTS=[
 dict(slug='hasrep',name='Has Rep',mark='HR',sector='Spor teknolojisi',kind='Donanım + App',
      short='Akıllı VBT fitness cihazı & app',
      desc='Ağırlık antrenmanlarını veriye dönüştüren akıllı spor teknolojisi: bara takılan VBT cihazı hareket hızını ölçer, tekrarları sayar; uygulama uzamsal form analizi yapar, yapay zekâ ile antrenman oluşturur ve analiz eder.'),
 dict(slug='citydiamond',name='City Diamond Turizm',mark='CD',sector='Turizm',kind='Kurumsal web sitesi',logo='logo-citydiamond.jpg',cover=True,site='https://citydiamondturizm.com.tr',
      short='Turizm firması web sitesi',
      desc='İzmir merkezli turizm ve VIP transfer firması için kurumsal web sitesi: araç filosu, transfer ve tur hizmetleri, rezervasyon talebi ve WhatsApp iletişimi.'),
 dict(slug='shuttlemerkezi',name='Shuttle Merkezi',mark='SM',sector='Turizm · Ulaşım',kind='Web platformu',logo='logo-shuttlemerkezi.png',
      short='Shuttle rezervasyon platformu',
      desc='Shuttle ve transfer rezervasyon platformu: online rezervasyon, sefer ve araç planlama, sürücü yönetimi, acente ve otel entegrasyonları — ayrı bir web sitesi olarak.'),
 dict(slug='cagriaslanfit',name='Cagriaslanfit',mark='CA',sector='Fitness',kind='Mobil App',logo='logo-prive.png',
      short='Fitness mobil uygulaması',
      desc='Fitness ve sporcu odaklı özel mobil uygulama: kişiye özel programlar, ilerleme takibi ve koç-sporcu iletişimi tek yerde.'),
 dict(slug='cemilhasmedikal',name='Cemil Has Medikal',mark='CH',sector='Medikal',kind='Yazılım + App',logo='logo-hasmedical.png',
      short='Medikal yazılımı',
      desc='Medikal sektör için geliştirilmiş özel yazılım ve uygulama: ürün kataloğu, sipariş ve teslimat takibi, saha ekibi mobil uygulaması.'),
 dict(slug='tbiathletics',name='TBI Athletics',mark='TBI',sector='Atletizm',kind='Performans App',logo='logo-tbi.jpg',
      short='Performans app’i',
      desc='Spor ve atletizm odaklı performans yazılımı: sporcu profilleri, antrenman yükü ve toparlanma takibi, antrenör raporları.'),
 dict(slug='hascontract',name='Has Contract',mark='HC',sector='Kurumsal · Yapay zekâ',kind='Mobil + Web App',soon=True,logo='logo-hascontract.png',
      short='AI sözleşme analizi & oluşturma',
      desc='Yapay zekâ ile sözleşme analizi ve sıfırdan sözleşme oluşturma uygulaması: yüklediğiniz sözleşmenin riskli maddelerini işaretler, sade Türkçeyle özetler; birkaç soruyla sıfırdan sözleşme taslağı üretir.'),
 dict(slug='hasvocab',name='HasVocab',mark='HV',sector='Eğitim',kind='Mobil App',soon=True,nopage=True,logo='logo-hasvocab.png',pill=True,
      short='Çok yakında',
      desc='Yeni mobil uygulamamız HasVocab çok yakında. Detaylar ve erken erişim için bizi takip edin.'),
]

def nav(active):
    items=[('index.html','Ana sayfa'),('index.html#hizmetler','Hizmetler'),('index.html#projeler','Ekosistem'),('hasrep.html','Has Rep'),('index.html#iletisim','İletişim')]
    li=''.join(f'<li><a href="{h}" data-kinetic data-delay="{.15+i*.08:.2f}" data-step="0.02">{t}</a></li>' for i,(h,t) in enumerate(items))
    return f'''<nav aria-label="Ana menü"><div class="wrap">
  <a class="logo" href="index.html" aria-label="Can Has Tech"><img src="canhastech-mark.png" width="39" height="40" alt="" decoding="async"><span class="w"><b>CAN HAS TECH</b><span>Technology Solutions</span></span></a>
  <ul>{li}</ul>
  <a class="btn sm primary" href="index.html#iletisim">Proje başlat</a>
  <button class="burger" type="button" aria-label="Menü" aria-expanded="false" aria-controls="mnav"><i></i><i></i><i></i></button>
</div></nav>
<div class="mnav" id="mnav">
  <a href="index.html">Ana sayfa</a><a href="index.html#hizmetler">Hizmetler</a><a href="index.html#projeler">Ekosistem</a><a href="hasrep.html">Has Rep</a><a href="index.html#iletisim">İletişim</a>
  <div class="k">Projeler</div>{''.join(f'<a class="sub" href="{p["slug"]}.html">{p["name"]}</a>' for p in PROJECTS if not p.get('nopage'))}
  <a class="btn primary" href="index.html#iletisim">Proje başlat</a>
</div>'''

def footer():
    links=''.join(f'<li><a href="{p["slug"]}.html">{p["name"]}</a></li>' for p in PROJECTS if not p.get('nopage'))
    return f'''<footer><div class="wrap">
  <a class="logo" href="index.html" aria-label="Can Has Tech"><img src="canhastech-mark.png" width="39" height="40" alt="" decoding="async"><span class="w"><b>CAN HAS TECH</b><span>Technology Solutions</span></span></a>
  <ul>{links}</ul>
  <span class="mono" style="font-size:11px;letter-spacing:.14em">© 2026 CANHASTECH · İZMİR · <a href="kvkk.html">KVKK</a> · <a href="hasrepkk.html">HAS REP KILAVUZ</a></span>
</div>
<div class="wrap umbrella"><a href="https://hassoftware.com.tr" target="_blank" rel="noopener" class="hs"><img src="logo-hassoftware.png" alt="HAS Software Technologies" loading="lazy" decoding="async"></a><span>CanhasTech, <b>HAS Software Technologies</b> bünyesinde bir markadır. Faturalandırma, sözleşme ve resmi işlemler HAS Software Technologies adına yürütülür.</span></div></footer>'''

WA=f'<a class="wa" href="https://wa.me/{WHATSAPP}?text=Merhaba%2C%20CanhasTech%20ile%20bir%20proje%20hakk%C4%B1nda%20g%C3%B6r%C3%BC%C5%9Fmek%20istiyorum." target="_blank" rel="noopener" aria-label="WhatsApp ile yazın"><svg viewBox="0 0 24 24"><path d="M12 2a10 10 0 0 0-8.6 15.1L2 22l5-1.3A10 10 0 1 0 12 2zm0 18.2a8.2 8.2 0 0 1-4.2-1.2l-.3-.2-3 .8.8-2.9-.2-.3A8.2 8.2 0 1 1 12 20.2zm4.5-6.1c-.2-.1-1.5-.7-1.7-.8s-.4-.1-.6.1-.6.8-.8 1-.3.2-.5.1a6.7 6.7 0 0 1-3.3-2.9c-.3-.4.2-.4.7-1.3.1-.2 0-.3 0-.4l-.8-1.8c-.2-.5-.4-.4-.6-.4h-.5a1 1 0 0 0-.7.3 2.9 2.9 0 0 0-.9 2.2 5 5 0 0 0 1.1 2.7 11.5 11.5 0 0 0 4.4 3.9c1.6.7 2.2.7 3 .6a2.6 2.6 0 0 0 1.7-1.2 2 2 0 0 0 .1-1.2c0-.1-.2-.2-.4-.3z"/></svg><span>WhatsApp</span><i class="dot"></i></a>'
SMOKE='<div class="smoke" aria-hidden="true"><i class="s1"></i><i class="s2"></i><i class="s3"></i></div>'

import re as _re
def _pictures(html):
    def sub(m):
        tag=m.group(0); src=m.group(1); base=os.path.splitext(src)[0]
        if not os.path.exists(os.path.join(OUT,base+'.webp')): return tag
        return f'<picture><source srcset="{base}.webp" type="image/webp">{tag}</picture>'
    return _re.sub(r'<img [^>]*?src="([^"]+\.(?:jpg|png))"[^>]*>',sub,html)

def shell(title,body,extra_css='',extra_js='',main=False,meta=''):
    body=_pictures(body)
    head=f'<title>{title}</title>\n{meta}\n{FONTS}\n<link rel="stylesheet" href="site.css">\n<style>{extra_css}</style>'
    doc=f'{head}\n{MARK}\n{SMOKE}\n<div class="page">\n{body}\n</div>\n{footer()}\n{WA}\n<script src="site.js" defer></script>\n<script defer>{extra_js}</script>'
    if main: return doc   # the Artifact tool wraps the main page in its own skeleton
    return f'<!doctype html>\n<html lang="tr"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">\n{doc[:doc.index("<svg")]}</head><body>\n{doc[doc.index("<svg"):]}\n</body></html>'

def pnav(slug):
    PP=[p for p in PROJECTS if not p.get('nopage')];i=[p['slug'] for p in PP].index(slug);prev=PP[i-1];nxt=PP[(i+1)%len(PP)]
    return f'''<div class="pnav rv"><a href="{prev['slug']}.html"><span class="k">← Önceki proje</span><b>{prev['name']}</b></a><a class="next" href="{nxt['slug']}.html"><span class="k">Sonraki proje →</span><b>{nxt['name']}</b></a></div>'''

def band():
    return '''<section class="band rv"><div class="wrap"><div class="eyebrow" style="justify-content:center">Birlikte çalışalım</div><h2><span class="line"><span>Benzer bir projeniz mi var?</span></span></h2><p>İhtiyacınıza göre özel web siteleri ve mobil uygulamalar geliştiriyoruz. Kapsamı birlikte çıkaralım.</p><a class="btn primary" href="index.html#iletisim">Projenizi anlatın <svg viewBox="0 0 16 16" fill="none"><path d="M3 8h10M9 4l4 4-4 4" stroke="currentColor" stroke-width="1.6" stroke-linecap="round"/></svg></a></div></section>'''

# ---------------------------------------------------------------- INDEX
INDEX_CSS='''
.hero{padding-top:104px;padding-bottom:40px}
/* schema menu: hub + orbiting nodes, spring-in, bounce on hover */
.schema{position:relative;height:340px;margin:72px auto 0;max-width:900px}
.schema svg.wires{position:absolute;inset:0;width:100%;height:100%;overflow:visible}
.schema .wire{stroke:rgba(255,255,255,.14);stroke-width:1;fill:none;stroke-dasharray:6 6;animation:dash 30s linear infinite}
@keyframes dash{to{stroke-dashoffset:-600}}
.node{position:absolute;transform:translate(-50%,-50%);display:grid;justify-items:center;gap:8px;opacity:.001;animation:nodeIn .9s var(--spring) forwards;text-align:center;width:120px}
@keyframes nodeIn{from{opacity:.001;transform:translate(-50%,-50%) translateY(40px) scale(.6)}to{opacity:1;transform:translate(-50%,-50%)}}
.node .pill{width:64px;height:64px;border-radius:20px;border:1px solid var(--line2);background:var(--card);display:grid;place-items:center;font-weight:500;font-size:15px;letter-spacing:-.02em;color:var(--silver);transition:transform .45s var(--spring),border-color .3s,background .3s,box-shadow .3s;box-shadow:0 10px 30px -18px rgba(0,0,0,.9)}
.node small{font-size:12px;color:var(--muted);transition:color .3s;line-height:1.3}
.node:hover .pill,.node:focus-visible .pill{transform:translateY(-10px) scale(1.06);border-color:#fff;background:#161616;box-shadow:0 0 0 1px rgba(255,255,255,.35),0 18px 40px -20px rgba(255,255,255,.4)}
.node:hover small{color:#fff}
.node.hub .pill{width:84px;height:84px;border-radius:26px;background:#fff;color:#000;border-color:#fff;animation:hubBob 4.5s ease-in-out infinite}
@keyframes hubBob{0%,100%{transform:translateY(0)}50%{transform:translateY(-6px)}}
.node.hub small{color:#fff}
.node .pill img{width:52px;height:auto}
@media(max-width:700px){.schema{height:auto;display:grid;grid-template-columns:repeat(3,1fr);gap:14px;padding:8px 0 24px}.schema svg.wires{display:none}.node{position:static;transform:none;width:auto}.node.hub{grid-column:span 3}@keyframes nodeIn{from{opacity:.001;transform:translateY(30px) scale(.7)}to{opacity:1;transform:none}}}

.services{display:grid;grid-template-columns:1fr 1fr;gap:14px}
.svc{border-radius:var(--r);border:1px solid var(--line);background:var(--card);padding:36px;position:relative;overflow:hidden;transition:border-color .3s}
.svc:hover{border-color:var(--line2)}
.svc::before{content:"";position:absolute;left:0;right:0;top:0;height:1px;background:linear-gradient(90deg,transparent,rgba(255,255,255,.45),transparent);opacity:.6}
.svc .k{font-family:var(--mono);font-size:12px;letter-spacing:.08em;color:var(--dim);text-transform:uppercase;margin-bottom:22px;display:flex;justify-content:space-between}
.svc h3{font-size:26px;margin-bottom:12px}
.svc>p{color:var(--muted);font-size:15px;max-width:44ch;margin-bottom:26px}
.svc ul{list-style:none;margin:0;padding:0;border-top:1px solid var(--line)}
.svc li{display:flex;justify-content:space-between;gap:16px;padding:12px 0;border-bottom:1px solid var(--line);font-size:14.5px}
.svc li span{color:var(--muted);font-family:var(--mono);font-size:12px;white-space:nowrap}
@media(max-width:820px){.services{grid-template-columns:1fr}.svc{padding:28px}}

.about{display:grid;grid-template-columns:1fr 1.2fr;gap:48px;align-items:start;border-radius:var(--r);border:1px solid var(--line);background:var(--card);padding:40px}
.about .head{margin:0}.about h2{font-size:clamp(30px,4vw,46px);margin-top:18px}
.about-text{display:grid;gap:16px;color:var(--muted);font-size:16px;line-height:1.7}
.about-text b{color:#fff;font-weight:500}
.about-facts{display:grid;grid-template-columns:repeat(4,1fr);gap:14px;margin-top:10px;padding-top:22px;border-top:1px solid var(--line)}
.about-facts div{display:grid;gap:2px}.about-facts b{color:#fff;font-weight:500;font-size:18px;letter-spacing:-.02em}.about-facts span{font-size:12.5px;color:var(--dim)}
@media(max-width:900px){.about{grid-template-columns:1fr;gap:24px;padding:28px}.about-facts{grid-template-columns:1fr 1fr}}
.refs{display:grid;grid-template-columns:repeat(8,1fr);gap:12px}
.ref.hs img{max-height:56px;opacity:.7}
.ref{border-radius:var(--r);border:1px solid var(--line);background:var(--card);height:120px;display:grid;place-items:center;padding:18px;transition:border-color .3s,transform .4s var(--ease);opacity:.9;overflow:hidden}
.ref:hover{border-color:var(--line2);transform:translateY(-3px);opacity:1}
.ref.cover{padding:0}.ref.cover img{width:100%;height:100%;object-fit:cover;border-radius:0}
.ref img{max-width:100%;max-height:100%;object-fit:contain;border-radius:8px}
.ref.pill img{background:#fff;padding:8px 12px;border-radius:10px;max-height:64px}
@media(max-width:1100px){.refs{grid-template-columns:repeat(4,1fr)}}@media(max-width:600px){.refs{grid-template-columns:repeat(2,1fr)}}
.projects{display:grid;grid-template-columns:repeat(3,1fr);gap:14px}
.pj{display:flex;flex-direction:column;min-height:360px;padding:0;cursor:pointer}
.pj .visual{height:160px;position:relative;overflow:hidden;background:var(--card2);border-bottom:1px solid var(--line);display:grid;place-items:center}
.pj .visual img{width:100%;height:100%;object-fit:cover;transition:transform .8s var(--ease)}
.pj:hover .visual img{transform:scale(1.04)}
.pj .visual img.plogo{width:auto;height:96px;object-fit:contain;filter:none;position:relative;border-radius:14px;transition:transform .6s var(--ease)}
.pj .visual img.plogo.pill{background:#fff;padding:10px 16px;height:64px}
.pj:hover .visual img.plogo{transform:scale(1.05)}
.pj .mark{font-size:44px;font-weight:300;letter-spacing:-.04em;color:var(--silver);position:relative;transition:transform .6s var(--ease)}
.pj:hover .mark{transform:scale(1.06)}
.pj .visual .g{position:absolute;inset:0;background-image:linear-gradient(rgba(255,255,255,.05) 1px,transparent 1px),linear-gradient(90deg,rgba(255,255,255,.05) 1px,transparent 1px);background-size:28px 28px;mask-image:radial-gradient(ellipse 70% 70% at 50% 50%,#000,transparent);-webkit-mask-image:radial-gradient(ellipse 70% 70% at 50% 50%,#000,transparent)}
.pj .body{padding:22px 24px 24px;display:flex;flex-direction:column;flex:1;position:relative;z-index:1}
.pj .tag{font-family:var(--mono);font-size:11px;letter-spacing:.08em;text-transform:uppercase;color:var(--dim);display:flex;justify-content:space-between;margin-bottom:12px}
.pj h3{font-size:20px;margin-bottom:8px}
.pj p{color:var(--muted);font-size:14.5px;flex:1}
.pj .more{margin-top:18px;font-size:13px;color:var(--silver);display:flex;align-items:center;gap:8px}
.pj .more::after{content:"→";transition:transform .3s}
.pj:hover .more::after{transform:translateX(4px)}
.pj .soon{position:absolute;top:12px;right:12px;font-family:var(--mono);font-size:10.5px;letter-spacing:.1em;text-transform:uppercase;color:#000;background:#fff;padding:5px 9px;border-radius:999px;z-index:2}
.pj.static{cursor:default}.pj.static .more::after{content:""}
.pj.feature{grid-column:span 2}.pj.feature .visual{height:210px}
@media(max-width:900px){.projects{grid-template-columns:1fr 1fr}}
@media(max-width:600px){.projects{grid-template-columns:1fr}.pj.feature,.pj.static{grid-column:auto}}

.cta{border-top:1px solid var(--line)}
.cta .wrap{display:grid;grid-template-columns:1fr 1fr;gap:56px;align-items:start}
.cta h2{font-size:clamp(34px,5vw,62px);margin:18px 0 18px}
.cta .lead{color:var(--muted);font-size:17px;max-width:44ch;margin-bottom:32px}
.contacts{display:grid;font-size:14px;color:var(--muted)}
.contacts a{display:flex;justify-content:space-between;padding:12px 0;border-bottom:1px solid var(--line);transition:color .2s}
.contacts a:hover{color:#fff}.contacts span{font-family:var(--mono);font-size:12px;color:var(--dim)}
form.card{display:grid;gap:14px}
.f{display:grid;gap:6px}.f label{font-size:12.5px;color:var(--muted)}
.f input,.f textarea{background:#000;border:1px solid var(--line2);border-radius:8px;color:#fff;padding:11px 13px;font-family:var(--sans);font-size:14px;transition:border-color .2s;width:100%}
.f input:focus,.f textarea:focus{outline:none;border-color:rgba(255,255,255,.5)}
.f textarea{min-height:110px;resize:vertical}.f input::placeholder,.f textarea::placeholder{color:var(--dim)}
.f2{display:grid;grid-template-columns:1fr 1fr;gap:12px}
.chips{display:flex;flex-wrap:wrap;gap:8px}
.chip{font-size:13px;padding:7px 12px;border-radius:999px;border:1px solid var(--line2);color:var(--muted);cursor:pointer;background:transparent;font-family:var(--sans);transition:all .2s}
.chip.on{background:#fff;color:#000;border-color:#fff}
.done{font-family:var(--mono);font-size:12px;color:var(--silver);min-height:18px}
@media(max-width:820px){.cta .wrap{grid-template-columns:1fr}.f2{grid-template-columns:1fr}}
'''

def index_page():
    # schema node positions (percent of the 900x300 stage)
    pos=[(10,22),(32,10),(68,10),(90,22),(10,84),(50,92),(90,84)]
    nodes=''.join(f'<a class="node" href="{p["slug"]}.html" style="left:{x}%;top:{y}%;animation-delay:{1.35+i*.1:.2f}s"><span class="pill">{p["mark"]}</span><small>{p["name"]}</small></a>' for i,(p,(x,y)) in enumerate(zip([q for q in PROJECTS if not q.get('nopage')],pos)))
    wires=''.join(f'<path class="wire" d="M450 180 L {x*9} {y*3.4}"/>' for x,y in pos)
    hub=f'<a class="node hub" href="#projeler" style="left:50%;top:53%;animation-delay:1.25s"><span class="pill"><img src="canhastech-mark.png" width="52" height="53" alt="CanhasTech"></span><small>CanhasTech Hub</small></a>'
    cards=''
    for i,p in enumerate(PROJECTS):
        if p['slug']=='hasrep': vis='<img src="hasrep-urun.jpg" width="1086" height="680" loading="lazy" decoding="async" alt="Has Rep sensörü" style="filter:none">'
        elif p.get('cover'): vis=f'<img src="{p["logo"]}" loading="lazy" decoding="async" alt="{p["name"]} logosu" style="filter:none">'
        elif p.get('logo'): vis=f'<div class="g"></div><img class="plogo{" pill" if p.get("pill") else ""}" src="{p["logo"]}" loading="lazy" decoding="async" alt="{p["name"]} logosu">'
        else: vis=f'<div class="g"></div><div class="mark">{p["mark"]}</div>'
        tag=f'<span class="soon">Çok yakında</span>' if p.get('soon') else ''
        inner=f'<div class="visual">{vis}{tag}</div><div class="body"><div class="tag"><span>{p["sector"]}</span><span>{p["kind"]}</span></div><h3>{p["name"]}</h3><p>{p["desc"]}</p><div class="more">{"Detaylar yakında" if p.get("nopage") else p["name"]+" sayfasına git"}</div></div>'
        if p.get('nopage'): cards+=f'<div class="card glass pj static">{inner}</div>'
        else: cards+=f'<a class="card glass pj{" feature" if p["slug"]=="hasrep" else ""}" href="{p["slug"]}.html">{inner}</a>'
    body=f'''{nav('index')}
<header class="hero" id="top">
  <div class="wrap">
    <div class="eyebrow up" style="animation-delay:.05s">Yazılım · Donanım · Yapay zekâ</div>
    <h1><span class="line"><span data-kinetic data-delay=".15">Can Has Tech</span></span><span class="line thin"><span data-kinetic data-delay=".4" data-step="0.02">Akıllı teknolojiler ekosistemi</span></span></h1>
    <p class="lede up" style="animation-delay:.9s">İhtiyacınıza göre özel web siteleri ve mobil uygulamalar geliştiriyoruz.</p>
    <p class="sub up" style="animation-delay:1s">Fikirden ürüne: tasarım, yazılım, gerekirse donanım ve yapay zekâ — tek ekipten, tek sorumlulukla.</p>
    <div class="cta-row up" style="animation-delay:1.1s"><a class="btn primary" href="#iletisim">Projenizi anlatın <svg viewBox="0 0 16 16" fill="none"><path d="M3 8h10M9 4l4 4-4 4" stroke="currentColor" stroke-width="1.6" stroke-linecap="round"/></svg></a><a class="btn" href="#projeler">Ekosistemi keşfet</a></div>
    <div class="schema up" style="animation-delay:1.2s" aria-label="Ekosistem şeması">
      <svg class="wires" viewBox="0 0 900 340" preserveAspectRatio="none" aria-hidden="true">{wires}</svg>
      {hub}{nodes}
    </div>
  </div>
</header>
<main>
<div class="metrics up" style="animation-delay:1.7s"><div class="wrap">
  <div class="m"><div class="v">6</div><div class="l">canlı ürün ve platform</div></div>
  <div class="m"><div class="v">2<span>alan</span></div><div class="l">web ve mobil geliştirme</div></div>
  <div class="m"><div class="v">1</div><div class="l">kendi donanımımız: Has Rep</div></div>
  <div class="m"><div class="v">48<span>sa</span></div><div class="l">içinde ilk dönüş</div></div>
</div></div>

<section id="hizmetler"><div class="wrap">
  <div class="head rv"><div><div class="eyebrow">Hizmetler</div><h2><span class="line"><span>Web ve mobil,</span></span><span class="line"><span>ölçeğinize göre.</span></span></h2></div><p>Şablon satmıyoruz. Her projeyi işin gerçek akışından başlayarak tasarlıyor, kendi ekibimizle geliştiriyor ve yayına aldıktan sonra da yanında kalıyoruz.</p></div>
  <div class="services rv">
    <article class="svc"><div class="k"><span>01 — Web</span><span>Kurumsal · Panel · E-ticaret</span></div><h3>Web sitesi geliştirme</h3><p>Hızlı açılan, arama motorlarında görünen ve yönetmesi kolay siteler. Kurumsal vitrinden yönetim paneline kadar.</p><ul><li>Kurumsal web sitesi<span>tasarım + kod</span></li><li>Rezervasyon ve operasyon panelleri<span>web app</span></li><li>Yönetim ve raporlama arayüzleri<span>dashboard</span></li><li>Performans, SEO, erişilebilirlik<span>standart</span></li></ul></article>
    <article class="svc"><div class="k"><span>02 — Mobil</span><span>iOS · Android</span></div><h3>Mobil uygulama geliştirme</h3><p>iOS ve Android’de aynı kalitede çalışan, mağazaya biz çıkaran, cihaz ve sensörlerle konuşabilen uygulamalar.</p><ul><li>iOS &amp; Android uygulamalar<span>native / cross</span></li><li>Donanım ve sensör entegrasyonu<span>BLE · IoT</span></li><li>Yapay zekâ destekli özellikler<span>on-device · bulut</span></li><li>Mağaza yayını ve sürüm yönetimi<span>App Store · Play</span></li></ul></article>
  </div>
</div></section>

<section id="hakkimizda" style="padding-top:0"><div class="wrap">
  <div class="about rv">
    <div><div class="eyebrow">Hakkımızda</div><h2><span class="line"><span>İzmir’den,</span></span><span class="line"><span>ürün gibi düşünen bir ekip.</span></span></h2></div>
    <div class="about-text">
      <p>CanhasTech, <b>İzmir</b> merkezli bir yazılım, donanım ve yapay zekâ stüdyosu. <b>HAS Software Technologies</b> bünyesinde faaliyet gösteriyoruz; resmi işlemler, sözleşme ve faturalandırma HAS Software Technologies adına yürütülür.</p>
      <p>İki şey yapıyoruz: müşterilerimiz için <b>ihtiyaca göre özel web siteleri ve mobil uygulamalar</b> geliştiriyoruz; kendi ürünlerimizi — <b>Has Rep</b> akıllı antrenman sensörü, <b>Has Contract</b> ve <b>HasVocab</b> — tasarlayıp üretiyoruz. Kendi ürünümüzü çıkarmanın disipliniyle müşteri projelerine yaklaşıyoruz: gerçek kullanıcı, gerçek veri, ölçülebilir sonuç.</p>
      <p>Tasarımdan yazılıma, gerekirse donanım ve yapay zekâya kadar tek ekip, tek sorumluluk. İzmir’de yerinde, Türkiye’nin her yerinde online çalışıyoruz.</p>
      <div class="about-facts"><div><b>İzmir</b><span>merkez</span></div><div><b>Web + Mobil</b><span>geliştirme</span></div><div><b>3</b><span>kendi ürünümüz</span></div><div><b>HAS Software</b><span>çatı şirket</span></div></div>
    </div>
  </div>
</div></section>

<section id="referanslar" style="padding-top:0"><div class="wrap">
  <div class="head rv"><div><div class="eyebrow">Referanslar &amp; markalar</div><h2><span class="line"><span>Birlikte çalıştıklarımız.</span></span></h2></div><p>Ekosistemimizdeki markalar ve çözüm geliştirdiğimiz kurumlar. CanhasTech, resmi işlemlerde HAS Software Technologies çatısı altında faaliyet gösterir.</p></div>
  <div class="refs rv">
    <a class="ref cover" href="citydiamond.html" title="City Diamond Turizm"><img src="logo-citydiamond.jpg" alt="City Diamond Turizm" loading="lazy" decoding="async"></a>
    <a class="ref" href="shuttlemerkezi.html" title="Shuttle Merkezi"><img src="logo-shuttlemerkezi.png" alt="Shuttle Merkezi" loading="lazy" decoding="async"></a>
    <a class="ref" href="cagriaslanfit.html" title="Privé — Cagriaslanfit"><img src="logo-prive.png" alt="Privé Elite Athlete Development" loading="lazy" decoding="async"></a>
    <a class="ref" href="cemilhasmedikal.html" title="HAS Medical Equipments"><img src="logo-hasmedical.png" alt="HAS Medical Equipments" loading="lazy" decoding="async"></a>
    <a class="ref" href="tbiathletics.html" title="TBI Athletics"><img src="logo-tbi.jpg" alt="TBI Athletics" loading="lazy" decoding="async"></a>
    <a class="ref" href="hascontract.html" title="Has Contract"><img src="logo-hascontract.png" alt="Has Contract" loading="lazy" decoding="async" style="max-height:72px"></a>
    <a class="ref hs" href="https://hassoftware.com.tr" target="_blank" rel="noopener" title="HAS Software Technologies"><img src="logo-hassoftware.png" alt="HAS Software Technologies" loading="lazy" decoding="async"></a>
  </div>
</div></section>

<section id="projeler" style="padding-top:0"><div class="wrap">
  <div class="head rv"><div><div class="eyebrow">Ekosistem &amp; projeler</div><h2><span class="line"><span>Kendi ürünlerimiz,</span></span><span class="line"><span>müşteri çözümlerimiz.</span></span></h2></div><p>Spor teknolojisinden turizme, medikalden kurumsal yönetime. Her kart kendi sayfasına açılır.</p></div>
  <div class="projects rv">{cards}</div>
</div></section>

<section class="cta" id="iletisim"><div class="wrap rv">
  <div><div class="eyebrow">İletişim</div><h2><span class="line"><span>Projenizi</span></span><span class="line"><span>hayata geçirelim.</span></span></h2><p class="lead">Bir fikir, bir ekran görüntüsü ya da yarım kalmış bir proje — nereden başladığınız fark etmez. 48 saat içinde dönüş yapar, ilk görüşmede kapsam ve yol haritasını birlikte çıkarırız.</p>
    <div class="contacts"><a href="mailto:info@canhastech.com">info@canhastech.com<span>E-posta</span></a><a href="https://canhastech.com" target="_blank" rel="noopener">canhastech.com<span>Web</span></a><a href="#top">İzmir, Türkiye<span>Konum</span></a></div></div>
  <form class="card" id="contact" action="https://api.web3forms.com/submit" method="POST"><input type="hidden" name="access_key" value="{WEB3FORMS_KEY}"><input type="hidden" name="subject" value="CanhasTech — yeni proje talebi"><input type="hidden" name="from_name" value="canhastech.com"><input type="hidden" name="proje_turu" id="ptype" value="Web sitesi"><input type="checkbox" name="botcheck" class="hp" tabindex="-1" autocomplete="off"><div class="f2"><div class="f"><label for="n">Ad Soyad <span class="req">*</span></label><input id="n" name="ad_soyad" placeholder="Adınız" required autocomplete="name"></div><div class="f"><label for="e">E-posta <span class="req">*</span></label><input id="e" name="email" type="email" placeholder="ornek@sirket.com" required autocomplete="email"></div></div>
    <div class="f"><label>Proje türü</label><div class="chips" id="chips"><button type="button" class="chip on">Web sitesi</button><button type="button" class="chip">Mobil uygulama</button><button type="button" class="chip">Web + Mobil</button><button type="button" class="chip">Donanım / IoT</button><button type="button" class="chip">Yapay zekâ</button></div></div>
    <div class="f"><label for="m">Kısaca anlatın</label><textarea id="m" name="mesaj" placeholder="Ne yapmak istiyorsunuz, kimin için, ne zaman?"></textarea></div>
    <label class="consent"><input type="checkbox" required name="kvkk"> <span>Gönderdiğim bilgilerin talebimle ilgili iletişim amacıyla işlenmesini kabul ediyorum. <a href="kvkk.html" target="_blank" rel="noopener">KVKK aydınlatma metni</a></span></label>
    <button class="btn primary" type="submit" id="send">Gönder</button><div class="done" id="done"></div></form>
</div></section>
</main>'''
    js='''
(function(){const chips=document.getElementById('chips');chips.addEventListener('click',e=>{const b=e.target.closest('.chip');if(!b)return;chips.querySelectorAll('.chip').forEach(c=>c.classList.remove('on'));b.classList.add('on')});
const form=document.getElementById('contact'),done=document.getElementById('done'),send=document.getElementById('send');
form.addEventListener('submit',async e=>{e.preventDefault();done.className='done';done.textContent='Gönderiliyor…';send.disabled=true;
  document.getElementById('ptype').value=chips.querySelector('.on').textContent;
  const name=document.getElementById('n').value.trim();
  try{const r=await fetch(form.action,{method:'POST',headers:{'Accept':'application/json'},body:new FormData(form)});const j=await r.json();
    if(r.ok&&j.success){done.textContent=`Teşekkürler ${name} — talebiniz ulaştı, 48 saat içinde dönüyoruz.`;form.reset();chips.querySelectorAll('.chip').forEach((c,i)=>c.classList.toggle('on',i===0))}
    else throw new Error(j.message||'Gönderilemedi')}
  catch(err){done.className='done err';done.textContent='Gönderilemedi. Lütfen tekrar deneyin ya da info@canhastech.com adresine yazın.'}
  finally{send.disabled=false}});})();'''
    meta=seo_head('index.html','CanhasTech — Özel web siteleri ve mobil uygulamalar','İhtiyacınıza göre özel web siteleri ve mobil uygulamalar geliştiriyoruz. Has Rep VBT cihazı, City Diamond Turizm, Cagriaslanfit, Cemil Has Medikal, TBI Athletics ve Has Contract — CanhasTech ekosistemi.',ORG)
    return shell('CanhasTech — Özel web siteleri ve mobil uygulamalar',body,INDEX_CSS,js,main=True,meta=meta)

# ---------------------------------------------------------------- HAS REP
HASREP_CSS='''
.hero .brand{display:block;width:min(260px,60vw);height:auto;margin:22px auto -6px;-webkit-mask-image:radial-gradient(ellipse 60% 60% at 50% 50%,#000 55%,transparent 100%);mask-image:radial-gradient(ellipse 60% 60% at 50% 50%,#000 55%,transparent 100%)}
.hero .product{margin:56px auto 0;max-width:820px;position:relative}
.gallery{display:grid;grid-template-columns:1.2fr 1fr;gap:14px;margin-top:14px}
.gallery figure{margin:0;border-radius:var(--r);border:1px solid var(--line);background:var(--card);overflow:hidden;position:relative}
.gallery img{display:block;width:100%;height:100%;object-fit:cover;aspect-ratio:4/3;transition:transform .9s var(--ease)}
.gallery figure:hover img{transform:scale(1.03)}
.gallery figcaption{position:absolute;left:0;right:0;bottom:0;padding:14px 18px;font-family:var(--mono);font-size:11px;letter-spacing:.12em;text-transform:uppercase;color:#fff;background:linear-gradient(0deg,rgba(0,0,0,.75),transparent)}
@media(max-width:700px){.gallery{grid-template-columns:1fr}}
.hero .product img{display:block;width:100%;height:auto;border-radius:16px;-webkit-mask-image:linear-gradient(90deg,transparent,#000 12%,#000 88%,transparent),linear-gradient(180deg,#000 70%,transparent);-webkit-mask-composite:source-in;mask-image:linear-gradient(90deg,transparent,#000 12%,#000 88%,transparent),linear-gradient(180deg,#000 70%,transparent);mask-composite:intersect}
.pillars{display:grid;grid-template-columns:repeat(4,1fr);gap:14px}
.pillar{border-radius:var(--r);border:1px solid var(--line);background:var(--card);padding:26px;min-height:220px;display:flex;flex-direction:column}
.pillar .ic{width:38px;height:38px;border-radius:9px;border:1px solid var(--line2);background:#000;display:grid;place-items:center;margin-bottom:20px;color:var(--silver)}
.pillar .ic svg{width:18px;height:18px}
.pillar h3{font-size:18px;margin-bottom:8px}.pillar p{color:var(--muted);font-size:14.5px;flex:1}
@media(max-width:900px){.pillars{grid-template-columns:1fr 1fr}}@media(max-width:560px){.pillars{grid-template-columns:1fr}}
.flow{display:grid;grid-template-columns:repeat(3,1fr);border-top:1px solid var(--line);margin-top:14px}
.fl{padding:30px 28px 30px 0;border-right:1px solid var(--line)}.fl+.fl{padding-left:28px}.fl:last-child{border-right:0}
.fl .n{font-family:var(--mono);font-size:12px;color:var(--dim);margin-bottom:12px}.fl h3{font-size:17px;margin-bottom:8px}.fl p{color:var(--muted);font-size:14px}
@media(max-width:820px){.flow{grid-template-columns:1fr}.fl{border-right:0;border-bottom:1px solid var(--line);padding-left:0}.fl+.fl{padding-left:0}}

/* guide */
.guide{border-top:1px solid var(--line)}
.guide-grid{display:grid;grid-template-columns:400px 1fr;gap:14px;align-items:start}
.stage{position:sticky;top:84px;border-radius:var(--r);border:1px solid var(--line);background:var(--card);padding:28px;display:grid;gap:22px}
.stage .pod{width:100%;display:grid;place-items:center;position:relative;border-radius:14px;overflow:hidden}
.stage .pod img{width:100%;height:auto;display:block;border-radius:14px}
.stage .pod.shake img{animation:shake .7s cubic-bezier(.36,.07,.19,.97) both}
.leddot{position:absolute;left:50%;top:32.5%;width:11px;height:11px;border-radius:50%;background:#2A2A2E;transform:translate(-50%,-50%);transition:background .35s,box-shadow .35s;border:1px solid rgba(0,0,0,.6)}
@keyframes shake{10%,90%{transform:translate3d(-2px,0,0) rotate(-1deg)}20%,80%{transform:translate3d(4px,0,0) rotate(1.5deg)}30%,50%,70%{transform:translate3d(-7px,0,0) rotate(-2.5deg)}40%,60%{transform:translate3d(7px,0,0) rotate(2.5deg)}}
.stage .halo{position:absolute;inset:18% 22%;border-radius:50%;background:radial-gradient(circle,var(--ledc,transparent) 0%,transparent 60%);opacity:0;transition:opacity .5s,background .5s;filter:blur(28px);pointer-events:none;z-index:1;mix-blend-mode:screen}
.stage .pod.lit .halo{opacity:.45}
.stage .pod.pulse .leddot{animation:ledPulse 1.6s ease-in-out infinite}
@keyframes ledPulse{0%,100%{opacity:1}50%{opacity:.25}}
.status{display:grid;grid-template-columns:1fr 1fr;gap:1px;background:var(--line);border:1px solid var(--line);border-radius:10px;overflow:hidden}
.status div{background:#0D0D0D;padding:12px 14px}
.status .k{font-family:var(--mono);font-size:10.5px;letter-spacing:.08em;text-transform:uppercase;color:var(--dim)}
.status .v{font-size:14px;font-weight:500;margin-top:2px;display:flex;align-items:center;gap:8px;white-space:nowrap}
.status .v i{width:8px;height:8px;border-radius:50%;background:var(--dim);display:inline-block;transition:background .3s,box-shadow .3s}
.gcards{display:grid;gap:14px}
.gc{border-radius:var(--r);border:1px solid var(--line);background:var(--card);padding:28px;transition:border-color .3s}
.gc:hover{border-color:var(--line2)}
.gc .k{font-family:var(--mono);font-size:12px;letter-spacing:.08em;color:var(--dim);text-transform:uppercase;margin-bottom:16px;display:flex;justify-content:space-between}
.gc h3{font-size:22px;margin-bottom:8px}.gc>p{color:var(--muted);font-size:15px;max-width:56ch}
.leds{display:grid;gap:8px;margin-top:20px}
.led{display:grid;grid-template-columns:auto 1fr auto;gap:16px;align-items:center;padding:14px 16px;border-radius:10px;border:1px solid var(--line);background:#0D0D0D;cursor:pointer;transition:border-color .25s,background .25s;text-align:left;font-family:var(--sans);color:#fff;width:100%}
.led:hover,.led.on{background:#161616;border-color:var(--line2)}
.led .dot{width:14px;height:14px;border-radius:50%;background:var(--c);box-shadow:0 0 0 3px rgba(255,255,255,.04),0 0 14px var(--c)}
.led.charging .dot{animation:ledPulse 1.6s ease-in-out infinite}
.led b{font-weight:500;font-size:15px;display:block}.led span{color:var(--muted);font-size:13.5px}
.led .when{font-family:var(--mono);font-size:11px;color:var(--dim);letter-spacing:.06em;text-transform:uppercase;white-space:nowrap}
.wake{display:flex;gap:14px;align-items:center;margin-top:20px;flex-wrap:wrap}
.wake .hint{font-family:var(--mono);font-size:12px;color:var(--dim)}.wake .hint b{color:var(--silver);font-weight:500}
.steps3{margin-top:20px;border-top:1px solid var(--line)}
.st{display:grid;grid-template-columns:28px 1fr;gap:14px;padding:14px 0;border-bottom:1px solid var(--line);align-items:start}
.st .n{width:24px;height:24px;border-radius:50%;border:1px solid var(--line2);font-family:var(--mono);font-size:11px;display:grid;place-items:center;color:var(--muted);transition:all .3s}
.st.active .n{background:#fff;color:#000;border-color:#fff}.st.done .n{border-color:var(--led-green);color:var(--led-green)}
.st b{font-weight:500;display:block;font-size:15px}.st span{color:var(--muted);font-size:13.5px}
.connect{display:grid;grid-template-columns:1fr 150px;gap:24px;align-items:start}
.phone{width:150px;aspect-ratio:9/17;border-radius:22px;border:1px solid var(--line2);background:#0A0A0A;padding:10px;position:relative}
.phone .bar{display:flex;justify-content:space-between;align-items:center;padding:4px 2px 8px;border-bottom:1px solid var(--line)}
.phone .bar span{font-size:8px;font-weight:500;letter-spacing:.06em}
.phone .podbtn{width:20px;height:20px;border-radius:6px;border:1px solid var(--line2);display:grid;place-items:center;font-size:10px;position:relative}
.phone .podbtn::after{content:"";position:absolute;inset:-6px;border-radius:10px;border:1px solid #fff;opacity:0}
.phone.hint .podbtn::after{opacity:1;animation:ring 1.2s ease-out infinite}
@keyframes ring{0%{transform:scale(.8);opacity:.9}100%{transform:scale(1.5);opacity:0}}
.phone .scr{padding:10px 2px;font-size:8.5px;color:var(--muted);line-height:1.5}
.phone .scr .row2{display:flex;justify-content:space-between;padding:6px 8px;border:1px solid var(--line);border-radius:6px;margin-top:8px;transition:all .3s}
.phone .scr .row2.found{border-color:rgba(255,255,255,.4);color:#fff}.phone .scr .row2.ok{border-color:var(--led-blue);color:#fff}.phone .scr .b{color:var(--led-blue);font-weight:500}
.actions{display:flex;gap:8px;margin-top:18px;flex-wrap:wrap}
.sup{display:grid;grid-template-columns:repeat(3,1fr);gap:14px;margin-top:14px}
.sup a{border-radius:var(--r);border:1px solid var(--line);background:var(--card);padding:20px 22px;display:grid;gap:4px;transition:border-color .3s,transform .3s var(--ease)}
.sup a:hover{border-color:var(--line2);transform:translateY(-2px)}
.sup b{font-weight:500;font-size:15px}.sup span{font-size:13px;color:var(--muted)}.sup .mono{font-size:11px;color:var(--dim);letter-spacing:.06em;margin-top:6px}
/* app tour */
.tour{position:relative;margin:0 -24px;padding:0 24px}
.tour .track{display:flex;gap:18px;overflow-x:auto;scroll-snap-type:x mandatory;padding:8px 0 22px;scrollbar-width:none}
.tour .track::-webkit-scrollbar{display:none}
.shot{flex:0 0 250px;scroll-snap-align:start}
.shot .frame{border-radius:34px;border:1px solid var(--line2);background:#000;padding:8px;box-shadow:0 30px 60px -40px rgba(0,0,0,1),inset 0 0 0 1px rgba(255,255,255,.04);transition:transform .5s var(--ease),border-color .3s}
.shot:hover .frame{transform:translateY(-6px);border-color:rgba(255,255,255,.4)}
.shot img{display:block;width:100%;height:auto;border-radius:27px}
.shot .cap{margin-top:14px}
.shot .cap b{display:block;font-weight:500;font-size:15px}
.shot .cap span{font-size:13px;color:var(--muted);line-height:1.5;display:block;margin-top:3px}
.tour .fade{position:absolute;top:0;bottom:0;width:60px;pointer-events:none;z-index:1}
.tour .fade.l{left:0;background:linear-gradient(90deg,#000,transparent)}.tour .fade.r{right:0;background:linear-gradient(270deg,#000,transparent)}
.tour-nav{display:flex;gap:8px;justify-content:flex-end;margin-top:-6px}
.tour-nav button{width:40px;height:40px;border-radius:50%;border:1px solid var(--line2);background:transparent;color:#fff;cursor:pointer;font-size:16px;transition:all .2s}
.tour-nav button:hover{background:#fff;color:#000}
/* signature flow */
.sig{display:grid;grid-template-columns:1.1fr 1fr;gap:14px;align-items:stretch}
.sig .big{border-radius:var(--r);border:1px solid var(--line);background:var(--card);padding:36px;display:flex;flex-direction:column;justify-content:space-between;gap:26px}
.sig .big h3{font-size:clamp(26px,3vw,36px);letter-spacing:-.035em}
.sig .big p{color:var(--muted);font-size:16px;max-width:44ch}
.sig .steps{display:grid;gap:14px}
.sig .s{border-radius:var(--r);border:1px solid var(--line);background:var(--card);padding:22px 24px;display:grid;grid-template-columns:44px 1fr;gap:16px;align-items:start}
.sig .s .n{width:36px;height:36px;border-radius:10px;border:1px solid var(--line2);display:grid;place-items:center;font-family:var(--mono);font-size:12px;color:var(--silver)}
.sig .s b{display:block;font-weight:500;font-size:16px;margin-bottom:4px}.sig .s span{color:var(--muted);font-size:14px}
@media(max-width:820px){.sig{grid-template-columns:1fr}}
/* faq */
.faq{display:grid;gap:8px;max-width:820px}
.faq details{border-radius:12px;border:1px solid var(--line);background:var(--card);transition:border-color .3s}
.faq details[open]{border-color:var(--line2)}
.faq summary{list-style:none;cursor:pointer;padding:18px 22px;font-weight:500;font-size:16px;display:flex;justify-content:space-between;gap:16px;align-items:center}
.faq summary::-webkit-details-marker{display:none}
.faq summary::after{content:"+";font-size:20px;color:var(--muted);transition:transform .3s;flex:none}
.faq details[open] summary::after{transform:rotate(45deg)}
.faq .a{padding:0 22px 20px;color:var(--muted);font-size:15px;max-width:66ch}
/* demo form */
.demo{border-top:1px solid var(--line)}
.demo .wrap{display:grid;grid-template-columns:1fr 1fr;gap:56px;align-items:start}
.demo h2{font-size:clamp(32px,4.4vw,52px);margin:18px 0 16px}
.demo .lead{color:var(--muted);font-size:17px;max-width:44ch;margin-bottom:26px}
.demo ul{list-style:none;margin:0;padding:0;display:grid;gap:10px;color:var(--muted);font-size:14.5px}
.demo li{display:flex;gap:10px}.demo li::before{content:"—";color:var(--dim)}
form.card{display:grid;gap:14px}
.f{display:grid;gap:6px}.f label{font-size:12.5px;color:var(--muted)}
.f input,.f textarea{background:#000;border:1px solid var(--line2);border-radius:8px;color:#fff;padding:11px 13px;font-family:var(--sans);font-size:14px;width:100%;transition:border-color .2s}
.f input:focus,.f textarea:focus{outline:none;border-color:rgba(255,255,255,.5)}.f textarea{min-height:96px;resize:vertical}
.f input::placeholder,.f textarea::placeholder{color:var(--dim)}
.f2{display:grid;grid-template-columns:1fr 1fr;gap:12px}
.chips{display:flex;flex-wrap:wrap;gap:8px}
.chip{font-size:13px;padding:7px 12px;border-radius:999px;border:1px solid var(--line2);color:var(--muted);cursor:pointer;background:transparent;font-family:var(--sans);transition:all .2s}
.chip.on{background:#fff;color:#000;border-color:#fff}
.done{font-family:var(--mono);font-size:12px;color:var(--silver);min-height:18px}
@media(max-width:820px){.demo .wrap{grid-template-columns:1fr}.f2{grid-template-columns:1fr}}
@media(max-width:960px){.guide-grid{grid-template-columns:1fr}.stage{position:static}.connect{grid-template-columns:1fr}.phone{margin:0 auto}}
@media(max-width:600px){.sup{grid-template-columns:1fr}.led{grid-template-columns:auto 1fr}.led .when{display:none}}
'''
HASREP_JS='''
/* app tour arrows */
(function(){const t=document.getElementById('track');if(!t)return;const step=()=>t.querySelector('.shot').getBoundingClientRect().width+18;
document.getElementById('tPrev').addEventListener('click',()=>t.scrollBy({left:-step(),behavior:'smooth'}));document.getElementById('tNext').addEventListener('click',()=>t.scrollBy({left:step(),behavior:'smooth'}))})();
/* demo form (Web3Forms) */
(function(){const chips=document.getElementById('dchips'),form=document.getElementById('demoform');if(!form)return;const done=document.getElementById('ddone'),send=document.getElementById('dsend');
chips.addEventListener('click',e=>{const b=e.target.closest('.chip');if(!b)return;chips.querySelectorAll('.chip').forEach(c=>c.classList.remove('on'));b.classList.add('on')});
form.addEventListener('submit',async e=>{e.preventDefault();done.className='done';done.textContent='Gönderiliyor…';send.disabled=true;document.getElementById('dtype').value=chips.querySelector('.on').textContent;const name=document.getElementById('dn').value.trim();
  try{const r=await fetch(form.action,{method:'POST',headers:{'Accept':'application/json'},body:new FormData(form)});const j=await r.json();if(r.ok&&j.success){done.textContent=`Teşekkürler ${name} — demo talebiniz ulaştı, 48 saat içinde dönüyoruz.`;form.reset();chips.querySelectorAll('.chip').forEach((c,i)=>c.classList.toggle('on',i===0))}else throw new Error()}
  catch(err){done.className='done err';done.textContent='Gönderilemedi. Lütfen tekrar deneyin ya da WhatsApp’tan yazın.'}finally{send.disabled=false}})})();
(function(){
  const $=id=>document.getElementById(id);
  const pod=$('pod'),led=$('led'),sState=$('sState'),sLed=$('sLed'),sConn=$('sConn'),sBat=$('sBat'),phone=$('phone'),prow=$('prow'),steps=[...$('steps').children];
  const C={blue:'#4DA3FF',red:'#FF5A5A',green:'#4FE08A',off:'#2A2A2E'};
  const dev={awake:false,conn:false,charging:false,full:false};
  let t=[];const later=(f,ms)=>t.push(setTimeout(f,ms));const clear=()=>{t.forEach(clearTimeout);t=[]};
  const idle=()=>{prow.className='row2';prow.innerHTML='<span>Cihaz aranmadı</span><span></span>';steps.forEach(s=>s.className='st');phone.classList.remove('hint')};
  function setLed(name,label,pulse){led.style.background=C[name];led.style.boxShadow=name==='off'?'none':'0 0 8px 2px '+C[name]+',0 0 22px '+C[name];pod.classList.toggle('lit',name!=='off');pod.classList.toggle('pulse',!!pulse);pod.style.setProperty('--ledc',C[name]);sLed.innerHTML=`<i style="${name==='off'?'':'background:'+C[name]+';box-shadow:0 0 10px '+C[name]}"></i>${label}`;document.querySelectorAll('.led').forEach(b=>b.classList.toggle('on',b.dataset.led===name))}
  function render(){
    sState.innerHTML=`<i style="${dev.awake?'background:#fff':''}"></i>${dev.awake?'Uyanık':'Uyku modunda'}`;
    sConn.textContent=dev.conn?'Uygulamaya bağlı':'Bağlı değil';
    sBat.textContent=dev.full?'%100':dev.charging?'%72 · şarj oluyor':'%72';
    if(dev.conn)setLed('blue','Mavi · bağlı');else if(dev.full)setLed('green','Yeşil · şarj dolu');else if(dev.charging)setLed('red','Kırmızı · şarjda',true);else setLed('off','Kapalı');
  }
  document.querySelectorAll('.led').forEach(b=>b.addEventListener('click',()=>{clear();const k=b.dataset.led;dev.awake=true;
    if(k==='blue'){dev.conn=true;dev.charging=false;dev.full=false;steps.forEach(s=>s.className='st done');prow.className='row2 ok';prow.innerHTML='<span>Has Rep · A1F3</span><span class="b">Bağlı</span>'}
    else{dev.conn=false;idle();dev.charging=k==='red';dev.full=k==='green'}
    render()}));
  $('shake').addEventListener('click',()=>{clear();pod.classList.remove('shake');void pod.offsetWidth;pod.classList.add('shake');$('wakeHint').innerHTML='Hareket algılandı — <b>uyanıyor</b>';
    later(()=>{dev.awake=true;dev.charging=false;dev.full=false;render();setLed('blue','Uyanma sinyali');later(()=>{render();$('wakeHint').innerHTML='Cihaz <b>uyanık</b> · bağlantıya hazır'},450)},500)});
  $('pair').addEventListener('click',()=>{clear();if(!dev.awake){$('wakeHint').innerHTML='Önce cihazı <b>sallayın</b>';pod.classList.remove('shake');void pod.offsetWidth;pod.classList.add('shake');dev.awake=true}
    dev.conn=false;dev.charging=false;dev.full=false;render();idle();steps[0].className='st active';prow.innerHTML='<span>Uygulama açıldı</span><span></span>';
    later(()=>{steps[0].className='st done';steps[1].className='st active';phone.classList.add('hint');prow.innerHTML='<span>Aranıyor…</span><span></span>'},900);
    later(()=>{phone.classList.remove('hint');prow.className='row2 found';prow.innerHTML='<span>Has Rep · A1F3</span><span>Eşleştir</span>'},2100);
    later(()=>{steps[1].className='st done';steps[2].className='st active'},2400);
    later(()=>{steps[2].className='st done';dev.conn=true;render();prow.className='row2 ok';prow.innerHTML='<span>Has Rep · A1F3</span><span class="b">Bağlı</span>'},3300);
  });
  $('unpair').addEventListener('click',()=>{clear();dev.conn=false;idle();render()});
  render();
})();'''

GUIDE='''<section class="guide" id="kilavuz" aria-labelledby="kilavuz-h"><div class="wrap">
  <div class="head rv"><div><div class="eyebrow">Kullanım kılavuzu &amp; destek</div><h2 id="kilavuz-h"><span class="line"><span>Cihazınızı</span></span><span class="line"><span>iki dakikada tanıyın.</span></span></h2></div><p>LED ne söylüyor, cihaz nasıl uyanır, uygulamaya nasıl bağlanır. Kartlardaki düğmeler soldaki cihazı canlı olarak etkiler.</p></div>
  <div class="guide-grid rv">
    <aside class="stage" aria-label="Has Rep cihaz durumu">
      <div class="pod" id="pod"><div class="halo"></div>
        <img src="hasrep-urun-sq.jpg" width="900" height="900" alt="Has Rep sensörü" decoding="async"><span id="led" class="leddot" aria-hidden="true"></span>
      </div>
      <div class="status"><div><div class="k">Durum</div><div class="v" id="sState"><i></i>Uyku modunda</div></div><div><div class="k">LED</div><div class="v" id="sLed"><i></i>Kapalı</div></div><div><div class="k">Bağlantı</div><div class="v" id="sConn">Bağlı değil</div></div><div><div class="k">Şarj</div><div class="v" id="sBat">%72</div></div></div>
    </aside>
    <div class="gcards">
      <article class="gc"><div class="k"><span>01 — LED durum göstergeleri</span><span>Tıklayın</span></div><h3>LED ne anlatıyor?</h3><p>Cihazın üstündeki tek LED üç durumu gösterir. Bir satıra tıklayarak cihazda görün.</p>
        <div class="leds"><button type="button" class="led" data-led="blue" style="--c:var(--led-blue)"><span class="dot"></span><span><b>Mavi LED</b><span>Cihaz telefona / uygulamaya bağlıyken yanar.</span></span><span class="when">Bağlı</span></button><button type="button" class="led charging" data-led="red" style="--c:var(--led-red)"><span class="dot"></span><span><b>Kırmızı LED</b><span>Cihaz şarjdayken yanar.</span></span><span class="when">Şarjda</span></button><button type="button" class="led" data-led="green" style="--c:var(--led-green)"><span class="dot"></span><span><b>Yeşil LED</b><span>Cihazın şarjı tam doluyken yanar.</span></span><span class="when">Şarj full</span></button></div></article>
      <article class="gc"><div class="k"><span>02 — Cihazı uyandırma</span><span>Shake</span></div><h3>Sallayın, uyanır.</h3><p>Has Rep kullanılmadığında pili korumak için uyku moduna geçer. Uyandırmak için düğmeye basmanız gerekmez: cihazı <b style="color:#fff;font-weight:500">hafifçe sallamak</b> yeterlidir. LED kısa bir kez yanıp söner ve cihaz bağlantıya hazır hale gelir.</p>
        <div class="wake"><button type="button" class="btn" id="shake">Cihazı salla</button><span class="hint" id="wakeHint">Hareket sensörü <b>bekliyor</b></span></div></article>
      <article class="gc"><div class="k"><span>03 — Bağlantı rehberi</span><span>iOS</span></div><h3>Üç adımda eşleştirin.</h3><p>Cihazı telefona bağlamak için Has Rep mobil uygulamasını açın, sağ üst köşedeki pod bağlama kısmına tıklayın ve cihazınızı eşleştirin.</p>
        <div class="connect"><div><div class="steps3" id="steps"><div class="st"><div class="n">1</div><div><b>Has Rep uygulamasını açın</b><span>Bluetooth’un açık ve cihazın uyanık olduğundan emin olun.</span></div></div><div class="st"><div class="n">2</div><div><b>Sağ üstteki pod bağlama simgesine dokunun</b><span>Uygulama yakındaki Has Rep cihazlarını tarar.</span></div></div><div class="st"><div class="n">3</div><div><b>Cihazınızı seçip eşleştirin</b><span>Bağlandığında cihazdaki LED maviye döner.</span></div></div></div>
          <div class="actions"><button type="button" class="btn primary" id="pair">Eşleştirmeyi simüle et</button><button type="button" class="btn" id="unpair">Bağlantıyı kes</button></div></div>
          <div class="phone" id="phone" aria-hidden="true"><div class="bar"><span>HAS REP</span><div class="podbtn">◎</div></div><div class="scr"><div>Cihazlar</div><div class="row2" id="prow"><span>Cihaz aranmadı</span><span></span></div></div></div></div></article>
    </div>
  </div>
  <div class="sup rv"><a href="#sss"><b>Sık sorulan sorular</b><span>Ölçüm, sayım, platform, pil</span><span class="mono">SSS bölümü ↓</span></a><a href="mailto:hasrep@canhastech.com"><b>Destek ekibi</b><span>Cihaz veya uygulama sorunları için</span><span class="mono">hasrep@canhastech.com</span></a><a href="index.html#iletisim"><b>Kulüp &amp; toplu kullanım</b><span>Antrenör paneli ve çoklu cihaz kurulumu</span><span class="mono">İletişim formu →</span></a></div>
'''

def hasrep_page():
    body=f'''{nav('hasrep')}
<header class="hero">
  <div class="wrap">
    <div class="crumb up"><a href="index.html">CanhasTech</a><i>/</i><a href="index.html#projeler">Ekosistem</a><i>/</i><span style="color:#fff">Has Rep</span></div>
    <img class="brand up" src="hasrep-logo.jpg" width="900" height="609" alt="Has Rep logosu" style="animation-delay:.1s" decoding="async">
    <h1><span class="line"><span data-kinetic data-delay=".15">Has Rep</span></span><span class="line thin"><span data-kinetic data-delay=".4" data-step="0.018">Ağırlık antrenmanlarını veriye dönüştürün</span></span></h1>
    <p class="lede up" style="animation-delay:1s">Bara takılan VBT cihazı hareket hızını ölçer ve tekrarları sayar; uygulama form analizi yapar, yapay zekâ ile antrenman oluşturur ve analiz eder.</p>
    <p class="sub up" style="animation-delay:1.1s">Sporcu ve antrenör için tek sistem: sensör pod + iOS uygulaması. Antrenmanı başlat, telefonu bırak.</p>
    <div class="cta-row up" style="animation-delay:1.2s"><a class="btn primary" href="#demo">Demo talep et</a><a class="btn" href="#uygulama">Uygulamayı gör</a><a class="btn" href="#kilavuz">Kullanım kılavuzu</a></div>
    <div class="product up" style="animation-delay:1.35s"><img src="hasrep-urun.jpg" width="1086" height="680" loading="eager" fetchpriority="high" decoding="async" alt="Has Rep sensörü"></div>
  </div>
</header>
<main>
<section id="vbt" style="padding-top:40px" aria-labelledby="vbt-h"><div class="wrap">
  <div class="head rv"><div><div class="eyebrow">VBT sistemi</div><h2 id="vbt-h"><span class="line"><span>Hız temelli antrenman,</span></span><span class="line"><span>cihazdan uygulamaya.</span></span></h2></div><p>Hız temelli antrenman (VBT) yükü değil bar hızını yönetir. Has Rep bu hızı bara oturan kompakt sensörden okur; uygulama veriyi antrenmana çevirir.</p></div>
  <div class="pillars rv">
    <div class="pillar"><div class="ic"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5"><path d="M4 16a8 8 0 0 1 16 0"/><path d="M12 16l4-5"/><circle cx="12" cy="16" r="1.5"/></svg></div><h3>Hareket hızı ölçümü</h3><p>Her tekrarın kaldırış hızını okur. Aynı yükte bar yavaşladıysa yorgunluk başlamıştır; hızlandıysa formdasınız.</p></div>
    <div class="pillar"><div class="ic"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5"><path d="M5 18v-5M10 18V8M15 18v-8M20 18V5"/></svg></div><h3>Otomatik tekrar sayımı</h3><p>Tekrarları cihaz kendisi ayırır ve sayar. Yarım tekrarı ve yeniden konumlanmayı saymaz; telefon cebinizde kalabilir.</p></div>
    <div class="pillar"><div class="ic"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5"><circle cx="12" cy="5" r="2"/><path d="M12 7v6l-3 6M12 13l3 6M8 10l4-2 4 2"/></svg></div><h3>Uzamsal form analizi</h3><p>Bar yolunu ve hareket kalitesini üç boyutta izler; sapan tekrarı işaretler, antrenöre ham izi bırakır.</p></div>
    <div class="pillar"><div class="ic"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5"><path d="M9 4a3 3 0 0 0-3 3v1a3 3 0 0 0-2 3 3 3 0 0 0 2 3v1a3 3 0 0 0 3 3h1V4H9zM15 4a3 3 0 0 1 3 3v1a3 3 0 0 1 2 3 3 3 0 0 1-2 3v1a3 3 0 0 1-3 3h-1V4h1z"/></svg></div><h3>Yapay zekâ: oluştur &amp; analiz et</h3><p>Uygulama sizin verinizle antrenman programı oluşturur, her antrenmanı analiz eder ve gelişimi raporlar.</p></div>
  </div>
  <div class="sig rv">
    <div class="big"><div><div class="eyebrow">İmza özellik</div><h3 style="margin-top:14px">Antrenmanı başlat,<br>telefonu bırak.</h3></div><p>Antrenman boyunca telefona dokunmazsınız. Pod her tekrarı kendi hafızasına kaydeder; bağlantı kopsa bile veri kaybolmaz. Antrenman bitince senkronize edilir, uygulama emin olamadığı birkaç şeyi kart kart sorar — sağa kaydır doğru, sola kaydır düzelt. 30 saniye, bitti.</p></div>
    <div class="steps">
      <div class="s"><div class="n">01</div><div><b>Antrenmanı başlat</b><span>Pod'u bara tak, uygulamada tek düğme. Sonra telefon cebe ya da dolaba.</span></div></div>
      <div class="s"><div class="n">02</div><div><b>Antrenmanını yap</b><span>Set, tekrar ve dinlenme otomatik ayrılır. Telefon yakınsa canlı bar hızı önizlemesi akar.</span></div></div>
      <div class="s"><div class="n">03</div><div><b>Bitir, kaydır, onayla</b><span>Senkronizasyon sonrası şüpheli tekrarlar kartla sorulur. Her rep doğrulanmış — sahte rep yok.</span></div></div>
    </div>
  </div>
  <div class="gallery rv">
    <figure><img src="hasrep-box.jpg" width="1100" height="905" loading="lazy" decoding="async" alt="Has Rep kutusu ve üzerinde sensör — Every rep counts"><figcaption>Every rep counts · Train · Measure · Improve</figcaption></figure>
    <figure><img src="hasrep-urun-sq.jpg" width="900" height="900" loading="lazy" decoding="async" alt="Has Rep sensörü masa üzerinde"><figcaption>Manyetik klips · Bar olan her yerde</figcaption></figure>
  </div>
</div></section>

<section id="uygulama" style="padding-top:0" aria-labelledby="app-h"><div class="wrap">
  <div class="head rv"><div><div class="eyebrow">Uygulama turu</div><h2 id="app-h"><span class="line"><span>Antrenman ekranından</span></span><span class="line"><span>rekor bildirimine.</span></span></h2></div><p>Gerçek uygulama ekranları. Canlı bar hızı, set özetleri, form analizi, kaydırmalı onay, kişisel rekorlar ve tahmini 1RM.</p></div>
  <div class="tour rv"><div class="fade l"></div><div class="fade r"></div>
    <div class="track" id="track">
      <figure class="shot"><div class="frame"><img src="app-antrenman.jpg" width="600" height="1304" loading="lazy" decoding="async" alt="Aktif antrenman ekranı: bar hızı 0.39 m/s, güç 239 W, form %83"></div><figcaption class="cap"><b>Canlı antrenman</b><span>Bar hızı, güç, form skoru ve RPE — set sürerken.</span></figcaption></figure>
      <figure class="shot"><div class="frame"><img src="app-set.jpg" width="600" height="1304" loading="lazy" decoding="async" alt="Set geçmişi: her setin ortalama hızı ve tekrar sayısı"></div><figcaption class="cap"><b>Set özeti</b><span>Her setin ortalama hızı ve tekrarı; hız düşüşü bir bakışta.</span></figcaption></figure>
      <figure class="shot"><div class="frame"><img src="app-form.jpg" width="600" height="1304" loading="lazy" decoding="async" alt="Form analizi: bar eğimi ve rep tutarlılığı grafikleri"></div><figcaption class="cap"><b>Form analizi</b><span>Bar eğimi, tekrar tutarlılığı ve sticking point.</span></figcaption></figure>
      <figure class="shot"><div class="frame"><img src="app-onay.jpg" width="600" height="1304" loading="lazy" decoding="async" alt="Kaydırmalı onay kartı: bu tekrar sayılsın mı?"></div><figcaption class="cap"><b>Kaydırmalı onay</b><span>Sağa kaydır say, sola kaydır sayma. Sadece şüpheliler sorulur.</span></figcaption></figure>
      <figure class="shot"><div class="frame"><img src="app-rekor.jpg" width="600" height="1304" loading="lazy" decoding="async" alt="Yeni kişisel rekor bildirimi"></div><figcaption class="cap"><b>Rekor bildirimi</b><span>Hız ve yük rekorları antrenman sonunda kutlanır.</span></figcaption></figure>
      <figure class="shot"><div class="frame"><img src="app-istatistik.jpg" width="600" height="1304" loading="lazy" decoding="async" alt="İstatistik: haftalık hacim trendi, kişisel rekorlar, tahmini 1RM"></div><figcaption class="cap"><b>İstatistik &amp; 1RM</b><span>Haftalık hacim, kişisel rekorlar, tahmini 1RM.</span></figcaption></figure>
      <figure class="shot"><div class="frame"><img src="app-gecmis.jpg" width="600" height="1304" loading="lazy" decoding="async" alt="Antrenman geçmişi listesi"></div><figcaption class="cap"><b>Geçmiş</b><span>Tüm antrenmanlar; süre, set ve toplam tonaj.</span></figcaption></figure>
    </div>
  </div>
  <div class="tour-nav rv"><button type="button" id="tPrev" aria-label="Önceki">←</button><button type="button" id="tNext" aria-label="Sonraki">→</button></div>
</div></section>

<section id="sss" style="padding-top:0" aria-labelledby="sss-h"><div class="wrap">
  <div class="head rv"><div><div class="eyebrow">Sık sorulanlar</div><h2 id="sss-h"><span class="line"><span>Merak edilenler.</span></span></h2></div><p>Cevabını bulamadığınız soru için WhatsApp ya da <a href="mailto:hasrep@canhastech.com" style="color:#fff;border-bottom:1px solid var(--line2)">hasrep@canhastech.com</a>.</p></div>
  <div class="faq rv"><details><summary>Has Rep tam olarak ne ölçüyor?</summary><div class="a">Ortalama konsantrik bar hızı (m/s), set içi hız kaybı yüzdesi ve tekrar sayısı çekirdek metriklerdir. Bunlara tepe hız, güç (W), hız bölgeleri ve tahmini 1RM eklenir. Form tarafında bar eğimi, tekrar tutarlılığı ve stabilite gösterilir.</div></details>\n<details><summary>Antrenman sırasında telefonu yanımda tutmam gerekiyor mu?</summary><div class="a">Hayır. Pod her şeyi kendi hafızasına kaydeder; telefon cepte, dolapta ya da evde kalabilir. Antrenman sonunda senkronize edersiniz. Telefon yakınsa ek olarak canlı önizleme de akar.</div></details>\n<details><summary>Tekrar sayımı ne kadar güvenilir? Sahte tekrar sayar mı?</summary><div class="a">Bar'ı alıp bırakma gibi hareketler filtrelenir; uygulamanın emin olamadığı tekrarlar antrenman sonunda kaydırmalı onayla size sorulur. Böylece kayıtlı her tekrar doğrulanmış olur.</div></details>\n<details><summary>Hangi hareketlerde çalışır?</summary><div class="a">Bar olan her harekette: squat, bench press, deadlift, row, overhead press ve olimpik kaldırışlar. Manyetik klips saniyeler içinde takılır. İlk sürümde temel hareketler en yüksek doğrulukla desteklenir, liste genişlemeye devam eder.</div></details>\n<details><summary>Form analizi kamera gibi milimetrik bar yolu veriyor mu?</summary><div class="a">Hayır, dürüst olalım: hareket sensörleri milimetrik bar yolu çıkaramaz. Has Rep bunun yerine yatay sapmayı bölge olarak (yeşil/sarı/kırmızı), tekrar tutarlılığını ve sallanma/stabiliteyi güvenilir biçimde ölçer.</div></details>\n<details><summary>Uygulama hangi platformda?</summary><div class="a">İlk sürüm iOS içindir. Android sürümü yol haritasında; demo formundan bekleme listesine katılabilirsiniz.</div></details>\n<details><summary>Pil ve şarj nasıl?</summary><div class="a">Pod kullanılmadığında uyku moduna geçer, sallayınca uyanır. Şarjdayken LED kırmızı, dolduğunda yeşil yanar. Kullanım kılavuzu bölümünde tüm LED durumları anlatılır.</div></details>\n<details><summary>Antrenör olarak birden fazla sporcuyu takip edebilir miyim?</summary><div class="a">Evet, kulüp ve antrenör kullanımı için çoklu cihaz kurulumu ve antrenör görünümü planlanıyor. Demo talebinde "Kulüp / antrenör" seçeneğini işaretleyin, sizinle ayrıca görüşelim.</div></details></div>
</div></section>

{GUIDE}
  {pnav('hasrep')}
</div></section>
<section class="demo" id="demo"><div class="wrap rv">
  <div><div class="eyebrow">Demo &amp; erken erişim</div><h2><span class="line"><span>Has Rep’i</span></span><span class="line"><span>kendiniz deneyin.</span></span></h2>
    <p class="lead">Bireysel sporcu, antrenör ya da kulüp — formu doldurun, size demo planlayalım ve ilk parti sevkiyatta öncelik verelim.</p>
    <ul><li>Cihaz + uygulama ile canlı demo (İzmir’de yerinde, diğer şehirlerde online)</li><li>Erken erişim fiyatı ve teslimat takvimi</li><li>Kulüpler için çoklu cihaz ve antrenör paneli planı</li></ul>
    <p style="margin-top:26px"><a class="btn" href="hasrepkk.html">Kullanım kılavuzu →</a></p></div>
  <form class="card" id="demoform" action="https://api.web3forms.com/submit" method="POST"><input type="hidden" name="access_key" value="{WEB3FORMS_KEY}"><input type="hidden" name="subject" value="Has Rep — demo / erken erişim talebi"><input type="hidden" name="from_name" value="canhastech.com/hasrep"><input type="hidden" name="profil" id="dtype" value="Bireysel sporcu"><input type="checkbox" name="botcheck" class="hp" tabindex="-1" autocomplete="off">
    <div class="f2"><div class="f"><label for="dn">Ad Soyad <span class="req">*</span></label><input id="dn" name="ad_soyad" required autocomplete="name" placeholder="Adınız"></div><div class="f"><label for="de">E-posta <span class="req">*</span></label><input id="de" name="email" type="email" required autocomplete="email" placeholder="ornek@kulup.com"></div></div>
    <div class="f"><label for="dp">Telefon (isteğe bağlı)</label><input id="dp" name="telefon" type="tel" autocomplete="tel" placeholder="+90 5xx xxx xx xx"></div>
    <div class="f"><label>Profil</label><div class="chips" id="dchips"><button type="button" class="chip on">Bireysel sporcu</button><button type="button" class="chip">Antrenör</button><button type="button" class="chip">Kulüp / akademi</button><button type="button" class="chip">Android bekleme listesi</button></div></div>
    <div class="f"><label for="dm">Not</label><textarea id="dm" name="mesaj" placeholder="Hangi sporu yapıyorsunuz, kaç sporcu, ne zaman?"></textarea></div>
    <label class="consent"><input type="checkbox" required name="kvkk"> <span>Bilgilerimin demo talebiyle ilgili iletişim amacıyla işlenmesini kabul ediyorum. <a href="kvkk.html" target="_blank" rel="noopener">KVKK aydınlatma metni</a></span></label>
    <button class="btn primary" type="submit" id="dsend">Demo talep et</button><div class="done" id="ddone"></div></form>
</div></section>

{band()}
</main>'''
    prod={"@context":"https://schema.org","@type":"Product","name":"Has Rep","brand":{"@type":"Brand","name":"CanhasTech"},"image":[SITE+"hasrep-urun-sq.jpg",SITE+"hasrep-box.jpg"],"description":"Ağırlık antrenmanlarını veriye dönüştüren VBT cihazı ve uygulaması: hareket hızı ölçümü, otomatik tekrar sayımı, uzamsal form analizi, yapay zekâ ile antrenman oluşturma ve analiz.","url":SITE+"hasrep.html","category":"Spor teknolojisi"}
    faq=[{'q':q,'a':a.replace('\\u0027',"'")} for q,a in [('Has Rep tam olarak ne ölçüyor?', 'Ortalama konsantrik bar hızı (m/s), set içi hız kaybı yüzdesi ve tekrar sayısı çekirdek metriklerdir. Bunlara tepe hız, güç (W), hız bölgeleri ve tahmini 1RM eklenir. Form tarafında bar eğimi, tekrar tutarlılığı ve stabilite gösterilir.'), ('Antrenman sırasında telefonu yanımda tutmam gerekiyor mu?', 'Hayır. Pod her şeyi kendi hafızasına kaydeder; telefon cepte, dolapta ya da evde kalabilir. Antrenman sonunda senkronize edersiniz. Telefon yakınsa ek olarak canlı önizleme de akar.'), ('Tekrar sayımı ne kadar güvenilir? Sahte tekrar sayar mı?', 'Bar\\u0027ı alıp bırakma gibi hareketler filtrelenir; uygulamanın emin olamadığı tekrarlar antrenman sonunda kaydırmalı onayla size sorulur. Böylece kayıtlı her tekrar doğrulanmış olur.'), ('Hangi hareketlerde çalışır?', 'Bar olan her harekette: squat, bench press, deadlift, row, overhead press ve olimpik kaldırışlar. Manyetik klips saniyeler içinde takılır. İlk sürümde temel hareketler en yüksek doğrulukla desteklenir, liste genişlemeye devam eder.'), ('Form analizi kamera gibi milimetrik bar yolu veriyor mu?', 'Hayır, dürüst olalım: hareket sensörleri milimetrik bar yolu çıkaramaz. Has Rep bunun yerine yatay sapmayı bölge olarak (yeşil/sarı/kırmızı), tekrar tutarlılığını ve sallanma/stabiliteyi güvenilir biçimde ölçer.'), ('Uygulama hangi platformda?', 'İlk sürüm iOS içindir. Android sürümü yol haritasında; demo formundan bekleme listesine katılabilirsiniz.'), ('Pil ve şarj nasıl?', 'Pod kullanılmadığında uyku moduna geçer, sallayınca uyanır. Şarjdayken LED kırmızı, dolduğunda yeşil yanar. Kullanım kılavuzu bölümünde tüm LED durumları anlatılır.'), ('Antrenör olarak birden fazla sporcuyu takip edebilir miyim?', 'Evet, kulüp ve antrenör kullanımı için çoklu cihaz kurulumu ve antrenör görünümü planlanıyor. Demo talebinde "Kulüp / antrenör" seçeneğini işaretleyin, sizinle ayrıca görüşelim.')]]
    faqld={"@context":"https://schema.org","@type":"FAQPage","mainEntity":[{"@type":"Question","name":x['q'],"acceptedAnswer":{"@type":"Answer","text":x['a']}} for x in faq]}
    meta=seo_head('hasrep.html','Has Rep — VBT cihazı ve kullanım kılavuzu | CanhasTech','Has Rep: bara takılan VBT cihazı hareket hızını ölçer ve tekrarları sayar; uygulama form analizi yapar, yapay zekâ ile antrenman oluşturur. LED göstergeleri, cihazı uyandırma ve uygulamaya bağlanma rehberi.',[prod,faqld,crumbs('Has Rep','hasrep.html')],preload='hasrep-urun.jpg',image='og-hasrep.jpg')
    return shell('Has Rep — VBT cihazı ve kullanım kılavuzu | CanhasTech',body,HASREP_CSS,HASREP_JS,meta=meta)

# ---------------------------------------------------------------- OTHER PROJECT PAGES
DETAIL={
 'citydiamond':dict(
   h1='Turizm firması web sitesi',lede='Araç filosu, transfer ve tur hizmetleri, rezervasyon talebi — İzmir merkezli turizm firması için kurumsal site.',
   sub='Hızlı açılan, mobil öncelikli, arama motorlarında görünen ve WhatsApp ile anında iletişime bağlanan bir vitrin.',
   feats=[('Hizmet & filo vitrini','VIP transfer, havalimanı transferi, günlük turlar ve araç filosu; her hizmet için ayrı sayfa.','Web'),('Rezervasyon talebi','Tarih, güzergâh ve yolcu sayısıyla talep formu; WhatsApp ve telefonla anında iletişim.','Dönüşüm'),('SEO & performans','Turizm aramalarında görünürlük için yapılandırılmış içerik, hızlı yükleme, mobil uyum.','Görünürlük')],
   steps=[('Keşif','Hizmetler, güzergâhlar ve hedef müşteri birlikte netleştirildi.'),('Tasarım','Marka kimliğine (altın / siyah) uygun, mobil öncelikli arayüz.'),('Geliştirme','Statik, hızlı ve yönetmesi kolay site; rezervasyon talebi entegrasyonu.'),('Yayın','Alan adı, SEO ve analitik kurulumu; canlı takip.')],
   metrics=[('Mobil','öncelikli'),('WhatsApp','anında iletişim'),('SEO','turizm aramaları'),('Canlı','citydiamondturizm.com.tr')]),
 'shuttlemerkezi':dict(
   h1='Shuttle rezervasyon platformu',lede='Rezervasyondan sefere, araçtan sürücüye: shuttle operasyonunun tamamı tek panelde.',
   sub='Oteller, acenteler ve yolcular aynı altyapıyı kullanır; operasyon ekibi her seferi canlı görür.',
   feats=[('Online rezervasyon','Yolcu ve acente için web rezervasyonu, anlık fiyatlandırma, kapasite kontrolü.','Web'),('Sefer & araç planlama','Araç, sürücü ve rota planlaması; doluluk ve boş koltuk takibi.','Panel'),('Acente & otel entegrasyonu','Partner girişleri, komisyon ve mutabakat raporları.','Entegrasyon')],
   steps=[('Talep','Otel, acente veya yolcu rezervasyonu açar; sistem kapasiteyi kontrol eder.'),('Planlama','Operasyon ekibi seferi araca ve sürücüye atar; yolcuya bilgi gider.'),('Sefer','Sürücü uygulamadan listeyi görür; teslim ve tamamlanma kaydedilir.'),('Mutabakat','Günlük ve aylık raporlar; acente komisyonları otomatik hesaplanır.')],
   metrics=[('7/24','rezervasyon alımı'),('1','panelden tüm filo'),('3','rol: yolcu · acente · operasyon'),('Web','+ sürücü uygulaması')]),
 'cagriaslanfit':dict(
   h1='Fitness mobil uygulaması',lede='Kişiye özel programlar, ilerleme takibi ve koç-sporcu iletişimi tek uygulamada.',
   sub='Koç programı yazar, sporcu uygular, gelişim her iki tarafta da görünür.',
   feats=[('Kişiye özel program','Antrenman ve beslenme planları; haftalık düzenlenir, sporcuya bildirim gider.','Sporcu'),('İlerleme takibi','Ölçümler, fotoğraf karşılaştırma, tamamlanan antrenman geçmişi.','Takip'),('Koç paneli & mesajlaşma','Koç tüm sporcularını tek ekranda yönetir; sorular uygulama içinde cevaplanır.','Koç')],
   steps=[('Kayıt','Sporcu hedefini ve seviyesini girer; koç profili inceler.'),('Program','Koç programı hazırlar; sporcu uygulamadan takip eder.'),('Uygulama','Antrenman tamamlanır, ölçümler girilir; koç anında görür.'),('Revizyon','Gelişime göre program güncellenir; döngü devam eder.')],
   metrics=[('iOS','+ Android'),('1','koç paneli'),('Haftalık','program döngüsü'),('Anlık','mesajlaşma')]),
 'cemilhasmedikal':dict(
   h1='Medikal yazılımı',lede='Ürün kataloğu, sipariş ve saha operasyonlarının dijital yönetimi.',
   sub='Medikal ürün tedarikinde stok, sipariş ve saha ekibini tek sistemde toplar.',
   feats=[('Ürün kataloğu & stok','Ürün, seri, son kullanma ve depo bazlı stok; kritik seviye uyarıları.','Yazılım'),('Sipariş & teslimat','Müşteri siparişi, hazırlama, sevkiyat ve teslim onayı tek akışta.','Operasyon'),('Saha ekibi uygulaması','Ziyaret planı, sipariş alma, teslimat onayı — sahadan mobil.','Mobil')],
   steps=[('Katalog','Ürünler ve stoklar sisteme tanımlanır; fiyat listeleri yönetilir.'),('Sipariş','Müşteri veya saha ekibi sipariş açar; stok otomatik ayrılır.'),('Sevkiyat','Hazırlama ve sevkiyat takibi; teslimde mobil onay.'),('Raporlama','Satış, stok devir ve saha performans raporları.')],
   metrics=[('1','merkezi katalog'),('Seri','ve SKT takibi'),('Mobil','saha uygulaması'),('Canlı','stok görünürlüğü')]),
 'tbiathletics':dict(
   h1='Performans app’i',lede='Sporcu verileri, antrenman yükü ve gelişim — antrenör için tek ekran.',
   sub='Atletizm ve takım sporlarında test sonuçlarını, yükü ve toparlanmayı birlikte okur.',
   feats=[('Sporcu profilleri','Test sonuçları, ölçümler ve sakatlık geçmişi tek profilde.','Veri'),('Yük & toparlanma','Günlük antrenman yükü, RPE ve toparlanma göstergeleri; aşırı yük uyarısı.','Takip'),('Antrenör raporları','Sporcu, grup ve dönem bazlı raporlar; dışa aktarma.','Rapor')],
   steps=[('Test','Dönem başı testleri girilir; referans değerler oluşur.'),('Yük','Her antrenman sonrası yük ve RPE kaydı; haftalık toplam izlenir.'),('Toparlanma','Uyku ve yorgunluk verisi; yeşil / sarı / kırmızı durum.'),('Rapor','Antrenör dönem raporunu tek tıkla alır.')],
   metrics=[('Sporcu','+ antrenör görünümü'),('Haftalık','yük özeti'),('3','durum: yeşil · sarı · kırmızı'),('PDF','rapor çıktısı')]),
 'hascontract':dict(
   h1='AI ile sözleşme analizi ve oluşturma',lede='Sözleşmenizi yükleyin, riskleri görün; ya da birkaç soruyla sıfırdan sözleşme oluşturun.',
   sub='Çok yakında. Hukuki danışmanlığın yerini almaz; sözleşmeyi anlamanızı ve hazırlamanızı hızlandırır.',
   feats=[('Yapay zekâ ile analiz','Sözleşmeyi yükleyin; riskli maddeler, eksik hükümler ve tek taraflı şartlar işaretlenir, sade Türkçeyle özetlenir.','Analiz'),('Sıfırdan oluşturma','Birkaç soruya cevap verin; kira, hizmet, gizlilik, iş sözleşmesi gibi türlerde taslak dakikalar içinde hazır.','Oluşturma'),('Düzenle & paylaş','Maddeleri yapay zekâ ile yeniden yazdırın, sürümleri karşılaştırın, PDF olarak paylaşın.','Belge')],
   steps=[('Yükle veya seç','Mevcut sözleşmenizi yükleyin ya da sıfırdan başlamak için sözleşme türünü seçin.'),('Analiz','Yapay zekâ maddeleri okur; risk, eksik ve dikkat gerektiren noktaları listeler.'),('Düzenle','Önerilen değişiklikleri tek dokunuşla uygulayın veya kendi ifadenizi yazın.'),('Oluştur & paylaş','Son hâli PDF olarak dışa aktarın; karşı tarafla paylaşın.')],
   metrics=[('AI','madde madde analiz'),('Dakikalar','içinde taslak'),('Sade','Türkçe özet'),('Çok yakında','iOS · Web')]),
}

def project_page(p):
    d=DETAIL[p['slug']]
    feats=''.join(f'<article class="card glass"><div class="k"><span>{k}</span></div><h3>{t}</h3><p>{x}</p></article>' for t,x,k in d['feats'])
    steps=''.join(f'<div class="row"><div class="n">0{i+1}</div><div><h3>{t}</h3><p>{x}</p></div></div>' for i,(t,x) in enumerate(d['steps']))
    metrics=''.join(f'<div class="m"><div class="v">{v}</div><div class="l">{l}</div></div>' for v,l in d['metrics'])
    body=f'''{nav(p['slug'])}
<header class="hero">
  <div class="wrap">
    <div class="crumb up"><a href="index.html">CanhasTech</a><i>/</i><a href="index.html#projeler">Ekosistem</a><i>/</i><span style="color:#fff">{p['name']}</span>{'<i>/</i><span style="color:#fff;background:#fff;color:#000;padding:2px 8px;border-radius:999px">Çok yakında</span>' if p.get('soon') else ''}</div>
    {f'<img class="plogo-hero{" pill" if p.get("pill") else ""} up" src="{p["logo"]}" alt="{p["name"]} logosu" style="animation-delay:.1s" decoding="async">' if p.get('logo') else ''}
    <h1><span class="line"><span data-kinetic data-delay=".15">{p['name']}</span></span><span class="line thin"><span data-kinetic data-delay=".4" data-step="0.02">{d['h1']}</span></span></h1>
    <p class="lede up" style="animation-delay:1s">{d['lede']}</p>
    <p class="sub up" style="animation-delay:1.1s">{d['sub']}</p>
    <div class="cta-row up" style="animation-delay:1.2s"><a class="btn primary" href="index.html#iletisim">Benzer proje için görüşelim</a>{f'<a class="btn" href="{p["site"]}" target="_blank" rel="noopener">Canlı site ↗</a>' if p.get('site') else ''}<a class="btn" href="#kapsam">Kapsam</a></div>
  </div>
</header>
<main>
<div class="metrics up" style="animation-delay:1.35s"><div class="wrap">{metrics}</div></div>
<section id="kapsam" aria-labelledby="kapsam-h"><div class="wrap">
  <div class="head rv"><div><div class="eyebrow">{p['sector']} · {p['kind']}</div><h2 id="kapsam-h"><span class="line"><span>Ne yapıyor?</span></span></h2></div><p>{p['desc']}</p></div>
  <div class="grid3 rv">{feats}</div>
</div></section>
<section style="padding-top:0"><div class="wrap">
  <div class="head rv"><div><div class="eyebrow">Nasıl çalışır</div><h2><span class="line"><span>Akış, adım adım.</span></span></h2></div></div>
  <div class="rows rv">{steps}</div>
  {pnav(p['slug'])}
</div></section>
{band()}
</main>'''
    title=f"{p['name']} — {d['h1']} | CanhasTech"
    meta=seo_head(f"{p['slug']}.html",title,f"{p['name']}: {p['desc']}",[{"@context":"https://schema.org","@type":"WebPage","name":title,"url":SITE+p['slug']+'.html',"description":p['desc'],"isPartOf":{"@type":"WebSite","name":"CanhasTech","url":SITE}},crumbs(p['name'],p['slug']+'.html')])
    return shell(title,body,'.plogo-hero{display:block;margin:22px auto 0;height:110px;width:auto;border-radius:16px}.plogo-hero.pill{background:#fff;padding:12px 18px;height:76px}',meta=meta)

# ---------------------------------------------------------------- 404
def notfound_page():
    body=f'''{nav('404')}
<header class="hero"><div class="wrap">
  <div class="eyebrow up">404</div>
  <h1><span class="line"><span data-kinetic data-delay=".15">Sayfa bulunamadı</span></span></h1>
  <p class="lede up" style="animation-delay:.8s">Aradığınız sayfa taşınmış ya da hiç var olmamış olabilir.</p>
  <div class="cta-row up" style="animation-delay:.95s"><a class="btn primary" href="index.html">Ana sayfaya dön</a><a class="btn" href="hasrep.html">Has Rep</a><a class="btn" href="index.html#iletisim">İletişim</a></div>
</div></header>
<main><section style="padding-top:0"><div class="wrap"><div class="grid3 rv">{''.join(f'<a class="card glass" href="{p["slug"]}.html"><div class="k"><span>{p["sector"]}</span></div><h3>{p["name"]}</h3><p>{p["short"]}</p></a>' for p in PROJECTS if not p.get('nopage'))}</div></div></section></main>'''
    return shell('Sayfa bulunamadı | CanhasTech',body,meta='<meta name="robots" content="noindex">')

# ---------------------------------------------------------------- KVKK
def kvkk_page():
    body=f'''{nav('kvkk')}
<header class="hero" style="padding-bottom:24px"><div class="wrap">
  <div class="crumb up"><a href="index.html">CanhasTech</a><i>/</i><span style="color:#fff">KVKK</span></div>
  <h1><span class="line"><span data-kinetic data-delay=".15" data-step="0.02">Aydınlatma Metni</span></span></h1>
  <p class="lede up" style="animation-delay:.8s">6698 sayılı Kişisel Verilerin Korunması Kanunu kapsamında bilgilendirme</p>
</div></header>
<main><section style="padding-top:24px"><div class="wrap"><div class="legal rv">
<p class="meta">Veri sorumlusu: <b>HAS Software Technologies</b> (CanhasTech markası) · İzmir · <a href="mailto:info@canhastech.com">info@canhastech.com</a> · Son güncelleme: 13 Eylül 2026</p>
<h2>1. Hangi verileri işliyoruz?</h2>
<p>Web sitemizdeki iletişim formu üzerinden paylaştığınız <b>ad-soyad, e-posta adresi, proje türü ve mesaj içeriği</b>; WhatsApp üzerinden yazmanız hâlinde telefon numaranız ve mesajınız. Sitemiz çerez kullanmaz ve ziyaretçi takibi yapmaz.</p>
<h2>2. Hangi amaçla?</h2>
<p>Talebinize yanıt vermek, teklif ve proje kapsamı hazırlamak, sizinle iletişim kurmak. Verileriniz pazarlama listelerine eklenmez, üçüncü kişilere satılmaz.</p>
<h2>3. Hukuki dayanak</h2>
<p>KVKK m. 5/2-c (sözleşmenin kurulması veya ifasıyla doğrudan ilgili olması) ve m. 5/2-f (meşru menfaat); formu göndererek verdiğiniz açık rıza.</p>
<h2>4. Kimlere aktarılıyor?</h2>
<p>Form gönderimleri, e-posta iletimi için <b>Web3Forms</b> (form işleme hizmeti) ve e-posta sağlayıcımız üzerinden tarafımıza ulaşır; site <b>GitHub Pages</b> altyapısında barındırılır. Bu hizmet sağlayıcıları yalnızca iletim amacıyla veri işler.</p>
<h2>5. Ne kadar süre saklıyoruz?</h2>
<p>Talebiniz sonuçlanana kadar; iş ilişkisi kurulmazsa en geç 1 yıl içinde silinir. İş ilişkisi kurulursa ilgili mevzuattaki saklama süreleri uygulanır.</p>
<h2>6. Haklarınız</h2>
<p>KVKK m. 11 kapsamında verilerinizin işlenip işlenmediğini öğrenme, düzeltilmesini veya silinmesini isteme, itiraz etme haklarınız vardır. Talebinizi <a href="mailto:info@canhastech.com">info@canhastech.com</a> adresine iletebilirsiniz; en geç 30 gün içinde yanıtlanır.</p>
</div></div></section></main>'''
    css='.legal{max-width:68ch;color:var(--muted);font-size:16px}.legal h2{font-size:20px;color:#fff;margin:34px 0 10px}.legal p{margin-bottom:12px}.legal b{color:#fff;font-weight:500}.legal a{color:#fff;border-bottom:1px solid var(--line2)}.legal .meta{font-family:var(--mono);font-size:12.5px;padding-bottom:18px;border-bottom:1px solid var(--line)}'
    meta=seo_head('kvkk.html','KVKK Aydınlatma Metni | CanhasTech','CanhasTech web sitesi iletişim formu ve WhatsApp üzerinden paylaşılan kişisel verilerin işlenmesine ilişkin KVKK aydınlatma metni.')
    return shell('KVKK Aydınlatma Metni | CanhasTech',body,css,meta=meta)

# ---------------------------------------------------------------- HAS REP MANUAL (QR on device opens this)
def hasrepkk_page():
    body=f'''{nav('hasrepkk')}
<header class="hero" style="padding-bottom:16px"><div class="wrap">
  <img class="brand up" src="hasrep-logo.jpg" width="900" height="609" alt="Has Rep logosu" style="animation-delay:.05s" decoding="async">
  <h1><span class="line"><span data-kinetic data-delay=".15" data-step="0.02">Kullanım Kılavuzu</span></span></h1>
  <p class="lede up" style="animation-delay:.8s">Has Rep’e hoş geldiniz. Bu sayfa cihazın arkasındaki QR koddan açılır; kurulumdan LED anlamlarına her şey burada.</p>
  <div class="cta-row up" style="animation-delay:.95s"><a class="btn primary" href="#hizli">Hızlı başlangıç</a><a class="btn" href="#kilavuz">LED &amp; bağlantı</a><a class="btn" href="#yardim">Yardım</a></div>
</div></header>
<main>
<section id="hizli" style="padding-top:40px" aria-labelledby="hizli-h"><div class="wrap">
  <div class="head rv"><div><div class="eyebrow">Hızlı başlangıç</div><h2 id="hizli-h"><span class="line"><span>Dört adımda hazır.</span></span></h2></div><p>İlk kullanımda cihazı tam şarj edin (LED yeşil yanana kadar). Sonrası bir dakika.</p></div>
  <div class="quick rv">
    <div class="q"><div class="n">1</div><b>Şarj edin</b><span>USB-C ile şarja takın. Şarj olurken LED kırmızı, dolunca yeşil yanar.</span></div>
    <div class="q"><div class="n">2</div><b>Uygulamayı indirin</b><span>App Store’dan Has Rep uygulamasını kurun ve e-postanızla kayıt olun.</span></div>
    <div class="q"><div class="n">3</div><b>Sallayıp eşleştirin</b><span>Cihazı hafifçe sallayın; uygulamada sağ üstteki pod simgesine dokunup cihazınızı seçin. LED maviye döner.</span></div>
    <div class="q"><div class="n">4</div><b>Bara takın, başlayın</b><span>Manyetik klipsle bara oturtun, “Antrenmanı Başlat”a basın, telefonu bırakın. Bitince senkronize edip tekrarları onaylayın.</span></div>
  </div>
</div></section>
{GUIDE.replace('<section class="guide" id="kilavuz" aria-labelledby="kilavuz-h">','<section class="guide" id="kilavuz" aria-labelledby="kilavuz-h" style="padding-top:0;border-top:0">')}
<section id="yardim" style="padding-top:0"><div class="wrap">
  <div class="head rv"><div><div class="eyebrow">Sorun mu var?</div><h2><span class="line"><span>Önce bunları deneyin.</span></span></h2></div><p>Çözülmezse yazın: <a href="mailto:hasrep@canhastech.com" style="color:#fff;border-bottom:1px solid var(--line2)">hasrep@canhastech.com</a> — ya da sağ alttaki WhatsApp düğmesi.</p></div>
  <div class="faq rv">
    <details><summary>Cihaz uygulamada görünmüyor</summary><div class="a">Cihazı sallayıp uyandırın (LED bir kez yanıp söner). Telefonun Bluetooth’u açık olsun. Uygulamada sağ üstteki pod simgesine dokunup yeniden tarayın. Hâlâ görünmüyorsa cihazı 1 dk şarja takıp tekrar deneyin.</div></details>
    <details><summary>LED hiç yanmıyor</summary><div class="a">Pil tamamen bitmiş olabilir; en az 30 dk şarj edin. Şarjda kırmızı LED yanmıyorsa kabloyu ve adaptörü değiştirip deneyin.</div></details>
    <details><summary>Tekrarlar eksik ya da fazla sayıldı</summary><div class="a">Antrenman sonunda kaydırmalı onay ekranında şüpheli tekrarları düzeltebilirsiniz. Cihazın bara sıkıca oturduğundan ve set arasında barı gereksiz sallamadığınızdan emin olun.</div></details>
    <details><summary>Senkronizasyon sonrası veri gelmedi</summary><div class="a">Cihaz telefona yakınken (1–2 m) senkronizasyonu tekrar başlatın. Uygulamayı tamamen kapatıp açmak çoğu zaman yeterlidir. Veriler cihazın hafızasında durur, kaybolmaz.</div></details>
    <details><summary>Cihazı nasıl temizlerim?</summary><div class="a">Hafif nemli, yumuşak bir bezle silin. Suya batırmayın, solvent kullanmayın. Manyetik klipsi metal talaşlarından uzak tutun.</div></details>
  </div>
  <div class="sup rv" style="margin-top:22px"><a href="mailto:hasrep@canhastech.com"><b>Has Rep destek</b><span>Cihaz ve uygulama soruları</span><span class="mono">hasrep@canhastech.com</span></a><a href="hasrep.html"><b>Has Rep ürün sayfası</b><span>VBT sistemi, uygulama turu, SSS</span><span class="mono">canhastech.com/hasrep.html</span></a><a href="index.html#iletisim"><b>CanhasTech</b><span>Diğer projeler ve iletişim</span><span class="mono">canhastech.com</span></a></div>
</div></section>
</main>'''
    css=HASREP_CSS+'.quick{display:grid;grid-template-columns:repeat(4,1fr);gap:14px}.q{border-radius:var(--r);border:1px solid var(--line);background:var(--card);padding:24px;display:grid;gap:8px;align-content:start}.q .n{width:32px;height:32px;border-radius:10px;background:#fff;color:#000;display:grid;place-items:center;font-family:var(--mono);font-size:12px;margin-bottom:6px}.q b{font-weight:500;font-size:16px}.q span{color:var(--muted);font-size:14px}@media(max-width:900px){.quick{grid-template-columns:1fr 1fr}}@media(max-width:520px){.quick{grid-template-columns:1fr}}'
    meta=seo_head('hasrepkk.html','Has Rep Kullanım Kılavuzu | CanhasTech','Has Rep kullanım kılavuzu: hızlı başlangıç, LED durum göstergeleri (mavi bağlı, kırmızı şarjda, yeşil dolu), cihazı sallayarak uyandırma, uygulamaya bağlanma ve sorun giderme.',image='og-hasrep.jpg')
    return shell('Has Rep Kullanım Kılavuzu | CanhasTech',body,css,HASREP_JS,meta=meta)

# ---------------------------------------------------------------- write
open(os.path.join(OUT,'hasrepkk.html'),'w').write(hasrepkk_page())
open(os.path.join(OUT,'kvkk.html'),'w').write(kvkk_page())
open(os.path.join(OUT,'CNAME'),'w').write('canhastech.com\n')
open(os.path.join(OUT,'404.html'),'w').write(notfound_page())
open(os.path.join(OUT,'index.html'),'w').write(index_page())
open(os.path.join(OUT,'hasrep.html'),'w').write(hasrep_page())
for p in PROJECTS[1:]:
    if p.get('nopage'): continue
    open(os.path.join(OUT,f"{p['slug']}.html"),'w').write(project_page(p))
pages=['index.html']+[f"{p['slug']}.html" for p in PROJECTS if not p.get('nopage')]+['kvkk.html','hasrepkk.html']
open(os.path.join(OUT,'sitemap.xml'),'w').write('<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'+''.join(f'  <url><loc>{SITE}{"" if pg=="index.html" else pg}</loc><changefreq>monthly</changefreq><priority>{"1.0" if pg=="index.html" else "0.8" if pg=="hasrep.html" else "0.6"}</priority></url>\n' for pg in pages)+'</urlset>\n')
open(os.path.join(OUT,'robots.txt'),'w').write(f'User-agent: *\nAllow: /\nSitemap: {SITE}sitemap.xml\n')
print('built:',sorted(f for f in os.listdir(OUT) if f.endswith('.html')))
