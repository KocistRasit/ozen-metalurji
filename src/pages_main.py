# -*- coding: utf-8 -*-
"""Ana sayfa ve kurumsal sayfalar."""
from data import OFFICE, FACTORY, EMAIL, MACHINES, SERVICES
from ui import (icon, page_hero, answer_box, faq_list, facts_table, map_embed, service_cards, tel)
import schema as S

PAGES = []


def add(**kw):
    PAGES.append(kw)


# ---------------------------------------------------------------- ANA SAYFA
HOME_FAQ = [
    ("Özen Metalurji hangi metalleri döker?",
     "Özen Metalurji demir dışı metaller döker: alüminyum (kum ve kokil döküm), pirinç (sarı döküm), bronz (kızıl döküm), zamak (çinko alaşımı) ve %99,80 saflıkta alüminyumdan anot döküm."),
    ("Özen Metalurji'nin fabrikası nerede?",
     "Üretim, 2014'ten bu yana Kastamonu'nun Abana ilçesindeki fabrikada yapılır (Merkez Mah. Sabri Kalafat Cad. No:66). Satış ve teklif ofisi İstanbul Eyüpsultan Topçular'dadır."),
    ("Teklif almak için ne göndermeliyim?",
     "Teknik resim (PDF, DWG/DXF veya STEP), istenen alaşım, adet (numune ve yıllık tahmin), parçanın işlenmiş mi ham mı teslim edileceği ve varsa mevcut model ya da kalıp bilgisi yeterlidir."),
    ("Model ve kalıbı siz mi yapıyorsunuz?",
     "Evet. Teknik resimden yola çıkılarak çekme ve işleme payları hesaplanır; model, kalıp ve maça aşamaları ilk numune ve analiz sonuçlarına kadar kendi bünyemizde yürütülür."),
    ("Alaşımın doğru olduğunu nasıl kontrol ediyorsunuz?",
     "Ergitilen metalin kimyasal bileşimi tam kalibrasyonlu Bruker S1 TITAN XRF cihazıyla kendi laboratuvarımızda ölçülür; döküm sıcaklığı IMPAC sıcaklık ölçüm cihazıyla takip edilir."),
]

