26 April 2025

# Artificial Neutral Networks ( Yapay Sinir Ağları )
* yapa sinir ağları ver türevleri günümüzde en yaygın kullanulan makine öğrenmesi modelleridir
* temlelleri 1940 yıkllara dayanmasına rağen 2010 lu yıllardan itibaren parlamıştır
* derin apların temellerini oluşturaktadır
* öğrenme ve eğitim kavramı tam olarak bu modellerde karşılığıın bulmuştur.
* yapay sinir ağları  biyolojik sinir ağlarını örnek alınarak oortaya çıkmıştır
* biyolojik sinir ağları insanlarda oldukça karışıktır
* insandaki sinir ağ yapısını takip eden yapay sinir ağları 3 katmandan oluşur

# Biyolojik Sinir Ağları
* Nöron : sinir sistemini oluşturan sinir hücreleridir.işleleri sinirsle uyarıoları elektirilsel sihnyaller biçiminde iletmektir
* Sinaps : nöronlar arasında iletişimi sağlayan bağlantılardır
* Aksiyom : nöronların sinyalleri iletmek için kullandığı uzantılardır
* Dendrit : nöronların diğer nöronlardan gelen sinyalleri almak için kullandığı uzantılardır
* Akson : nöronların diğer nöronlara sinyalleri iletmek için kullandığı uzantılardır
* Sinir hücreleri birbirleriyle sinaps adı verilen bağlantılarla iletişim kurar

# Heb Öğrenme Kuralı (1949)
* en eski ve basit öğrenme kuralıdır.
* eğer birbirine bağlu iki nöron aynı anda aynı iaşrete sahispope bu nöronlar arasındaki aplrık dğeri artılır.
* eğer birbirine bağlı iki nöron aynı anda farklı işaretlere sahipse bu nöronlar arasındaki bağlantı değeri azalır.

## Heb Öğrenme Kuralı için eğitim algoritması
* Adım 1: Ağırlıkların başlatılması
  * Ağırlıklar genellikle rastgele değerlerle başlatılır.
* Adım 2: Girdi ve Çıkışların Belirlenmesi
  * Girdi ve çıkış verileri belirlenir.
* Adım 3: Ağırlıkların Güncellenmesi
  * Ağırlıklar, girdi ve çıkış verilerine göre güncellenir.
* Adım 4: Hata Hesaplama
  * Hata, beklenen çıkış ile elde edilen çıkış arasındaki farktır.
* Adım 5: Ağırlıkların Güncellenmesi
  * Ağırlıklar, hata değerine göre güncellenir.

* Örnek tablo:
| Girdi 1 | Girdi 2 | Çıkış |
|---------|---------|-------|
| 0       | 0       | 0     |
| 0       | 1       | 0     |
| 1       | 0       | 0     |
| 1       | 1       | 1     |



# Perceptron Modeli
* Treshold logic unit modeli öğrenmeye elverişli değildi
* 1949 yılında doanld hebb biyolojik noronlar hakkında bir görüş ortaya attı
* hebb e göre aynı sinap iki noron aynı anda etkinleştirilse bağ güçlenir ve öğrenme kolaylaşltırıldı
* bu tezi örnek alan rosenblatt 1958 yılında perceptron modelini yani öğrenilen yapay sinir ağ modeli geliştirdi.
* bu modele göre her girdi kendi ağırlığı ile çarpılır
* nu çarpımlar toplanır ve dengeleyici olarak bir bias değeri eklenir
* bulnan çıkış bir aktivasyon fonksiyonuna sokulur ve çıkış y değeri bulunur
* bu aynı zamanda ileri beslemeli bir ağ örneğidir.

# Aktivasyon Fonksiyonları
* aktivasyon fonksiyolarmı teöel görevi belirnen eşik değerler arasında bir değere çevirmektir.
* birçıj aktivasyon fonksiyonu olmasına rağmen yaygın olanları linear,sigmoid,tanh,relu , softmax ve binary step tir.

| Activation Func  | Equation                               | Derivative                             | Range   |
|------------------|----------------------------------------|----------------------------------------|---------|
| Sigmoid          | f(x) = 1 / (1 + e^(-x))                | f'(x) = f(x)(1 - f(x))                 | (0, 1)  |
| Tanh             | f(x) = (e^x - e^(-x)) / (e^x + e^(-x)) | f'(x) = 1 - f(x)^2                     | (-1, 1) |
| ReLU             | f(x) = max(0, x)                       | f'(x) = 1 (x > 0), 0 (x <= 0)          | [0, ∞)  |
| Leaky ReLU       | f(x) = x (x > 0), αx (x <= 0)          | f'(x) = 1 (x > 0), α (x <= 0)          | (-∞, ∞) |
| Softmax          | f(x_i) = e^(x_i) / Σ(e^(x_j))          | f'(x_i) = f(x_i)(1 - f(x_i))           | (0, 1)  |
| Softplus         | f(x) = log(1 + e^x)                    | f'(x) = 1 / (1 + e^(-x))               | (0, ∞)  |
| Binary Step      | f(x) = 1 (x >= 0), 0 (x < 0)           | f'(x) = 0                              | {0, 1}  |
| Linear           | f(x) = x                               | f'(x) = 1                              | (-∞, ∞) |
| Swish            | f(x) = x * sigmoid(x)                  | f'(x) = f(x) + sigmoid(x)              | (-∞, ∞) |
| ELU              | f(x) = x (x > 0), α(e^x - 1) (x <= 0)  | f'(x) = 1 (x > 0), αe^x (x <= 0)       | (-α, ∞) |
| SELU             | f(x) = λ * (x > 0 ? x : α(e^x - 1))    | f'(x) = λ * (1 (x > 0), αe^x (x <= 0)) | (-∞, ∞) |
| Piecewise Linear | f(x) = x (x > 0), 0 (x <= 0)           | f'(x) = 1 (x > 0), 0 (x <= 0)          | (-∞, ∞) |
| Gaussian         | f(x) = e^(-x^2)                        | f'(x) = -2x * e^(-x^2)                 | (0, 1)  |
| Sinusoidal       | f(x) = sin(x)                          | f'(x) = cos(x)                         | (-1, 1) |

