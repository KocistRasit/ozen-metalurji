# -*- coding: utf-8 -*-
"""Ortak arayüz parçaları: başlık, alt bilgi, ikonlar, bileşenler.
Yer tutucular: [[B]] = site kök yolu (/ veya /ozen-metalurji/), [[A]] = tema/asset yolu,
[[S]] = canlı alan adı (canonical ve şema için)."""
from html import escape
from data import OFFICE, FACTORY, EMAIL, SERVICES, BRAND

ICONS = {
    "phone": '<path d="M5 4h4l2 5-2.5 1.5a11 11 0 0 0 5 5L15 13l5 2v4a2 2 0 0 1-2 2A16 16 0 0 1 3 6a2 2 0 0 1 2-2"/>',
    "mail": '<rect x="3" y="5" width="18" height="14" rx="2"/><path d="m3 7 9 6 9-6"/>',
    "pin": '<path d="M12 21s-7-6.2-7-11.5A7 7 0 0 1 19 9.5C19 14.8 12 21 12 21z"/><circle cx="12" cy="9.5" r="2.5"/>',
    "arrow": '<path d="M5 12h14M13 6l6 6-6 6"/>',
    "check": '<path d="m5 12.5 4.5 4.5L19 7.5"/>',
    "menu": '<path d="M4 7h16M4 12h16M4 17h16"/>',
    "close": '<path d="M6 6l12 12M18 6 6 18"/>',
    "chev": '<path d="m6 9 6 6 6-6"/>',
    "route": '<circle cx="6" cy="19" r="2"/><circle cx="18" cy="5" r="2"/><path d="M8 19h8.5a3.5 3.5 0 0 0 0-7h-9a3.5 3.5 0 0 1 0-7H16"/>',
    "doc": '<path d="M14 3H7a2 2 0 0 0-2 2v14a2 2 0 0 0 2 2h10a2 2 0 0 0 2-2V8z"/><path d="M14 3v5h5M9 13h6M9 17h6"/>',
    "flask": '<path d="M9 3h6M10 3v6L4.5 18.5A1.7 1.7 0 0 0 6 21h12a1.7 1.7 0 0 0 1.5-2.5L14 9V3"/><path d="M7 15h10"/>',
    "fire": '<path d="M12 22c4 0 7-2.7 7-6.8 0-3.6-2.4-5.6-4-8.2-.6 2.3-2 3.6-3.4 3.6C12.6 7.300 11.6 4.3 9 2c0 4-5 6.5-5 13.200C4 19.300 7.500 22 12 22z"/>',
    "factory": '<path d="M3 21V10l6 4V10l6 4V6l6 3v12z"/><path d="M7 18h2M12 18h2M17 18h2"/>',
    "shield": '<path d="M12 3 4 6v6c0 5 3.5 8 8 9 4.5-1 8-4 8-9V6z"/><path d="m8.5 12 2.5 2.5 4.5-5"/>',
    "gear": '<circle cx="12" cy="12" r="3"/><path d="M12 2v3M12 19v3M4.9 4.9l2.1 2.1M17 17l2.1 2.1M2 12h3M19 12h3M4.9 19.1 7 17M17 7l2.1-2.1"/>',
    "truck": '<path d="M3 6h11v10H3zM14 10h4l3 3v3h-7"/><circle cx="7" cy="18" r="2"/><circle cx="17.5" cy="18" r="2"/>',
    "clock": '<circle cx="12" cy="12" r="9"/><path d="M12 7v5l3 2"/>',
    "sand": '<path d="M3 17h18M5 17l3-6h8l3 6"/><path d="M9 11V7h6v4"/><circle cx="7" cy="20" r=".6"/><circle cx="12" cy="20" r=".6"/><circle cx="17" cy="20" r=".6"/>',
    "die": '<rect x="3" y="4" width="8" height="16" rx="1"/><rect x="13" y="4" width="8" height="16" rx="1"/><path d="M11 9h2M11 15h2"/>',
    "brass": '<path d="M4 10h6l2-3h0l2 3h6v5h-6l-2 3-2-3H4z"/><path d="M10 12.5h4"/>',
    "bronze": '<circle cx="12" cy="12" r="8"/><circle cx="12" cy="12" r="3.5"/><path d="M12 2v2.5M12 19.5V22M2 12h2.5M19.5 12H22"/>',
    "zamak": '<path d="M12 3 20 7.5v9L12 21l-8-4.5v-9z"/><path d="M12 12 20 7.5M12 12v9M12 12 4 7.5"/>',
    "anode": '<rect x="5" y="6" width="14" height="12" rx="1.5"/><path d="M9 3v3M15 3v3M8 11h8M8 14h5"/>',
    "quote": '<path d="M7 7h4v4H8v2a2 2 0 0 0 2 2M15 7h4v4h-3v2a2 2 0 0 0 2 2"/>',
}