home_body = """
<section class="hero">
  <div class="hero-art" aria-hidden="true"><div class="hero-glow"></div><div class="hero-pour"></div><div class="hero-grid"></div></div>
  <div class="wrap hero-in">
    <div class="hero-copy">
      <p class="eyebrow">Demir dışı metal dökümhanesi · 1974'ten beri</p>
      <h1>Alüminyum, pirinç, bronz ve zamak dökümde <span class="molten">50 yılı aşkın</span> ustalık.</h1>
      <p class="lead">Özen Metalurji; teknik resminizden model ve kalıba, XRF ile doğrulanmış alaşımdan sevkiyata kadar dökümün her adımını Kastamonu Abana'daki fabrikasında tek elden yürütür.</p>
      <div class="hero-actions">
        <a class="btn btn-molten btn-lg" href="[[B]]iletisim/#teklif">Teklif İste %(arrow)s</a>
        <a class="btn btn-ghost-light btn-lg" href="[[B]]hizmetler/">Döküm hizmetleri</a>
      </div>
      <ul class="hero-trust">
        <li>%(check)s Model ve kalıp kendi bünyemizde</li>
        <li>%(check)s XRF ile alaşım analizi</li>
        <li>%(check)s Yurt içi ve yurt dışı sevkiyat</li>
      </ul>
    </div>
    <div class="hero-card" aria-label="Kısa bilgi">
      <p class="hc-k">Özen Metalurji kimdir?</p>
      <p class="hc-a">1974'te İstanbul Topçular'da kurulan, bugün Kastamonu Abana'daki fabrikasında <strong>alüminyum kum ve kokil döküm, pirinç, bronz, zamak ve anot döküm</strong> yapan aile şirketi bir demir dışı metal dökümhanesidir.</p>
      <dl class="hc-facts">
        <div><dt>Kuruluş</dt><dd>1974</dd></div>
        <div><dt>Fabrika</dt><dd>Abana / Kastamonu</dd></div>
        <div><dt>Ofis</dt><dd>Eyüpsultan / İstanbul</dd></div>
        <div><dt>Ergitme</dt><dd>500 kg'a kadar indüksiyon</dd></div>
      </dl>
    </div>
  </div>
</section>

<section class="stats" aria-label="Rakamlarla Özen Metalurji"><div class="wrap stats-in">
  <div class="stat"><span class="stat-n" data-count="1974">1974</span><span class="stat-l">Topçular'da ilk döküm</span></div>
  <div class="stat"><span class="stat-n">3.000 m²</span><span class="stat-l">Abana tesisi (1.000 m² kapalı)</span></div>
  <div class="stat"><span class="stat-n">5</span><span class="stat-l">Alaşım ailesi: Al, pirinç, bronz, zamak, anot</span></div>
  <div class="stat"><span class="stat-n">6</span><span class="stat-l">Ergitme ve test ocağı</span></div>
</div></section>

<section class="section"><div class="wrap">
  <div class="sec-head"><p class="eyebrow">Döküm hizmetleri</p>
  <h2>Hangi parçaya hangi döküm? Hepsi tek çatı altında.</h2>
  <p>Alaşımı ve yöntemi parçanızın kullanım yerine göre seçiyoruz. Her hizmet sayfasında yöntemi, uygun alaşımları ve teklif için gerekenleri bulabilirsiniz.</p></div>
  %(cards)s
</div></section>

<section class="section section-dark"><div class="wrap split">
  <div>
    <p class="eyebrow eyebrow-light">Neden Özen Metalurji</p>
    <h2>Teknik resimden sevkiyata kadar tek muhatap.</h2>
    <p class="lead-sm">Dökümde sorunların çoğu, model ile döküm ve analiz farklı yerlerde yapıldığında ortaya çıkar. Biz bu adımları aynı ekip ve aynı tesiste yürütüyoruz.</p>
    <a class="btn btn-molten" href="[[B]]uretim-sureci/">Üretim sürecini incele %(arrow)s</a>
  </div>
  <div class="why-grid">
    <div class="why">%(i_doc)s<h3>Çekme ve işleme payı hesabı</h3><p>Teknik resminiz üzerinden metalin çekmesi ve talaş payları hesaplanır; ölçü riski numuneden önce çözülür.</p></div>
    <div class="why">%(i_gear)s<h3>Kendi modelhanemiz</h3><p>Model, kalıp ve maça kendi bünyemizde hazırlanır; revizyonlar hızlı ve kontrollü yapılır.</p></div>
    <div class="why">%(i_flask)s<h3>XRF ile doğrulanan alaşım</h3><p>Bruker S1 TITAN XRF cihazıyla kimyasal bileşim ölçülür; istenen alaşım raporla teyit edilir.</p></div>
    <div class="why">%(i_shield)s<h3>Tekrarlanabilir kalite</h3><p>Onaylanan ilk numune, seri üretimin referansı olur. Değerlerimizin başında tekrarlanabilir kalite gelir.</p></div>
  </div>
</div></section>

<section class="section"><div class="wrap">
  <div class="sec-head"><p class="eyebrow">Nasıl çalışıyoruz</p><h2>4 adımda dökümünüz hazır</h2></div>
  <ol class="steps">
    <li><span class="step-n">01</span><h3>Teknik resim ve teklif</h3><p>Resim, alaşım ve adet bilgisiyle yöntemi (kum / kokil) ve fiyatı netleştiririz.</p></li>
    <li><span class="step-n">02</span><h3>Model ve kalıp</h3><p>Çekme ve işleme payları hesaplanır, model ve kalıp modelhanemizde hazırlanır.</p></li>
    <li><span class="step-n">03</span><h3>İlk numune ve analiz</h3><p>Numune dökülür, XRF ile alaşım doğrulanır; onayınızla seri üretime geçilir.</p></li>
    <li><span class="step-n">04</span><h3>Seri üretim ve sevkiyat</h3><p>Dekopaj, kumlama ve kontrol sonrası parçalar paketlenip sevk edilir.</p></li>
  </ol>
</div></section>

<section class="section section-tint"><div class="wrap split split-rev">
  <div class="sectors-list">
    <p class="eyebrow">Hizmet verdiğimiz sektörler</p>
    <h2>Makine yedek parçasından cam sanayisine</h2>
    <ul class="chips">
      <li>Makine yedek parçaları</li><li>Cam sanayi</li><li>Plastik şişirme kalıpları</li>
      <li>Tekstil yedek parçaları</li><li>Otomotiv yan sanayi</li><li>Anot döküm sistemleri</li>
    </ul>
    <a class="link-arrow" href="[[B]]sektorler/">Sektörlere göre çözümler %(arrow)s</a>
  </div>
  <figure class="photo photo-tall"><img src="[[A]]img/anot-dokum.jpg" alt="Özen Metalurji Abana fabrikasında dökülmüş alüminyum anotlar" width="800" height="600" loading="lazy" decoding="async"><figcaption>Abana fabrikasında anot döküm</figcaption></figure>
</div></section>

<section class="section"><div class="wrap">
  <div class="sec-head"><p class="eyebrow">İki konum</p><h2>İstanbul'da ofis, Kastamonu Abana'da fabrika</h2>
  <p>Teklif ve proje görüşmeleri için İstanbul ofisimize, üretim ve numune incelemesi için Abana fabrikamıza bekleriz. Ziyaret öncesi telefonla randevu almanızı öneririz.</p></div>
  <div class="maps">%(map1)s%(map2)s</div>
</div></section>

<section class="section section-tint"><div class="wrap narrow">
  <div class="sec-head"><p class="eyebrow">Sık sorulanlar</p><h2>Döküm siparişi öncesi merak edilenler</h2></div>
  %(faq)s
  <p class="center"><a class="link-arrow" href="[[B]]sss/">Tüm soruları gör %(arrow)s</a></p>
</div></section>
""" % {"arrow": icon("arrow", "ic ic-sm"), "check": icon("check", "ic ic-sm"), "cards": service_cards(),
       "i_doc": icon("doc", "ic ic-lg"), "i_gear": icon("gear", "ic ic-lg"), "i_flask": icon("flask", "ic ic-lg"),
       "i_shield": icon("shield", "ic ic-lg"), "map1": map_embed(OFFICE), "map2": map_embed(FACTORY),
       "faq": faq_list(HOME_FAQ, open_first=True)}