---

## 1. Sigmoid
- **Fonksiyon:**  
  \( f(x) = \frac{1}{1 + e^{-x}} \)
- **Türev:**  
  \( f'(x) = f(x)(1 - f(x)) \)
- **Aralık:**  
  (0, 1)
- **Açıklama:**  
  Çıktıları 0 ile 1 arasında sıkıştırır. Özellikle olasılık gibi yorumlanan çıktılar için uygundur. Ancak büyük değerlerde "vanishing gradient" (kaybolan gradyan) sorununa neden olabilir.

---

## 2. Tanh (Hiperbolik Tanjant)
- **Fonksiyon:**  
  \( f(x) = \frac{e^x - e^{-x}}{e^x + e^{-x}} \)
- **Türev:**  
  \( f'(x) = 1 - f(x)^2 \)
- **Aralık:**  
  (-1, 1)
- **Açıklama:**  
  Sigmoid'e benzer ama çıktılar -1 ile 1 arasındadır. Bu, verinin merkezlenmesini sağlar ve öğrenmeyi hızlandırabilir.

---

## 3. ReLU (Rectified Linear Unit)
- **Fonksiyon:**  
  \( f(x) = \max(0, x) \)
- **Türev:**  
  \( f'(x) = 1 \ (x > 0), \ 0 \ (x \leq 0) \)
- **Aralık:**  
  [0, ∞)
- **Açıklama:**  
  Pozitif değerleri geçirir, negatifleri sıfıra kırpar. Hesaplaması basittir ve derin ağlarda çok etkilidir. Ancak negatif değerler için "ölü nöron" problemi oluşabilir.

---

## 4. Leaky ReLU
- **Fonksiyon:**  
  \( f(x) = \begin{cases} x, & x > 0 \\ \alpha x, & x \leq 0 \end{cases} \)
- **Türev:**  
  \( f'(x) = \begin{cases} 1, & x > 0 \\ \alpha, & x \leq 0 \end{cases} \)
- **Aralık:**  
  (-∞, ∞)
- **Açıklama:**  
  ReLU'nun geliştirilmiş halidir. Negatif değerler için küçük bir eğim (α) verir, böylece ölü nöron sorununun önüne geçilir.

---

## 5. Softmax
- **Fonksiyon:**  
  \( f(x_i) = \frac{e^{x_i}}{\sum_j e^{x_j}} \)
- **Türev:**  
  \( f'(x_i) = f(x_i)(1 - f(x_i)) \)
- **Aralık:**  
  (0, 1)
- **Açıklama:**  
  Çıktıları 0 ile 1 arasında normalize eder ve hepsinin toplamı 1 olur. Çok sınıflı sınıflandırma problemlerinde kullanılır.

---

## 6. Binary Step
- **Fonksiyon:**  
  \( f(x) = \begin{cases} 1, & x \geq 0 \\ 0, & x < 0 \end{cases} \)
- **Türev:**  
  \( f'(x) = 0 \)
- **Aralık:**  
  {0, 1}
- **Açıklama:**  
  Bir eşiğe göre karar verir. Ancak türevinin sıfır olması nedeniyle geriye yayılım (backpropagation) için uygun değildir.

---

## 7. Linear
- **Fonksiyon:**  
  \( f(x) = x \)
- **Türev:**  
  \( f'(x) = 1 \)
- **Aralık:**  
  (-∞, ∞)
- **Açıklama:**  
  Doğrusal bir dönüşümdür. Ancak doğrusal aktivasyonlar, ağın karmaşık öğrenme yapmasını engeller.

---

## 8. Swish
- **Fonksiyon:**  
  \( f(x) = x \times sigmoid(x) \)
- **Türev:**  
  \( f'(x) = f(x) + sigmoid(x) \)
- **Aralık:**  
  (-∞, ∞)
- **Açıklama:**  
  Google tarafından önerilmiştir. Özellikle derin sinir ağlarında iyi sonuçlar verir.

---

## 9. ELU (Exponential Linear Unit)
- **Fonksiyon:**  
  \( f(x) = \begin{cases} x, & x > 0 \\ \alpha(e^x - 1), & x \leq 0 \end{cases} \)
- **Türev:**  
  \( f'(x) = \begin{cases} 1, & x > 0 \\ \alpha e^x, & x \leq 0 \end{cases} \)
- **Aralık:**  
  (-α, ∞)
- **Açıklama:**  
  ReLU gibi çalışır ama negatif değerlerde de küçük çıkışlar verir. Böylece ağırlıkların sıfıra saplanmasını önler.

---

## 10. SELU (Scaled Exponential Linear Unit)
- **Fonksiyon:**  
  \( f(x) = \lambda \times \begin{cases} x, & x > 0 \\ \alpha(e^x - 1), & x \leq 0 \end{cases} \)
- **Türev:**  
  \( f'(x) = \lambda \times \begin{cases} 1, & x > 0 \\ \alpha e^x, & x \leq 0 \end{cases} \)
- **Aralık:**  
  (-∞, ∞)
- **Açıklama:**  
  Özellikle derin sinir ağlarında "self-normalizing" (kendi kendine normalleşen) özellik gösterir. Böylece ağı daha stabil hale getirir.

---

## 11. Piecewise Linear
- **Fonksiyon:**  
  \( f(x) = \begin{cases} x, & x > 0 \\ 0, & x \leq 0 \end{cases} \)
- **Türev:**  
  \( f'(x) = \begin{cases} 1, & x > 0 \\ 0, & x \leq 0 \end{cases} \)
- **Aralık:**  
  (-∞, ∞)
- **Açıklama:**  
  ReLU ile çok benzerdir. Sınırlı doğrusal bir yapı sunar.

---

## 12. Gaussian
- **Fonksiyon:**  
  \( f(x) = e^{-x^2} \)
- **Türev:**  
  \( f'(x) = -2x \times e^{-x^2} \)
- **Aralık:**  
  (0, 1)
- **Açıklama:**  
  Girdi değerini bir Gauss eğrisine göre dönüştürür. Belirli uygulamalarda kullanılır.

---

## 13. Sinusoidal
- **Fonksiyon:**  
  \( f(x) = \sin(x) \)
- **Türev:**  
  \( f'(x) = \cos(x) \)
- **Aralık:**  
  (-1, 1)
- **Açıklama:**  
  Girdiyi sinüs fonksiyonuna göre değiştirir. Özellikle periyodik verilerle çalışırken kullanışlıdır.

---

## 14. Softplus
- **Fonksiyon:**  
  \( f(x) = \log(1 + e^x) \)
- **Türev:**  
  \( f'(x) = \frac{1}{1 + e^{-x}} \)
- **Aralık:**  
  (0, ∞)
- **Açıklama:**  
  ReLU'nun yumuşatılmış versiyonudur. Negatif değerlerde de küçük bir çıkış verir. Bu, "ölü nöron" sorununu azaltır.

---

## 15. Swish
- **Fonksiyon:**  
  \( f(x) = x \times \text{sigmoid}(x) \)
- **Türev:**  
  \( f'(x) = f(x) + \text{sigmoid}(x) \)
- **Aralık:**  
  (-∞, ∞)
- **Açıklama:**  
  Google tarafından önerilen bir aktivasyon fonksiyonudur. Derin sinir ağlarında iyi sonuçlar verir. Özellikle derin öğrenme uygulamalarında kullanılır.

---

## 16. Gaussian
- **Fonksiyon:**  
  \( f(x) = e^{-x^2} \)
- **Türev:**  
  \( f'(x) = -2x \times e^{-x^2} \)
- **Aralık:**  
  (0, 1)
- **Açıklama:**  
  Girdi değerini bir Gauss eğrisine göre dönüştürür. Belirli uygulamalarda kullanılır.

---

## 17. Sinusoidal
- **Fonksiyon:**  
  \( f(x) = \sin(x) \)
- **Türev:**  
  \( f'(x) = \cos(x) \)
- **Aralık:**  
  (-1, 1)
- **Açıklama:**  
  Girdiyi sinüs fonksiyonuna göre değiştirir. Özellikle periyodik verilerle çalışırken kullanışlıdır.

---

## Perceptron Öğrenme Kuramı
* petceptron öğrenme lagoritmasnın amaco poizitif girdileri ve negatif girrdileri doğru sınıflandırabilen bir karar sınırı oluşturmaktır.

## Perceptron Öğrenme Kuramında kullanılan parametreler
* Bias: çıktı değerini kontrol edebilmeyi sağlayan sabit dğerdir. bütün girdiler sufur olduğunda sürecin hala devam edebilmesini de sğalar
* bias değeri aktivasyon fonksiyonunu sağa veya sola ötelenmesini shift sağlar
* learning rate öğrenme oranıu olarka bilinir daha sonra ayrıntıları ile anlatılacak.

## Perceptron Öğrenme Algoritması
* **1. Başlatma**  
  - Ağırlıklar (w) ve bias (b) küçük rastgele değerlerle veya sıfırla başlatılır.
* **2. Girdi Seçimi**  
  - Eğitim veri setinden bir giriş örneği (x) seçilir.  
  - Bu örneğin doğru çıktısı (y) biliniyor olmalıdır.
* **3. Çıktıyı Hesaplama**  
  - Girdi ve ağırlıklar çarpılarak bir toplam hesaplanır:  
    z = (w . x) + b  
  - Aktivasyon fonksiyonu uygulanır (genellikle Binary Step fonksiyonu):  
    Eğer z >= 0 ise tahmin edilen çıktı (y^) = 1,  
    Eğer z < 0 ise tahmin edilen çıktı (y^) = 0.
* **4. Hata Hesaplama**  
  - Gerçek çıktı (y) ile tahmin edilen çıktı (y^) arasındaki hata hesaplanır:  
    Hata = y - y^
* **5. Ağırlık ve Bias Güncelleme**  
  - Eğer hata sıfır değilse, ağırlıklar ve bias güncellenir:  
    w = w + (öğrenme oranı × hata × x)  
    b = b + (öğrenme oranı × hata)
* **6. Tüm Veriler İçin Tekrarlama**  
  - Tüm eğitim verileri üzerinde bu işlem adım adım uygulanır.  
  - Eğer hata yapan örnek kalmazsa veya maksimum epoch sayısına ulaşılırsa durulur.
* **7. Modelin Eğitimi Tamamlanır**  
  - Eğitim bittiğinde perceptron, verilen verileri doğru şekilde sınıflandırmayı öğrenmiş olur.


# Çok Katmanlı Yapay Sinir Ağları
* tek katmanlı yapay sinitr ağları lineer problemlerde etkili çözümler sunabilmektedir
* ancak lineer olamayam pronlemdeler vea daha karmaşk problemlerlerde sıkıntı yaşanabilir
* Bu tip durumlarda giriş ve çıkış arasına gizli katmanlar ilave edilebilir.

# Hata fonkisyonu ( loss function )
* hata fonksiyonu modelin tahmin ettiği değer ile gerçek değer arasındaki farkı ölçen bir fonksiyondur
* yapay sinir ağı modellerinin veri seti üzerindeki basarısını bir ölçüsüdür
* amaç bu fonksiyon değerini sıfıra yaklaştırmaktır.

## Regression Loss Functions
* Regression loss functions are used for regression tasks, where the goal is to predict continuous values. The most common regression loss functions include:
* Mean Squared Error (MSE) , Mean Absolute Error (MAE), Huber Loss, Log-Cosh Loss, Quantile Loss, Poisson Loss, Kullback-Leibler Divergence (KL Divergence), R-squared Loss, and Smooth L1 Loss.
## Classificatiob Loss Functions
* Classification loss functions are used for classification tasks, where the goal is to predict discrete classes. The most common classification loss functions include:
* Binary Cross-Entropy Loss, Categorical Cross-Entropy Loss, Sparse Categorical Cross-Entropy Loss, Hinge Loss, Squared Hinge Loss, Kullback-Leibler Divergence (KL Divergence), Focal Loss, and Categorical Hinge Loss.

### Binary Cross-Entropy Loss
* Binary Cross-Entropy Loss, ikili sınıflandırma problemlerinde kullanılan bir kayıp fonksiyonudur. Modelin tahmin ettiği olasılık değerleri ile gerçek etiketler arasındaki farkı ölçer. Aşağıdaki formülle tanımlanır:

### Categorical Cross-Entropy Loss
* Categorical Cross-Entropy Loss, çok sınıflı sınıflandırma problemlerinde kullanılan bir kayıp fonksiyonudur. Modelin tahmin ettiği olasılık dağılımı ile gerçek etiketler arasındaki farkı ölçer. Aşağıdaki formülle tanımlanır:
* one-hot encoding ile etiketlenmiş veriler için kullanılır. ( görüntü işleme, doğal dil işleme gibi alanlarda yaygın olarak kullanılır. )

### Sparse Categorical Cross-Entropy Loss
* Sparse Categorical Cross-Entropy Loss, çok sınıflı sınıflandırma problemlerinde kullanılan bir kayıp fonksiyonudur. Ancak, etiketlerin tam sayı olarak temsil edildiği durumlarda kullanılır. Aşağıdaki formülle tanımlanır:
* etiketlerin label encoding olması gerekmektedir.
* Multiclass içni kullanılan kayıp fonksiyonudur.

### Hinge Loss / Çok sınıflı destek vektör makineleri
* Hinge Loss, destek vektör makineleri (SVM) gibi sınıflandırma algoritmalarında kullanılan bir kayıp fonksiyonudur. Modelin tahmin ettiği değer ile gerçek etiketler arasındaki farkı ölçer. Aşağıdaki formülle tanımlanır:
* Hinge Loss, genellikle ikili sınıflandırma problemlerinde kullanılır. Ancak, çok sınıflı sınıflandırma problemlerinde de kullanılabilir.

### Squared Hinge Loss
* Squared Hinge Loss, Hinge Loss'un karelenmiş versiyonudur. Modelin tahmin ettiği değer ile gerçek etiketler arasındaki farkı ölçer. Aşağıdaki formülle tanımlanır:
* Squared Hinge Loss, genellikle ikili sınıflandırma problemlerinde kullanılır. Ancak, çok sınıflı sınıflandırma problemlerinde de kullanılabilir.

### Focal Loss ( odak kaybı )
* Focal Loss, dengesiz veri setlerinde kullanılan bir kayıp fonksiyonudur. Modelin tahmin ettiği değer ile gerçek etiketler arasındaki farkı ölçer. Aşağıdaki formülle tanımlanır:
* Focal Loss, genellikle ikili sınıflandırma problemlerinde kullanılır. Ancak, çok sınıflı sınıflandırma problemlerinde de kullanılabilir.
* Genelde görüntü işlemede imbalance problemler için kullanılır

| Kayıp Fonksiyonu                 | Kullanım Alanı            | Açıklama                                                           |
|----------------------------------|---------------------------|--------------------------------------------------------------------|
| Binary Cross-Entropy             | İkili sınıflandırma       | İkili sınıflandırma problemlerinde kullanılır.                     |
| Categorical Cross-Entropy        | Çok sınıflı sınıflandırma | Çok sınıflı sınıflandırma problemlerinde kullanılır.               |
| Sparse Categorical Cross-Entropy | Çok sınıflı sınıflandırma | Etiketlerin tam sayı olarak temsil edildiği durumlarda kullanılır. | 
| Hinge Loss                       | Destek vektör makineleri  | İkili sınıflandırma problemlerinde kullanılır.                     | 
| Squared Hinge Loss               | Destek vektör makineleri  | Hinge Loss'un karelenmiş versiyonudur.                             | 
| Focal Loss                       | Dengesiz veri setleri     | Dengesiz veri setlerinde kullanılır.                               |


# Optimizasyhon Algoritmaları
* burada lsos fonksiyonun minimize etmek için en uygun 'w' ve 'b' değelerini bulmaya çalısıyoruz
* Gradyan inişi metodu, çok güclü ve çok genel optimizasyon metodudur.

## Gradient Descent ( Gradyan Azalama )
* gradyan azalma modelinde tastgele seçilmiş olan parametre değerleri ile global minimuma ulaşılmak hedeflenir.
* Avatantajları:
  * mimnumun noktaya kararlı bir yakınsama ypar
  * vektörleşmeyi verimli kullanabişir
  * hesaplama açısından verimlidir
* dezavatajları:
  * lokal minumum a düşebilşir
  * bütün dataeti kullandığından dolayı yavaş öprenir
  * sonuç olarak batch gradyan azalma küçük veri setlerinde mükemmel çalısabilmektedir.

## Stochastic Gradient Descent
* granya azalma gibidir ancak bunda tek bir örnemklem kullanılırç
* tek seçieln veriyle işlem yapıklıdğı için global min için kararlı değildir
* rasygeke paranetre katsayıları örnek üzerinde işlem yaptığından local minimaya düşme ihtimali daha düşüktür.
* avatanjalrı:
  * büyük veri setlerinde minimuma faha hızlı ulaşır
  * tek örbek üzerinde çaklıstığından hesaplama olarka hızlı
  * farklı rtasgele beriler sçerek işlem yağıtğı için ocal minimaya düşme ihtaimli azdır
* dezavatanları
  * mimum noktaya kararlı yakınsayama yapmaz

### MiniBatch Gradient Descent
* gradyan azalma ve stokastik gradyan azalma arasında bir yöntemdir.
* veri setini küçük parçalara böler ve her bir parçayı kullanarak gradyan azalma uygular.
* bu sayede hem gradyan azalma kadar kararlı bir yakınsama sağlar hem de stokastik gradyan azalma kadar hızlı çalışır.
* avantajları:
  * büyük veri setlerinde etkili bir şekilde çalışır
  * gradyan azalma kadar kararlı bir yakınsama sağlar
  * stokastik gradyan azalma kadar hızlı çalışır
* Dezavantajları:
  * mini batch boyutunu seçmek zor olabilir
  * mini batch boyutu çok küçükse gradyan azalma kadar kararlı bir yakınsama sağlam
  * mini batch boyutu çok büyükse stokastik gradyan azalma kadar hızlı çalışmaz
### Momentum
* Stokastik gradyan azalama ile kullanılan popüler bir tekniktir. 
* Amaç, gradyan azalma sürecini hızlandırmak ve daha kararlı hale getirmektir.
* Momentum, önceki gradyanların etkisini dikkate alarak güncellemeleri yapar.
* Bu sayede, gradyan azalma sürecinde "sarsıntıları" azaltır ve daha hızlı bir yakınsama sağlar.
* Momentum, gradyan azalma algoritmasına eklenen bir terimdir ve genellikle aşağıdaki formülle güncellenir:
  * v(t) = β * v(t-1) + (1 - β) * g(t)
  * w(t) = w(t-1) - α * v(t)
  * burada:
    * v(t): güncellenmiş gradyan
    * β: momentum katsayısı (genellikle 0.9)
    * g(t): mevcut gradyan
    * α: öğrenme oranı
    * w(t): güncellenmiş ağırlıklar
    * w(t-1): önceki ağırlıklar
    * t: iterasyon sayısı
    * momentum, önceki gradyanların etkisini dikkate alarak güncellemeleri yapar.
* avantajları:
  * gradyan azalma sürecini hızlandırır
  * daha kararlı bir yakınsama sağlar
  * lokal minimuma düşme ihtimalini azaltır
  * daha hızlı bir yakınsama sağlar
  * daha az iterasyon ile daha iyi sonuçlar elde edilir
* dezavantajları:
  * momentum katsayısını seçmek zor olabilir
  * çok büyük bir momentum katsayısı, gradyan azalma sürecini kararsız hale getirebilir
  * çok küçük bir momentum katsayısı, gradyan azalma sürecini yavaşlatabilir

## RMSE  Prop
* RMSE Prop, gradyan azalma algoritmasının bir varyasyonudur.
* Amaç, gradyan azalma sürecini hızlandırmak ve daha kararlı hale getirmektir.
* RMSE Prop, her bir ağırlık için ayrı ayrı gradyan hesaplar ve bu gradyanları kullanarak ağırlıkları günceller.
* Bu sayede, gradyan azalma sürecinde "sarsıntıları" azaltır ve daha hızlı bir yakınsama sağlar.
* RMSE Prop, gradyan azalma algoritmasına eklenen bir terimdir ve genellikle aşağıdaki formülle güncellenir:
  * w(t) = w(t-1) - α * (g(t) / √(v(t) + ε))
* Avantajları:
  * gradyan azalma sürecini hızlandırır
  * daha kararlı bir yakınsama sağlar
  * lokal minimuma düşme ihtimalini azaltır
  * daha hızlı bir yakınsama sağlar
  * daha az iterasyon ile daha iyi sonuçlar elde edilir
* Dezavantajları:
  * RMSE Prop algoritması, gradyan azalma algoritmasına göre daha karmaşık bir yapıya sahiptir.
  * Bu nedenle, daha fazla hesaplama gücü gerektirebilir.
  * RMSE Prop algoritması, gradyan azalma algoritmasına göre daha fazla bellek kullanabilir.
  * Bu nedenle, büyük veri setlerinde daha fazla bellek gerektirebilir.
  * RMSE Prop algoritması, gradyan azalma algoritmasına göre daha fazla bellek kullanabilir.

## Uyarlanabikir Gradyan Algoritması ( Adagrad )
* Adagrad, gradyan azalma algoritmasının bir varyasyonudur.
* Amaç, gradyan azalma sürecini hızlandırmak ve daha kararlı hale getirmektir.
* Adagrad, her bir ağırlık için ayrı ayrı gradyan hesaplar ve bu gradyanları kullanarak ağırlıkları günceller.
* Bu sayede, gradyan azalma sürecinde "sarsıntıları" azaltır ve daha hızlı bir yakınsama sağlar.
* Adagrad, gradyan azalma algoritmasına eklenen bir terimdir ve genellikle aşağıdaki formülle güncellenir:
  * w(t) = w(t-1) - α * (g(t) / √(v(t) + ε))
* NLP ve görüntü işleme gibi alanlarda yaygın olarak kullanılır.
* Avantajları:
  * gradyan azalma sürecini hızlandırır
  * daha kararlı bir yakınsama sağlar
  * lokal minimuma düşme ihtimalini azaltır
  * daha hızlı bir yakınsama sağlar
  * daha az iterasyon ile daha iyi sonuçlar elde edilir
* Dezavantajları:
  * Adagrad algoritması, gradyan azalma algoritmasına göre daha karmaşık bir yapıya sahiptir.
  * Bu nedenle, daha fazla hesaplama gücü gerektirebilir.
  * Adagrad algoritması, gradyan azalma algoritmasına göre daha fazla bellek kullanabilir.
  * Bu nedenle, büyük veri setlerinde daha fazla bellek gerektirebilir.
  * Adagrad algoritması, gradyan azalma algoritmasına göre daha fazla bellek kullanabilir.



## Adam Optimizasyon Algoritması
* Adam, gradyan azalma algoritmasının bir varyasyonudur.
* Amaç, gradyan azalma sürecini hızlandırmak ve daha kararlı hale getirmektir.
* Adam, her bir ağırlık için ayrı ayrı gradyan hesaplar ve bu gradyanları kullanarak ağırlıkları günceller.
* Bu sayede, gradyan azalma sürecinde "sarsıntıları" azaltır ve daha hızlı bir yakınsama sağlar.
* Momenta ve RMSProp algoritmalarının birleşimidir.
* Adam, gradyan azalma algoritmasına eklenen bir terimdir ve genellikle aşağıdaki formülle güncellenir:
  * m(t) = β1 * m(t-1) + (1 - β1) * g(t)
  * v(t) = β2 * v(t-1) + (1 - β2) * g(t)^2
  * w(t) = w(t-1) - α * (m(t) / √(v(t) + ε))
* Avantajları:
  * gradyan azalma sürecini hızlandırır
  * daha kararlı bir yakınsama sağlar
  * lokal minimuma düşme ihtimalini azaltır
  * daha hızlı bir yakınsama sağlar
  * daha az iterasyon ile daha iyi sonuçlar elde edilir
* Dezavantajları:
  * Adam algoritması, gradyan azalma algoritmasına göre daha karmaşık bir yapıya sahiptir.
  * Bu nedenle, daha fazla hesaplama gücü gerektirebilir.
  * Adam algoritması, gradyan azalma algoritmasına göre daha fazla bellek kullanabilir.
  * Bu nedenle, büyük veri setlerinde daha fazla bellek gerektirebilir.
  * Adam algoritması, gradyan azalma algoritmasına göre daha fazla bellek kullanabilir.

## Adadelta
* Adadelta, gradyan azalma algoritmasının bir varyasyonudur.
* Amaç, gradyan azalma sürecini hızlandırmak ve daha kararlı hale getirmektir.
* Adadelta, her bir ağırlık için ayrı ayrı gradyan hesaplar ve bu gradyanları kullanarak ağırlıkları günceller.
* Bu sayede, gradyan azalma sürecinde "sarsıntıları" azaltır ve daha hızlı bir yakınsama sağlar.
* Adadelta, gradyan azalma algoritmasına eklenen bir terimdir ve genellikle aşağıdaki formülle güncellenir:
  * w(t) = w(t-1) - α * (g(t) / √(v(t) + ε))

## Cordinate Descent
* gradyan azalma ile benzerlik gösterir
* ancak burada her bir parametre için ayrı ayrı gradyan hesaplanır
* her bir parametre için gradyan hesaplanır ve o parametre güncellenir
* bu işlem tüm parametreler için tekrarlanır
* bu yöntem genellikle yüksek boyutlu veri setlerinde kullanılır
* avantajları:
  * yüksek boyutlu veri setlerinde etkili bir şekilde çalışır
  * gradyan azalma kadar kararlı bir yakınsama sağlar
  * hesaplama açısından verimlidir
  * her bir parametre için ayrı ayrı gradyan hesaplandığı için daha az bellek kullanır
* dezavantajları:
  * lokal minimuma düşme ihtimali vardır
  * gradyan azalma kadar hızlı çalışmaz
  * her bir parametre için ayrı ayrı gradyan hesaplandığı için daha fazla işlem süresi alabilir

| Optimizasyon Yöntemi        | Açıklama                                           | Avantajları                                                  | Dezavantajları                            |
|-----------------------------|----------------------------------------------------|--------------------------------------------------------------|-------------------------------------------|
| Gradient Descent            | Tüm veri setini kullanarak gradyan hesaplar.       | Kararlı yakınsama sağlar.                                    | Büyük veri setlerinde yavaş çalışır.      |
| Stochastic Gradient Descent | Tek bir örnek kullanarak gradyan hesaplar.         | Hızlı çalışır, lokal minimuma düşme ihtimali azdır.          | Kararlı yakınsama sağlamaz.               |
| MiniBatch Gradient Descent  | Veri setini küçük parçalara böler.                 | Hızlı çalışır, kararlı yakınsama sağlar.                     | Mini batch boyutunu seçmek zor olabilir.  |
| Coordinate Descent          | Her bir parametre için ayrı ayrı gradyan hesaplar. | Yüksek boyutlu veri setlerinde etkili çalışır.               | Lokal minimuma düşme ihtimali vardır.     |
| Momentum                    | Önceki gradyanların etkisini dikkate alır.         | Hızlı yakınsama sağlar, lokal minimuma düşme ihtimali azdır. | Momentum katsayısını seçmek zor olabilir. |
| RMSE Prop                   | Her bir ağırlık için ayrı ayrı gradyan hesaplar.   | Hızlı yakınsama sağlar, lokal minimuma düşme ihtimali azdır. | Daha fazla hesaplama gücü gerektirebilir. |
| Adam                        | Her bir ağırlık için ayrı ayrı gradyan hesaplar.   | Hızlı yakınsama sağlar, lokal minimuma düşme ihtimali azdır. | Daha fazla hesaplama gücü gerektirebilir. |
| Adagrad                     | Her bir ağırlık için ayrı ayrı gradyan hesaplar.   | Hızlı yakınsama sağlar, lokal minimuma düşme ihtimali azdır. | Daha fazla hesaplama gücü gerektirebilir. |
| Adadelta                    | Her bir ağırlık için ayrı ayrı gradyan hesaplar.   | Hızlı yakınsama sağlar, lokal minimuma düşme ihtimali azdır. | Daha fazla hesaplama gücü gerektirebilir. |
| Cordinate Descent           | Her bir parametre için ayrı ayrı gradyan hesaplar. | Yüksek boyutlu veri setlerinde etkili çalışır.               | Lokal minimuma düşme ihtimali vardır.     |
| ----------------------      | ----------                                         | -------------                                                | ----------------                          |


## Karşılaştırma Tablosu
| Algoritma                   | Yakınsama hızı   | Bellek kullanımı | seyrek veri işleme | yerel min kurtulma   | hiperparametre hassasiyeti   | büyük veri kümeleri | öğrenme oranı   |
|-----------------------------|------------------|------------------|--------------------|----------------------|------------------------------|---------------------|-----------------|
| Gradient Descent            | Yavaş            | Yüksek           | Evet               | Evet                 | Düşük                        | Evet                | Düşük           |
| Stochastic Gradient Descent | Hızlı            | Düşük            | Evet               | Hayır                | Yüksek                       | Hayır               | Yüksek          |
| MiniBatch Gradient Descent  | Orta             | Orta             | Evet               | Hayır                | Orta                         | Evet                | Orta            |
| Coordinate Descent          | Orta             | Düşük            | Hayır              | Evet                 | Orta                         | Evet                | Orta            |
| Momentum                    | Hızlı            | Düşük            | Evet               | Hayır                | Yüksek                       | Hayır               | Yüksek          |
| RMSE Prop                   | Hızlı            | Düşük            | Evet               | Hayır                | Yüksek                       | Hayır               | Yüksek          |
| Adam                        | Hızlı            | Düşük            | Evet               | Hayır                | Yüksek                       | Hayır               | Yüksek          |
| Adagrad                     | Hızlı            | Düşük            | Evet               | Hayır                | Yüksek                       | Hayır               | Yüksek          |
| Adadelta                    | Hızlı            | Düşük            | Evet               | Hayır                | Yüksek                       | Hayır               | Yüksek          |


# Öğrenme Oranı Nedir?
* Öğrenme oranı, makine mğrenmesi algoritmalarında özellikle gradyan tabanlı optimizasyon algoritmalarında kiritk bir hiperparametredir.
  * Adım büyüklüğü kontrolü: Modelin parametrelerini ( örneğin, ağırlıklarını ve biaslarını ) her güncelleme adımında ne kadar değiştireceğimibelirler.
  * Gradyan Tepki,: Kayıp fonksiyonun gradyanına göre modelin ne kadar hızlı veya yavaş bir şeilde en iyi çözüme (öimiöıö kayıp ) doğru ilerleyeceği etkiler.
  * Küçük Değerler: küçük bir öğrenme oranu, modelin çok yavaş ve küçük aıdmlarla optimuma doğru ilerlemesine neden olur. Bu kararlılığı artrabilir ancak yakınsamayı yaaşlatabili ve çok sayıda iterasyn gerektirebilir.
  * Büyük değerler: modelin optimum noktasının üzerinden atlamasına veya kararsız bir şekiklde salınmasına yol açabikir. Bu hızlı başlangıc sağlayabikir ancak en iyi çözüme ulaşmayı engelleyebilir
  * hiperparametre ayarı: deneme yanılma veya otomatik yönltemlerle blulur. Model performansı üzerinde hassas nit etkiye sahiptir
  * Algoritma bağımlılığı: Farklı algoritamalr adaptif oalrka ayaralyanilir.

## Öğrenme oranı azalması ( Learning Rate Delay )
* Learning rate delay (öğrenme oranı azaltma), makine öğrenmesi ve derin öğrenme modellerinin eğitim sürecinde kullanılan bir tekniktir.
* Amaç: Öğrenme oranını zamanla azaltarak modelin daha iyi bir şekilde öğrenmesini sağlamak.
* Yöntemler:
  * Sabit oran: Öğrenme oranını sabit bir oranda azaltma.
  * Çarpanla azaltma: Öğrenme oranını belirli bir çarpanla azaltma.
  * Zaman tabanlı azaltma: Öğrenme oranını zamanla azaltma.
  * Erken durdurma: Modelin performansı belirli bir eşiğin altına düştüğünde öğrenme oranını azaltma.

## Dropout
* Dropout, derin öğrenme modellerinde aşırı öğrenmeyi (overfitting) önlemek için kullanılan bir tekniktir.
* Amaç, modelin genel performansını artırmak ve daha iyi genelleme yapabilmesini sağlamaktır.
* Dropout, eğitim sırasında rastgele olarak bazı nöronları "kapatarak" (drop) modelin daha sağlam hale gelmesini sağlar.
* Bu sayede, modelin belirli nöronlara aşırı bağımlı hale gelmesini önler.
* Dropout, genellikle aşağıdaki adımlarla uygulanır:
  * Eğitim sırasında, her bir nöronun belirli bir olasılıkla kapatılması (dropout oranı).
  * Kapatılan nöronlar, modelin güncellenmesi sırasında dikkate alınmaz.
  * Test sırasında, tüm nöronlar kullanılır ve dropout oranı ile çarpılır.
* Dropout oranı genellikle 0.2 ile 0.5 arasında bir değere ayarlanır.
* Dropout, derin öğrenme modellerinde yaygın olarak kullanılan bir tekniktir ve genellikle CNN (Convolutional Neural Network) ve RNN (Recurrent Neural Network) gibi modellerde kullanılır.

## Batch Normalization
* Batch Normalization, derin öğrenme modellerinde eğitim sürecini hızlandırmak ve daha kararlı hale getirmek için kullanılan bir tekniktir.
* Amaç, her bir katmanın giriş verilerini normalize ederek modelin daha hızlı ve kararlı bir şekilde öğrenmesini sağlamaktır.
* Batch Normalization, genellikle aşağıdaki adımlarla uygulanır:
  * Her bir mini batch için giriş verilerinin ortalamasını ve standart sapmasını hesaplama.
  * Giriş verilerini normalize etme (ortalama ve standart sapma ile bölme).
  * Normalize edilmiş verilere bir ölçekleme (scaling) ve kaydırma (shifting) işlemi uygulama.
* Eğitim sırasında, her bir mini batch için ortalama ve standart sapma değerleri güncellenir.
* Katman Girişlerini Normalleştirme, iç kovaryans kaymasıı azaltma.
* Daha hızlı yakınsama sağlar.
* Modelin genelliliği daha sağlam olur.

## Activity Regularization (Aktivite Düzenlileştirme)

* **Katman Çıktılarını Hedefleme:**  
  Activity regularization, sinir ağı içindeki katmanların aktivasyon (çıkış) değerlerini belirli bir düzeyde tutmayı amaçlayan bir düzenlileştirme yöntemidir.  
  Aşırı büyük aktivasyonlar modeli karmaşıklaştırabilir ve aşırı öğrenmeye (overfitting) neden olabilir. Bu yüzden aktivasyonların büyüklüğü kontrol altında tutulur.

* **L1 ve L2 Normları Uygulama:**  
  Aktivasyonların büyüklüğünü kontrol etmek için genellikle L1 ve L2 normları kullanılır:

  * **L1 Aktivite Düzenlileştirme (L1 Activity Regularization):**  
    - Aktivasyon değerlerinin mutlak değerlerinin toplamı minimize edilmeye çalışılır.  
    - Aktivasyonların sıfıra yakın olmasını teşvik eder.  
    - Daha seyrek (sparse) bir aktivasyon yapısı oluşturur, böylece sadece gerekli nöronlar aktif kalır.

  * **L2 Aktivite Düzenlileştirme (L2 Activity Regularization):**  
    - Aktivasyon değerlerinin karelerinin toplamı minimize edilir.  
    - Aktivasyonları çok büyümekten alıkoyar ama tamamen sıfıra zorlamaz.  
    - Aktivasyonların dengeli ve yumuşak kalmasını sağlar.

* **Özellik Seçimi Benzeri Bir Etki:**  
  - L1 düzenlileştirme, bazı nöronların aktivasyonunu tamamen sıfırlayarak, ağın yalnızca en önemli nöronları kullanmasını sağlar.  
  - Bu, adeta bir **özellik seçimi** (feature selection) gibi çalışır:  
    gereksiz nöronları devre dışı bırakır ve modelin daha sade, daha anlamlı bir yapı öğrenmesine yardımcı olur.
  - Özellikle veri setinde çok fazla gürültü (noise) veya gereksiz bilgi varsa, bu yöntem genel doğruluk üzerinde olumlu etkiler yaratabilir.

