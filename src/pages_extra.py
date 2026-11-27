# -*- coding: utf-8 -*-
"""SSS, Bilgi Merkezi, İletişim, KVKK, 404."""
from data import OFFICE, FACTORY, EMAIL, SERVICES
from ui import icon, page_hero, answer_box, faq_list, data_table, map_embed, tel
import schema as S

PAGES = []

# ---------------------------------------------------------------- SSS
FAQ_GROUPS = [
    ("Firma ve konum", [
        ("Özen Metalurji nedir?", "Özen Metalurji, 1974'te İstanbul Topçular'da kurulan ve bugün Kastamonu Abana'daki fabrikasında alüminyum, pirinç, bronz, zamak ve anot döküm yapan bir demir dışı metal dökümhanesidir."),
        ("Fabrikanız ve ofisiniz nerede?", "Fabrikamız Merkez Mah. Sabri Kalafat Cad. No:66 Abana / Kastamonu adresindedir. Ofisimiz Topçular Mah. Rami Kışla Cad. Uzak Çiftlik Sok. No:19/B Eyüpsultan / İstanbul adresindedir (Bayrampaşa – Maltepe metro durağına yakın)."),
        ("Tesisinizi ziyaret edebilir miyim?", "Evet. Ofis ya da fabrika ziyareti için önceden telefonla randevu almanızı rica ederiz: İstanbul 0 212 567 71 26, Abana 0 366 564 14 97."),
        ("Yurt dışına üretim yapıyor musunuz?", "Evet. Yurt içi müşterilerimizin yanı sıra yurt dışındaki müşterilere de üretim ve sevkiyat yapıyoruz."),
    ]),
    ("Döküm ve alaşımlar", [
        ("Hangi metalleri döküyorsunuz?", "Demir dışı metaller döküyoruz: alüminyum (kum ve kokil), pirinç (sarı döküm), bronz (kızıl döküm), zamak ve %99,80 saf alüminyumdan anot. Pik, sfero ve çelik döküm yapmıyoruz."),
        ("Kum döküm ile kokil döküm arasındaki fark nedir?", "Kum dökümde her parça için bozulan bir kum kalıp kullanılır; kalıp maliyeti düşüktür, numune ve büyük parçalara uygundur. Kokil dökümde kalıcı metal kalıp kullanılır; seri üretimde daha tekrarlanabilir ölçü ve daha düzgün yüzey sağlar."),
        ("Pirinç ve bronz döküm arasındaki fark nedir?", "Pirincin ana alaşım elementi çinko, bronzunki kalaydır (veya alüminyum). Pirinç daha kolay işlenir ve ekonomiktir; bronz aşınma ve sürtünmeye daha dayanıklıdır, bu yüzden burç ve yataklarda tercih edilir."),
        ("Tek seferde ne kadar metal ergitebiliyorsunuz?", "İndüksiyon ocaklarımız 300 kg ve 500 kg, alüminyum rezistanslı ocaklarımız 200, 300 ve 350 kg kapasitelidir. Döküm parçanın ağırlık sınırı yöntem ve kalıplama şekline göre teklif aşamasında teyit edilir."),
        ("Alaşım analizi yapıyor musunuz?", "Evet. Kendi laboratuvarımızda tam kalibrasyonlu Bruker S1 TITAN XRF cihazıyla kimyasal bileşim ölçüyoruz; talep edilirse analiz raporu veriyoruz."),
    ]),
    ("Sipariş ve teklif", [
        ("Teklif için ne göndermeliyim?", "Teknik resim (PDF, DWG/DXF veya STEP), alaşım veya parçanın kullanım yeri, adet (numune ve yıllık tahmin), ham ya da işlenmiş teslim bilgisi ve varsa mevcut model/kalıp bilgisi."),
        ("Model ve kalıp yapıyor musunuz?", "Evet. Çekme ve işleme payları hesaplanarak model, kalıp ve maça aşamaları kendi bünyemizde yürütülür."),
        ("Elimde model var, kullanabilir misiniz?", "Mevcut modeliniz incelenir; ölçü ve durumu uygunsa kullanılabilir, gerekirse revize edilir."),
        ("Numune üretiyor musunuz?", "Evet. Seri üretim öncesi ilk numune dökülür, ölçü ve analiz değerleri onayınıza sunulur; onaylanan numune seri üretimin referansı olur."),
        ("Teslim süresi ne kadar?", "Teslim süresi; model/kalıp ihtiyacına, alaşıma, adede ve parça ağırlığına göre değişir. Teklifimizde net termin bilgisini paylaşırız."),
        ("Teklif talebime ne kadar sürede dönüş yapılır?", "Teklif talepleri İstanbul ofisimizde değerlendirilir. Acil işleriniz için 0 212 567 71 26 numarasından bize doğrudan ulaşabilirsiniz."),
    ]),
]
all_faq = [qa for _, g in FAQ_GROUPS for qa in g]
faq_html = "".join('<h2 class="faq-h">%s</h2>%s' % (t, faq_list(g)) for t, g in FAQ_GROUPS)
PAGES.append(dict(slug="sss", nav="sss",
    title="Sık Sorulan Sorular | Döküm, Alaşım ve Teklif — Özen Metalurji",
    description="Döküm siparişi öncesi merak edilenler: hangi metaller dökülür, kum ve kokil döküm farkı, ergitme kapasitesi, XRF analiz, model/kalıp, numune ve teklif süreci.",
    body=page_hero("Sık sorulan sorular", "Döküm hakkında sık sorulan sorular",
                   "Özen Metalurji, döküm yöntemleri, alaşımlar, teklif ve sipariş süreci hakkında en çok sorulan soruların kısa ve net cevapları.",
                   [("SSS", "sss/")]) + '<section class="section"><div class="wrap narrow">%s</div></section>' % faq_html,
    schema=[S.webpage("sss/", "Sık Sorulan Sorular", "Döküm hakkında sık sorulan sorular.", "FAQPage"),
            S.breadcrumb([("SSS", "sss/")]), S.faqpage("sss/", all_faq)]))
