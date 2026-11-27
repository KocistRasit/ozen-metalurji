# -*- coding: utf-8 -*-
"""Döküm hizmeti sayfaları."""
from data import SERVICES
from ui import icon, page_hero, answer_box, faq_list, data_table, facts_table, service_cards
import schema as S

PAGES = []
ALLOY_NOTE = ("Tablodaki alaşımlar sık talep edilen örneklerdir. İstediğiniz alaşımın dökülebilirliği ve parçanıza uygunluğu "
              "teklif aşamasında teyit edilir; kimyasal bileşim XRF ile doğrulanır.")

SVC = {
"aluminyum-kum-dokum": dict(
    title="Alüminyum Kum Döküm | Numuneden Seriye — Özen Metalurji",
    desc="Alüminyum kum döküm nedir, ne zaman tercih edilir? AlSi12, AlSi7Mg, AlSi10Mg alaşımlarında kum döküm; model ve maça bizde, XRF analizli. Abana/Kastamonu fabrika.",
    h1="Alüminyum kum döküm",
    lead="Karmaşık iç boşluklu gövdelerden tek parça numunelere kadar; modeli ve maçası kendi bünyemizde hazırlanan, XRF ile analiz edilen alüminyum kum döküm parçalar.",
    q="Alüminyum kum döküm nedir?",
    a="Alüminyum kum döküm, ergitilmiş alüminyum alaşımının modelden şekil alan kum kalıba dökülmesiyle yapılan üretim yöntemidir. Kalıp maliyeti düşük olduğundan numune, az adetli ve büyük ya da karmaşık parçalar için en ekonomik yoldur.",
    intro="""<p>Kum dökümde parçanın modeli kalıp kumuna basılarak boşluk oluşturulur, iç kanallar için maça yerleştirilir ve ergimiş alüminyum bu boşluğa dökülür. Kalıp her dökümde bozulduğu için yöntem son derece esnektir: model değişikliği hızlıdır, büyük parçalar ve karmaşık iç geometriler kolayca üretilebilir.</p>
<p>Özen Metalurji'de kalıp kumu kendi kum değirmenlerimizde hazırlanır, elenir ve açılır; maçalar tam otomatik maça makinesinde üretilir. Alüminyum, 200, 300 ve 350 kg kapasiteli rezistanslı ocaklarımızda ergitilir ve döküm öncesi XRF ile analiz edilir.</p>""",
    when=["Numune ve prototip parçalar, düşük–orta adetli siparişler", "Büyük boyutlu ya da ağır gövdeler",
          "İç kanal ve boşluk içeren, maça gerektiren karmaşık parçalar", "Kalıp yatırımını düşük tutmak istediğiniz projeler"],
    alloys=(["Alaşım (EN)", "Kısa ad", "Öne çıkan özelliği", "Tipik kullanım"], [
        ["EN AC-44100", "AlSi12", "Çok iyi akışkanlık, ince kesitler", "İnce cidarlı gövde ve kapaklar"],
        ["EN AC-42100", "AlSi7Mg0,3", "Isıl işlemle yüksek dayanım", "Yük taşıyan makine parçaları"],
        ["EN AC-43000", "AlSi10Mg", "Dayanım ve dökülebilirlik dengesi", "Pompa, motor ve makine gövdeleri"],
        ["EN AC-46000", "AlSi9Cu3(Fe)", "İyi işlenebilirlik, ekonomik", "Genel amaçlı parçalar"],
    ]),
    pros=[("Düşük kalıp maliyeti", "Ahşap/reçine model, metal kalıba göre çok daha ekonomiktir."),
          ("Boyut esnekliği", "Ergitme ve kalıplama kapasitesi dahilinde büyük parçalar üretilebilir."),
          ("Hızlı revizyon", "Model modelhanemizde düzeltilir; tasarım değişikliği kısa sürede uygulanır.")],
    faq=[("Alüminyum kum döküm mü, kokil döküm mü seçmeliyim?", "Adet düşükse, parça büyükse veya tasarım henüz kesinleşmediyse kum döküm; adet yüksekse ve daha düzgün yüzey ile dar ölçü toleransı isteniyorsa kokil döküm daha uygundur. Kararı teknik resminiz üzerinden birlikte veririz."),
         ("Kum dökümde yüzey kalitesi nasıldır?", "Kum dökümde yüzey kokile göre daha pürüzlüdür. Kumlama ile temizlenen yüzey, sızdırmazlık veya hassas ölçü gereken bölgelerde talaşlı işleme ile tamamlanır; bu nedenle model işleme payına göre hazırlanır."),
         ("Kum döküm için en az kaç adet sipariş verilebilir?", "Kum döküm tek parça numuneden seri üretime kadar uygundur. Adet ve parça ağırlığına göre teklif hazırlanır.")],
    materials=["Alüminyum alaşımı"], related=["aluminyum-kokil-dokum", "bronz-dokum"]),

"aluminyum-kokil-dokum": dict(
    title="Alüminyum Kokil Döküm | Seri Üretim, Düzgün Yüzey — Özen Metalurji",
    desc="Alüminyum kokil (metal kalıp, gravite) döküm: tekrarlanabilir ölçü, düzgün yüzey ve seri üretim. Kokil kalıp ve maça kendi bünyemizde. Özen Metalurji, Abana.",
    h1="Alüminyum kokil döküm",
    lead="Metal kalıpla, yer çekimiyle yapılan kokil döküm; seri üretimde tekrarlanabilir ölçü, düzgün yüzey ve sık yapılı, sağlam parçalar sağlar.",
    q="Alüminyum kokil döküm nedir?",
    a="Kokil döküm, ergimiş alüminyumun çelik veya dökme demirden yapılmış kalıcı bir metal kalıba (kokil) yer çekimiyle dökülmesidir. Aynı kalıpla binlerce parça dökülebildiği için seri üretimde ölçü tutarlılığı, yüzey kalitesi ve birim maliyet avantajı sağlar.",
    intro="""<p>Kokil dökümde metal kalıp ergiyiğin ısısını kuma göre çok daha hızlı çeker. Bu hızlı katılaşma, daha ince taneli ve dolayısıyla mekanik özellikleri daha iyi bir yapı oluşturur. Kalıp kalıcı olduğundan parça ölçüleri dökümden döküme değişmez.</p>
<p>Abana fabrikamızda iki adet kokil döküm makinesi bulunur. İç boşluklar için kum maçalar tam otomatik maça makinemizde hazırlanır; böylece kokil dökümde de karmaşık iç geometriler elde edilebilir.</p>""",
    when=["Orta ve yüksek adetli, tekrarlı siparişler", "Düzgün yüzey ve dar ölçü toleransı istenen parçalar",
          "Talaşlı işleme payını azaltmak istediğiniz projeler", "Basınçlı dökümün kalıp yatırımının yüksek kaldığı adetler"],
    alloys=(["Alaşım (EN)", "Kısa ad", "Öne çıkan özelliği", "Tipik kullanım"], [
        ["EN AC-44100", "AlSi12", "Mükemmel kalıp doldurma", "İnce cidarlı, detaylı parçalar"],
        ["EN AC-42100", "AlSi7Mg0,3", "Isıl işlem sonrası yüksek dayanım", "Otomotiv ve makine parçaları"],
        ["EN AC-43000", "AlSi10Mg", "Sızdırmazlık ve dayanım", "Gövde, kapak, flanş"],
        ["EN AC-46000", "AlSi9Cu3(Fe)", "İyi işlenebilirlik", "Genel makine parçaları"],
    ]),
    pros=[("Tekrarlanabilir ölçü", "Kalıcı metal kalıp sayesinde parçalar arası ölçü farkı azdır."),
          ("Daha iyi mekanik özellik", "Hızlı katılaşma, ince taneli ve sağlam bir iç yapı oluşturur."),
          ("Düşük birim maliyet", "Kalıp yatırımı adetlere yayıldıkça parça başı maliyet düşer.")],
    faq=[("Kokil döküm ile basınçlı döküm arasındaki fark nedir?", "Kokil dökümde metal kalıba yer çekimiyle dolar; basınçlı dökümde ise yüksek basınçla enjekte edilir. Kokil döküm daha düşük kalıp maliyetiyle orta adetlerde ekonomiktir ve ısıl işleme uygun, sağlam parçalar verir."),
         ("Kokil kalıp kime ait olur?", "Sipariş için üretilen kalıbın mülkiyeti ve bakım koşulları teklif aşamasında yazılı olarak belirlenir."),
         ("Kokil dökümde iç boşluk yapılabilir mi?", "Evet. İç boşluklar kum maça ile oluşturulur; maçalar tam otomatik maça makinemizde üretilir.")],
    materials=["Alüminyum alaşımı"], related=["aluminyum-kum-dokum", "zamak-dokum"]),

"pirinc-dokum": dict(
    title="Pirinç Döküm (Sarı Döküm) | Vana, Rakor, Parça — Özen Metalurji",
    desc="Pirinç (sarı) döküm: işlenebilirliği yüksek, korozyona dayanıklı vana, rakor ve makine parçaları. CuZn39Pb1Al, CuZn33Pb2 alaşımları, XRF analizli. Özen Metalurji.",
    h1="Pirinç döküm (sarı döküm)",
    lead="Bakır-çinko alaşımlarıyla, işlenebilirliği yüksek ve korozyona dayanıklı sarı döküm parçalar; ergitmeden analiz ve temizlemeye kadar tek tesiste.",
    q="Pirinç döküm (sarı döküm) nedir?",
    a="Pirinç döküm, ağırlıklı olarak bakır ve çinkodan oluşan pirinç alaşımının ergitilip kum veya kokil kalıba dökülmesidir. Rengi nedeniyle sanayide 'sarı döküm' olarak bilinir; kolay işlenir, korozyona dayanıklıdır ve vana, rakor, armatür ile makine parçalarında yaygın kullanılır.",
    intro="""<p>Pirinç alaşımları iyi akışkanlıkları sayesinde ayrıntılı parçaların dökümüne uygundur. Kurşun içeren türleri talaşlı işlemede kısa talaş verir ve işleme süresini kısaltır; manganlı ve alüminyumlu yüksek mukavemetli pirinçler ise daha zorlu mekanik koşullara dayanır.</p>
<p>Özen Metalurji'de pirinç, 300 kg ve 500 kg kapasiteli indüksiyon ocaklarımızda ergitilir. Çinkonun buharlaşma eğilimi nedeniyle bileşim döküm öncesi XRF ile kontrol edilir ve gerekiyorsa düzeltilir.</p>""",
    when=["Vana, rakor, armatür ve bağlantı parçaları", "Talaşlı işleme sonrası temiz yüzey istenen parçalar",
          "Su ve hava ortamında korozyona dayanım gereken uygulamalar", "Dekoratif ya da elektriksel iletkenlik gerektiren parçalar"],
    alloys=(["Alaşım (EN 1982)", "Malzeme no.", "Öne çıkan özelliği", "Tipik kullanım"], [
        ["CuZn39Pb1Al-C", "CC754S", "Çok iyi işlenebilirlik", "Vana gövdesi, armatür"],
        ["CuZn33Pb2-C", "CC750S", "İyi dökülebilirlik", "Genel amaçlı parçalar"],
        ["CuZn35Mn2Al1Fe1-C", "CC765S", "Yüksek mukavemetli (manganlı) pirinç", "Yük altında çalışan parçalar"],
    ]),
    pros=[("Kolay işlenebilirlik", "Kurşunlu pirinçler hızlı ve temiz talaşlı işlemeye izin verir."),
          ("Korozyon direnci", "Su ve atmosfer koşullarında uzun ömür sağlar."),
          ("Ayrıntılı geometri", "İyi akışkanlık, ince detayların kalıbı doldurmasını kolaylaştırır.")],
    faq=[("Pirinç ile bronz arasındaki fark nedir?", "Pirincin ana alaşım elementi çinko, bronzunki ise kalaydır (alüminyum bronzunda alüminyum). Pirinç daha kolay işlenir ve genellikle daha ekonomiktir; bronz ise aşınma ve sürtünme dayanımında üstündür. Ayrıntı için <a href=\"[[B]]bilgi-merkezi/pirinc-ve-bronz-dokum-farki/\">pirinç ve bronz döküm farkı</a> yazımıza bakın."),
         ("İçme suyu tesisatı için pirinç dökebilir misiniz?", "İçme suyuyla temas eden parçalarda kurşun sınırları ve ilgili mevzuat önemlidir. Kullanım yerini ve uymanız gereken standardı teklif talebinizde belirtirseniz uygun alaşımı birlikte belirleriz."),
         ("Pirinç döküm parçalar işlenmiş teslim edilebilir mi?", "İşlenmiş teslim talebinizi teklif aşamasında belirtin; parça geometrisine göre değerlendirme yapılır.")],
    materials=["Pirinç (bakır-çinko alaşımı)"], related=["bronz-dokum", "zamak-dokum"]),

"bronz-dokum": dict(
    title="Bronz Döküm (Kızıl Döküm) | Burç, Yatak, Dişli — Özen Metalurji",
    desc="Bronz (kızıl) döküm: aşınmaya ve sürtünmeye dayanıklı burç, yatak, dişli ve makine parçaları. CuSn10, CuSn12, CuSn5Zn5Pb5, alüminyum bronzu. Özen Metalurji.",
    h1="Bronz döküm (kızıl döküm)",
    lead="Sürtünme, aşınma ve korozyon altında çalışan parçalar için kalay ve alüminyum bronzlarından kızıl döküm; XRF ile doğrulanmış alaşım.",
    q="Bronz döküm (kızıl döküm) nedir?",
    a="Bronz döküm, bakırın başta kalay olmak üzere alüminyum, nikel veya kurşunla oluşturduğu alaşımların kalıba dökülmesidir. Kızılımsı rengi nedeniyle 'kızıl döküm' de denir. Aşınma ve sürtünmeye dayanımı yüksek olduğu için burç, yatak, dişli, kızak ve pompa parçalarında tercih edilir.",
    intro="""<p>Kalay bronzları düşük sürtünme katsayısı ve yüksek aşınma dayanımıyla kaymalı yatak ve burçların klasik malzemesidir. Kurşunlu bronzlar yağlamanın zayıf olduğu koşullarda bile iyi çalışır; alüminyum bronzları ise yüksek mukavemet ve deniz suyu dahil zorlu ortamlarda korozyon direnci sunar.</p>
<p>Bronz alaşımları indüksiyon ocaklarımızda ergitilir, bileşimleri XRF ile ölçülür. Kum dökümde model ve maçalar kendi bünyemizde hazırlanır; böylece burçtan karmaşık gövdeye kadar farklı geometriler üretilebilir.</p>""",
    when=["Kaymalı yatak, burç ve kızaklar", "Dişli, sonsuz vida çarkı ve aşınma plakaları",
          "Pompa ve vana parçaları, deniz ortamı uygulamaları", "Cam sanayi ve kalıp uygulamalarında ısıl dayanım gereken parçalar"],
    alloys=(["Alaşım (EN 1982)", "Malzeme no.", "Öne çıkan özelliği", "Tipik kullanım"], [
        ["CuSn10-C", "CC480K", "Yüksek aşınma dayanımı", "Burç, yatak, dişli"],
        ["CuSn12-C", "CC483K", "Ağır yük ve düşük hız", "Sonsuz vida çarkı, ağır yük yatakları"],
        ["CuSn5Zn5Pb5-C", "CC491K", "İyi dökülebilirlik, sızdırmazlık", "Vana ve pompa gövdeleri"],
        ["CuSn7Zn4Pb7-C", "CC493K", "Kayma özellikleri iyi", "Genel amaçlı yatak ve burçlar"],
        ["CuAl10Fe5Ni5-C", "CC333G", "Yüksek mukavemet, deniz suyu direnci", "Pervane, pompa, ağır hizmet parçaları"],
    ]),
    pros=[("Aşınma dayanımı", "Sürtünmeli çalışan parçalarda uzun servis ömrü."),
          ("Korozyon direnci", "Özellikle alüminyum bronzları zorlu ortamlarda dayanıklıdır."),
          ("Geniş alaşım seçeneği", "Uygulamaya göre kalay, kurşunlu veya alüminyum bronzu seçilebilir.")],
    faq=[("Bronz burç için hangi alaşım seçilmeli?", "Genel amaçlı burçlarda CuSn10 veya kurşunlu CuSn7Zn4Pb7 yaygındır; ağır yük ve darbe varsa CuSn12 ya da alüminyum bronzu düşünülür. Çalışma yükü, hız ve yağlama koşullarını paylaşırsanız öneride bulunuruz."),
         ("Bronz döküm parçalar talaşlı işlenebilir mi?", "Evet. Döküm modeli işleme payıyla hazırlanır; işlenmiş teslim talebinizi teklif aşamasında belirtin."),
         ("Bronz alaşımın doğru olduğunu nasıl anlarım?", "Kimyasal bileşim XRF cihazımızla ölçülür ve talep edilirse partiyle birlikte raporlanır.")],
    materials=["Bronz (bakır-kalay / bakır-alüminyum alaşımı)"], related=["pirinc-dokum", "aluminyum-kum-dokum"]),

"zamak-dokum": dict(
    title="Zamak Döküm | Çinko Alaşımı Detaylı Parçalar — Özen Metalurji",
    desc="Zamak (çinko-alüminyum alaşımı) döküm: ince detaylı, kaplamaya uygun, düzgün yüzeyli parçalar. Zamak 3, Zamak 5, Zamak 2. Özen Metalurji, Abana/Kastamonu.",
    h1="Zamak döküm",
    lead="Düşük ergime sıcaklığı ve mükemmel akışkanlığıyla zamak; ince detaylı, düzgün yüzeyli ve kaplamaya hazır parçalar için ideal alaşım.",
    q="Zamak döküm nedir?",
    a="Zamak, çinko esaslı; alüminyum, magnezyum ve bakır içeren bir döküm alaşımıdır. Yaklaşık 380–390 °C gibi düşük sıcaklıkta ergir, kalıbı çok iyi doldurur ve kaplama (krom, nikel, boya) için uygun düzgün bir yüzey verir. Aksesuar, kulp, kilit, menteşe ve küçük mekanik parçalarda yaygındır.",
    intro="""<p>Zamak alaşımlarının adı, içerdiği metallerin Almanca baş harflerinden gelir: <em>Zink, Aluminium, Magnesium, Kupfer</em>. Düşük ergime sıcaklığı enerji tüketimini ve kalıp yıpranmasını azaltır; yüksek akışkanlık ise ince cidar ve keskin detayların dökülmesini sağlar.</p>
<p>Zamak dökümde alaşım saflığı kritiktir: kurşun, kadmiyum ve kalay gibi safsızlıklar zamanla parçada bozulmaya yol açabilir. Bu nedenle hammadde ve ergiyik bileşimini XRF ile kontrol ediyoruz. Döküm yöntemi parçanızın geometrisine ve adedine göre belirlenir.</p>""",
    when=["Kaplanacak (krom, nikel, boya) parçalar", "İnce detay ve keskin hatlar içeren küçük ve orta boy parçalar",
          "Mobilya, kapı ve aksesuar donanımları", "Ağırlığın ve maliyetin dengelenmesi gereken parçalar"],
    alloys=(["Alaşım", "Standart adı", "Öne çıkan özelliği", "Tipik kullanım"], [
        ["Zamak 3", "ZP3 / ZnAl4", "En yaygın tür, iyi boyutsal kararlılık", "Genel amaçlı parçalar"],
        ["Zamak 5", "ZP5 / ZnAl4Cu1", "Bakır sayesinde daha yüksek dayanım", "Kulp, kilit, mekanik parçalar"],
        ["Zamak 2", "ZP2 / ZnAl4Cu3", "En yüksek sertlik ve dayanım", "Aşınmaya maruz parçalar"],
    ]),
    pros=[("Mükemmel yüzey", "Kaplama ve boya öncesi minimum hazırlık."),
          ("İnce detay", "Yüksek akışkanlık; ince cidar ve keskin hatlar."),
          ("Düşük ergime sıcaklığı", "Enerji tasarrufu ve uzun kalıp ömrü.")],
    faq=[("Zamak ile alüminyum döküm arasındaki fark nedir?", "Zamak daha ağırdır ama daha düşük sıcaklıkta ergir, daha ince detay ve daha düzgün yüzey verir; kaplamaya çok uygundur. Alüminyum ise hafiftir ve yüksek sıcaklıkta dayanımını daha iyi korur. Hafiflik öncelikliyse alüminyum, detay ve kaplama öncelikliyse zamak tercih edilir."),
         ("Zamak parçalar paslanır mı?", "Zamak demir içermediği için kırmızı pas yapmaz; ancak nemli ortamda yüzeyde beyaz oksitlenme görülebilir. Kaplama veya boya bu riski ortadan kaldırır."),
         ("Zamak 3 mü Zamak 5 mi seçmeliyim?", "Genel amaçlı ve kaplanacak parçalarda Zamak 3, daha yüksek dayanım ve sertlik gereken mekanik parçalarda Zamak 5 tercih edilir.")],
    materials=["Zamak (çinko-alüminyum alaşımı)"], related=["aluminyum-kokil-dokum", "pirinc-dokum"]),

"anot-dokum": dict(
    title="Alüminyum Anot Döküm | %99,80 Saf Alüminyum — Özen Metalurji",
    desc="Yurt dışı menşeli %99,80 saflıkta alüminyumdan anot döküm. Ambalajlı, 2,5 tonluk paletlerde sevkiyat. Abana/Kastamonu fabrikasında üretim — Özen Metalurji.",
    h1="Alüminyum anot döküm",
    lead="Yurt dışı menşeli %99,80 saflıkta alüminyumdan anot dökümü; analizli üretim, düzenli istif ve 2,5 tonluk paletlerde ambalajlı sevkiyat.",
    q="Alüminyum anot döküm nedir?",
    a="Alüminyum anot döküm, yüksek saflıktaki alüminyumun belirli ölçü ve ağırlıkta anot bloklarına dökülmesidir. Özen Metalurji, yurt dışı menşeli %99,80 saflıkta alüminyum kullanarak anot döker ve ürünleri 2,5 tonluk paletlerde ambalajlayarak sevk eder.",
    intro="""<p>Anotlar; elektrokimyasal süreçlerde ve katodik koruma gibi sistemlerde akımın ya da korumanın kaynağı olarak görev yapan metal bloklardır. Bu uygulamalarda anodun saflığı ve bileşiminin tutarlılığı, sistemin performansını doğrudan etkiler.</p>
<p>Abana fabrikamızda anot dökümünde yurt dışı menşeli <strong>%99,80 saflıkta alüminyum</strong> hammadde kullanıyoruz. Ergiyik bileşimi XRF ile kontrol edilir; dökülen anotlar malzeme depolama alanında düzenli istiflenir ve <strong>2,5 tonluk paletler</strong> halinde ambalajlanarak sevk edilir.</p>""",
    when=["Saflığı belgelenmiş alüminyum anot ihtiyacı", "Tekrarlı ve düzenli sevkiyat gerektiren tedarik",
          "Belirli ölçü ve ağırlıkta anot bloğu üretimi", "Paletli, istiflenmiş ve ambalajlı teslimat beklentisi"],
    alloys=None,
    facts=[("Hammadde", "Yurt dışı menşeli %99,80 saf alüminyum"), ("Kontrol", "XRF ile kimyasal bileşim analizi"),
           ("Ambalaj", "2,5 ton paletler"), ("Üretim yeri", "Abana / Kastamonu fabrikası"), ("Sevkiyat", "Yurt içi ve yurt dışı")],
    gallery=[("anot-aluminyum-hammadde.jpg", "%99,80 saflıkta alüminyum hammadde"), ("anot-dokum.jpg", "Anot döküm"),
             ("anot-malzeme-depolama.jpg", "Malzeme depolama alanı"), ("anot-palet-ambalaj.jpg", "Ambalajlı anotlar (2,5 ton palet)"),
             ("anot-sevkiyat.jpg", "Sevk edilen anotlar")],
    pros=[("Yüksek saflık", "%99,80 saflıkta ithal alüminyum hammadde."),
          ("Analizli üretim", "Bileşim XRF ile kontrol edilir."),
          ("Düzenli lojistik", "2,5 tonluk ambalajlı paletlerle güvenli sevkiyat.")],
    faq=[("Anot dökümde hangi saflıkta alüminyum kullanıyorsunuz?", "Yurt dışı menşeli %99,80 saflıkta alüminyum kullanıyoruz."),
         ("Anotlar nasıl paketlenip sevk ediliyor?", "Anotlar ambalajlanarak 2,5 tonluk paletler halinde istiflenir ve sevk edilir."),
         ("Özel ölçü ve ağırlıkta anot dökülebilir mi?", "Anot ölçüsü, ağırlığı ve bağlantı detaylarını teknik resimle paylaşırsanız uygunluk ve teklif çalışması yapılır.")],
    materials=["Alüminyum (%99,80)"], related=["aluminyum-kum-dokum", "aluminyum-kokil-dokum"]),
}

