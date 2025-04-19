19 April 2025  
Week 3 Day 5  

Tüm bu yazılanlar GitHub wiki için uygun formatta yazılacaktır.  

# Unsupervised Learning (Gözetimsiz Öğrenme)  

## Unsupervised Learning (Gözetimsiz Öğrenme)  
* Unsupervised learning, etiketlenmemiş verilerle çalışan bir makine öğrenimi yaklaşımıdır.  
* Bu yöntemler, veri setindeki yapıları ve ilişkileri keşfetmek için kullanılır.  
* Verinin içsel yapısını anlamak, veri noktalarını gruplandırmak, benzerlikleri ve farkları ortaya çıkarmak için kullanılır.  
* Örnek kullanım alanları:  
  * Müşteri segmentasyonu  
  * Anomali tespiti  
  * Veri sıkıştırma  
  * Boyut azaltma  
  * Veri keşfi  

## Clustering (Kümeleme)  
* Kümeleme, veri noktalarını benzerliklerine göre gruplandırma işlemidir.  
* Her bir grup içindeki veriler birbirine daha yakındır.  
* Yöntemler:  
  * K-Means: Veri noktalarını k sayıda küme ile böler. Her nokta en yakın küme merkezine atanır.  
  * DBSCAN: Yoğunluk tabanlı bir yöntemdir. Yoğun bölgelerdeki veri noktalarını kümelemeye çalışır ve düşük yoğunluktaki bölgeleri ayrık değer olarak işaretler.
  * Hierarchical Clustering: Veri noktalarını hiyerarşi içinde kümeler. Ağaç yapısı içinde dendrogram olarak gösterir.  

## Dimensionality Reduction (Boyut Azaltma)  
* Boyut azaltma, veri setindeki özellik sayısını azaltarak veriyi daha yönetilebilir ve anlamlı hale getirme işlemidir.  
* Yöntemler:  
  * PCA (Principal Component Analysis): Verinin varyansını en iyi açıklayan yeni özellik temelleri oluşturur ve veriyi bu yeni özelliklerle projekte eder.  
  * t-SNE (t-Distributed Stochastic Neighbor Embedding): Yüksek boyutlu veriyi iki veya üç boyuta indirgerken veri noktalarının komşuluk ilişkilerini korur.  

## Özellik Öğrenme  
* Autoencoder: Veriyi sıkıştırarak ve yeniden inşa ederek önemli özellikleri öğrenir. Genellikle boyut azaltma ve özellik mühendisliği için kullanılır.  
* Principal Component Analysis: Özellik mühendisliği ve veri özetleme için kullanılır.  

## Anomali Tespiti  
* İstatistiksel yöntemler: Verinin normal dağılımına göre aykırı değerleri tespit eder.  
* Yoğunluk tabanlı yöntemler: DBSCAN gibi algoritmalar, veri yoğunluğunu kullanarak aykırı değerleri belirler.  

# Clustering (Kümeleme)  

## K-Means Kümeleme  
* K-Means, veriyi k sayıda küme veya gruba ayırmayı amaçlayan bir algoritmadır.  
* Çalışma prensibi:  
  * **Küme sayısı belirleme**: İlk olarak kullanıcı belirli bir k sayıda küme sayısı seçer.  
  * **Başlangıç merkezleri**: Rastgele k merkez (centroid) seçilir.  
  * **Atama adımı**: Her veri noktası en yakın merkezle ilişkilendirilir.  
  * **Güncelleme adımı**: Her küme için merkez, kümeye ait noktaların ortalaması alınarak güncellenir.  
  * **Tekrarlama**: Atama ve güncelleme adımları, merkezlerin değişmediği veya çok az değiştiği noktaya kadar tekrar edilir.

### K-Means Kümeleme - Özellikler ve Kullanım
* **Özellikler**:
  * Basit ve hızlı: Genellikle büyük veri setleri için uygundur.
  * Küme sayısı belirlenmeli: K önceden belirlenmelidir.
  * Hassasiyet: Başlangıç merkezlerine duyarlıdır ve yerel minimumlara takılabilir.
