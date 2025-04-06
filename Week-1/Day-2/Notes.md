6 April 2025
Week 1 Day 2

# Preprocessing
Eksik veri imputasyonu ( imputation ) SimpleImputer

# imputasyon ( Doldurma) nedir?
Eksik verilerin yerine tahmin edilen veya hesaplnana değerler koyma işlemidir.
Amaç: Veri kaybını önlemek,modelin daha iyi performans göstermesini sağlamak.

SimpleImputer kullanımı
* scikitlearn kütüphanesinden SimpleImputer sınıfını kullanarak eksik verileri doldurabiliriz.
* Eksik verileri ortalama medyan veya en sık değer mod ile doldurabilir.
*  Sayısal ve kategorik veriler için gfarklı statejiler uygulanabilir.
*  strategy parametresi ile doldurma yönntemi belirlenir:
  * mean: Ortalama ile doldurma ( sayısal veriler için)
  * median: Medyan ile doldurma ( sayısal veriler için)
  * most_frequent: En sık değer ile doldurma ( kategorik veya sayısal veriler için)
  * constant: Sabit bir değer ile doldurma ( sayısal veya kategorik veriler için)
* fill_value parametresi, constant seç,ldiği zaman dolduraak olan değeri belirler


# Veri Dönüşümü ( Transformation )
* mevcut özellikler kullanılarak yeni özellikler oluşturma işlemidir.
* Amaç: Modelin karmaşıklığını artırmaki veri setinde bulunmaya ilkileri ortaya çıkarmak.
* modelin çğrenme kapasitesini artırır.

Veri Dönüşümü ( Transformation ) - PolynomialFeatures
* Özelliklerin polinomlarını oluşturur.
* Özelliklerin çarpımlarını ve kuvvetlerini oluşturur.
* Özelliklerin etkileşimlerini yakalar. 

Veri Dönüşümü ( Transformation ) - FunctionTransformer
* Kullanıcı tanımlı bir fonksiyonu veri setine uygular.
* Logaritmik üstel veya trigionmetrik dföünüşmler gibi özel durumlarda kullanılır.
* func parametresi ile uygulanacak fonksiyon belirtlir.

Veri Dönüşümü ( Transformation ) - Karşılaştırma
* PolynomialFeatures: Mofrlein karşmaşılpını artırmak için pılinem özellikleri ouşturur.
* function transformer verilere özel fonksiyonlar uyugularayak özel dönüşümler sağlar.

# Özellik Seçimi ( Feature Selection )
* Model içim en önemli özellikleri belirleme ve geri kalanları eleme işlemidir.
* Neden önemli:
  * Modelin performansını artıtır.
  * Eğitim süresini kısaltır.
  * Aşırı öğrenmeyi ( overfitting ) azaltır.
  * Veri setinin anlaşılabilirliğini sağlar.

Özellik Seçimi ( Feature Selection ) - Varyans Eşiği ( VarianceThreshold )
* varyansı belirli bir eşiğin aktubda olan özelliğikleri kaldırır.
* sabit veya neredeeyse sabit değelere sahip özellikleri temizlemek için kullanılır.
* Varyans değeri düşük olan özellikler modelin öğrenmesine pek bir katkı sağlamaz.

Özellik Seçimi ( Feature Selection ) - Korelasyon Tabanlı Öznitelik Seçimi ( SelectKBest )
* hedef değikenle yüksek korelasyona sahip özellikleri seçer
* çoklu doğrısalık sorunun azaltmaya yardımcı olur
* özellikler arasıdnki doğrsul illiki ölçülür
* veri setindeki hedef değişken ile diğer değerlerin arasındaki korelasyon matrisi bulunur
* istenilen korelasyon değerine göre değikenler seçilir veya elenir.

Özellik Seçimi ( Feature Selection ) - SelectFromModel
* bir makine öğreniim modelinin özellik önemine göre seçilim ypar
* regresyon modellerini lasso ridge veya ağac tabanlı modeller randorm forest kullanılabilir.
* Modelin en iyi sonuç verdiği değişkenler tutulur.

Özellik Seçimi ( Feature Selection ) - Karşılaştırma
* Varyans Eşiği: Düşük varyansa sahip özelliklerri temizler.
* Koreslasyon tabanlı öznitelik seçimi hedef değilkenle yüksek korelasyona sahip değişkenler seçilir.
* SelectFromModel: Modelin özellik önemine göre seçim yapar.