# FAQPage hem webpage tipi hem mainEntity taşıyor: ikisini birleştir
PAGES[-1]["schema"] = [S.breadcrumb([("SSS", "sss/")]),
                       dict(S.faqpage("sss/", all_faq), **{"url": "[[S]]sss/", "name": "Sık Sorulan Sorular",
                                                          "inLanguage": "tr-TR", "isPartOf": {"@id": S.SITE_ID}})]

# ---------------------------------------------------------------- BİLGİ MERKEZİ
ARTICLES = []


def art(slug, title, h1, desc, lead, answer_q, answer_a, body, faqs=None, read="5 dk"):
    ARTICLES.append((slug, h1, desc, read))
    path = "bilgi-merkezi/%s/" % slug
    faq_block = ('<h2>Sık sorulan sorular</h2>' + faq_list(faqs)) if faqs else ""
    html = page_hero("Bilgi merkezi", h1, lead, [("Bilgi Merkezi", "bilgi-merkezi/"), (h1, path)],
                     extra='<p class="meta">Özen Metalurji · Güncelleme: 27 Kasım 2026 · Okuma süresi: %s</p>' % read) + """
<section class="section"><div class="wrap split split-top">
  <article class="prose">%s%s%s</article>
  <aside class="side side-sticky"><div class="side-card side-card-dark">
    <p class="eyebrow eyebrow-light">Parçanız için öneri alın</p>
    <p>Teknik resminizi gönderin; yöntem ve alaşım önerisiyle teklif hazırlayalım.</p>
    <a class="btn btn-molten btn-block" href="[[B]]iletisim/#teklif">Teklif İste %s</a></div>
    <div class="side-card"><h3>Döküm hizmetleri</h3><ul class="rel">%s</ul></div>
  </aside>
</div></section>""" % (answer_box(answer_q, answer_a), body, faq_block, icon("arrow", "ic ic-sm"),
                       "".join('<li><a href="[[B]]hizmetler/%s/">%s %s</a></li>' % (s, icon(ic, "ic ic-sm"), n) for s, n, _, ic in SERVICES))
    sch = [S.webpage(path, h1, desc), S.breadcrumb([("Bilgi Merkezi", "bilgi-merkezi/"), (h1, path)]), S.article(path, h1, desc)]
    if faqs:
        sch.append(S.faqpage(path, faqs))
    PAGES.append(dict(slug=path.rstrip("/"), nav="bilgi", title=title, description=desc, body=html, schema=sch, og_type="article"))


