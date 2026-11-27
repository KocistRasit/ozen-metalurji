#!/usr/bin/env bash
# Eski siteden (ozenmetalurji.com.tr) firma görsellerini indirir. Var olan dosyalar atlanır.
set -u
mkdir -p assets-img
U=http://www.ozenmetalurji.com.tr/resimler/normal
while read -r name path; do
  [ -z "$name" ] && continue
  [ -s "assets-img/$name" ] && { echo "var: $name"; continue; }
  if curl -fsSL --retry 3 --max-time 60 -A "Mozilla/5.0" -o "assets-img/$name" "$U/$path"; then echo "indirildi: $name"; else echo "UYARI: indirilemedi $name"; rm -f "assets-img/$name"; fi
done <<'LIST'
ozen-metalurji-banner.jpg 2016-01/FirmaArkaBanner1_hP46vGcZjeU6ry1OsjBHimg-414613254693929.jpeg
anot-aluminyum-hammadde.jpg 2016-01/UrunKucukResimUrl1_Er8f7PUqfE0Elki3xPV31-aliminyum-kucuk.jpg
anot-malzeme-depolama.jpg 2016-01/UrunKucukResimUrl1_OfN4eM6H1F2nIxKvHCDK2-malzeme-depolama-alani-k.jpg
anot-palet-ambalaj.jpg 2016-01/UrunKucukResimUrl1_S2xBsypXBQztdttv3yVx3-ambalajlanmis-anotlar-2-5ton-palet-k.jpg
anot-dokum.jpg 2016-01/UrunKucukResimUrl1_bgofIciPmdxlmVsAMuEF4-anot-dokum-k.jpg
anot-sevkiyat.jpg 2016-01/UrunKucukResimUrl1_mx9rKa73BPILeTPILmAk5-sevk-edilen-anotlar-k.jpg
logo-eski-site.png 2015-11/SiteLogo_k3jKsbAcxZxDK1sRctY0ozen.png
LIST
ls -la assets-img