add(slug="", nav="home",
    title="Özen Metalurji | Alüminyum, Pirinç, Bronz ve Zamak Döküm Firması",
    description="1974'ten beri alüminyum kum ve kokil, pirinç, bronz, zamak ve anot döküm. Fabrika Abana/Kastamonu, ofis Eyüpsultan/İstanbul. Teklif için hemen arayın.",
    body=home_body,
    schema=[S.webpage("", "Özen Metalurji — Demir dışı metal dökümhanesi", "Alüminyum, pirinç, bronz, zamak ve anot döküm.", about={"@id": S.ORG_ID}),
            S.itemlist("Döküm hizmetleri", [(n, "hizmetler/%s/" % s) for s, n, _, _ in SERVICES]),
            S.faqpage("", HOME_FAQ)],
    page_class="page-home")


# ---------------------------------------------------------------- HAKKIMIZDA
about_body = page_hero("Kurumsal", "Hakkımızda: 1974'ten bugüne Özen Metalurji",
    "Topçular'da küçük bir dökümhane olarak başlayan yolculuk, bugün Kastamonu Abana'da 3.000 m²'lik bir fabrikada üçüncü kuşağa uzanan bir döküm geleneği.",
    [("Hakkımızda", "hakkimizda/")]) + """
<section class="section"><div class="wrap split split-top">
  <div class="prose">
    %(answer)s
    <h2>Kısa tarihçe</h2>
    <p>Firmamız, 1974 Cumhuriyet Bayramı'nın ardından <strong>Mehmet ve Cemal Baş kardeşler</strong> tarafından <strong>Özen Döküm Sanayi</strong> unvanıyla İstanbul Topçular'da faaliyete başladı.</p>
    <p>2007'de bayrağı <strong>Murat, Mustafa ve Musa Baş kardeşler</strong> devraldı ve firma <strong>Özen Metalurji Makine ve Kalıp Sanayi</strong> unvanıyla yoluna devam etti.</p>
    <p>2014'ten itibaren üretim, kardeşlerin memleketi <strong>Kastamonu Abana</strong>'da kurulan fabrikada sürüyor. Tesis 2.000 m² açık ve 1.000 m² kapalı alanıyla hizmet veriyor; İstanbul Eyüpsultan'daki ofis ise satış, teklif ve proje koordinasyonunu yürütüyor.</p>
    <h2>Ne yapıyoruz?</h2>
    <p>Demir dışı metallerin dökümünde uzmanız: <a href="[[B]]hizmetler/aluminyum-kum-dokum/">alüminyum kum</a> ve <a href="[[B]]hizmetler/aluminyum-kokil-dokum/">kokil döküm</a>, <a href="[[B]]hizmetler/pirinc-dokum/">sarı-pirinç döküm</a>, <a href="[[B]]hizmetler/bronz-dokum/">kızıl-bronz döküm</a>, <a href="[[B]]hizmetler/zamak-dokum/">zamak döküm</a> ve <a href="[[B]]hizmetler/anot-dokum/">anot döküm</a>. Makine yedek parçası, cam sanayi, plastik şişirme kalıpları, tekstil yedek parçaları, otomotiv ve anot döküm sistemleri gibi geniş bir yelpazede yurt içi ve yurt dışındaki müşterilere üretim yapıyoruz.</p>
    <p>Yapılacak işin teknik resminden yola çıkarak çekme ve işleme paylarını hesaplıyor; model ve kalıp aşamalarını ilk numune ve analiz değerlerine kadar kendi bünyemizde, tekrarlanabilir kaliteyle ve en uygun fiyatla yürütüyoruz. Gerekli analizleri kendi laboratuvarımızda yaparak müşterilerimize doğrulanmış bilgiyle hizmet veriyoruz.</p>
  </div>
  <aside class="side">
    <div class="timeline">
      <div class="tl"><span class="tl-y">1974</span><p>Özen Döküm Sanayi, Topçular / İstanbul'da kuruldu.</p></div>
      <div class="tl"><span class="tl-y">2007</span><p>İkinci kuşak devraldı: Özen Metalurji Makine ve Kalıp Sanayi.</p></div>
      <div class="tl"><span class="tl-y">2014</span><p>Üretim Kastamonu Abana'daki yeni fabrikaya taşındı.</p></div>
      <div class="tl tl-now"><span class="tl-y">Bugün</span><p>Al, pirinç, bronz, zamak ve anot dökümde yurt içi ve yurt dışına üretim.</p></div>
    </div>
    %(facts)s
  </aside>
</div></section>

<section class="section section-tint"><div class="wrap">
  <div class="sec-head"><p class="eyebrow">Biz kimiz</p><h2>Vizyon, misyon ve değerlerimiz</h2></div>
  <div class="vmv">
    <article class="vm"><h3>Vizyonumuz</h3><p>Yenilikçi, akılcı, ilkeli ve sorumlu yaklaşımlarımızla sektörde öncü ve üretimde örnek bir firma olabilmek.</p></article>
    <article class="vm"><h3>Misyonumuz</h3><p>Uzman kadrolarımızla doğru, güvenilir, çözüm ve üretim odaklı hizmet verebilmek.</p></article>
    <article class="vm"><h3>Değerlerimiz</h3><ul class="ticks"><li>%(c)s Tekrarlanabilir kalite odaklılık</li><li>%(c)s Dürüstlük</li><li>%(c)s Güvenilirlik</li><li>%(c)s Sürekli yenilik</li></ul></article>
  </div>
</div></section>

<section class="section"><div class="wrap split">
  <figure class="photo"><img src="[[A]]img/ozen-metalurji-banner.jpg" alt="Özen Metalurji döküm üretimi" width="1200" height="600" loading="lazy" decoding="async"></figure>
  <div class="prose">
    <p class="eyebrow">Kalite politikamız</p>
    <h2>Müşteri memnuniyetini ihtiyaç ve talepler doğrultusunda en üst seviyede tutmak</h2>
    <ul class="ticks">
      <li>%(c)s Kalite geliştirme çalışmalarını tüm çalışanlarımızın gelişimiyle desteklemek</li>
      <li>%(c)s Müşterilerimize uluslararası düzeyde kabul görmüş ürün ve hizmetler sunmak</li>
      <li>%(c)s Çevreye saygılı, kullanıcısına güven veren ürünlerimizi müşteri istekleri doğrultusunda geliştirmek</li>
      <li>%(c)s Çalışanlarımızı sürekli gelişme ve iyileştirme bilinciyle eğitmek</li>
      <li>%(c)s Tecrübe ve teknolojimizi dünya pazarlarına taşımak</li>
    </ul>
    <a class="link-arrow" href="[[B]]kalite-ve-laboratuvar/">Kalite ve laboratuvar %(arrow)s</a>
  </div>
</div></section>
""" % {"answer": answer_box("Özen Metalurji ne zaman kuruldu ve nerede üretim yapıyor?",
                            "Özen Metalurji'nin temeli 1974'te İstanbul Topçular'da atıldı. 2014'ten bu yana üretim Kastamonu Abana'daki 2.000 m² açık, 1.000 m² kapalı alana sahip fabrikada yapılıyor; satış ofisi İstanbul Eyüpsultan'da."),
       "facts": facts_table([("Unvan", "Özen Metalurji Makine ve Kalıp San. Tic. Ltd. Şti."), ("Kuruluş", "1974 (Özen Döküm Sanayi)"),
                             ("Fabrika", "Abana / Kastamonu — 2.000 m² açık, 1.000 m² kapalı"), ("Ofis", "Topçular, Eyüpsultan / İstanbul"),
                             ("Uzmanlık", "Demir dışı metal dökümü")], "Künye"),
       "c": icon("check", "ic ic-sm"), "arrow": icon("arrow", "ic ic-sm")}