art("kum-dokum-ve-kokil-dokum-farki",
    "Kum Döküm ile Kokil Döküm Arasındaki Fark | Hangisi Seçilmeli?",
    "Kum döküm ile kokil döküm arasındaki fark nedir?",
    "Kum döküm ve kokil (metal kalıp) döküm karşılaştırması: kalıp maliyeti, adet, yüzey kalitesi, ölçü ve mekanik özellikler. Hangi parça için hangisi seçilmeli?",
    "Alüminyum, pirinç ve bronz parçalarda en sık sorulan soru: kum mu, kokil mi? Kalıp maliyetinden yüzey kalitesine farkları ve doğru seçimi tek tabloda topladık.",
    "Kum döküm mü, kokil döküm mü?",
    "Kum dökümde her parça için bozulan kum kalıp kullanılır; kalıp maliyeti düşük, esneklik yüksektir ve numune, az adet ve büyük parçalar için uygundur. Kokil dökümde kalıcı metal kalıp kullanılır; seri üretimde tekrarlanabilir ölçü, düzgün yüzey ve daha iyi mekanik özellik sağlar.",
    """<h2>Kum döküm nedir?</h2>
<p>Kum dökümde parçanın modeli bağlayıcılı kalıp kumuna basılarak bir boşluk oluşturulur. İç kanallar için maça yerleştirilir ve ergimiş metal bu boşluğa dökülür. Metal katılaştıktan sonra kalıp bozularak parça çıkarılır. Her döküm için yeni kalıp hazırlandığından yöntem esnektir; model değişikliği kolaydır.</p>
<h2>Kokil döküm nedir?</h2>
<p>Kokil döküm (gravite döküm), çelik veya dökme demirden işlenmiş kalıcı bir metal kalıba ergimiş metalin yer çekimiyle dökülmesidir. Aynı kalıpla çok sayıda parça üretilir. Metal kalıp ısıyı hızlı çektiği için parça daha ince taneli ve sağlam bir yapıyla katılaşır.</p>
<h2>Karşılaştırma tablosu</h2>
""" + data_table(["Kriter", "Kum döküm", "Kokil döküm"], [
        ["Kalıp maliyeti", "Düşük (model yeterli)", "Yüksek (işlenmiş metal kalıp)"],
        ["Ekonomik adet", "Numune – orta seri", "Orta – yüksek seri"],
        ["Parça boyutu", "Küçükten çok büyüğe", "Küçük ve orta boy"],
        ["Yüzey kalitesi", "Daha pürüzlü", "Daha düzgün"],
        ["Ölçü tekrarlanabilirliği", "İyi", "Çok iyi"],
        ["Mekanik özellik", "İyi", "Daha iyi (hızlı katılaşma)"],
        ["Tasarım değişikliği", "Hızlı ve ucuz", "Kalıp revizyonu gerekir"],
    ], caption="Kum döküm ve kokil döküm karşılaştırması") + """
<h2>Hangi durumda hangisi?</h2>
<ul class="ticks"><li><strong>Kum döküm seçin:</strong> numune veya prototip aşamasındaysanız, adet düşükse, parça büyükse ya da tasarım henüz kesinleşmediyse.</li>
<li><strong>Kokil döküm seçin:</strong> tasarım kesinleştiyse, yıllık adet yüksekse, düzgün yüzey ve dar ölçü toleransı istiyorsanız.</li></ul>
<p>Pratikte birçok proje kum dökümle başlar; numuneler onaylanıp adetler netleştikten sonra kokile geçilir. Özen Metalurji'de her iki yöntem de aynı tesiste uygulandığı için bu geçiş, aynı ekip ve aynı alaşım kontrolüyle yapılır. Detaylar için <a href="[[B]]hizmetler/aluminyum-kum-dokum/">alüminyum kum döküm</a> ve <a href="[[B]]hizmetler/aluminyum-kokil-dokum/">alüminyum kokil döküm</a> sayfalarımıza bakabilirsiniz.</p>""",
    faqs=[("Kokil döküm kum dökümden daha mı kalitelidir?", "Daha kaliteli değil, farklı amaçlara uygundur. Kokil döküm seri üretimde daha düzgün yüzey ve ölçü verir; kum döküm ise büyük, karmaşık ve az adetli parçalarda daha ekonomik ve esnektir."),
          ("Kum dökümden kokile geçmek için model değişir mi?", "Evet; kokil için metal kalıp ayrıca işlenir. Kum döküm numunesiyle onaylanan ölçüler kalıp tasarımına referans olur.")])