# Boyut İndirgeme ( diminsionality reduction) : temel bileşen analizi ( principal Compenent analysis - PCA)
* yüksek boyutlu veri setlerinde özellik sayısını azalatma işlenmidir.
* Amaç:
  * Veri kümrsisin karmaşıklığımı azalatmak7
  * hesaplama maliyetini düşürmek
  * görsellestirmeyi kolaylastırmak 2d veya 3d
  * aşırı öprenmeyi overfitting önlemek
  * özellikler arasındaki çoklu doğrsallık ( multicollinearity ) sorunun çözmek

Temel Bileşen Analizi ( PCA )
* en yaygın boyut indirgeme tekniklerinde biriir
* verideki en büyük varyansı yakalan yeni eksenler temel bileşenler bulut
* özllikler arasındaki korealsyonu azaltır
* doğrusal bir yöntemdir.

PCA çalışma prensini
* 1.Adım: veri setinin ortalamasını al
* 2.Adım korvayons marrisi hesaplanir
* 3.Adım korvanyans amrisin özvekterleri ve özdeğelrini bulunur
* 4.Adım özdeğerlere gmre mzvektler sıralanaır ( en büyükten en kğçğoe )
* 5.Adım ilk k özvektör en büyük özdeğere karşılık gelen sçeilir
* 6.Adım veri seti seçilen özvektöerele dönüştürülür
* matematisel alt yapı temel bileşenler özvekler ile orijibal verinin doğrısal kombinasyolarıdır.

PCA de boyut seçimi
* kaç temel bileşen seçileceği önemlidir
* Açıklanan varyans oranı kullanılır.
* Genellikle toplma varyansın % 90 95 imi açıklayan bileşenler seçilir
* Dirsek grafikleri ( elbow plots ) kullanılabilir.

PCA'nın Kullanım alanları
* görüntü sıkıştırma
* yüz tanıma
* genetik veri analizi
* finansal veri analizi
* veri görselleştirme

Feature Selection ( Özellik Seçimi ) ile Dimensionality Reduction ( Boyut İndirgeme ) Arasındaki Farklar
* Amaç: En önemli özellikleri seçmek / Daha az özellik ile veri setini temsil etmek
* Yöntem: En önemli özelliği seç diğerini at / Özellikleri matematiksel olarak birleştirierek yenisini oluşturur.
* Sonuç: Seçilen özellikler orijinal ,özgündür,özelliklerdir / Özellikler Özgünlüğnü kaybeder
* Yorumlanabilir: Yorumlanabiliği yüksek olabilir / Yorumlanabilirlik azalır
* Örnekler: SelectKBest, Recursive Feature Elimination / PCA, t-SNE

--- End of one part ---

# Eksik, Yanlış ve Marjinal Verilerle Çalışma

Neden veri temizliği önemlidir?
* Makine öğreinim modellerinin doğru ve güvenilir sonuçlar vermesi için kritik.
* Yanlışi veya eksilk veeriler hatalı tahminlere ve yanlış kararlara yol açalbilir
* Kaliteli veri daha güçlü ve genellebilir modeller oluşturmamızı sağlar
* Matemaitksel alt yapı istatiksel yönntemlerin ortalam standart sapma vb. doğru hesaplanması için veirleri temiz olması gerekir.

Veri kalitesi sorunları 
* Eksik veri bazı gözmlwmder bazı özellklerin değerlenin olmaması
* yanlış veri yanluş girilmiş tutarsız veya geçerli olmayan veirleri
* aykırı marjinal verile r diğer gözlemrden çok farlı olan uç noktalar
* tutarsızlıklar aynı biligiyi farklı formatlada veya farklı şekillerde temsil eden değerler

Veri temizleme süreci
1. Veri tespiti hataları ve eksikleri belirlemek
2. veri düzenlemtme hataları düzeltmek veya eksikleri gidermek
3. veri döünüşümü veriyi analizi çin ıyugun bir formata getirmek
4. doğrılama temizlenmi şverinin dıpru olduğundan emin olmak

Kullanılan Araçlar ve Kütüphaneler
* Pandas: veri analizi ve işleme için güçlü bir kütüphane
* NumPy: sayısal hesaplamalar için temel kütüphane
* Matplotlib ve Seaborn: veri görselleştirme için kullanılır
* Scikit-learn: makine öğrenimi ve veri ön işleme için geniş bir kütüphane
* Missingno: eksik verileri görselleştirmek ve analiz etmek için kullanılır

# Eksik veri tespiti 
* bir veri seitnden gözlemlerde belirli sutunlerşn değelerini mamasıdır
* "Nan" not a bumver oalrak gösterilir
* Neden önemli?
  * Eksik veriler modelin performansını etkileyebilir
  * Eksik verilerin nedenleri anlaşılmalıdır
  * Eksik verilerin nasıl ele alınacağına karar verilmelidir

