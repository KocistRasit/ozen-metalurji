# -*- coding: utf-8 -*-
"""Özen Metalurji site üreticisi.

Tek içerik kaynağından iki çıktı üretir:
  1) dist/                 → GitHub Pages statik önizleme (Google'a kapalı)
  2) wordpress/ozen-metalurji/  → Natro'ya yüklenecek WordPress teması (+ .zip)

Kullanım:  python3 src/build.py            (BASE=/ozen-metalurji/ varsayılan)
           BASE=/ python3 src/build.py     (kök alan adında önizleme)
"""
import json, os, re, shutil, sys, zipfile
from html import escape

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
sys.path.insert(0, HERE)

from data import SITE_URL, BRAND, OFFICE, FACTORY, EMAIL, SERVICES, MACHINES  # noqa
import ui, schema as S  # noqa
import pages_main, pages_services, pages_extra  # noqa

BASE = os.environ.get("BASE", "/ozen-metalurji/")
PROD = SITE_URL.rstrip("/") + "/"
PAGES = pages_main.PAGES[:1] + pages_services.PAGES + pages_main.PAGES[1:] + pages_extra.PAGES
FONTS = "https://fonts.googleapis.com/css2?family=Archivo:wdth,wght@62..125,400..800&family=IBM+Plex+Mono:wght@500&display=swap"
VERSION = "1.0.0"


def graph(page):
    return {"@context": "https://schema.org", "@graph": S.base_graph() + page.get("schema", [])}


def fill(s, base, assets, site, form="#", form_hidden=""):
    return (s.replace("[[B]]", base).replace("[[A]]", assets).replace("[[S]]", site)
             .replace("[[FORM_HIDDEN]]", form_hidden).replace("[[FORM]]", form))


def page_path(p):
    return "" if p["slug"] == "" else p["slug"] + "/"


# ------------------------------------------------------------------ STATİK
def static_html(p):
    path = page_path(p)
    canonical = PROD + path
    body_cls = p.get("page_class", "")
    og_type = p.get("og_type", "website")
    head = """<!doctype html>
<html lang="tr">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>%(title)s</title>
<meta name="description" content="%(desc)s">
<meta name="robots" content="noindex, nofollow, noarchive, nosnippet, noimageindex">
<meta name="googlebot" content="noindex, nofollow">
<link rel="canonical" href="%(canonical)s">
<meta property="og:locale" content="tr_TR">
<meta property="og:type" content="%(og_type)s">
<meta property="og:site_name" content="Özen Metalurji">
<meta property="og:title" content="%(title)s">
<meta property="og:description" content="%(desc)s">
<meta property="og:url" content="%(canonical)s">
<meta property="og:image" content="[[A]]img/og-ozen-metalurji.jpg">
<meta property="og:image:width" content="1200"><meta property="og:image:height" content="630">
<meta name="twitter:card" content="summary_large_image">
<meta name="theme-color" content="#111317">
<meta name="geo.region" content="TR-37"><meta name="geo.placename" content="Abana, Kastamonu"><meta name="geo.position" content="%(flat)s;%(flng)s"><meta name="ICBM" content="%(flat)s, %(flng)s">
<link rel="icon" href="[[A]]img/favicon.svg" type="image/svg+xml">
<link rel="apple-touch-icon" href="[[A]]img/apple-touch-icon.png">
<link rel="alternate" type="text/plain" title="LLM özeti" href="[[B]]llms.txt">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="%(fonts)s">
<link rel="stylesheet" href="[[A]]css/site.css?v=%(v)s">
<script type="application/ld+json">%(ld)s</script>
</head>
<body class="%(cls)s" data-static="1">
""" % {"title": escape(p["title"]), "desc": escape(p["description"]), "canonical": canonical, "og_type": og_type,
       "fonts": FONTS, "v": VERSION, "cls": body_cls, "flat": FACTORY["lat"], "flng": FACTORY["lng"],
       "ld": json.dumps(fill_json(graph(p), PROD), ensure_ascii=False, separators=(",", ":"))}
    html = (head + ui.header() + '\n<main id="icerik">' + p["body"] + "</main>\n" +
            (ui.cta_band() if p["slug"] not in ("iletisim", "404") else "") + ui.footer() +
            '\n<script src="[[A]]js/site.js?v=%s" defer></script>\n</body>\n</html>\n' % VERSION)
    return fill(html, BASE, BASE + "assets/", PROD)