art("pirinc-ve-bronz-dokum-farki",
    "Pirinç ve Bronz Döküm Farkı | Sarı Döküm mü Kızıl Döküm mü?",
    "Pirinç ve bronz döküm arasındaki fark nedir?",
    "Pirinç (sarı döküm) ile bronz (kızıl döküm) farkı: alaşım elementleri, işlenebilirlik, aşınma dayanımı, maliyet ve kullanım alanları. Hangi parça için hangi alaşım?",
    "Sanayide 'sarı döküm' ve 'kızıl döküm' diye anılan iki bakır alaşımı arasındaki farkları, hangi parçada hangisinin seçileceğiyle birlikte anlattık.",
    "Pirinç mi bronz mu?",
    "Pirinç bakır ile çinkonun, bronz ise bakır ile başta kalayın (veya alüminyumun) alaşımıdır. Pirinç daha kolay işlenir ve genellikle daha ekonomiktir; vana, rakor ve armatürde kullanılır. Bronz aşınma ve sürtünmeye daha dayanıklıdır; burç, yatak ve dişlide tercih edilir.",
    """<h2>Pirinç (sarı döküm)</h2>
<p>Pirinç, bakıra çinko katılarak elde edilir; rengi altın sarısıdır. Kurşun ilaveli türleri talaşlı işlemede çok kısa talaş verdiği için işleme süresini kısaltır. Su ve atmosfer ortamında korozyona dayanıklıdır. Vana gövdeleri, rakorlar, armatürler ve genel makine parçaları başlıca kullanım alanlarıdır.</p>
<h2>Bronz (kızıl döküm)</h2>
<p>Bronz, bakıra başta kalay olmak üzere alüminyum, nikel veya kurşun katılarak elde edilir; kızılımsı bir renge sahiptir. Düşük sürtünme katsayısı ve yüksek aşınma dayanımı nedeniyle kaymalı yatak, burç, dişli ve kızakların klasik malzemesidir. Alüminyum bronzları yüksek mukavemet ve deniz suyu dahil zorlu ortamlarda korozyon direnci sunar.</p>
<h2>Karşılaştırma tablosu</h2>
""" + data_table(["Kriter", "Pirinç (sarı)", "Bronz (kızıl)"], [
        ["Ana alaşım elementi", "Çinko", "Kalay (veya alüminyum)"],
        ["Renk", "Sarı", "Kızılımsı kahve"],
        ["İşlenebilirlik", "Çok iyi (kurşunlu türler)", "İyi"],
        ["Aşınma / sürtünme dayanımı", "Orta", "Yüksek"],
        ["Korozyon direnci", "İyi", "Çok iyi (özellikle Al bronzu)"],
        ["Maliyet", "Genellikle daha ekonomik", "Genellikle daha yüksek"],
        ["Tipik parçalar", "Vana, rakor, armatür", "Burç, yatak, dişli, pompa parçası"],
    ], caption="Pirinç ve bronz döküm karşılaştırması") + """
<h2>Doğru seçim için sorulacak 3 soru</h2>
<ol class="olist"><li><strong>Parça sürtünerek mi çalışıyor?</strong> Evetse bronz.</li>
<li><strong>Yoğun talaşlı işleme var mı ve maliyet öncelikli mi?</strong> Evetse pirinç.</li>
<li><strong>Deniz suyu, yüksek yük veya darbe var mı?</strong> Alüminyum bronzu değerlendirilmeli.</li></ol>
<p>Her iki alaşımı da Abana fabrikamızda indüksiyon ocaklarında ergitip XRF ile analiz ederek döküyoruz. Ayrıntılar: <a href="[[B]]hizmetler/pirinc-dokum/">pirinç döküm</a> · <a href="[[B]]hizmetler/bronz-dokum/">bronz döküm</a>.</p>""",
    faqs=[("Sarı döküm ve kızıl döküm ne demek?", "Sanayide pirinç döküme rengi nedeniyle 'sarı döküm', bronz döküme ise 'kızıl döküm' denir."),
          ("Bronz burç yerine pirinç burç kullanılabilir mi?", "Hafif yük ve düşük hızda mümkün olabilir; ancak sürtünmeli ve yüklü çalışmada bronz çok daha uzun ömürlüdür.")])