* **Kullanım alanları**: 
  * Pazar segmentasyonu
  * Görüntü sıkıştırma
  * Belirli özelliklere göre veri gruplama

### K-Means Kümeleme - Küme Seçme - Dirsek Metodu
* **Dirsek yöntemi (Elbow Method)**:
  * Farklı küme sayıları için küme içi varyans hesaplanır ve küme sayısına karşı inertia grafiği çizilir.  
  * Grafiğin dirsek noktası, küme sayısı artışının getirisinin azaldığı ve küme sayısının daha fazla artmasının anlamlı bir iyileşme sağlamadığı noktayı gösterir.

### K-Means Kümeleme - Küme Seçme - Siluet Analizi
* **Siluet analizi**:
  * Her bir veri noktasının siluet değeri hesaplanır.
  * Siluet değeri, bir veri noktasının kendi kümesindeki diğer noktalara olan uzaklık ortalamasının, diğer kümelerdeki en yakın noktaya olan ortalama uzaklığa oranıdır. Siluet değeri -1 ile +1 arasında değişir.
  * **1**'e yakın değerler iyi kümelemeyi, **0**'a yakın değerler belirsiz kümelemeyi ve **-1**'e yakın değerler yanlış kümelemeyi gösterir.

## Hiyerarşik Kümeleme
* Hiyerarşik kümeleme, veri noktalarını bir hiyerarşi içinde kümelmenin bir yoludur.
* Çalışma prensibi:
  * **Başlangıç**: Her veri noktası kendi kümesi olarak başlar (birinci seviyede).
  * **Birleştirme (Agglomerative)**: En yakın iki küme birleştirilir ve süreç, tüm noktalar tek bir küme haline gelene kadar devam eder.
  * **Bölme (Divisive)**: Tek bir küme, en küçük alt kümelere bölünene kadar bölünür.

### Hiyerarşik Kümeleme - Özellikler ve Kullanım
* **Özellikler**:
  * **Dendrogram**: Kümeleme süreci görsel olarak dendrogram (ağaç yapısı) ile gösterilebilir.
  * **Küme Sayısı Belirlenmeli**: Küme sayısı, dendrogramı keserek belirlenir.
  * **Esneklik**: Küme sayısı önceden belirlenmez, dinamik olarak ayarlanabilir.
* **Kullanım Alanları**:
  * Genetik analiz
  * Biyoinformatik
  * Sosyal ağ analizi

### Hiyerarşik Kümeleme - Linkage Matrislerini Hesaplama
* `linkage` fonksiyonu, hiyerarşik kümeleme adımlarını temsil eden bir bağlantı matrisi oluşturur. Farklı `method` parametreleri (`ward`, `complete`, `average`, `single`) farklı kümeleme yaklaşımlarını temsil eder:
  * **Ward**: Küme içi varyansı en aza indirmeye çalışır. Birleştirilecek iki küme, birleştikten sonraki toplam küme içi varyansı en az artıran kümelerdir.
  * **Complete (Maksimum Bağlantı)**: İki kümedeki tüm nokta çiftleri arasındaki maksimum mesafeyi en aza indirmeye çalışır.
  * **Average (Ortalama Bağlantı)**: İki kümedeki tüm nokta çiftleri arasındaki ortalama mesafeyi en aza indirmeye çalışır.
  * **Single (Minimum Bağlantı)**: İki kümedeki herhangi bir iki nokta arasındaki minimum mesafeyi en aza indirmeye çalışır. Bu yöntem zincirleme etkisine yakındır.

## DBSCAN (Density-Based Spatial Clustering of Applications with Noise)
* DBSCAN, veriyi yoğunluk tabanlı olarak kümeleyen bir y��ntemdir ve **aykırı değerleri** tanımlamak için kullanılır.
* Çalışma prensibi:
  * **Çekirdek noktalar**: `eps` mesafesi içinde `min_samples` sayıda komşuya sahip noktalar çekirdek nokta olarak kabul edilir.
  * **Kümeleme**: Çekirdek noktanın komşuları aynı kümeye dahil edilir.
  * **Aykırı değerler**: Çekirdek noktaların `eps` mesafesi içinde olmayan noktalar aykırı değer olarak belirlenir.