def fill_json(obj, site):
    return json.loads(json.dumps(obj, ensure_ascii=False).replace("[[S]]", site).replace("[[B]]", site))


def llms(site, full=False):
    L = []
    L.append("# Özen Metalurji\n")
    L.append("> 1974'te İstanbul Topçular'da kurulan, 2014'ten bu yana Kastamonu Abana'daki fabrikasında alüminyum kum ve kokil döküm, "
             "pirinç (sarı) döküm, bronz (kızıl) döküm, zamak döküm ve %99,80 saf alüminyumdan anot döküm yapan demir dışı metal dökümhanesi. "
             "Model, kalıp, maça ve XRF alaşım analizi kendi bünyesindedir.\n")
    L.append("## Temel bilgiler\n")
    L.append("- Unvan: Özen Metalurji Makine ve Kalıp San. Tic. Ltd. Şti.")
    L.append("- Kuruluş: 1974 (Özen Döküm Sanayi, Topçular / İstanbul); 2007'den beri Özen Metalurji")
    L.append("- Fabrika: %s, Abana / Kastamonu — 2.000 m² açık, 1.000 m² kapalı alan — Tel: %s" % (FACTORY["street"], FACTORY["phone_display"]))
    L.append("- Ofis: %s, Eyüpsultan / İstanbul — Tel: %s / %s" % (OFFICE["street"], OFFICE["phone_display"], OFFICE["phone_alt_display"]))
    L.append("- E-posta: %s" % EMAIL)
    L.append("- Dökülen metaller: alüminyum (kum ve kokil), pirinç, bronz, zamak, alüminyum anot. Pik, sfero ve çelik döküm yapılmaz.")
    L.append("- Ekipman: 300 kg ve 500 kg indüksiyon ocakları; 200/300/350 kg alüminyum rezistanslı ocaklar; tam otomatik maça makinesi; 2 kokil döküm makinesi; Bruker S1 TITAN XRF; IMPAC sıcaklık ölçer.")
    L.append("- Sektörler: makine yedek parçaları, cam sanayi, plastik şişirme kalıpları, tekstil yedek parçaları, otomotiv yan sanayi, anot döküm sistemleri; yurt içi ve yurt dışı.\n")
    groups = [("Döküm hizmetleri", lambda p: p["slug"].startswith("hizmetler")),
              ("Kurumsal", lambda p: p["slug"] in ("hakkimizda", "tesislerimiz", "kalite-ve-laboratuvar", "uretim-sureci", "sektorler")),
              ("Rehberler", lambda p: p["slug"].startswith("bilgi-merkezi")),
              ("Diğer", lambda p: p["slug"] in ("sss", "iletisim"))]
    for g, fn in groups:
        L.append("## %s\n" % g)
        for p in PAGES:
            if fn(p):
                L.append("- [%s](%s%s): %s" % (p["title"].split(" | ")[0].split(" — ")[0], site, page_path(p), p["description"]))
        L.append("")
    if full:
        L.append("## Sık sorulan sorular\n")
        for _, g in pages_extra.FAQ_GROUPS:
            for q, a in g:
                L.append("### %s\n%s\n" % (q, a))
    return "\n".join(L) + "\n"


def build_static():
    out = os.path.join(ROOT, "dist")
    shutil.rmtree(out, ignore_errors=True)
    os.makedirs(out)
    for p in PAGES:
        html = static_html(p)
        if p.get("file404"):
            target = os.path.join(out, "404.html")
        else:
            d = os.path.join(out, p["slug"]) if p["slug"] else out
            os.makedirs(d, exist_ok=True)
            target = os.path.join(d, "index.html")
        with open(target, "w", encoding="utf-8") as f:
            f.write(html)
    shutil.copytree(os.path.join(HERE, "assets"), os.path.join(out, "assets"))
    imgsrc = os.path.join(ROOT, "assets-img")
    if os.path.isdir(imgsrc):
        for fn in os.listdir(imgsrc):
            shutil.copy(os.path.join(imgsrc, fn), os.path.join(out, "assets", "img", fn))
    with open(os.path.join(out, "robots.txt"), "w") as f:
        f.write("# Önizleme sürümü — arama motorlarına kapalıdır.\nUser-agent: *\nDisallow: /\n")
    with open(os.path.join(out, "llms.txt"), "w", encoding="utf-8") as f:
        f.write(llms(PROD))
    with open(os.path.join(out, "llms-full.txt"), "w", encoding="utf-8") as f:
        f.write(llms(PROD, full=True))
    open(os.path.join(out, ".nojekyll"), "w").close()
    return out