add(slug="hakkimizda", nav="kurumsal",
    title="Hakkımızda | 1974'ten Beri Döküm — Özen Metalurji",
    description="1974'te Topçular'da Özen Döküm olarak kuruldu, 2014'ten beri Kastamonu Abana'da üretiyor. Tarihçe, vizyon, misyon ve kalite politikamız.",
    body=about_body,
    schema=[S.webpage("hakkimizda/", "Hakkımızda", "Özen Metalurji tarihçesi, vizyon, misyon ve kalite politikası.", "AboutPage", about={"@id": S.ORG_ID}),
            S.breadcrumb([("Hakkımızda", "hakkimizda/")])])


# ---------------------------------------------------------------- TESİSLERİMİZ
mach = "".join('<div class="mgroup"><h3>%s</h3><ul class="ticks">%s</ul></div>' %
               (g, "".join("<li>%s %s</li>" % (icon("check", "ic ic-sm"), m) for m in items)) for g, items in MACHINES)
plant_body = page_hero("Kurumsal", "Tesislerimiz ve makine parkurumuz",
    "Kastamonu Abana'daki döküm fabrikamız ve İstanbul Eyüpsultan'daki ofisimiz; indüksiyon ve rezistanslı ocaklardan XRF analiz cihazına kadar tüm ekipmanımız.",
    [("Tesislerimiz", "tesislerimiz/")]) + """
<section class="section"><div class="wrap">
  %(answer)s
  <div class="plants">
    <article class="plant"><p class="eyebrow">Üretim</p><h2>Abana Döküm Fabrikası</h2>
      <p>2014'te faaliyete geçen fabrikamız Kastamonu'nun Abana ilçesinde, <strong>2.000 m² açık ve 1.000 m² kapalı alan</strong> üzerinde kuruludur. Ergitme, kalıplama, maça, döküm, dekopaj, kumlama ve analiz aynı tesiste yapılır.</p>
      <address>%(fstreet)s, Abana / Kastamonu</address><p>%(phone)s %(ftel)s</p></article>
    <article class="plant"><p class="eyebrow">Satış ve proje</p><h2>İstanbul Merkez Ofis</h2>
      <p>Eyüpsultan Topçular'daki ofisimiz teklif, teknik görüşme, numune onayı ve sevkiyat koordinasyonunu yürütür. Firmamızın 1974'te kurulduğu semtteyiz.</p>
      <address>%(ostreet)s, Eyüpsultan / İstanbul</address><p>%(phone)s %(otel)s</p></article>
  </div>
</div></section>
<section class="section section-tint"><div class="wrap">
  <div class="sec-head"><p class="eyebrow">Makine parkuru</p><h2>Ergitmeden temizlemeye ekipmanlarımız</h2>
  <p>Toplamda tek seferde 500 kg'a kadar indüksiyonla ergitme kapasitesi; alüminyum için ayrı rezistanslı ocaklar.</p></div>
  <div class="mgrid">%(mach)s</div>
</div></section>
<section class="section"><div class="wrap">
  <div class="sec-head"><p class="eyebrow">Fabrikadan kareler</p><h2>Anot üretimi ve sevkiyat</h2></div>
  <div class="gallery">
    <figure><img src="[[A]]img/anot-aluminyum-hammadde.jpg" alt="Yurt dışı menşeli %%99,80 saflıkta alüminyum hammadde" width="600" height="450" loading="lazy" decoding="async"><figcaption>%%99,80 saf alüminyum hammadde</figcaption></figure>
    <figure><img src="[[A]]img/anot-dokum.jpg" alt="Dökülmüş alüminyum anotlar" width="600" height="450" loading="lazy" decoding="async"><figcaption>Anot döküm</figcaption></figure>
    <figure><img src="[[A]]img/anot-malzeme-depolama.jpg" alt="Abana fabrikası malzeme depolama alanı" width="600" height="450" loading="lazy" decoding="async"><figcaption>Malzeme depolama alanı</figcaption></figure>
    <figure><img src="[[A]]img/anot-palet-ambalaj.jpg" alt="2,5 tonluk paletlerde ambalajlanmış anotlar" width="600" height="450" loading="lazy" decoding="async"><figcaption>Ambalajlı anotlar (2,5 ton palet)</figcaption></figure>
    <figure><img src="[[A]]img/anot-sevkiyat.jpg" alt="Sevkiyata hazırlanan anotlar" width="600" height="450" loading="lazy" decoding="async"><figcaption>Sevk edilen anotlar</figcaption></figure>
  </div>
</div></section>
<section class="section section-tint"><div class="wrap"><div class="maps">%(map1)s%(map2)s</div></div></section>
""" % {"answer": answer_box("Özen Metalurji'nin üretim kapasitesi ve ekipmanı nedir?",
                            "Abana fabrikasında 300 kg ve 500 kg indüksiyon ocakları, 200/300/350 kg alüminyum rezistanslı ocaklar, tam otomatik maça makinesi, 2 kokil döküm makinesi ve Bruker S1 TITAN XRF analiz cihazı bulunur."),
       "fstreet": FACTORY["street"], "ostreet": OFFICE["street"], "phone": icon("phone", "ic ic-xs"),
       "ftel": tel(FACTORY), "otel": tel(OFFICE), "mach": mach, "map1": map_embed(FACTORY), "map2": map_embed(OFFICE)}