pandas.isnull() ve pandas.isna()

Missingno Kütüphanesi
* Eksik verileri görselleştirmek için kullanılır
* Matrix(), bar(), heatmap() gibi fonksiyonlar ile eksik verileri görselleştirir
* msno.matrix() ile eksik verilerin dağılımını görselleştirir
* msno.bar() ile eksik verilerin sayısını ve oranını gösterir
* msno.heatmap() ile eksik verilerin korelasyonunu gösterir
* msno.dendrogram() ile eksik verilerin hiyerarşik yapısını gösterir

# Eksik veri doldurma teknileri
* Eksik veri veri analizini ve modellemeyi olumsuz etkileyebilir
* doldurma veri kaybını en aza inderek analiz doğruluğunu artılabilir
* bazı makine öğrenimi algoritmaları eksik velriere işleyemez bu yüzden doldurma gereklidir


Eksik veri dıkdurma teknileri - Ortalama, medyan mod ile doldurma
* Ortalama: sayıssal sütunlardaki eksik değerleri sütunun ortalamasoyla doldurma.
  * df['column_name'].fillna(df['column_name'].mean(), inplace=True)
  * df['sutun'].fillna(df['sutun'].mean(), inplace=True)
  * avantajı basit ve hızlı
  * dezavantajı aykırı değerlendern etkilernir vayansı azaltır

* Medyan: sayıssal sütunlardaki eksik değerleri sütunun medyanı ile doldurma.
  * df['column_name'].fillna(df['column_name'].median(), inplace=True)
  * df['sutun'].fillna(df['sutun'].median(), inplace=True)
  * avantajı aykırı değerlere karşı daha dayanıklıdır
  * dezavantajı varyansı azaltır

* Mod: kategorik sütunlardaki eksik değerleri sütunun moduyla doldurma.
  * df['column_name'].fillna(df['column_name'].mode()[0], inplace=True)
  * df['sutun'].fillna(df['sutun'].mode()[0], inplace=True)
  * avantajı kategorik veriler için uygundur
  * dezavantajı en sık değeri baskın hale getirebilir

Eksik veri doldurma teknikleri - ileri ve geri doldurma
İleri doldurma: eksik değerleri kendinden öncekigeçerli verilerle doldurma
  * df['column_name'].fillna(method='ffill', inplace=True)
  * df['sutun'].fillna(method='ffill', inplace=True)
  * avantajı zaman serisi verilerinde kullanışlıdır
  * dezavantajı yanlış tahminlere yol açabilir ani değişiklikleri yakalyamaz.

Geri doldurma: eksik değerleri kendinden sonraki geçerli değerle doldurma
  * df['column_name'].fillna(method='bfill', inplace=True)
  * df['sutun'].fillna(method='bfill', inplace=True)
  * avantajı zaman serisi verilerinde kullanışlıdır
  * dezavantajı yanlış tahminlere yol açabilir Ani değişiklikleri yakalaymaz.


Eksik veri doldurma teknikleri - Tahmine Dayalı Doldurma
* Eksik değerleri diğer özelliklere dayanarak tahmin etme
  * Regresyon
    * sayısal eksiklikler için 
    * örneğin linear regresyon kullanarak eksik değerleri tahmin edebiliriz
  * K-En Yakın komşular (KNN)
    * sayısal ve kategorik eksikler için
    * KNNImputer sınıfı kullanarak eksik değerleri tahmin edebiliriz ( Scikit-learn kütüphanesi)
* Avantajı: Daha doğru sonuçlar verir
* Dezavantajı: Hesaplama maliyeti yüksektir, Modelleme hatalarına duyarlı

Yanlış veri tespiti ve düzeltme
* veri toplama süreçlerindeki hatalar ( insan hatası, lçüm cihazı sorunları)
* Veri giriş hataları
* Veri dönüştürme veya birleştirme sırasında oluşan sorunlar.
* Yanlış veriler, analiz sonuçlarını ve model perfomansını olumsuz etkiler.

Veri tiplerinin doğrulupunu kontrol etme
* Amaç: sütunların veri tiplerini beklenenlerle eşleşip eşleşmediğini kontrol etmek
* Yöntemler:
  * df.info() datagrame deki sütunların veri tiplerini gösteriri
  * df.dtypes() Her sütunun veri tipini dönüdürür
  * pd.to_numeric() bir sğtunu sauyısal bir ütre dönüştürmeye çalısır ( hata durumunda error parametristle ne yapılacağını belirtebilirsiniz.)
  * astype() bir sütunun veri tipini değiştirir.
