13 April 2025

6. Gün  
* Giriş ve Temel Kavramlar  
* Temel Lineer Regresyon  
* Çoklu Lineer Regresyon  
* Regresyonun İleri Teknikleri  

---

### Giriş ve Temel Kavramlar

#### Regresyon Analizi
* Regresyon analizi, bir bağımlı değişkenin (sonuç) bir veya daha fazla bağımsız değişkenle (girdiler) olan ilişkisini modellemeye yönelik bir istatistiksel tekniktir.  
* Değişkenler arasındaki ilişkiyi anlamak ve gelecekteki gözlemler için tahmin yapmak amacıyla kullanılır.  
* Ekonomi, finans, biyoloji, mühendislik, sosyal bilimler gibi birçok alanda uygulanır.  

---

#### Regresyon Temel Kavramlar
* **Bağımlı Değişken (y)**: Sonuç veya tahmin edilmek istenen değişken.  
  * Örnek: Ev fiyatları, satış rakamları.  
* **Bağımsız Değişken (x)**: Bağımlı değişkeni etkileyen faktörler.  
  * Örnek: Ev büyüklüğü, oda sayısı, lokasyon.  
* **Regresyon Modeli**:  
  \[
  y = \beta_0 + \beta_1 \cdot x_1 + e
  \]
  * \(\beta_0\): Sabit terim (intercept).  
  * \(\beta_1\): Regresyon/eğim katsayısı (slope).  
  * \(e\): Hata terimi (residual).  

---

#### Temel Kavramlar
* **Yapısal Veri**: Düzenli aralıklarla veya belirli bir formatta toplanan veriler.  
  * Örnek: Anket sonuçları, satış verileri.  
* **Zaman Serisi Verisi**: Zaman içinde belirli aralıklarla toplanan veri.  
  * Örnek: Aylık satışlar, günlük sıcaklıklar.  
* **Panel Veri**: Farklı birey veya birimlerin zaman içinde gözlemlendiği veri.  
  * Örnek: Ülkelerin yıllık büyüme oranları.  

---

#### R^2 (Determination Coefficient)
* **Açıklama**: R², modelin bağımlı değişkendeki varyansın ne kadarını açıkladığını gösterir. 0 ile 1 arasında bir değerdir.  
  * **1**: Model, bağımlı değişkendeki tüm varyasyonu açıklar.  
  * **0**: Model, bağımlı değişkendeki hiçbir varyasyonu açıklamaz.  
* **Kullanımı**: Yüksek R² değeri, modelin veriye iyi uyduğunu ve iyi bir tahmin yapabildiğini gösterir.  

---

#### MSE (Mean Squared Error)
* **Açıklama**: MSE, tahmin edilen değerler ile gerçek değerler arasındaki farkların karelerinin ortalamasını alır. Kare alma işlemi pozitif ve negatif hataları aynı şekilde cezalandırır ve büyük hataları daha fazla önemser.  
* **Kullanımı**: Daha düşük MSE değerleri, modelin daha doğru tahminler yaptığını gösterir. Ancak MSE'nin ölçüm bağımlı değişkenin birimine bağlı olduğundan, yorumlanması diğer metrikler ile birlikte yapılmalıdır.  

---

#### Root Mean Squared Error (RMSE)
* **Açıklama**: RMSE, MSE'nin kareköküdür. Gerçek ve tahmin edilen değerler arasındaki farkın ortalama büyüklüğünü verir.  
* **Kullanımı**: RMSE, MSE'nin birimiyle aynı birimi kullandığından, modelin tahmin doğruluğunu daha anlaşılır bir şekilde ifade eder.  

---

#### Mean Absolute Error (MAE)
* **Açıklama**: MAE, tahmin edilen değerler ile gerçek değerler arasındaki farkların mutlak değerlerinin ortalamasıdır.  
* **Kullanımı**: MAE, ortalama tahmin hatasını verir ve diğer metriklerle birlikte kullanıldığında modelin genel performansını değerlendirmek için kullanılır.  

---

#### Adjusted R^2
* **Açıklama**: Adjusted R², R²'yi düzeltilmiş bir şekilde ifade eder ve modeldeki bağımsız değişken sayısını da dikkate alır. Modeldeki gereksiz değişkenlerin etkisini azaltmak için kullanılır.  
* **Kullanımı**: Bağımsız değişken sayısı arttıkça R² değeri de artabilir. Bu nedenle Adjusted R² daha güvenilir bir performans ölçütü olarak kabul edilir.  

---

#### Genel Tablo
| Metrik         | Açıklama                                                                 | Kullanım                                                                                     |
|----------------|--------------------------------------------------------------------------|---------------------------------------------------------------------------------------------|
| R^2           | Modelin bağımlı değişkendeki varyansın ne kadarını açıkladığını gösterir. | Yüksek R^2 değerleri, modelin veriye iyi uyduğunu gösterir.                                 |
| MSE           | Tahmin edilen değerler ile gerçek değerler arasındaki farkların karelerinin ortalamasını alır. | Daha düşük MSE değerleri, modelin daha doğru tahminler yaptığını gösterir.                  |
| RMSE          | MSE'nin kareköküdür. Gerçek ve tahmin edilen değerler arasındaki farkın ortalama büyüklüğünü verir. | RMSE, MSE'nin birimiyle aynı birimi kullandığından, modelin tahmin doğruluğunu daha anlaşılır bir şekilde ifade eder. |
| MAE           | Tahmin edilen değerler ile gerçek değerler arasındaki farkların mutlak değerlerinin ortalamasıdır. | MAE, ortalama tahmin hatasını verir ve diğer metriklerle birlikte kullanıldığında modelin genel performansını değerlendirmek için kullanılır. |
| Adjusted R^2  | R^2'yi düzeltilmiş bir şekilde ifade eder ve modeldeki bağımsız değişken sayısını dikkate alır. | Modeldeki gereksiz değişkenlerin etkisini azaltmak için kullanılır.                         |

---

## Multiple Linear Regression (Çoklu Lineer Regresyon)
* Y = \(\beta_0 + \beta_1 \cdot x_1 + \beta_2 \cdot x_2 + ... + \beta_n \cdot x_n + e\)
* **y**: Bağımlı değişken (tahmin etmek istediğimiz değişken).  
* **β₀**: Sabit terim (kesişim noktası).  
* **β₁, β₂, ...**: Regresyon katsayıları (bağımsız değişkenlerin bağımlı değişken üzerindeki etkisini gösterir).  
* **x₁, x₂, ...**: Bağımsız değişkenler (tahmin etmek için kullandığımız değişkenler).  
* **e**: Hata terimi (modelin açıklayamadığı varyasyonu temsil eder).  

---

### Neden Çoklu Doğrusal Regresyon?
* **Karmaşık ilişkilerin analizi**: Birden fazla değişken arasındaki karmaşık ilişkileri modelleyerek daha iyi tahminler yapmamızı sağlar.  
* **Varyansın açıklanması**: Bağımlı değişkendeki varyansın büyük bir kısmını açıklayarak daha iyi bir model oluşturmanıza yardımcı olur.  
* **Karar verme**: Elde edilen sonuçlar sayesinde daha iyi kararlar vermemizi sağlar.  
* **Özetle**: Çoklu doğrusal regresyon, birden fazla bağımsız değişkenin bir bağımlı değişken üzerindeki etkisini anlamak ve tahmin yapmak için kullanılır. Bu sayede karmaşık ilişkileri modelleyerek daha iyi tahminler yapabiliriz.