add(slug="tesislerimiz", nav="kurumsal",
    title="Tesislerimiz ve Makine Parkuru | Abana Fabrikası — Özen Metalurji",
    description="Abana fabrikamız: 2.000 m² açık, 1.000 m² kapalı alan; 300 ve 500 kg indüksiyon ocakları, alüminyum rezistanslı ocaklar, kokil makineleri ve XRF analiz.",
    body=plant_body,
    schema=[S.webpage("tesislerimiz/", "Tesislerimiz ve Makine Parkuru", "Abana fabrikası ve makine parkuru."),
            S.breadcrumb([("Tesislerimiz", "tesislerimiz/")])])


# ---------------------------------------------------------------- KALİTE
QFAQ = [
    ("XRF analizi nedir, dökümde neden önemlidir?",
     "XRF (X-ışını floresansı) metalin kimyasal bileşimini numuneye zarar vermeden saniyeler içinde ölçen bir yöntemdir. Dökümde, ergitilen metalin istenen alaşım sınırları içinde olup olmadığını döküm öncesinde ve sonrasında doğrulamaya yarar."),
    ("Analiz raporu verebiliyor musunuz?",
     "Evet. XRF ile ölçülen kimyasal bileşim, talep edilmesi halinde partiyle birlikte raporlanır. Mekanik test gibi ek test ihtiyaçlarınızı teklif aşamasında belirtmenizi rica ederiz."),
    ("Döküm sıcaklığını nasıl kontrol ediyorsunuz?",
     "Döküm sıcaklığı IMPAC sıcaklık ölçüm cihazıyla ölçülür. Doğru sıcaklık; akışkanlık, gaz boşluğu ve çekinti hataları açısından kritik olduğu için her alaşımda takip edilir."),
]
quality_body = page_hero("Kurumsal", "Kalite ve laboratuvar",
    "Alaşımı tahmine bırakmıyoruz: ergitmeden numuneye kadar kimyasal bileşim XRF ile ölçülür, sıcaklık kontrol altında tutulur, ilk numune onayı seri üretimin referansı olur.",
    [("Kalite ve Laboratuvar", "kalite-ve-laboratuvar/")]) + """
<section class="section"><div class="wrap split split-top">
  <div class="prose">
    %(answer)s
    <h2>Laboratuvarımız</h2>
    <p>Abana fabrikamızdaki laboratuvarda paslanmaz çelik ve hafif element alaşımlarının analizi için tasarlanmış, Amerikan-Alman ortak yapımı <strong>Bruker S1 TITAN XRF</strong> cihazını tam kalibrasyonla kullanıyoruz. Alüminyum, pirinç, bronz ve zamak alaşımlarının kimyasal bileşimi bu cihazla ölçülür.</p>
    <p>Yeni alaşımlar ve küçük partiler için <strong>indüksiyonlu test ocağı</strong> ile deneme ergitmesi yapabiliyoruz. Döküm sıcaklığı <strong>IMPAC</strong> ölçüm cihazıyla takip edilir.</p>
    <h2>Kalite nasıl güvence altına alınır?</h2>
    <ol class="olist">
      <li><strong>Hammadde kontrolü:</strong> Gelen külçe ve hurdanın bileşimi XRF ile kontrol edilir.</li>
      <li><strong>Ergitme kontrolü:</strong> Ergiyik, döküm öncesi analiz edilir; gerekiyorsa alaşım düzeltilir.</li>
      <li><strong>Sıcaklık takibi:</strong> Her alaşım kendi döküm sıcaklığı aralığında dökülür.</li>
      <li><strong>İlk numune onayı:</strong> Ölçü ve analiz değerleri onaylanan numune, serinin referansı olur.</li>
      <li><strong>Son kontrol:</strong> Dekopaj ve kumlama sonrası görsel ve ölçüsel kontrol yapılır.</li>
    </ol>
  </div>
  <aside class="side">%(facts)s</aside>
</div></section>
<section class="section section-tint"><div class="wrap narrow">
  <div class="sec-head"><h2>Kalite hakkında sorular</h2></div>%(faq)s
</div></section>
""" % {"answer": answer_box("Özen Metalurji alaşım kalitesini nasıl doğrular?",
                            "Kimyasal bileşim, kendi laboratuvarımızdaki tam kalibrasyonlu Bruker S1 TITAN XRF cihazıyla ergitme sırasında ve numunede ölçülür; döküm sıcaklığı IMPAC cihazıyla izlenir; seri üretim, onaylanan ilk numuneye göre yapılır."),
       "facts": facts_table([("Analiz cihazı", "Bruker S1 TITAN XRF (tam kalibrasyon)"), ("Sıcaklık ölçümü", "IMPAC ölçüm cihazı"),
                             ("Deneme ergitmesi", "İndüksiyonlu test ocağı"), ("Referans", "Onaylı ilk numune"),
                             ("Rapor", "Talebe göre kimyasal analiz raporu")], "Laboratuvar özeti"),
       "faq": faq_list(QFAQ)}