art("aluminyum-anot-nedir",
    "Alüminyum Anot Nedir? Saflık, Kullanım ve Tedarik — Özen Metalurji",
    "Alüminyum anot nedir, nerede kullanılır?",
    "Alüminyum anot nedir, hangi saflıkta olmalı, nasıl üretilir ve sevk edilir? %99,80 saf alüminyumdan anot döküm hakkında bilmeniz gerekenler.",
    "Anot seçiminde saflık, bileşim tutarlılığı ve düzenli tedarik neden önemli? Alüminyum anotların temel özelliklerini ve üretim adımlarını özetledik.",
    "Alüminyum anot nedir?",
    "Alüminyum anot; elektrokimyasal süreçlerde ve katodik koruma gibi sistemlerde akımın ya da korumanın kaynağı olarak görev yapan, belirli ölçü ve ağırlıkta dökülmüş alüminyum bloktur. Performansı büyük ölçüde hammaddenin saflığına ve bileşimin tutarlılığına bağlıdır.",
    """<h2>Anot ne işe yarar?</h2>
<p>Elektrokimyada anot, elektronların devreden ayrıldığı elektrottur. Katodik koruma uygulamalarında ise daha aktif bir metal olan anot, korunacak yapı yerine kendisi kontrollü biçimde tükenerek çelik yapıları korozyona karşı korur. Her iki durumda da anodun bileşimi, verimini ve ömrünü belirler.</p>
<h2>Saflık neden önemli?</h2>
<p>Demir, bakır gibi istenmeyen elementler anodun düzensiz tükenmesine ve veriminin düşmesine yol açabilir. Bu nedenle anot dökümünde hammaddenin saflığı ve ergiyiğin analizle kontrol edilmesi kritiktir. Özen Metalurji, anot dökümünde yurt dışı menşeli <strong>%99,80 saflıkta alüminyum</strong> kullanır ve bileşimi XRF ile kontrol eder.</p>
<h2>Üretim ve sevkiyat adımları</h2>
<ol class="olist"><li>Saflığı belgeli alüminyum hammaddenin kabulü ve depolanması</li>
<li>Ergitme ve XRF ile bileşim kontrolü</li>
<li>Anot kalıplarına döküm ve soğutma</li>
<li>Temizleme, istifleme ve ambalajlama</li>
<li>2,5 tonluk paletler halinde sevkiyat</li></ol>
<p>Ürün detayları için <a href="[[B]]hizmetler/anot-dokum/">alüminyum anot döküm</a> sayfamızı inceleyebilirsiniz.</p>""",
    faqs=[("Anot alaşımlı mı olmalı, saf mı?", "Uygulamaya göre değişir. Bazı katodik koruma uygulamalarında belirli alaşım elementleri eklenir; bazı süreçlerde ise yüksek saflık istenir. İhtiyacınızı ve uymanız gereken şartnameyi paylaşmanız yeterlidir.")])