# ------------------------------------------------------------------ WORDPRESS
def wp_key(slug):
    return "home" if slug == "" else slug.replace("/", "__")


def build_wp():
    theme = os.path.join(ROOT, "wordpress", "ozen-metalurji")
    tpl = os.path.join(HERE, "wp")
    shutil.rmtree(theme, ignore_errors=True)
    shutil.copytree(tpl, theme)
    shutil.copytree(os.path.join(HERE, "assets"), os.path.join(theme, "assets"))
    imgsrc = os.path.join(ROOT, "assets-img")
    if os.path.isdir(imgsrc):
        for fn in os.listdir(imgsrc):
            shutil.copy(os.path.join(imgsrc, fn), os.path.join(theme, "assets", "img", fn))
    cdir = os.path.join(theme, "content")
    os.makedirs(cdir, exist_ok=True)
    pdir = os.path.join(theme, "partials")
    os.makedirs(pdir, exist_ok=True)
    with open(os.path.join(pdir, "header.html"), "w", encoding="utf-8") as f:
        f.write(ui.header())
    with open(os.path.join(pdir, "footer.html"), "w", encoding="utf-8") as f:
        f.write(ui.footer())
    with open(os.path.join(pdir, "cta.html"), "w", encoding="utf-8") as f:
        f.write(ui.cta_band())
    manifest = []
    for p in PAGES:
        k = wp_key(p["slug"])
        with open(os.path.join(cdir, k + ".html"), "w", encoding="utf-8") as f:
            f.write(p["body"])
        with open(os.path.join(cdir, k + ".json"), "w", encoding="utf-8") as f:
            json.dump({"title": p["title"], "description": p["description"], "og_type": p.get("og_type", "website"),
                       "schema": p.get("schema", []), "cta": p["slug"] not in ("iletisim", "404"),
                       "body_class": p.get("page_class", "")}, f, ensure_ascii=False)
        if p.get("file404"):
            continue
        # sayfa oluşturma listesi: başlık (H1'den kısa ad), slug, üst sayfa
        parts = p["slug"].split("/") if p["slug"] else [""]
        short = re.sub(r"<[^>]+>", "", re.search(r"<h1>(.*?)</h1>", p["body"], re.S).group(1)) if p["slug"] else "Ana Sayfa"
        manifest.append({"key": k, "slug": parts[-1] if p["slug"] else "ana-sayfa",
                         "parent": wp_key("/".join(parts[:-1])) if len(parts) > 1 else "", "title": short})
    with open(os.path.join(cdir, "_pages.json"), "w", encoding="utf-8") as f:
        json.dump(manifest, f, ensure_ascii=False, indent=1)
    with open(os.path.join(cdir, "_base_schema.json"), "w", encoding="utf-8") as f:
        json.dump(S.base_graph(), f, ensure_ascii=False)
    with open(os.path.join(theme, "llms.txt"), "w", encoding="utf-8") as f:
        f.write(llms("[[S]]"))
    with open(os.path.join(theme, "llms-full.txt"), "w", encoding="utf-8") as f:
        f.write(llms("[[S]]", full=True))
    # zip
    zpath = os.path.join(ROOT, "wordpress", "ozen-metalurji-tema.zip")
    if os.path.exists(zpath):
        os.remove(zpath)
    with zipfile.ZipFile(zpath, "w", zipfile.ZIP_DEFLATED) as z:
        for dp, _, files in os.walk(theme):
            for fn in files:
                full = os.path.join(dp, fn)
                z.write(full, os.path.relpath(full, os.path.dirname(theme)))
    return theme, zpath


if __name__ == "__main__":
    out = build_static()
    theme, z = build_wp()
    os.makedirs(os.path.join(out, "indir"), exist_ok=True)
    shutil.copy(z, os.path.join(out, "indir", "ozen-metalurji-tema.zip"))
    print("Statik:", out, "| sayfa:", len(PAGES))
    print("WP tema:", theme, "| zip:", z)
