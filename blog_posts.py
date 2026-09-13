# Blog içerikleri (TR). Her yazı: slug, başlık, özet, tarih, okuma süresi, etiketler, HTML gövde.
POSTS = [
dict(slug='vbt-nedir', title='VBT Nedir? Hız Temelli Antrenmana Giriş', date='2026-09-14', minutes=6, tags=['VBT','Kuvvet antrenmanı'],
 summary='Hız temelli antrenman (VBT) yükü değil bar hızını yönetir. Neden önemli, hangi metrikler ölçülür, hız bölgeleri ne anlatır — sıfırdan anlatıyoruz.',
 body='''
<p>Klasik kuvvet antrenmanında tek değişken vardır: yük. "Bugün 100 kg ile 5×5 squat." Ama 100 kg, iyi uyuduğunuz bir günle üç gün üst üste çalıştığınız bir günde aynı yük <em>değildir</em>. Vücudunuz o gün ne verebiliyorsa o kadar hızlı kaldırır. <strong>Hız temelli antrenman (Velocity-Based Training, VBT)</strong> tam olarak bu gerçeği kullanır: bar hızı, o günkü gerçek kapasitenizin en dürüst göstergesidir.</p>
<h2>Bar hızı neyi söyler?</h2>
<p>Aynı yükte bar yavaşladıysa yorgunsunuz; hızlandıysa formdasınız. Bu ilişki o kadar tutarlıdır ki, belirli bir hareket için hız ile 1RM yüzdesi arasında neredeyse doğrusal bir bağ vardır (yük-hız profili). Örneğin bench press'te ortalama konsantrik hız yaklaşık 0,50 m/s ise bu çoğu sporcuda 1RM'in %80–85'ine denk gelir. Yani bar hızını ölçtüğünüzde, o gün o yükün size gerçekte "yüzde kaç" geldiğini görürsünüz.</p>
<h2>Ölçülen temel metrikler</h2>
<ul>
<li><strong>Ortalama konsantrik hız (MCV, m/s):</strong> kaldırış fazının ortalama hızı. En güvenilir, en çok kullanılan metrik.</li>
<li><strong>Tepe hız (PV):</strong> kaldırış içindeki en yüksek anlık hız. Patlayıcı hareketlerde (clean, jump squat) anlamlı.</li>
<li><strong>Hız kaybı (%):</strong> set içinde ilk tekrara göre hızın ne kadar düştüğü. Yorgunluğun canlı ölçüsü.</li>
<li><strong>Güç (W):</strong> yük × hız; güç antrenmanının hedef çıktısı.</li>
<li><strong>Tahmini 1RM:</strong> yük-hız profilinden hesaplanan günlük maksimum.</li>
</ul>
<h2>Hız bölgeleri</h2>
<p>Bar hızı, antrenmanın hangi kaliteyi geliştirdiğini de söyler. Yaygın kabul gören bölgeler (ortalama hız için):</p>
<table><thead><tr><th>Bölge</th><th>Hız (m/s)</th><th>Hedef</th></tr></thead><tbody>
<tr><td>Mutlak kuvvet</td><td>&lt; 0,50</td><td>Maksimal kuvvet, ağır yük</td></tr>
<tr><td>Hızlanan kuvvet</td><td>0,50 – 0,75</td><td>Kuvvet ve hipertrofi</td></tr>
<tr><td>Kuvvet-hız</td><td>0,75 – 1,00</td><td>Güç üretimi</td></tr>
<tr><td>Hız-kuvvet</td><td>1,00 – 1,30</td><td>Patlayıcılık</td></tr>
<tr><td>Hız</td><td>&gt; 1,30</td><td>Hız ve reaktivite</td></tr>
</tbody></table>
<p>Bir sprinter için hedef 1,00 m/s üstü olabilirken, bir powerlifter'ın ağır günü 0,40 m/s civarında geçer. VBT'nin gücü budur: aynı cihaz, farklı hedefler için farklı bölgeleri işaretler.</p>
<h2>Pratikte nasıl kullanılır?</h2>
<ol>
<li><strong>Günlük yük ayarı:</strong> Isınmada sabit bir yükle 2–3 tekrar yapın; hız baz değerinizin altındaysa o gün yükü düşürün, üstündeyse artırın.</li>
<li><strong>Set sonlandırma:</strong> Hız, ilk tekrara göre belirlediğiniz eşiğin (ör. %20) altına düşünce seti bitirin. Böylece gereksiz yorgunluk birikmez.</li>
<li><strong>Anında geri bildirim:</strong> Her tekrarda hızı görmek, sporcunun her tekrarı maksimum niyetle yapmasını sağlar — araştırmalar bunun tek başına güç kazanımını artırdığını gösteriyor.</li>
</ol>
<h2>Sensör mü, kamera mı?</h2>
<p>VBT için üç teknoloji var: doğrusal konum dönüştürücü (LPT, tel-makara), kamera ve atalet sensörü (IMU). LPT laboratuvar standardıdır ama pahalı ve hantaldır; kamera bar yolunu iyi çıkarır ama kurulum ister. IMU tabanlı sensörler — <a href="../hasrep.html">Has Rep</a> gibi — bara takılır, saniyeler içinde hazırdır ve <em>ortalama hızda</em> güvenilirdir; tepe hız ve milimetrik bar yolu konusunda dürüst sınırları vardır. Günlük antrenman için pratiklik-doğruluk dengesi en iyi olan yaklaşım budur.</p>
<p>Sonraki yazı: <a href="@blog/hiz-kaybi-esigi.html">hız kaybı eşiğini hedefinize göre nasıl seçersiniz</a>.</p>
'''),
dict(slug='hiz-kaybi-esigi', title='Hız Kaybı Eşiği Nasıl Seçilir? %10, %20 ve %30 Ne Zaman', date='2026-09-16', minutes=5, tags=['VBT','Programlama'],
 summary='Set içi hız kaybı, yorgunluğu canlı ölçer. Güç, kuvvet ve hipertrofi hedeflerine göre hangi eşiği seçmeli, neden "başarısızlığa kadar" çoğu zaman yanlış — pratik rehber.',
 body='''
<p>Bir sette kaç tekrar yapmalısınız? Klasik cevap "8–12" ya da "başarısızlığa kadar"dır. VBT bu soruya bambaşka bir cevap verir: <strong>hız, ilk tekrara göre belirli bir yüzde düşene kadar</strong>. Buna hız kaybı eşiği (velocity loss threshold) denir ve set hacmini o günkü gerçek yorgunluğa göre otomatik ayarlar.</p>
<h2>Neden tekrar sayısı değil, hız kaybı?</h2>
<p>Aynı 8 tekrar, dinlenmiş bir sporcuda %12 hız kaybıyla, yorgun bir sporcuda %35 hız kaybıyla biter. İkincisi çok daha fazla yorgunluk biriktirir, toparlanması uzar ve bir sonraki antrenmanı bozar. Hız kaybı eşiği koyduğunuzda set, vücudun verdiği sinyale göre biter — sayıya göre değil.</p>
<h2>Hangi eşik, hangi hedef?</h2>
<table><thead><tr><th>Eşik</th><th>Hedef</th><th>Tipik his</th></tr></thead><tbody>
<tr><td>%10</td><td>Güç, hız, patlayıcılık; sezon içi sporcular</td><td>Her tekrar taze, "daha yapabilirdim"</td></tr>
<tr><td>%20</td><td>Kuvvet; dengeli hipertrofi</td><td>Son 1–2 tekrar zorlanır, form bozulmaz</td></tr>
<tr><td>%30+</td><td>Hipertrofi odaklı, toparlanma zamanı bol</td><td>Başarısızlığa yakın, belirgin yorgunluk</td></tr>
</tbody></table>
<p>Araştırmalar %20 eşiğinin, %40'a kıyasla <em>yarı hacimle</em> benzer kuvvet kazanımı verdiğini ve sprint/sıçrama performansını daha iyi koruduğunu gösteriyor. Yani çoğu sporcu için varsayılan %20'dir; hipertrofi hedefinde %25–30'a çıkılır, sezon içi ya da yarışma haftasında %10'a inilir.</p>
<h2>Pratik kurallar</h2>
<ol>
<li><strong>İlk tekrarı patlayıcı yapın.</strong> Referans o tekrardır; yavaş başlarsanız eşik anlamsızlaşır.</li>
<li><strong>Tekrar sayısını değil, seti sabitleyin.</strong> "4 set, %20 eşik" deyin; tekrar sayısı gün gün değişsin.</li>
<li><strong>Yük ile eşiği karıştırmayın.</strong> Yükü yük-hız profiliyle (hedef başlangıç hızı), hacmi eşikle yönetin.</li>
<li><strong>Eşiğe gelince durun — bir tekrar daha değil.</strong> Eşiğin işe yaraması disiplin ister; cihazın titreşim uyarısı bunu kolaylaştırır.</li>
</ol>
<h2>Bir örnek</h2>
<p>Squat, 120 kg, hedef %20. İlk tekrar 0,62 m/s. Tekrarlar: 0,61 · 0,59 · 0,57 · 0,53 · 0,49 (%21 kayıp) → set 5. tekrarda biter. Ertesi hafta aynı yük, ilk tekrar 0,66 m/s ve 7. tekrarda eşik → hem daha güçlüsünüz hem de hacim kendiliğinden arttı. Yükü artırma zamanı geldiğinin işareti de budur: başlangıç hızı hedef bölgenin üstüne çıkınca yükü artırın.</p>
<p><a href="../hasrep.html">Has Rep</a>'te eşik %10 / %20 / %30 olarak seçilir; eşik aşıldığında cihaz titreşir, uygulama seti kapatır ve bir sonraki set için öneri verir.</p>
'''),
dict(slug='tahmini-1rm', title='Test Günü Olmadan 1RM: Yük-Hız Profili Nasıl Çalışır', date='2026-09-18', minutes=5, tags=['VBT','1RM'],
 summary='Maksimum test riskli ve yorucudur. Yük-hız profili, iki-üç alt-maksimal yükten günlük 1RM\'i tahmin eder. Yöntem, hata payı ve dikkat edilecekler.',
 body='''
<p>1RM (bir tekrar maksimum) programlamanın temelidir: yüzdeler ona göre hesaplanır. Ama gerçek 1RM testi yorucudur, sakatlık riski taşır ve sık yapılamaz. Üstelik 1RM her gün değişir — uyku, stres, önceki antrenman. <strong>Yük-hız profili (load-velocity profile)</strong> bu sorunu çözer: birkaç alt-maksimal yükteki bar hızından, o günkü maksimumu tahmin eder.</p>
<h2>Yöntem</h2>
<ol>
<li>Aynı harekette 2–4 farklı yükle (ör. 1RM'in %50, %65, %80'i) 1–3 patlayıcı tekrar yapın.</li>
<li>Her yükün ortalama konsantrik hızını kaydedin.</li>
<li>Yük–hız noktalarına doğru çizgi uydurun (doğrusal regresyon). Yük arttıkça hız düşer; ilişki neredeyse doğrusaldır.</li>
<li>Çizgiyi, o hareketin "minimum hız eşiğine" (1RM'de gözlenen hız; bench için ~0,15–0,20 m/s, squat için ~0,30 m/s) kadar uzatın. O noktadaki yük, tahmini 1RM'dir.</li>
</ol>
<h2>Ne kadar doğru?</h2>
<p>Literatürde bireysel profil kullanıldığında hata payı genellikle %3–5 civarındadır. Genel (herkes için aynı) denklemler daha az doğrudur; profilin <em>size ait</em> olması önemlidir. Bu yüzden iyi bir sistem profili her sette sessizce günceller.</p>
<h2>Dikkat edilecekler</h2>
<ul>
<li><strong>Niyet maksimum olmalı.</strong> Hafif yükü isteyerek yavaş kaldırırsanız profil bozulur.</li>
<li><strong>Aynı teknik, aynı hareket açıklığı.</strong> Yarım squat ile tam squat aynı profile girmez.</li>
<li><strong>Isınmış olun.</strong> Soğuk ilk set profilin sol ucunu düşürür.</li>
<li><strong>Tahmini test gibi kullanmayın.</strong> Amaç her gün "gerçek 1RM'i bilmek" değil, yüzdeleri o günün formuna göre ayarlamaktır.</li>
</ul>
<h2>Günlük hazırlık (readiness) ölçümü</h2>
<p>Aynı mantığın basitleştirilmiş hali: ısınmada her zaman aynı yükle (ör. 60 kg bench) 2 tekrar yapın, hızı baz değerinizle karşılaştırın. %5'ten fazla yavaşsanız o gün yükü düşürün; hızlıysanız artırın. İki dakikada, test yapmadan, günlük otomatik yük ayarı.</p>
<p><a href="../hasrep.html">Has Rep</a> yük-hız profilini her antrenmanda arka planda günceller; tahmini 1RM'i uygulamanın istatistik ekranında görürsünüz. Uygulama turu için <a href="../hasrep.html#uygulama">buraya</a> bakın.</p>
'''),
dict(slug='sahte-tekrar', title='"Ghost Rep" Sorunu: Sensör Neden Fazla Sayar, Nasıl Doğrulanır', date='2026-09-20', minutes=4, tags=['Teknoloji','Ürün'],
 summary='Barı raftan alma, yeniden yerleştirme, set arası sallanma — sensörler bunları tekrar sanabilir. Filtreleme, onay ve dürüst tasarım üzerine.',
 body='''
<p>Bara takılan her sensörün ortak düşmanı vardır: <strong>sahte tekrar</strong> (ghost rep). Barı raftan alırken, yeniden yerleştirirken, set arasında elinizle sallarken sensör bir hareket görür ve bunu tekrar sanabilir. Rakip ürünlerin kullanıcı yorumlarında en sık şikâyet budur — "8 yaptım, 11 saydı".</p>
<h2>Neden olur?</h2>
<p>Bir tekrar, sensör açısından "aşağı-yukarı bir ivme deseni"dir. Raftan alıp indirme de aşağı-yukarı bir desendir. Fark, hareket açıklığı, süre ve hızın tutarlılığındadır — ama bu farklar her sporcuda, her harekette biraz değişir. Eşikleri çok sıkı tutarsanız gerçek tekrarları kaçırırsınız; gevşek tutarsanız sahte tekrar sayarsınız.</p>
<h2>Üç katmanlı çözüm</h2>
<ol>
<li><strong>Filtreleme:</strong> Gerçek salon verisiyle ayarlanmış eşikler — minimum hareket açıklığı, minimum konsantrik süre, ardışık tekrarlar arasındaki tutarlılık. Çoğu sahte tekrar burada elenir.</li>
<li><strong>Güven skoru:</strong> Her tekrar için "ne kadar eminim" değeri. Emin olunanlar otomatik kabul edilir; şüpheliler işaretlenir.</li>
<li><strong>Kullanıcı onayı — ama antrenman sonunda:</strong> Şüpheli tekrarlar antrenman bitince kart olarak sorulur: "Bu 3 tekrar ısınma mıydı?", "Bu set yarım görünüyor, saymayayım mı?" Sağa kaydır doğru, sola kaydır düzelt. Antrenman sırasında telefona bakmak gerekmez; onay 30 saniye sürer.</li>
</ol>
<h2>Neden "her rep doğrulanmış" demek daha dürüst?</h2>
<p>"%100 doğru sayım" iddiası, sensör fiziğiyle çelişir. Dürüst yaklaşım, sistemin emin olamadığını söylemesi ve son sözü sporcuya bırakmasıdır. Sonuç: kayıtlı her tekrar ya sistemin yüksek güvenle saydığı ya da sizin onayladığınız bir tekrardır. Uzun vadede verinin güvenilirliğini sağlayan da budur — hız kaybı, 1RM tahmini, haftalık hacim hepsi doğru sayıma dayanır.</p>
<p><a href="../hasrep.html">Has Rep</a>'in kaydırmalı onay ekranı tam olarak bu mantıkla çalışır; uygulama turunda görebilirsiniz.</p>
'''),
dict(slug='telefonu-birak', title='Antrenmanda Telefonu Bırakmak: Offline Kayıt Neden Şart', date='2026-09-22', minutes=4, tags=['Ürün','Tasarım'],
 summary='Canlı Bluetooth bağlantısına bağımlı cihazlar salonda kopar. Pod üstünde kayıt, sonradan senkron ve "başlat, bırak, onayla" akışının gerekçesi.',
 body='''
<p>Çoğu antrenman sensörü canlı Bluetooth bağlantısıyla çalışır: telefon yakında değilse ya da bağlantı bir an koparsa veri gider. Salonda telefon dolapta, cepte, başka bir istasyonda kalır; metal raflar sinyali keser. Sonuç: eksik setler, kayıp antrenmanlar, "cihaz bağlanmadı" ekranıyla boşa geçen dakikalar.</p>
<h2>Tasarım kararı: pod gerçek kaynaktır</h2>
<p>Has Rep'te veri yolu ikiye ayrılır. <strong>Canlı akış</strong> telefon yakınsa önizleme gösterir; <strong>kayıt</strong> ise her durumda pod'un kendi hafızasına yazılır. Bağlantı kopsa da hareket varken pod kaydetmeye devam eder; antrenman bitince senkronizasyonla tam kayıt telefona aktarılır. Canlı görüntü bir önizlemedir, pod'daki kayıt gerçek kaynaktır.</p>
<h2>"Başlat, bırak, onayla"</h2>
<ol>
<li><strong>Antrenmanı başlat:</strong> tek düğme. Telefonu cebe, dolaba, arabaya.</li>
<li><strong>Antren:</strong> set, tekrar ve dinlenme otomatik ayrılır. Duraklama süresine göre set arası mı, egzersiz geçişi mi tahmin edilir.</li>
<li><strong>Bitir ve onayla:</strong> senkron sonrası şüpheli kısımlar kartla sorulur; 30 saniyede biter.</li>
</ol>
<h2>Bu neden önemli?</h2>
<ul>
<li><strong>Odak:</strong> Set arasında telefona bakmak antrenman kalitesini düşürür. Sensörün amacı sizi telefona bağlamak değil, telefondan kurtarmaktır.</li>
<li><strong>Güvenilirlik:</strong> Veri kaybı sıfır. Bağlantı sorunları antrenmanı değil, sadece canlı önizlemeyi etkiler.</li>
<li><strong>Pil:</strong> Pod sürekli yayın yapmak zorunda değildir; hareket yokken derin uykuya geçer, sallayınca uyanır.</li>
</ul>
<p>Sesli geri bildirim (hedef hıza ulaşınca/altına düşünce kulaklıktan kısa bir uyarı) bu felsefenin doğal devamıdır ve yol haritamızdadır. Kullanım detayları için <a href="../hasrepkk.html">kullanım kılavuzu</a>, ürün için <a href="../hasrep.html">Has Rep sayfası</a>.</p>
'''),
]