def icon(name, cls="ic"):
    return ('<svg class="%s" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.7" '
            'stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">%s</svg>') % (cls, ICONS[name])


LOGO = ('<svg class="logo-mark" viewBox="0 0 48 48" aria-hidden="true">'
        '<defs><linearGradient id="lg-molten" x1="0" y1="0" x2="0" y2="1">'
        '<stop offset="0" stop-color="#ffcf6b"/><stop offset=".55" stop-color="#ff7a1a"/><stop offset="1" stop-color="#d9480f"/></linearGradient></defs>'
        '<path d="M9 10h30l-3.5 24a6 6 0 0 1-6 5h-11a6 6 0 0 1-6-5z" fill="none" stroke="currentColor" stroke-width="3" stroke-linejoin="round"/>'
        '<path d="M13 20h22l-2 13.5a3 3 0 0 1-3 2.5H18a3 3 0 0 1-3-2.5z" fill="url(#lg-molten)"/>'
        '<path d="M5 10h38" stroke="currentColor" stroke-width="3" stroke-linecap="round"/></svg>')


def logo_block():
    return ('<a class="brand" href="[[B]]" aria-label="Özen Metalurji ana sayfa">%s'
            '<span class="brand-text"><span class="brand-name">ÖZEN</span>'
            '<span class="brand-sub">METALURJİ · 1974</span></span></a>') % LOGO


def tel(loc, alt=False):
    if alt:
        return '<a href="tel:%s">%s</a>' % (loc["phone_alt_e164"], loc["phone_alt_display"])
    return '<a href="tel:%s">%s</a>' % (loc["phone_e164"], loc["phone_display"])


def nav():
    svc = "".join('<li><a href="[[B]]hizmetler/%s/">%s%s</a></li>' % (s, icon(ic, "ic ic-sm"), escape(n))
                  for s, n, _, ic in SERVICES)
    return """
<nav class="nav" id="site-nav" aria-label="Ana menü">
  <ul class="nav-list">
    <li class="has-sub"><button class="nav-btn" aria-expanded="false">Kurumsal %(chev)s</button>
      <ul class="sub">
        <li><a href="[[B]]hakkimizda/">Hakkımızda</a></li>
        <li><a href="[[B]]tesislerimiz/">Tesislerimiz ve Makine Parkuru</a></li>
        <li><a href="[[B]]kalite-ve-laboratuvar/">Kalite ve Laboratuvar</a></li>
        <li><a href="[[B]]uretim-sureci/">Üretim Süreci</a></li>
      </ul></li>
    <li class="has-sub"><button class="nav-btn" aria-expanded="false">Döküm Hizmetleri %(chev)s</button>
      <ul class="sub sub-wide">%(svc)s<li class="sub-all"><a href="[[B]]hizmetler/">Tüm hizmetler %(arrow)s</a></li></ul></li>
    <li><a href="[[B]]sektorler/">Sektörler</a></li>
    <li><a href="[[B]]bilgi-merkezi/">Bilgi Merkezi</a></li>
    <li><a href="[[B]]sss/">SSS</a></li>
    <li><a href="[[B]]iletisim/">İletişim</a></li>
  </ul>
  <a class="btn btn-molten nav-cta" href="[[B]]iletisim/#teklif">Teklif İste %(arrow)s</a>
</nav>""" % {"chev": icon("chev", "ic ic-xs"), "svc": svc, "arrow": icon("arrow", "ic ic-sm")}


def header():
    return """
<a class="skip" href="#icerik">İçeriğe geç</a>
<div class="topbar"><div class="wrap topbar-in">
  <span class="tb-item">%(pin)s Eyüpsultan / İstanbul · Abana / Kastamonu</span>
  <span class="tb-right"><span class="tb-item">%(phone)s %(tel)s</span>
  <span class="tb-item">%(mail)s <a href="mailto:%(email)s">%(email)s</a></span></span>
</div></div>
<header class="site-header" id="top"><div class="wrap header-in">
  %(logo)s
  <button class="burger" aria-controls="site-nav" aria-expanded="false" aria-label="Menüyü aç">%(menu)s%(close)s</button>
  %(nav)s
</div></header>""" % {
        "pin": icon("pin", "ic ic-xs"), "phone": icon("phone", "ic ic-xs"), "mail": icon("mail", "ic ic-xs"),
        "tel": tel(OFFICE), "email": EMAIL, "logo": logo_block(), "nav": nav(),
        "menu": icon("menu", "ic i-open"), "close": icon("close", "ic i-close")}


