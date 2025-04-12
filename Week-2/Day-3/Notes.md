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


# Supervised Learning
* Veri, enformasyon ve bilgi, dataset, performans ölçekleri

Veri (Data) Nedir?
* Olgu, kavram veya komutların iletişim, yorum ve işlem için elverişli biçimde gösterimi (bilişim).
* Gözlem ve deneye dayalı araştırmanın sonuçları (istatistik).
* Bir problemde bilinen, belirli bir amaca yönelik olarak toplanmış, işlenmiş ve analiz edilmiş bilgi (veri bilimi).

Veri - Enformasyon - Bilgi
Veri
* Gerçek hayattaki gözlem, sonuç, ölçüm ve donelerin dijitale çevrilmiş halidir.
* Hamdır, yani işlenmemiştir.

Enformasyon (Bilgi)
* Bilgi dönüşümünün 2. basamağıdır.
* Verinin düzenlenmiş, gruplanmış, derlenmiş, özetlenmiş, sorgulanmış vb. işlemlerden geçirilmiş halidir.

Bilgi (Knowledge)
* Bilgi dönüşümünün 3. basamağıdır.
* Veri ve enformasyonun analiz edilerek anlamlı hale getirilmiş halidir.

Verileri Elde Etme Şekli
* JSON
* XML
* CSV

Veriseti (Dataset)
* Veri seti, belirli bir amaca yönelik olarak toplanmış, işlenmiş ve analiz edilmiş veri kümesidir.
* Veri setleri, genellikle bir tablo şeklinde düzenlenir ve her satır bir gözlemi, her sütun ise bir değişkeni temsil eder.
* Veri setleri, veri analizi, makine öğrenimi ve istatistiksel modelleme gibi alanlarda kullanılır.
* Veri setleri, genellikle birden fazla değişken içerir ve bu değişkenler arasındaki ilişkileri incelemek için kullanılır.

Veri Türleri
* Kategorik Değişkenler: Sınıflandırma veya gruplama amacıyla kullanılan değişkenlerdir. Örnek: cinsiyet, ürün kategorisi.
  * Nominal Değişkenler: Sıralama veya derecelendirme içermeyen kategorik değişkenlerdir. Örnek: renk, şehir.
  * Ordinal Değişkenler: Sıralama veya derecelendirme içeren kategorik değişkenlerdir. Örnek: eğitim seviyesi, memnuniyet derecesi.
* Sayısal Değişkenler: Sayısal değerler içeren değişkenlerdir. Örnek: yaş, gelir, harcama tutarı.
  * Sürekli Veriler
  * Ayrık Veriler

Kayıp, Marjinal Veri
* Kayıp veri, veri setinde eksik veya boş olan gözlemleri ifade eder. Kayıp veriler, analiz sonuçlarını etkileyebilir.
* Marjinal veri, veri setinde belirli bir değişkenin değerlerinin çok az gözlemle temsil edildiği durumu ifade eder. Marjinal veriler, analiz sonuçlarını etkileyebilir ve dikkatli bir şekilde ele alınmalıdır.

Kategorik Verilerin Dönüşümü
* Kategorik veriler, sayısal verilere dönüştürülerek analiz edilebilir.
* Bu dönüşüm, kategorik değişkenlerin sayısal değerlerle temsil edilmesini sağlar.
* Örnek: cinsiyet değişkeni "erkek" ve "kadın" olarak iki kategoriye sahipse, bu kategoriler 0 ve 1 ile temsil edilebilir.

Label Encoding
* Kategorik değişkenlerin her bir kategorisini benzersiz bir sayısal değere dönüştürür.
* Örnek: "erkek" = 0, "kadın" = 1
* Label encoding, sıralı kategorik değişkenler için uygundur.

One-Hot Encoding
* Kategorik değişkenlerin her bir kategorisini ayrı bir sütun olarak temsil eder.
* Her sütun, belirli bir kategorinin varlığını veya yokluğunu gösterir.
* Örnek: "erkek" = [1, 0], "kadın" = [0, 1]
* One-hot encoding, sıralı olmayan kategorik değişkenler için uygundur.

Öznitelik Çıkarımı (Feature Extraction)
* Veri setindeki önemli özelliklerin belirlenmesi ve bu özelliklerin yeni değişkenler olarak kullanılmasıdır.

Verisetleri Bölümlendirme İşlemleri
* Hold Out
* Cross Validation