art("dokum-teklifi-icin-gerekenler",
    "Döküm Teklifi İçin Gerekenler: 7 Maddelik Liste — Özen Metalurji",
    "Döküm teklifi almak için neler gerekir?",
    "Döküm teklifi isterken gönderilecekler: teknik resim, alaşım, adet, tolerans, işleme, yüzey ve ambalaj bilgisi. Hızlı ve doğru teklif için kontrol listesi.",
    "Eksiksiz bir teklif talebi hem fiyatı hem termini netleştirir. Dökümhanelerin en çok sorduğu bilgileri 7 maddede topladık.",
    "Döküm teklifi için ne göndermeliyim?",
    "Teknik resim (PDF ve mümkünse DWG/DXF veya STEP), alaşım ya da kullanım yeri, adet (numune ve yıllık tahmin), kritik ölçü ve toleranslar, ham ya da işlenmiş teslim bilgisi, yüzey beklentisi ve varsa mevcut model veya kalıp bilgisi.",
    """<h2>Kontrol listesi</h2>
<ol class="olist">
<li><strong>Teknik resim:</strong> PDF ölçülü resim; mümkünse 3B model (STEP) veya DWG/DXF. Resmi yoksa numune parça da değerlendirilebilir.</li>
<li><strong>Alaşım:</strong> Standart adı (ör. AlSi12, CuSn10, CuZn39Pb1Al, Zamak 3). Bilinmiyorsa parçanın çalıştığı ortamı ve görevi yazın.</li>
<li><strong>Adet:</strong> Numune adedi ve yıllık tahmini ihtiyaç. Yöntem seçimi (kum veya kokil) büyük ölçüde buna bağlıdır.</li>
<li><strong>Kritik ölçüler ve toleranslar:</strong> Hangi yüzeyler işlenecek, hangi ölçüler kritik?</li>
<li><strong>Teslim durumu:</strong> Ham döküm mü, kumlanmış mı, işlenmiş mi?</li>
<li><strong>Test ve belge:</strong> Kimyasal analiz raporu veya ek test ihtiyacı.</li>
<li><strong>Ambalaj ve sevkiyat:</strong> Teslim adresi, ambalaj ve palet beklentisi.</li>
</ol>
<p>Bu bilgilerle teknik ekibimiz çekme ve işleme paylarını hesaplayarak model, kalıp ve döküm maliyetini netleştirir. <a href="[[B]]iletisim/#teklif">Teklif formumuzdan</a> veya <a href="mailto:info@ozenmetalurji.com.tr">info@ozenmetalurji.com.tr</a> adresinden bize ulaşabilirsiniz.</p>""",
    read="3 dk")

cards = "".join('<a class="post-card" href="[[B]]bilgi-merkezi/%s/"><p class="eyebrow">Rehber · %s</p><h2>%s</h2><p>%s</p><span class="more">Oku %s</span></a>'
                % (s, r, h, d, icon("arrow", "ic ic-sm")) for s, h, d, r in ARTICLES)
PAGES.insert(len(PAGES) - len(ARTICLES), dict(slug="bilgi-merkezi", nav="bilgi",
    title="Bilgi Merkezi | Döküm Rehberleri — Özen Metalurji",
    description="Döküm yöntemleri ve alaşımlar hakkında rehberler: kum ve kokil döküm farkı, pirinç ve bronz farkı, alüminyum anot ve döküm teklifi için gerekenler.",
    body=page_hero("Bilgi merkezi", "Döküm rehberleri",
                   "Doğru yöntemi ve alaşımı seçmenize yardımcı olacak, sahadaki tecrübemizle hazırladığımız kısa ve net rehberler.",
                   [("Bilgi Merkezi", "bilgi-merkezi/")]) + '<section class="section"><div class="wrap"><div class="post-grid">%s</div></div></section>' % cards,
    schema=[S.webpage("bilgi-merkezi/", "Bilgi Merkezi", "Döküm rehberleri.", "CollectionPage"),
            S.breadcrumb([("Bilgi Merkezi", "bilgi-merkezi/")]),
            S.itemlist("Döküm rehberleri", [(h, "bilgi-merkezi/%s/" % s) for s, h, _, _ in ARTICLES])]))

