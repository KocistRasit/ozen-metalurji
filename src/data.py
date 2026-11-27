# -*- coding: utf-8 -*-
"""Özen Metalurji — firma bilgileri (tek kaynak). Eski siteden (ozenmetalurji.com.tr) ve
Google Haritalar kayıtlarından alınmıştır. Burada değişen bilgi tüm sayfalara, şemalara,
llms.txt dosyasına ve WordPress temasına yansır."""

SITE_URL = "https://www.ozenmetalurji.com.tr"   # canlı alan adı (canonical / şema)
BRAND = "Özen Metalurji"
LEGAL_NAME = "Özen Metalurji Makine ve Kalıp Sanayi Ticaret Ltd. Şti."
FOUNDED = "1974"
EMAIL = "info@ozenmetalurji.com.tr"

OFFICE = {
    "id": "ofis",
    "name": "Özen Metalurji Ofis",
    "label": "İstanbul Merkez Ofis",
    "street": "Topçular Mah. Rami Kışla Cad. Uzak Çiftlik Sok. No:19/B",
    "district": "Eyüpsultan",
    "city": "İstanbul",
    "region": "İstanbul",
    "phone_display": "0 212 567 71 26",
    "phone_alt_display": "0 212 567 71 48",
    "phone_e164": "+902125677126",
    "phone_alt_e164": "+902125677148",
    "fax_display": "0 212 565 27 17",
    "fax_e164": "+902125652717",
    "lat": 41.04422021277057,
    "lng": 28.918870396446437,
    "maps_query": "Özen Metalurji Ofis, Uzak Çiftlik Sok. 19B, Topçular, Eyüpsultan, İstanbul",
    "transit": "Bayrampaşa – Maltepe metro durağına yakın",
}

FACTORY = {
    "id": "fabrika",
    "name": "Özen Metalurji Abana",
    "label": "Abana Döküm Fabrikası",
    "street": "Merkez Mah. Sabri Kalafat Cad. No:66",
    "district": "Abana",
    "city": "Kastamonu",
    "region": "Kastamonu",
    "phone_display": "0 366 564 14 97",
    "phone_e164": "+903665641497",
    "fax_display": "0 366 564 14 98",
    "fax_e164": "+903665641498",
    "lat": 41.970275648565455,
    "lng": 34.00407585315406,
    "maps_query": "Özen Metalurji Abana, Sabri Kalafat Cad. No:66, Abana, Kastamonu",
    "area_open": "2.000 m²",
    "area_closed": "1.000 m²",
}

MACHINES = [
    ("Ergitme", [
        "300 kg 5M IGBT indüksiyon eritme ocağı",
        "500 kg 5M indüksiyon eritme ocağı",
        "200 kg alüminyum rezistanslı eritme ocağı",
        "300 kg alüminyum rezistanslı eritme ocağı",
        "350 kg alüminyum rezistanslı eritme ocağı",
        "Seymenler indüksiyonlu test ocağı",
    ]),
    ("Analiz ve ölçüm", [
        "Bruker S1 TITAN XRF analiz cihazı (tam kalibrasyonlu)",
        "IMPAC ısı (sıcaklık) ölçüm cihazı",
    ]),
    ("Kalıplama ve maça", [
        "Tam otomatik maça makinesi",
        "2 adet kokil döküm makinesi",
        "3 adet kum değirmeni",
        "2 adet eleme makinesi",
        "2 adet kum açma makinesi",
        "Modelhane takımları",
    ]),
    ("Temizleme ve işleme", [
        "2 adet kumlama makinesi",
        "Temelsan dekopaj makinesi",
        "3 adet testere",
        "Torna tezgâhı",
    ]),
]

SERVICES = [
    # slug, kısa ad, kart açıklaması, ikon anahtarı
    ("aluminyum-kum-dokum", "Alüminyum Kum Döküm", "Tek parçadan seriye, karmaşık geometriler ve büyük gövdeler için esnek yöntem.", "sand"),
    ("aluminyum-kokil-dokum", "Alüminyum Kokil Döküm", "Metal kalıpla tekrarlanabilir ölçü, düzgün yüzey ve seri üretim.", "die"),
    ("pirinc-dokum", "Pirinç (Sarı) Döküm", "Vana, rakor, armatür ve makine parçaları için işlenebilir sarı döküm.", "brass"),
    ("bronz-dokum", "Bronz (Kızıl) Döküm", "Burç, yatak, dişli ve aşınmaya dayanıklı parçalar için kızıl döküm.", "bronze"),
    ("zamak-dokum", "Zamak Döküm", "Çinko esaslı alaşımla ince detaylı, kaplamaya uygun parçalar.", "zamak"),
    ("anot-dokum", "Alüminyum Anot Döküm", "%99,80 saflıkta ithal alüminyumdan anot dökümü, paletli sevkiyat.", "anode"),
]