add(slug="kalite-ve-laboratuvar", nav="kurumsal",
    title="Kalite ve Laboratuvar | XRF Alaşım Analizi — Özen Metalurji",
    description="Özen Metalurji laboratuvarında Bruker S1 TITAN XRF ile alaşım analizi, IMPAC ile sıcaklık takibi ve ilk numune onayıyla tekrarlanabilir döküm kalitesi.",
    body=quality_body,
    schema=[S.webpage("kalite-ve-laboratuvar/", "Kalite ve Laboratuvar", "XRF ile alaşım analizi ve kalite güvencesi."),
            S.breadcrumb([("Kalite ve Laboratuvar", "kalite-ve-laboratuvar/")]), S.faqpage("kalite-ve-laboratuvar/", QFAQ)])


# ---------------------------------------------------------------- ÜRETİM SÜRECİ
PROC = [
    ("Teknik resim ve fizibilite", "Teknik resminizi (PDF, DWG/DXF, STEP) inceler; alaşımı, döküm yöntemini (kum veya kokil), parça ağırlığını ve adedi birlikte netleştiririz."),
    ("Çekme ve işleme payı hesabı", "Her metal soğurken farklı oranda çeker. Model ölçüleri bu çekmeye ve sonradan yapılacak talaşlı işleme payına göre hesaplanır."),
    ("Model ve kalıp imalatı", "Model ve kokil kalıplar modelhanemizde hazırlanır. İç boşluklar için maçalar tam otomatik maça makinesinde üretilir."),
    ("Kalıplama", "Kum döküm için kalıp kumu kum değirmenlerinde hazırlanır, elenir ve kalıplanır. Kokil dökümde metal kalıp ön ısıtılarak döküme hazırlanır."),
    ("Ergitme ve analiz", "Metal, alaşımına göre indüksiyon ya da rezistanslı ocakta ergitilir. Bileşim XRF ile ölçülür, döküm sıcaklığı IMPAC ile kontrol edilir."),
    ("Döküm", "Ergiyik metal, kontrollü hız ve sıcaklıkla kalıba dökülür; parça kalıpta katılaşır."),
    ("Dekopaj, kesme ve kumlama", "Parça kalıptan çıkarılır (dekopaj), yolluk ve besleyiciler testereyle kesilir, yüzey kumlama makinesinde temizlenir."),
    ("Kontrol ve sevkiyat", "Ölçü ve görsel kontroller yapılır; ilk numune onaylandıktan sonra seri üretim paketlenerek sevk edilir."),
]
proc_html = "".join('<li class="pstep"><span class="pstep-n">%02d</span><div><h3>%s</h3><p>%s</p></div></li>' % (i, t, d) for i, (t, d) in enumerate(PROC, 1))
process_body = page_hero("Kurumsal", "Döküm üretim süreci: teknik resimden sevkiyata 8 adım",
    "Bir döküm parçası atölyemize teknik resim olarak girer, analiz raporuyla çıkar. Her adımda ne yaptığımızı ve neden önemli olduğunu anlattık.",
    [("Üretim Süreci", "uretim-sureci/")]) + """
<section class="section"><div class="wrap narrow">
  %(answer)s
  <ol class="process">%(proc)s</ol>
  <div class="note"><h2>Teklif sürecini hızlandırmak için</h2>
  <p>Teknik resmin yanında alaşım (ör. AlSi12, CuSn10, CuZn39Pb1Al), adet, işlenmiş/ham teslim bilgisi ve varsa mevcut model veya kalıp fotoğraflarını gönderin. <a href="[[B]]bilgi-merkezi/dokum-teklifi-icin-gerekenler/">Döküm teklifi için gerekenler</a> rehberimize göz atabilirsiniz.</p></div>
</div></section>
""" % {"answer": answer_box("Döküm parçası nasıl üretilir?",
                            "Teknik resimden çekme ve işleme payları hesaplanır, model ve kalıp hazırlanır, metal ergitilip XRF ile analiz edilir, kalıba dökülür; ardından dekopaj, kesme, kumlama ve kontrolden geçirilerek sevk edilir."),
       "proc": proc_html}

