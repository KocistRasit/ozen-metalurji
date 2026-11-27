/* Özen Metalurji — küçük, bağımlılıksız etkileşimler */
(function () {
  var d = document, b = d.body;

  // Mobil menü
  var burger = d.querySelector('.burger');
  if (burger) burger.addEventListener('click', function () {
    var open = b.classList.toggle('nav-open');
    burger.setAttribute('aria-expanded', open ? 'true' : 'false');
    burger.setAttribute('aria-label', open ? 'Menüyü kapat' : 'Menüyü aç');
  });

  // Alt menüler (dokunmatik + klavye)
  d.querySelectorAll('.nav-btn').forEach(function (btn) {
    btn.addEventListener('click', function (e) {
      var li = btn.parentElement, was = li.classList.contains('open');
      d.querySelectorAll('.has-sub.open').forEach(function (x) { x.classList.remove('open'); x.querySelector('.nav-btn').setAttribute('aria-expanded', 'false'); });
      if (!was) { li.classList.add('open'); btn.setAttribute('aria-expanded', 'true'); }
      e.stopPropagation();
    });
  });
  d.addEventListener('click', function (e) {
    if (!e.target.closest('.has-sub')) d.querySelectorAll('.has-sub.open').forEach(function (x) { x.classList.remove('open'); });
  });
  d.addEventListener('keydown', function (e) {
    if (e.key === 'Escape') { b.classList.remove('nav-open'); d.querySelectorAll('.has-sub.open').forEach(function (x) { x.classList.remove('open'); }); }
  });

  // Aktif menü öğesi
  var here = location.pathname.replace(/index\.html$/, '');
  d.querySelectorAll('.nav a, .f-links a').forEach(function (a) {
    var p = a.pathname.replace(/index\.html$/, '');
    if (p === here) a.setAttribute('aria-current', 'page');
  });

  // Yıl
  d.querySelectorAll('[data-year]').forEach(function (el) { el.textContent = new Date().getFullYear(); });

  // Görsel yüklenemezse zarif yer tutucu
  d.querySelectorAll('figure img').forEach(function (img) {
    function miss() { var f = img.closest('figure'); if (f) { f.classList.add('img-missing'); img.style.visibility = 'hidden'; } }
    if (img.complete && img.naturalWidth === 0) miss(); else img.addEventListener('error', miss);
  });

  // Görünür olunca belirme
  if ('IntersectionObserver' in window) {
    var els = d.querySelectorAll('.svc-card,.why,.steps li,.map-card,.vm,.sector,.post-card,.mgroup,.pstep,.plant');
    var io = new IntersectionObserver(function (en) {
      en.forEach(function (x) { if (x.isIntersecting) { x.target.classList.add('in'); io.unobserve(x.target); } });
    }, { rootMargin: '0px 0px -8% 0px' });
    els.forEach(function (el) { el.classList.add('reveal'); io.observe(el); });
  }

  // Teklif formu
  var form = d.getElementById('teklif');
  if (form) {
    var st = form.querySelector('.form-status');
    var q = new URLSearchParams(location.search);
    if (q.get('gonderildi') === '1') { st.textContent = 'Teşekkürler! Talebiniz bize ulaştı, en kısa sürede dönüş yapacağız.'; st.className = 'form-status ok'; }
    if (q.get('gonderildi') === '0') { st.textContent = 'Gönderim sırasında bir sorun oluştu. Lütfen 0 212 567 71 26 numarasından bize ulaşın.'; st.className = 'form-status err'; }
    if (b.dataset.static === '1') {
      // Önizleme (statik) sürümde sunucu yok: talebi e-posta taslağına dönüştür.
      form.addEventListener('submit', function (e) {
        e.preventDefault();
        if (!form.reportValidity()) return;
        var f = new FormData(form), lines = [];
        [['ad', 'Ad soyad'], ['firma', 'Firma'], ['telefon', 'Telefon'], ['eposta', 'E-posta'], ['hizmet', 'Döküm türü'], ['adet', 'Adet'], ['mesaj', 'Mesaj']]
          .forEach(function (k) { var v = f.get(k[0]); if (v) lines.push(k[1] + ': ' + v); });
        location.href = 'mailto:' + form.dataset.mailto + '?subject=' + encodeURIComponent('Teklif talebi - ' + (f.get('firma') || f.get('ad'))) + '&body=' + encodeURIComponent(lines.join('\n') + '\n\n(Teknik resmi bu e-postaya ek olarak ekleyiniz.)');
        st.textContent = 'E-posta uygulamanız açılıyor. Teknik resminizi e-postaya eklemeyi unutmayın.'; st.className = 'form-status ok';
      });
    }
  }
})();