def cta_band():
    return """
<section class="cta-band"><div class="wrap cta-in">
  <div><p class="eyebrow eyebrow-light">Teknik resminiz hazır mı?</p>
  <h2>Parçanızı konuşalım; alaşımı, yöntemi ve maliyeti birlikte netleştirelim.</h2>
  <p>Teknik resim, alaşım ve adet bilgisini gönderin; ekibimiz yöntem önerisiyle birlikte dönüş yapsın.</p></div>
  <div class="cta-actions">
    <a class="btn btn-molten btn-lg" href="[[B]]iletisim/#teklif">Teklif İste %(arrow)s</a>
    <a class="btn btn-ghost-light btn-lg" href="tel:%(tel)s">%(phone)s %(teld)s</a>
  </div>
</div></section>""" % {"arrow": icon("arrow", "ic ic-sm"), "phone": icon("phone", "ic ic-sm"),
                        "tel": OFFICE["phone_e164"], "teld": OFFICE["phone_display"]}


def footer():
    svc = "".join('<li><a href="[[B]]hizmetler/%s/">%s</a></li>' % (s, escape(n)) for s, n, _, _ in SERVICES)

    def loc(l, extra=""):
        return """<div class="f-loc"><h3>%(label)s</h3>
<address>%(street)s<br>%(district)s / %(city)s</address>
<p>%(phone)s %(tel)s%(extra)s</p><p class="muted">Faks: %(fax)s</p>
<a class="f-route" href="https://www.google.com/maps/dir/?api=1&amp;destination=%(lat)s,%(lng)s" target="_blank" rel="noopener">%(route)s Yol tarifi al</a></div>""" % {
            "label": l["label"], "street": l["street"], "district": l["district"], "city": l["city"],
            "phone": icon("phone", "ic ic-xs"), "tel": tel(l), "extra": extra, "fax": l["fax_display"],
            "lat": l["lat"], "lng": l["lng"], "route": icon("route", "ic ic-xs")}
    return """
<footer class="site-footer"><div class="wrap">
  <div class="f-grid">
    <div class="f-brand">%(logo)s
      <p>1974'ten bu yana demir dışı metal dökümü: alüminyum (kum ve kokil), pirinç, bronz, zamak ve anot döküm. İstanbul'da ofis, Kastamonu Abana'da fabrika.</p>
      <p><a class="f-mail" href="mailto:%(email)s">%(mail)s %(email)s</a></p>
    </div>
    <div><h3>Döküm Hizmetleri</h3><ul class="f-links">%(svc)s</ul></div>
    <div><h3>Kurumsal</h3><ul class="f-links">
      <li><a href="[[B]]hakkimizda/">Hakkımızda</a></li>
      <li><a href="[[B]]tesislerimiz/">Tesislerimiz</a></li>
      <li><a href="[[B]]kalite-ve-laboratuvar/">Kalite ve Laboratuvar</a></li>
      <li><a href="[[B]]uretim-sureci/">Üretim Süreci</a></li>
      <li><a href="[[B]]sektorler/">Sektörler</a></li>
      <li><a href="[[B]]bilgi-merkezi/">Bilgi Merkezi</a></li>
      <li><a href="[[B]]sss/">Sık Sorulan Sorular</a></li>
    </ul></div>
    %(office)s
    %(factory)s
  </div>
  <div class="f-bottom"><p>© <span data-year>2026</span> %(legal)s</p>
  <p><a href="[[B]]kvkk/">KVKK Aydınlatma Metni</a> · <a href="[[B]]iletisim/">İletişim</a></p></div>
</div></footer>
<div class="mbar" aria-label="Hızlı iletişim">
  <a href="tel:%(tel)s">%(phone)s<span>Ara</span></a>
  <a href="[[B]]iletisim/#teklif" class="mbar-main">%(doc)s<span>Teklif İste</span></a>
  <a href="[[B]]iletisim/#konumlar">%(pin)s<span>Konum</span></a>
</div>""" % {
        "logo": logo_block(), "email": EMAIL, "mail": icon("mail", "ic ic-xs"), "svc": svc,
        "office": loc(OFFICE, ' · <a href="tel:%s">%s</a>' % (OFFICE["phone_alt_e164"], OFFICE["phone_alt_display"])),
        "factory": loc(FACTORY), "legal": "Özen Metalurji Makine ve Kalıp San. Tic. Ltd. Şti.",
        "tel": OFFICE["phone_e164"], "phone": icon("phone"), "doc": icon("doc"), "pin": icon("pin")}