add(slug="uretim-sureci", nav="kurumsal",
    title="Döküm Üretim Süreci: 8 Adımda Parça Üretimi — Özen Metalurji",
    description="Döküm nasıl yapılır? Teknik resim, çekme payı hesabı, model ve kalıp, kalıplama, ergitme ve XRF analiz, döküm, dekopaj ve kumlama, kontrol ve sevkiyat adımları.",
    body=process_body,
    schema=[S.webpage("uretim-sureci/", "Döküm Üretim Süreci", "Teknik resimden sevkiyata 8 adımda döküm üretimi."),
            S.breadcrumb([("Üretim Süreci", "uretim-sureci/")]),
            {"@type": "ItemList", "name": "Döküm üretim adımları", "itemListOrder": "https://schema.org/ItemListOrderAscending",
             "itemListElement": [{"@type": "ListItem", "position": i, "name": t, "description": d} for i, (t, d) in enumerate(PROC, 1)]}])


# ---------------------------------------------------------------- SEKTÖRLER
SECTORS = [
    ("Makine yedek parçaları", "gear", "Gövde, kapak, flanş, kasnak, burç ve yatak gibi parçalar; alüminyum, pirinç ve bronz alaşımlarında.", "bronz-dokum"),
    ("Cam sanayi", "fire", "Cam şekillendirme hatlarında kullanılan demir dışı döküm parçalar; ısıl dayanım ve ölçü tutarlılığı odaklı.", "bronz-dokum"),
    ("Plastik şişirme kalıpları", "die", "Şişirme kalıplarında ısı iletimi yüksek alüminyum ve bronz kalıp parçaları.", "aluminyum-kum-dokum"),
    ("Tekstil yedek parçaları", "gear", "Tekstil makineleri için hafif alüminyum parçalar ve aşınmaya dayanıklı bronz burçlar.", "aluminyum-kokil-dokum"),
    ("Otomotiv yan sanayi", "truck", "Hafiflik ve tekrarlanabilir ölçü gerektiren alüminyum ve zamak parçalar.", "aluminyum-kokil-dokum"),
    ("Anot döküm sistemleri", "anode", "%99,80 saf alüminyumdan anot dökümü, 2,5 tonluk paletlerde sevkiyat.", "anot-dokum"),
]
sec_html = "".join('<article class="sector"><span class="svc-ic">%s</span><h2>%s</h2><p>%s</p><a class="link-arrow" href="[[B]]hizmetler/%s/">İlgili döküm hizmeti %s</a></article>'
                   % (icon(ic), n, d, l, icon("arrow", "ic ic-sm")) for n, ic, d, l in SECTORS)