Hold Out
* Veri setinin belirli bir oranını eğitim ve test setlerine ayırma işlemidir.
* Eğitim seti modelin eğitilmesi için kullanılırken, test seti modelin performansını değerlendirmek için kullanılır.
* Hold out yöntemi, veri setinin %70-80'ini eğitim seti ve %20-30'unu test seti olarak ayırmayı önerir.
* Bu oranlar veri setinin büyüklüğüne ve modelin karmaşıklığına bağlı olarak değişebilir.
* Hold out yöntemi, veri setinin büyüklüğüne bağlı olarak modelin performansını değerlendirmek için yeterli veri sağlamayabilir.
* Bu nedenle, daha büyük veri setlerinde daha güvenilir sonuçlar elde etmek için cross-validation yöntemi tercih edilebilir.

Test Dataset
* Test seti, modelin performansını değerlendirmek için kullanılan veri setidir.
* Test seti, modelin eğitilmesi sırasında kullanılmaz ve modelin genel performansını değerlendirmek için kullanılır.
* Test seti, modelin gerçek dünya verileri üzerindeki performansını değerlendirmek için önemlidir.
* Test seti, modelin aşırı öğrenme (overfitting) yapıp yapmadığını kontrol etmek için kullanılır.

Dataset Ayrımı
* Veri setinin eğitim ve test setlerine ayrılması, modelin performansını değerlendirmek için önemlidir.
* Veri setinin eğitim ve test setlerine ayrılması, modelin aşırı öğrenme (overfitting) yapıp yapmadığını kontrol etmek için önemlidir.
* Veri setinin eğitim ve test setlerine ayrılması, modelin genel performansını değerlendirmek için önemlidir.
* Veri setinin eğitim ve test setlerine ayrılması, modelin gerçek dünya verileri üzerindeki performansını değerlendirmek için önemlidir.

Overfitting
* Aşırı öğrenme veya ezberleme anlamına gelir.
* Beklenenden daha kompleks bir model sonucu, model train dataset'e aşırı uyumludur.
* Ancak validation ve testte beklenen sonuçları vermez.
* Yüksek varyans, düşük bias sonucudur.
* Train işlemi sonucu olarak düşük loss, yüksek accuracy verir.
* Ama test sonuçları yüksek loss, daha düşük accuracy'dir.

Overfitting Önlemek İçin Tavsiyeler
* Modeli sadeleştir.
* Daha az öznitelik ele (feature selection olabilir).
* Daha fazla örnek ekle.
* Data augmentation ile veri çoğalt.
* Regularization (düzleştirme) yap.
* Erken durdurma algoritmaları kullan.
* Cross-validation kullan.
* Hâlâ varsa, o zaman farklı modeller kullan.

Underfitting
* Eksik öğrenme veya öğrenmeme anlamına gelir.
* Model sınıflandırma veya regresyon işlemlerini başaramaz.
* Bazen test sonuçları train sonuçlarından iyi gelebilir.
* Yüksek bias'ın bir sonucudur.
* Yüksek loss'a karşılık düşük accuracy alınır.

Underfitting'i Önlemek İçin Tavsiyeler
* Modeli karmaşıklaştır.
* Daha fazla öznitelik ekle.
* Daha fazla örnek ekle.
* Data augmentation ve sentetik veri üretimi teknikleri kullan.
* Daha uzun süre train yap.
* Hâlâ mı underfitting? Model belki yanlıştır, değiştir.

Just Right
* Modelin overfitting ve underfitting durumlarından arındırılmış hali.
* Varyans ve bias'ı düşüktür.
* Train, validation ve test loss'ları düşük, accuracy oranları yüksektir.
* Modelden beklenen durumdur.

Fitting Karşılaştırmaları
https://www.tutorialandexample.com/overfitting-and-underfitting-in-machine-learning

Varience, Bias, Overfitting, Underfitting ( Görsel bul)
* Low variance, low bias: Modelin doğru tahminler yapabilmesi için yeterli bilgiye sahip olduğu durum. ( optimal capacity )
https://towardsdatascience.com/what-bias-variance-bulls-eye-diagram-really-represent-ff6fb9670993
https://www.geeksforgeeks.org/underfitting-and-overfitting-in-machine-learning/
https://datascience.stackexchange.com/questions/117189/relation-between-underfitting-vs-high-bias-and-low-variance

  
Cross Validation
* Veri setinin eğitim ve test setlerine ayrılması yerine, veri setinin farklı alt kümeleri üzerinde modelin performansını değerlendirme yöntemidir.
* Cross-validation, modelin genel performansını değerlendirmek için daha güvenilir sonuçlar sağlar.
* Cross-validation, modelin aşırı öğrenme (overfitting) yapıp yapmadığını kontrol etmek için kullanılır.
* Cross-validation, modelin gerçek dünya verileri üzerindeki performansını değerlendirmek için önemlidir.
* https://medium.com/@mtterribile/understanding-cross-validations-purpose-53490faf6a86

