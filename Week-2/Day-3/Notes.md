12 April 2024 Week 2 Day 3

Scikit-Learn

Değişkenler Arasındaki İlişkilerin Analizi

Neden ilişki analizi?
* Değişkenler arasındaki ilişkileri anlamak veri setinden değerli bilgiler elde etmemizi sağlar.
* Bu bilgiler iş kararları almak, tahminler yapmak ve olayları açıklamak için kullanılır.
* Farklı değişken türleri arasındaki ilişkileri incelemek için farklı yöntemler gereklidir.

Çapraz Tablolama (Cross-tabulations)
* pandas.crosstab() fonksiyonu ile oluşturulur.
* İki veya daha fazla kategorik değişkenler arasındaki ilişkiyi özetler.
* Her hücre belirli bir kategori kombinasyonuna ait gözlem sayısını gösterir.
* Örnek: Müşteri cinsiyeti ile satın alınan ürün kategorisi arasındaki ilişkiyi gösterir.

Gruplandırılmış İstatistikler
* pandas.groupby() fonksiyonu ile hesaplanır.
* Kategorik değişkenlere göre sayısal değişkenlerin özet istatistiklerini (ortalama, medyan, toplam vb.) gösterir.
* Örnek: Farklı müşteri segmentlerinin ortalama harcama tutarları.

Hipotez Testleri - Ki-kare Testi
* Kategorik değişkenler arasındaki bağımsızlığı test eder.
* Gözlenen frekanslar ile beklenen frekanslar arasındaki farkı ölçer.
* Formül: X^2 = Σ((O - E)^2 / E)
* X^2: Ki-kare istatistiği
* O: Gözlenen frekans
* E: Beklenen frekans
* Σ: Tüm hücreler için toplam
* Örnek: Müşteri cinsiyeti ile satın alınan ürün kategorisi arasındaki bağımsızlık testi.

Hipotez Testleri - ANOVA
* Sayısal bir değişkenin kategorik bir değişkene göre ortalamalarının farklı olup olmadığını test eder.
* Gruplar arası ve gruplar içi varyasyonu karşılaştırır.
* Formül: F = Varyasyonlar arası / Varyasyonlar içi (MST / MSE)
* F: ANOVA istatistiği
* MST: Gruplar arası ortalama kareler toplamı (Mean Square Treatment)
* MSE: Gruplar içi ortalama kareler toplamı (Mean Square Error)
* ANOVA'nın geçerli olabilmesi için bazı varsayımlar sağlanması gerekir.
* Varsayımlar:
  * Normal dağılım: Her grup içindeki verilerin normal dağılıma sahip olması.
  * Varyans homojenliği: Grupların varyanslarının eşit olması.
  * Bağımsızlık: Gözlemlerin birbirinden bağımsız olması.
* Kontrol yöntemleri:
  * Normallik: Shapiro-Wilk testi, Kolmogorov-Smirnov testi, histogram, Q-Q grafiği.
  * Varyans homojenliği: Levene testi, Bartlett testi.

ANOVA - Post-hoc Testler
* ANOVA'da anlamlı sonuç alındığında hangi gruplar arasında anlamlı fark olduğunu belirlemek için kullanılır.
* Tukey HSD testi, Bonferroni testi, Scheffe testi gibi yöntemler kullanılır.

ANOVA - Etki Ölçüleri
* Hipotez testinin sonuçlarını pratik önemini değerlendirmek için kullanılır.
* Örnekler: Etki büyüklüğü (effect size) Cohen's d, eta kare, omega kare gibi ölçüler kullanılır.

Sayısal Değişkenler Arasındaki İlişkiler - Korelasyon ve Kovaryans
* Korelasyon, iki sayısal değişken arasındaki doğrusal ilişkinin yönünü ve gücünü ölçer.
  * Pearson korelasyonu: İki değişken arasındaki doğrusal ilişkiyi ölçer.
  * Pearson korelasyon katsayısı (r).
* Kovaryans, iki sayısal değişkenin birlikte ne kadar değiştiğini gösterir.

Sayısal Değişkenler Arasındaki İlişkiler - Korelasyon Matrisi Görselleştirme
* Sayısal değişkenler arasındaki korelasyonları bir matris şeklinde gösterir.
* Isı haritası (heatmap) ile görselleştirerek yorumlanması kolaylaştırılır.

Sayısal Değişkenler Arasındaki İlişkiler - Regresyon Analizi
* Sayısal bir bağımlı değişken ile bir veya daha fazla bağımsız değişken arasındaki ilişkiyi inceler.
* Türler:
  * Doğrusal regresyon: Bağımlı değişken ile bağımsız değişkenler arasındaki doğrusal ilişkiyi inceler.
  * Lojistik regresyon: Bağımlı değişkenin ikili (binary) olduğu durumlarda kullanılır.

Regresyon Analizi - Varsayım Kontrolleri
* Regresyon modelinin geçerli olabilmesi için bazı varsayımları sağlaması gerekir.
* Varsayımlar:
  * Doğrusallık.
  * Hata terimlerinin normalliği.
  * Hata terimlerinin varyans homojenliği (homoskedastisite).
  * Hata terimlerinin bağımsızlığı.

Regresyon Analizi - Etkileşim Terimleri
Regresyon Analizi - Karışıklık Terimleri

Diğer Sınıflandırma Algoritmaları ile İlişki Analizi (Eğer Gerekirse)
* Lojistik regresyon dışında diğer sınıflandırma algoritmaları (örneğin karar ağaçları, destek vektör makineleri) kullanılarak da değişkenler arasındaki ilişkiler incelenebilir.


# Models