# ---------------------------------------------------------------- İLETİŞİM
svc_opts = "".join("<option>%s</option>" % n for _, n, _, _ in SERVICES)
contact_body = page_hero("İletişim", "İletişim ve teklif",
    "Teklif, numune ve proje görüşmeleri için İstanbul ofisimize; üretim ve sevkiyat için Abana fabrikamıza ulaşabilirsiniz.",
    [("İletişim", "iletisim/")]) + """
<section class="section"><div class="wrap contact">
  <div class="contact-cards">
    <a class="ccard" href="tel:%(otel)s">%(phone)s<span><small>İstanbul ofis</small>%(otd)s</span></a>
    <a class="ccard" href="tel:%(oalt)s">%(phone)s<span><small>İstanbul ofis (2. hat)</small>%(oaltd)s</span></a>
    <a class="ccard" href="tel:%(ftel)s">%(phone)s<span><small>Abana fabrika</small>%(ftd)s</span></a>
    <a class="ccard" href="mailto:%(email)s">%(mail)s<span><small>E-posta</small>%(email)s</span></a>
  </div>
  <form class="quote" id="teklif" method="post" action="[[FORM]]" enctype="multipart/form-data" data-mailto="%(email)s">
    <h2>Teklif formu</h2>
    <p class="muted">Bilgileriniz yalnızca talebinize dönüş yapmak için kullanılır. Yıldızlı alanlar zorunludur.</p>
    [[FORM_HIDDEN]]
    <div class="fgrid">
      <label>Ad soyad *<input name="ad" required autocomplete="name"></label>
      <label>Firma<input name="firma" autocomplete="organization"></label>
      <label>Telefon *<input name="telefon" type="tel" required autocomplete="tel"></label>
      <label>E-posta *<input name="eposta" type="email" required autocomplete="email"></label>
      <label>Döküm türü<select name="hizmet"><option value="">Seçiniz</option>%(opts)s<option>Emin değilim</option></select></label>
      <label>Adet<input name="adet" placeholder="Ör. 2 numune, yıllık 5.000"></label>
      <label class="full">Mesajınız *<textarea name="mesaj" rows="5" required placeholder="Alaşım, parça ağırlığı, ham/işlenmiş teslim gibi bilgileri yazabilirsiniz."></textarea></label>
      <label class="full">Teknik resim (PDF, DWG, DXF, STEP — en fazla 10 MB)<input name="dosya" type="file" accept=".pdf,.dwg,.dxf,.step,.stp,.jpg,.jpeg,.png,.zip"></label>
      <label class="hp" aria-hidden="true">Web sitesi<input name="website" tabindex="-1" autocomplete="off"></label>
      <label class="check full"><input type="checkbox" name="kvkk" required> <span><a href="[[B]]kvkk/" target="_blank">KVKK Aydınlatma Metni</a>'ni okudum; talebime dönüş yapılması için verilerimin işlenmesini kabul ediyorum. *</span></label>
    </div>
    <button class="btn btn-molten btn-lg" type="submit">Teklif talebini gönder %(arrow)s</button>
    <p class="form-status" role="status" aria-live="polite"></p>
  </form>
</div></section>
<section class="section section-tint" id="konumlar"><div class="wrap">
  <div class="sec-head"><p class="eyebrow">Konumlarımız</p><h2>Google Haritalar'da Özen Metalurji</h2></div>
  <div class="maps">%(map1)s%(map2)s</div>
</div></section>
""" % {"otel": OFFICE["phone_e164"], "otd": OFFICE["phone_display"], "oalt": OFFICE["phone_alt_e164"], "oaltd": OFFICE["phone_alt_display"],
       "ftel": FACTORY["phone_e164"], "ftd": FACTORY["phone_display"], "email": EMAIL, "phone": icon("phone", "ic ic-lg"),
       "mail": icon("mail", "ic ic-lg"), "opts": svc_opts, "arrow": icon("arrow", "ic ic-sm"),
       "map1": map_embed(OFFICE, eager=True), "map2": map_embed(FACTORY, eager=True)}