NAMES = {s: n for s, n, _, _ in SERVICES}
ICONS = {s: ic for s, _, _, ic in SERVICES}

for slug, d in SVC.items():
    path = "hizmetler/%s/" % slug
    name = NAMES[slug]
    when = "".join("<li>%s %s</li>" % (icon("check", "ic ic-sm"), w) for w in d["when"])
    pros = "".join('<div class="pro"><h3>%s</h3><p>%s</p></div>' % p for p in d["pros"])
    if d.get("alloys"):
        h, rows = d["alloys"]
        alloys = '<h2>Sık talep edilen alaşımlar</h2>' + data_table(h, rows, note=ALLOY_NOTE)
    else:
        alloys = '<h2>Ürün özeti</h2>' + facts_table(d["facts"])
    gallery = ""
    if d.get("gallery"):
        gallery = '<div class="gallery gallery-sm">%s</div>' % "".join(
            '<figure><img src="[[A]]img/%s" alt="%s" width="600" height="450" loading="lazy" decoding="async"><figcaption>%s</figcaption></figure>' % (f, c, c)
            for f, c in d["gallery"])
    related = "".join('<li><a href="[[B]]hizmetler/%s/">%s %s</a></li>' % (r, icon(ICONS[r], "ic ic-sm"), NAMES[r]) for r in d["related"])
    body = page_hero("Döküm hizmetleri", d["h1"], d["lead"], [("Döküm Hizmetleri", "hizmetler/"), (name, path)],
                     extra='<div class="hero-actions"><a class="btn btn-molten" href="[[B]]iletisim/#teklif">%s için teklif iste %s</a></div>'
                           % (name, icon("arrow", "ic ic-sm"))) + """
<section class="section"><div class="wrap split split-top">
  <div class="prose">
    %(answer)s
    <h2>%(name)s nasıl yapılır?</h2>
    %(intro)s
    <h2>Ne zaman tercih edilir?</h2>
    <ul class="ticks">%(when)s</ul>
    %(alloys)s
    %(gallery)s
    <h2>Avantajları</h2>
    <div class="pros">%(pros)s</div>
    <h2>%(name)s hakkında sık sorulan sorular</h2>
    %(faq)s
  </div>
  <aside class="side side-sticky">
    <div class="side-card side-card-dark">
      <p class="eyebrow eyebrow-light">Teklif için gerekenler</p>
      <ul class="ticks ticks-light">
        <li>%(c)s Teknik resim (PDF, DWG/DXF, STEP)</li>
        <li>%(c)s Alaşım veya kullanım yeri</li>
        <li>%(c)s Adet (numune + yıllık tahmin)</li>
        <li>%(c)s Ham / işlenmiş teslim bilgisi</li>
      </ul>
      <a class="btn btn-molten btn-block" href="[[B]]iletisim/#teklif">Teklif İste %(arrow)s</a>
      <a class="btn btn-ghost-light btn-block" href="tel:+902125677126">%(phone)s 0 212 567 71 26</a>
    </div>
    <div class="side-card"><h3>İlgili hizmetler</h3><ul class="rel">%(related)s</ul>
      <a class="link-arrow" href="[[B]]hizmetler/">Tüm döküm hizmetleri %(arrow)s</a></div>
  </aside>
</div></section>
""" % {"answer": answer_box(d["q"], d["a"]), "name": name, "intro": d["intro"], "when": when, "alloys": alloys,
       "gallery": gallery, "pros": pros, "faq": faq_list(d["faq"]), "c": icon("check", "ic ic-sm"),
       "arrow": icon("arrow", "ic ic-sm"), "phone": icon("phone", "ic ic-sm"), "related": related}
    faqs_all = [(d["q"], d["a"])] + d["faq"]
    PAGES.append(dict(slug="hizmetler/" + slug, nav="hizmetler", title=d["title"], description=d["desc"], body=body,
                      schema=[S.webpage(path, name, d["desc"]),
                              S.breadcrumb([("Döküm Hizmetleri", "hizmetler/"), (name, path)]),
                              S.service(path, name, d["a"], name, d["materials"]),
                              S.faqpage(path, faqs_all)]))

