# -*- coding: utf-8 -*-
"""JSON-LD (schema.org) üreticileri. [[S]] = canlı alan adı + kök yol."""
from data import OFFICE, FACTORY, EMAIL, BRAND, LEGAL_NAME, FOUNDED, SERVICES

ORG_ID = "[[S]]#organizasyon"
SITE_ID = "[[S]]#website"


def _addr(l):
    return {"@type": "PostalAddress", "streetAddress": l["street"], "addressLocality": l["district"],
            "addressRegion": l["region"], "addressCountry": "TR"}


def _place(l, kind):
    d = {
        "@type": ["LocalBusiness"],
        "@id": "[[S]]#" + l["id"],
        "name": l["name"],
        "description": kind,
        "url": "[[S]]iletisim/",
        "parentOrganization": {"@id": ORG_ID},
        "address": _addr(l),
        "geo": {"@type": "GeoCoordinates", "latitude": round(l["lat"], 6), "longitude": round(l["lng"], 6)},
        "hasMap": "https://www.google.com/maps/search/?api=1&query=%s,%s" % (l["lat"], l["lng"]),
        "telephone": l["phone_e164"],
        "faxNumber": l["fax_e164"],
        "email": EMAIL,
        "image": "[[S]]assets/img/og-ozen-metalurji.jpg",
        "logo": "[[S]]assets/img/logo-ozen-metalurji.png",
        "priceRange": "Teklif üzerine",
        "areaServed": [{"@type": "Country", "name": "Türkiye"}, "Yurt dışı"],
        "knowsAbout": ["Alüminyum kum döküm", "Alüminyum kokil döküm", "Pirinç döküm", "Bronz döküm", "Zamak döküm", "Alüminyum anot döküm"],
    }
    return d


def organization():
    return {
        "@type": "Organization",
        "@id": ORG_ID,
        "name": BRAND,
        "legalName": LEGAL_NAME,
        "alternateName": ["Özen Metalurji ve Kalıp", "Özen Döküm"],
        "url": "[[S]]",
        "logo": {"@type": "ImageObject", "url": "[[S]]assets/img/logo-ozen-metalurji.png"},
        "image": "[[S]]assets/img/og-ozen-metalurji.jpg",
        "foundingDate": FOUNDED,
        "foundingLocation": {"@type": "Place", "name": "Topçular, Eyüpsultan, İstanbul"},
        "description": ("1974'te İstanbul Topçular'da kurulan, bugün Kastamonu Abana'daki fabrikasında alüminyum kum ve "
                        "kokil döküm, pirinç (sarı) döküm, bronz (kızıl) döküm, zamak döküm ve alüminyum anot döküm "
                        "yapan demir dışı metal dökümhanesi."),
        "email": EMAIL,
        "telephone": OFFICE["phone_e164"],
        "address": _addr(OFFICE),
        "location": [{"@id": "[[S]]#ofis"}, {"@id": "[[S]]#fabrika"}],
        "contactPoint": [
            {"@type": "ContactPoint", "contactType": "sales", "telephone": OFFICE["phone_e164"], "email": EMAIL,
             "areaServed": "TR", "availableLanguage": ["Turkish"]},
            {"@type": "ContactPoint", "contactType": "customer support", "telephone": FACTORY["phone_e164"],
             "areaServed": "TR", "availableLanguage": ["Turkish"]},
        ],
        "knowsAbout": ["Demir dışı metal dökümü", "Kum döküm", "Kokil döküm", "Alüminyum alaşımları",
                       "Pirinç alaşımları", "Bronz alaşımları", "Zamak (çinko) alaşımları", "XRF alaşım analizi",
                       "Model ve kalıp imalatı", "Anot döküm"],
        "sameAs": ["https://yandex.com.tr/maps/org/ozen_metalurji_ve_kalip/1076529115/"],
    }


def website():
    return {"@type": "WebSite", "@id": SITE_ID, "url": "[[S]]", "name": BRAND, "inLanguage": "tr-TR",
            "publisher": {"@id": ORG_ID}}


def base_graph():
    return [organization(), website(),
            _place(OFFICE, "Özen Metalurji İstanbul merkez ofisi — satış, teklif ve proje koordinasyonu."),
            _place(FACTORY, "Özen Metalurji Abana döküm fabrikası — demir dışı metal döküm üretimi (2.000 m² açık, 1.000 m² kapalı alan).")]


def breadcrumb(items):
    """items: [(ad, yol)]"""
    lst = [{"@type": "ListItem", "position": 1, "name": "Ana Sayfa", "item": "[[S]]"}]
    for i, (n, p) in enumerate(items, start=2):
        lst.append({"@type": "ListItem", "position": i, "name": n, "item": "[[S]]" + p})
    return {"@type": "BreadcrumbList", "itemListElement": lst}


def webpage(path, name, desc, kind="WebPage", about=None):
    d = {"@type": kind, "@id": "[[S]]%s#sayfa" % path, "url": "[[S]]" + path, "name": name, "description": desc,
         "inLanguage": "tr-TR", "isPartOf": {"@id": SITE_ID}, "publisher": {"@id": ORG_ID},
         "dateModified": "2026-11-27"}
    if about:
        d["about"] = about
    return d


def faqpage(path, faqs):
    import re
    strip = lambda s: re.sub(r"<[^>]+>", "", s)
    return {"@type": "FAQPage", "@id": "[[S]]%s#sss" % path, "mainEntity": [
        {"@type": "Question", "name": strip(q), "acceptedAnswer": {"@type": "Answer", "text": strip(a)}} for q, a in faqs]}


def service(path, name, desc, service_type, materials=None):
    d = {"@type": "Service", "@id": "[[S]]%s#hizmet" % path, "name": name, "serviceType": service_type,
         "description": desc, "url": "[[S]]" + path, "provider": {"@id": ORG_ID},
         "areaServed": [{"@type": "Country", "name": "Türkiye"}],
         "availableChannel": {"@type": "ServiceChannel", "serviceUrl": "[[S]]iletisim/",
                              "servicePhone": {"@type": "ContactPoint", "telephone": OFFICE["phone_e164"]}}}
    if materials:
        d["material"] = materials
    return d


def article(path, headline, desc, date="2026-11-27"):
    return {"@type": "Article", "@id": "[[S]]%s#makale" % path, "headline": headline, "description": desc,
            "inLanguage": "tr-TR", "datePublished": date, "dateModified": date,
            "mainEntityOfPage": {"@id": "[[S]]%s#sayfa" % path},
            "author": {"@id": ORG_ID}, "publisher": {"@id": ORG_ID},
            "image": "[[S]]assets/img/og-ozen-metalurji.jpg"}


def itemlist(name, items):
    return {"@type": "ItemList", "name": name, "itemListElement": [
        {"@type": "ListItem", "position": i, "name": n, "url": "[[S]]" + p} for i, (n, p) in enumerate(items, 1)]}