def breadcrumbs(items):
    """items: [(ad, yol)] — son öğe geçerli sayfa"""
    lis = ['<li><a href="[[B]]">Ana Sayfa</a></li>']
    for i, (name, path) in enumerate(items):
        if i == len(items) - 1:
            lis.append('<li aria-current="page">%s</li>' % escape(name))
        else:
            lis.append('<li><a href="[[B]]%s">%s</a></li>' % (path, escape(name)))
    return '<nav class="crumbs" aria-label="Sayfa yolu"><ol>%s</ol></nav>' % "".join(lis)


def page_hero(eyebrow, h1, lead, crumbs, extra=""):
    return """
<section class="phero"><div class="phero-glow" aria-hidden="true"></div><div class="wrap">
  %(crumbs)s
  <p class="eyebrow">%(eyebrow)s</p>
  <h1>%(h1)s</h1>
  <p class="lead">%(lead)s</p>%(extra)s
</div></section>""" % {"crumbs": breadcrumbs(crumbs), "eyebrow": eyebrow, "h1": h1, "lead": lead, "extra": extra}


def answer_box(q, a):
    """AEO: soruya doğrudan, alıntılanabilir kısa cevap."""
    return ('<aside class="answer" aria-label="Kısa cevap"><p class="answer-k">Kısa cevap</p>'
            '<p class="answer-q">%s</p><p class="answer-a">%s</p></aside>') % (q, a)


def faq_list(faqs, open_first=False):
    out = []
    for i, (q, a) in enumerate(faqs):
        out.append('<details class="faq"%s><summary><span>%s</span>%s</summary><div class="faq-a"><p>%s</p></div></details>'
                   % (" open" if (open_first and i == 0) else "", q, icon("chev", "ic ic-sm"), a))
    return '<div class="faqs">%s</div>' % "".join(out)


def facts_table(rows, caption=None):
    cap = '<caption>%s</caption>' % caption if caption else ""
    body = "".join('<tr><th scope="row">%s</th><td>%s</td></tr>' % (k, v) for k, v in rows)
    return '<div class="table-wrap"><table class="facts">%s<tbody>%s</tbody></table></div>' % (cap, body)


def data_table(head, rows, caption=None, note=None):
    cap = '<caption>%s</caption>' % caption if caption else ""
    th = "".join('<th scope="col">%s</th>' % h for h in head)
    body = "".join("<tr>%s</tr>" % "".join(('<th scope="row">%s</th>' if j == 0 else "<td>%s</td>") % c for j, c in enumerate(r)) for r in rows)
    n = '<p class="table-note">%s</p>' % note if note else ""
    return '<div class="table-wrap"><table class="data">%s<thead><tr>%s</tr></thead><tbody>%s</tbody></table></div>%s' % (cap, th, body, n)


def map_embed(loc, eager=False):
    from urllib.parse import quote
    q = quote(loc["maps_query"])
    return """<div class="map-card" id="harita-%(id)s">
  <div class="map-frame"><iframe title="%(name)s — Google Haritalar" src="https://maps.google.com/maps?q=%(q)s&amp;ll=%(lat)s,%(lng)s&amp;z=15&amp;hl=tr&amp;output=embed" loading="%(loading)s" referrerpolicy="no-referrer-when-downgrade" allowfullscreen></iframe></div>
  <div class="map-info">
    <p class="eyebrow">%(label)s</p><h3>%(name)s</h3>
    <address>%(street)s<br>%(district)s / %(city)s</address>
    <ul class="map-meta"><li>%(phone)s %(tel)s</li><li class="muted">Faks: %(fax)s</li></ul>
    <div class="map-actions">
      <a class="btn btn-dark btn-sm" href="https://www.google.com/maps/dir/?api=1&amp;destination=%(lat)s,%(lng)s" target="_blank" rel="noopener">%(route)s Yol tarifi</a>
      <a class="btn btn-line btn-sm" href="https://www.google.com/maps/search/?api=1&amp;query=%(q)s" target="_blank" rel="noopener">Haritada aç</a>
    </div>
  </div>
</div>""" % {"id": loc["id"], "name": loc["name"], "q": q, "lat": loc["lat"], "lng": loc["lng"],
             "loading": "eager" if eager else "lazy", "label": loc["label"], "street": loc["street"],
             "district": loc["district"], "city": loc["city"], "phone": icon("phone", "ic ic-xs"),
             "tel": tel(loc), "fax": loc["fax_display"], "route": icon("route", "ic ic-xs")}


def service_cards(exclude=None):
    out = []
    for s, n, d, ic in SERVICES:
        if s == exclude:
            continue
        out.append('<a class="svc-card" href="[[B]]hizmetler/%s/"><span class="svc-ic">%s</span><h3>%s</h3><p>%s</p>'
                   '<span class="more">Detaylı incele %s</span></a>' % (s, icon(ic), escape(n), escape(d), icon("arrow", "ic ic-sm")))
    return '<div class="svc-grid">%s</div>' % "".join(out)