# ---------------------------------------------------------------- HİZMETLER HUB
COMPARE = data_table(["Yöntem / alaşım", "En uygun adet", "Öne çıkan avantaj", "Tipik parçalar"], [
    ['<a href="[[B]]hizmetler/aluminyum-kum-dokum/">Alüminyum kum döküm</a>', "Numune – orta seri", "Düşük kalıp maliyeti, büyük ve karmaşık parça", "Gövde, kapak, kalıp parçası"],
    ['<a href="[[B]]hizmetler/aluminyum-kokil-dokum/">Alüminyum kokil döküm</a>', "Orta – yüksek seri", "Tekrarlanabilir ölçü, düzgün yüzey", "Otomotiv ve makine parçaları"],
    ['<a href="[[B]]hizmetler/pirinc-dokum/">Pirinç (sarı) döküm</a>', "Numune – seri", "Kolay işlenebilirlik, korozyon direnci", "Vana, rakor, armatür"],
    ['<a href="[[B]]hizmetler/bronz-dokum/">Bronz (kızıl) döküm</a>', "Numune – seri", "Aşınma ve sürtünme dayanımı", "Burç, yatak, dişli"],
    ['<a href="[[B]]hizmetler/zamak-dokum/">Zamak döküm</a>', "Orta – yüksek seri", "İnce detay, kaplamaya uygun yüzey", "Kulp, kilit, aksesuar"],
    ['<a href="[[B]]hizmetler/anot-dokum/">Alüminyum anot döküm</a>', "Tonaj bazlı", "%99,80 saf alüminyum, paletli sevkiyat", "Anot blokları"],
], caption="Hangi döküm yöntemi size uygun?")
hub_body = page_hero("Döküm hizmetleri", "Demir dışı metal döküm hizmetleri",
    "Alüminyum kum ve kokil döküm, pirinç, bronz, zamak ve anot döküm. Yöntemi ve alaşımı parçanızın görevine göre seçiyor, modelden analize kadar her adımı kendi bünyemizde yürütüyoruz.",
    [("Döküm Hizmetleri", "hizmetler/")]) + """
<section class="section"><div class="wrap">%(answer)s%(cards)s</div></section>
<section class="section section-tint"><div class="wrap">%(compare)s</div></section>
""" % {"answer": answer_box("Özen Metalurji hangi döküm hizmetlerini veriyor?",
                            "Alüminyum kum döküm, alüminyum kokil döküm, pirinç (sarı) döküm, bronz (kızıl) döküm, zamak döküm ve %99,80 saf alüminyumdan anot döküm. Model, kalıp, maça ve XRF analizi kendi bünyemizdedir."),
       "cards": service_cards(), "compare": COMPARE}
PAGES.insert(0, dict(slug="hizmetler", nav="hizmetler",
    title="Döküm Hizmetleri | Alüminyum, Pirinç, Bronz, Zamak — Özen Metalurji",
    description="Alüminyum kum ve kokil döküm, pirinç (sarı) döküm, bronz (kızıl) döküm, zamak ve anot döküm hizmetleri. Yöntem karşılaştırması ve teklif. Özen Metalurji.",
    body=hub_body,
    schema=[S.webpage("hizmetler/", "Döküm Hizmetleri", "Demir dışı metal döküm hizmetleri.", "CollectionPage"),
            S.breadcrumb([("Döküm Hizmetleri", "hizmetler/")]),
            S.itemlist("Döküm hizmetleri", [(n, "hizmetler/%s/" % s) for s, n, _, _ in SERVICES])]))