### DBSCAN - Özellikler ve Kullanım
* **Özellikler**:
  * **Parametreler**: `eps` (mesafe) ve `min_samples` (minimum komşu sayısı) ayarlanmalıdır.
  * **Esneklik**: Küme sayısı önceden belirlenmez ve verinin yoğunluk yapısına göre kümeleme yapar.
  * **Aykırı değerler**: Aykırı değerleri tanımlama yeteneğine sahiptir.
* **Kullanım Alanları**:
  * Coğrafi veri analizi
  * Gürültü verisi analizi
  * Anomali tespiti

### DBSCAN - Temel Kavramlar
* **Epsilon (`eps`)**: Bir nokta etrafındaki arama yarıçapını belirler. Bu yarıçap içindeki noktalara komşu denir.
* **Minimum nokta sayısı (`min_samples`)**: Bir noktanın çekirdek nokta (`core point`) olarak kabul edilmesi için `eps` yarıçapı içinde bulunması gereken minimum komşu nokta sayısıdır (kendisi dahil).
* **Çekirdek nokta (`core point`)**: Etrafındaki `eps` yarıçapı içinde en az `min_samples` komşusu olan bir noktadır. Bir kümenin iç kısmında yer alır.
* **Sınır noktası (`border point`)**: Kendisi çekirdek nokta olmamasına rağmen bir çekirdek noktanın `eps` yarıçapı içinde yer alan bir noktadır. Bir kümenin sınırında yer alır.
* **Gürültü noktası (`noise point`)**: Ne çekirdek nokta olan ne de herhangi bir çekirdek noktanın `eps` yarıçapı içinde yer alan bir noktadır. Herhangi bir kümeye ait olmayan aykırı değer olarak kabul edilir.

### DBSCAN - Algoritması
1. **Başlangıç**: Veri setindeki tüm noktalar işlenmemiş olarak işaretlenir.
2. **Nokta seçimi**: İşlenmemiş bir nokta seçilir.
3. **Komşu bulma**: Seçilen noktanın `eps` yarıçapı içindeki komşuları bulunur.
4. **Çekirdek nokta kontrolü**: Eğer nokta çekirdek nokta ise kümeleme başlar.
5. **Kümeleme**: Nokta ve komşuları aynı kümeye atanır.
6. **Genişleme**: Komşuların her biri için adım 3-5 tekrarlanır.
7. **Tekrar**: Tüm noktalar işlenene kadar adım 2-6 tekrarlanır.

### DBSCAN - Avantaj ve Dezavantaj
* **Avantajlar**:
  * Küme sayısını önceden belirlemeye gerek yoktur.
  * Gürültü ve aykırı değerleri tanımlama yeteneği vardır.
  * Farklı yoğunluklarda kümeleri tespit edebilir.
* **Dezavantajlar**:
  * `eps` ve `min_samples` parametrelerinin doğru ayarlanması zor olabilir.
  * Küme şekilleri karmaşık olduğunda performansı düşebilir.
  * Yüksek boyutlu verilerde etkili olmayabilir.

### DBSCAN - Parametre Seçimi

* **Epsilon (`eps`) için K-Mesafe Grafiği**:
  * Her nokta için `n`'inci en yakın komşu mesafesini görselleştirin.
  * Grafikteki dirsek noktası, potansiyel `eps` değerini gösterebilir.

* **Minimum Nokta Sayısı (`min_samples`) için**:
  * Genellikle 2 ile 5 arasında bir değer seçilir.
  * Veri setinin yoğunluğuna bağlı olarak ayarlanabilir.

* **Optics Algoritması**:
  * DBSCAN'ın bir genellemesidir.
  * Farklı yoğunluklarda kümeleri tespit edebilir.
  * Parametre ayarlama gereksinimini azaltır.

* **Gaussian Mixture Model (GMM)**:
  * Veriyi birden fazla Gauss dağılımı ile modelleyerek kümeleme yapar.
  * Küme sayısını belirlemek için BIC veya AIC gibi kriterler kullanılabilir.
  * Daha esnek ve karmaşık veri yapıları için uygundur.