* örnek "yaş" sütunun sayısal olması gerekirken, metin türünde olması

# Aykırı değer tespiti ve eleme
* Aykırı değerler: Veri setibib genelinden önemli ölçüde farklı olan gözlemler
* Neden Önemli?
  * İstatisksel analizleri etkieleyebilri ( portalama sandart sapma )
  * Model perfomansını düşürebilir.
  * yöntemler:
    * Görselleştirme
      * Kutu grafikleri ( sns.boxplot() )
      * Histogramlar ( sns.histplot() )
      * Saçılım grafikleri ( sns.scatterplot() )
    * İstatksel yönetemler
      * Z-Score bir değerin ortalamadan kaç sranart sapma uzakrta olduğunu ölçer
      * IQR ( çeyrekler arası aralık) verinin orta yüzde ellisini kapsayan aralık
  * Eleme aykırı değerleri veri setinden çıkarmak

Marjinal aykırı değerlerle başa çıkma
* Veri setindeki diğer gözlemlerden önemli ölçüde farklı uç değerlerdir
* Dağılımn kuyruklarında yer alırlar
* Neden önemlidir?
  * istatistiksel analizleri etkileyebilir ( ortlama,standart sapma).
  * Model performansını bozabilir
  * Yanlış sonuçlara yol açabilir

Aykırı değerleri tespit etme görselleştirme yöntemleri
* Kutu grafikleri ( sns.boxplot() ): verini dağılımını çeyrekliler medyan ve aykuru değerler cinsinden gösterir.
* Histogramlar ( sns.histplot() ): verinin dağılımını frekans tabanlı gösterir.
* Saçılım grafikleri ( sns.scatterplot() ): iki değişken arasındaki ilişkiyi gösterir ve aykırı değerleri görsel olarak ortaya çıkarabilir.

Aykırı değerleri tespit etme - istatiskler yöntemler
* Z-Score: bir değerin ortalamadan kaç standart sapma uzaklıkta olduğunu ölçer.
  * Z-Score = (x - ortalama) / standart sapma
  * Genellikle Z-Score > 3 veya Z-Score < -3 olan değerler aykırı olarak kabul edilir.
* IQR (Çeyrekler Arası Aralık): verinin orta yüzde ellisini kapsayan aralık
  * Q1: 1. çeyrek ( %25)
  * Q3: 3. çeyrek ( %75)
  * IQR = Q3 - Q1
  * Aykırı değerler: Q1 - 1.5 * IQR ve Q3 + 1.5 * IQR dışındaki değerlerdir.

Aykırı değerleri tespit etme - Aykırı değerleri dönüştürme veya budama
* Dönüştürme:
  * Log dönüşümü: Sağa çarpık veriler daha simetrij hale getirerek aykırı değerlerin etkisini azalabilir
    * Formül: y = log(X)
  * Karekök Dönüşümü: Log dönüşümüne benzer şekilde sağa çarpıklığı azalbilir
    * Formül: y = kökx
* Budama: 
  * Winsorizing aykırı değeleri beliri bir aralıktaki en yakın değerlere değişitmre
    * Formül: if x < Q1 - 1.5 * IQR: x = Q1 - 1.5 * IQR
* Trimming: Aykırı değerleri veri setinden çıkarmak
  * Formül: if x < Q1 - 1.5 * IQR or x > Q3 + 1.5 * IQR: drop x
  
Aykırı değerleri tespit etme - Robust istatiskler yöntemler kullanma
* aykırı değerlere karşı daha dayanıklı olan istatiksel yöntemleri tercih etme
* örnekler: ortalama yerine medtan kullanma: medyan aykırı değerlrden daha az etkilenir
* standart sapma yerine iqr kullanma iqr aykırı değerlenden daha az etkilenir
* Robust ölçeklendirme yöntemleri ( RobustScaler ) kullanma

# Veri tutarsızlarını düzeltme
* Amaç: aynı varlığı temsil eden farklı değerleri birleştirmek veya standartlaştırma
* Örnekler:
  * "İstanbul","İSTANBUL","istanbul" gibi farklı yazım şekillerini birleştirme
  * Farklı biirmlerdeki değerleri aynı birime dönüştürmek ( örneğin, metre ve santimetre)
* Yöntemler:
  * str.lower(), str.upper(),str.strip(): Metin verilerini dönüştürmek.
  * replace(): Belirli değerleri değiştirmek
  * Fuzzy matching algoritmaları: Yazım hatalarına yakın değerleri bulmak ve düzeltmek.