sectors_body = page_hero("Sektörler", "Hizmet verdiğimiz sektörler",
    "Makine yedek parçasından cam sanayisine, plastik şişirme kalıplarından anot sistemlerine kadar farklı sektörlere demir dışı döküm parça üretiyoruz.",
    [("Sektörler", "sektorler/")]) + """
<section class="section"><div class="wrap">%(answer)s<div class="sector-grid">%(sec)s</div></div></section>
""" % {"answer": answer_box("Özen Metalurji hangi sektörlere döküm yapıyor?",
                            "Makine yedek parçaları, cam sanayi, plastik şişirme kalıpları, tekstil yedek parçaları, otomotiv yan sanayi ve anot döküm sistemleri başta olmak üzere yurt içi ve yurt dışındaki müşterilere demir dışı döküm parça üretiyoruz."),
       "sec": sec_html}

add(slug="sektorler", nav="sektorler",
    title="Sektörler | Makine, Cam, Kalıp, Tekstil, Otomotiv — Özen Metalurji",
    description="Özen Metalurji; makine yedek parçası, cam sanayi, plastik şişirme kalıpları, tekstil, otomotiv ve anot sistemleri için alüminyum, pirinç, bronz ve zamak döküm yapar.",
    body=sectors_body,
    schema=[S.webpage("sektorler/", "Sektörler", "Hizmet verilen sektörler."), S.breadcrumb([("Sektörler", "sektorler/")])])