PAGES.append(dict(slug="iletisim", nav="iletisim",
    title="İletişim ve Teklif | İstanbul Ofis, Abana Fabrika — Özen Metalurji",
    description="Özen Metalurji iletişim: İstanbul ofis 0 212 567 71 26, Abana fabrika 0 366 564 14 97, info@ozenmetalurji.com.tr. Teklif formu ve Google Haritalar.",
    body=contact_body,
    schema=[S.webpage("iletisim/", "İletişim", "Özen Metalurji iletişim bilgileri ve teklif formu.", "ContactPage", about={"@id": S.ORG_ID}),
            S.breadcrumb([("İletişim", "iletisim/")])]))

# ---------------------------------------------------------------- KVKK
PAGES.append(dict(slug="kvkk", nav="",
    title="KVKK Aydınlatma Metni — Özen Metalurji",
    description="Özen Metalurji Makine ve Kalıp San. Tic. Ltd. Şti. kişisel verilerin korunması aydınlatma metni.",
    body=page_hero("Yasal", "KVKK Aydınlatma Metni", "6698 sayılı Kişisel Verilerin Korunması Kanunu kapsamında web sitemiz üzerinden iletilen kişisel verilere ilişkin bilgilendirme.", [("KVKK", "kvkk/")]) + """
<section class="section"><div class="wrap narrow prose">
<h2>Veri sorumlusu</h2><p>Özen Metalurji Makine ve Kalıp San. Tic. Ltd. Şti. (“Şirket”), Topçular Mah. Rami Kışla Cad. Uzak Çiftlik Sok. No:19/B Eyüpsultan / İstanbul.</p>
<h2>İşlenen veriler</h2><p>Teklif ve iletişim formları aracılığıyla paylaştığınız ad soyad, firma, telefon, e-posta, mesaj içeriği ve yüklediğiniz teknik dosyalar.</p>
<h2>İşleme amaçları</h2><p>Talebinize dönüş yapılması, teklif hazırlanması, sözleşme süreçlerinin yürütülmesi ve yasal yükümlülüklerin yerine getirilmesi.</p>
<h2>Hukuki sebep</h2><p>Kanun'un 5/2-c (sözleşmenin kurulması veya ifasıyla doğrudan ilgili olması) ve 5/2-f (meşru menfaat) maddeleri ile açık rızanızın bulunduğu hâller.</p>
<h2>Aktarım</h2><p>Kişisel verileriniz, yasal zorunluluklar dışında üçüncü kişilerle paylaşılmaz; e-posta ve barındırma hizmeti sağlayıcılarıyla yalnızca hizmetin gerektirdiği ölçüde paylaşılabilir.</p>
<h2>Haklarınız</h2><p>Kanun'un 11. maddesi kapsamındaki haklarınıza ilişkin taleplerinizi <a href="mailto:info@ozenmetalurji.com.tr">info@ozenmetalurji.com.tr</a> adresine iletebilirsiniz.</p>
<p class="muted">Bu metin genel bilgilendirme amaçlıdır; yayına almadan önce şirketin hukuk danışmanınca gözden geçirilmesi önerilir.</p>
</div></section>""",
    schema=[S.webpage("kvkk/", "KVKK Aydınlatma Metni", "Kişisel verilerin korunması aydınlatma metni."), S.breadcrumb([("KVKK", "kvkk/")])]))

# ---------------------------------------------------------------- 404
PAGES.append(dict(slug="404", nav="", title="Sayfa bulunamadı — Özen Metalurji", description="Aradığınız sayfa bulunamadı.",
    body="""<section class="phero phero-404"><div class="phero-glow" aria-hidden="true"></div><div class="wrap center">
<p class="eyebrow">404</p><h1>Bu sayfa kalıptan çıkmamış.</h1><p class="lead">Aradığınız sayfa taşınmış ya da hiç dökülmemiş olabilir.</p>
<div class="hero-actions center"><a class="btn btn-molten" href="[[B]]">Ana sayfa</a><a class="btn btn-ghost-light" href="[[B]]hizmetler/">Döküm hizmetleri</a><a class="btn btn-ghost-light" href="[[B]]iletisim/">İletişim</a></div></div></section>""",
    schema=[], noindex=True, file404=True))
