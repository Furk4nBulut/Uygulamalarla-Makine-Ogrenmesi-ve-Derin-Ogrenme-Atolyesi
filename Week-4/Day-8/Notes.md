# Deep Learning ( Derin Öğrenme ) Nedir?
* derin öğrenme ypaay sinir ağalrının haliyle yapay zekanı bir alt dalıdır
* aslında çok katmanlı yapay sinir ağlarına verilen isimdir.
* büyük miktarda veri ile çalışmak için ideal bir yapıdadır.
*şu anda ypay zeka ile ypaılan çalışmaların büyük bölümü derin ağlar ileyapılmaktadır.
* yapay sinir ağlarında olan epştşim öğrenme test gibi kavramların tamamı ve daha faszlası derin öğrenmeye transfer olmuştur
* makine öğrenmesinin büyük veri karsısındaki başarımınn istenilen seviyelerde omamasından dolayı 2010 yılından itibaren derin öğrenme ile ilgili çalışmalar hız kazanmıştır.

## Derin Öğrenme Teknik Meseleler
* derin öğrenme mimarisi bir yapay sinir ağıdır o yüzden bunları birbirine raki olarak değilde çok iyi bir gikrin dajice gelişirilmiş hali olarak tanımlamalı.
* klasik yapay sinir ağı giriş ve çıkış katmanları arasına 1 2 g,zli katman varken derin ağlarca bu  sayı binlerce onlarca seviyesinde olabilmektedir.
* gizi katmanların önemini kabaca anlatmak fgerkeirse 1 2 gizli katman kış ve insanu birbriniden ayırt wedevilrken biraz daha gizli katman koyduğunda kışların alt familyasını ayırt eder daha da eklersen cinslerini daha da eklersen türleri ayırtadebekirsin.
* ancak unutulmamalıdır ki her katman sistem kaynaklaru öin fazladan yüktür
* o yüzden katman dengelemesi iy yapılmalıdr
* katman sayısı artıkça performans kritine göre başarım artar gibi bir genelleme yoktur
* genel presibimz basit düşün basitle başla.
* tek bir doğru yoktur doğruya ulaşılabilecek bir çok yol vardır.

### Peki derin öğrenme için neden bu kadar beklendi
* a) yetersiz veri setleri
* b) birçok matematiksel hesala ve fonksi,yonun yetresiz kalması
* c) donanısal yetersizlikler ( düşük ram, düşük cpu dar veriyolları GPU)

## Derin öğrenme nasıl çalsıır?
* derin öğrenme bir çok katmanlı yapay sinir ağlarıdır
* giriş katmanı gizli katmanlar ve çıkış katmanı vard
geri besemeli olarka ağırlıkları geriye doğrı giderek değiştirlme yöneti ile çalısır
* ödül ceza yöntemine göre ağırlıklar değiştirlerek model dengelerinir
* diğer özelikleri yapay sinir ağları ile benzerlik göstermektedir.
* çok fazla hidden layer ( derinlik buradan geliyor ) bir yapay sinir ağıdır.
* ilk olarak rastgele ağırlıklar verilerek katmanlar oluştururlurç
* daha sonra gerçek veriler katmanlardan geçerek tahmin değerlerini ortaya çıakrır
* gerçek hedefler tahminlerle birlikte kayıp fonksyunna eklenerek bir akyıp ğunaı belirlenir ve bu kayıp puanına göre optimize edici fonksiyon ile ağrılıklar yeniden hesaplanur
* kayıp skorunu loss skorunu en düşük olduğu yere kadar işlemler tekrarlanır.

## Derin öğrenmede eğitim aşaması
* sıfıran öğrenme: ağırlıklar rastgele alnarak sıdıedan model eğitimi yspılır. Daha uzun eğitim zamanı gerektiri
* transfer learning bnenzer bir problemin çözümüne yönelik bir modelin mimarisi parametreleri ve ağırlıklarını kendi problemimizin çözümü için aktarılması udurmudur7
* özellik çıkarımı sınıflandırma regreasyon amaçlar aolmadan sadece verisetine ait özelik çıkarma işlemidir.

## Bazı derin öğrenme mimarileri
* CNN: Convolutional Neural Network
* RNN: Recurrent Neural Network
* LSTM: Long Short Term Memory
* GAN: Generative Adversarial Network
* VAE: Variational Autoencoder
* Transformer
* BERT: Bidirectional Encoder Representations from Transformers
* GPT: Generative Pre-trained Transformer

# Convolution ( Evrişim ) Nedir?
* matematikte ve özellike fonksiyonel analizde konvolüsyon ya da evrişim bir fonksiyon şeklinin başka fonksiyon tarafından nasıl modifiye edildiğini göster  bir integral işlemdir. bi f ile fonksiyonun konvolüsoynu .(f*g) ile gösteririz.
* Convolution * ile ifade edilir.

## Kernel and Filter
* görüntü işlemede kerneller convolution blur işlemi edge işlemleri ve keskinleştirme gibi işlemler için kullanılan matrislerdir.
* Genellikle 3x3, 5x5, 7x7 gibi matrisler şeklinde kullanılır.

# Convolutional Neural Network ( CNN ) Nedir?
* Convolutional Neural Network (CNN) bir tür derin öğrenme mimarisidir.
* genellikle örüntü işleme işlemlerinde kullanul bir ferin öğrenme modelimidr
* konvolüsyon evrişim katmanları ile çalışır.

## Genel CNN Mimarisi
* CNN mimarisi genellikle aşağıdaki katmanları içerir:
  * Giriş Katmanı: Görüntü verisinin alındığı katmandır.
  * Konvolüsyon Katmanı: Görüntü üzerinde konvolüsyon işlemi yaparak özellik haritaları oluşturur.
  * Aktivasyon Katmanı: Genellikle ReLU (Rectified Linear Unit) gibi aktivasyon fonksiyonları kullanılır.
  * Havuzlama Katmanı: Özellik haritalarını boyutlandırmak ve önemli bilgileri korumak için kullanılır.
  * Tam Bağlantılı Katman: Sonuçları sınıflandırmak için kullanılır.
  * Çıkış Katmanı: Son sınıflandırma sonuçlarını verir.

### Genel CNN Mimarisi ( Instructor notes )
* Convolution Layer - özellik çıkarma için kullanılır
* non-linearity - sisteme doğrusal olmayanlığın tanıtılması için kullanılır. aktivasyon fonksiyonları kullanılır
* pooling (downsampling) layer - ağırlık sayısını azaltır ve uygunluğu kontrol edr
* flattening layer - klasik sinir ağı için veirleri hazrlar. matris alır ve vektöre çevirir
* fully connected layer - sınıflandırmada kullanılan standart sinir ağı

## Convolution Layer
* konvolüsyon katmanı, görüntü üzerinde kaydırılan bir filtre (kernel) kullanarak özellik haritaları oluşturur.
* görüntüye ayırt edici özellikler çıkarabilmek için filtrefeer uygulanır
* bu filtreleri uygulanken matris çarpımı yerine matematikteki evrişim convolution işlemi uygulanır
* uygulnan filtrenin sonuna ortaya çıkar tabloya Feature map adı verilir
* CNN'in temel yapı taşını oluşturur.

## Non-linearity ( Aktivasyon Fonksiyonları )
* bu katman aktivasyon aktmanı olarak tanımlanır
* hyapay sinir ağlarında kullanılan tanh sigmiod relu vb birçok aktivason fonksiyonaları bu katmanda kullanılmaktadır
* önceki yıllarda tanh ve sigmoid kullanısalda günümüzse relu ve türevleri kullanılmaktadır
* bunun en büyük sebeibi relu nun performans olarak diğer aktivasyon fonksiyonlarında daha hızlı çalışmasıdırç
* Relu Fonksiyonu: f(x) = max(0, x)

## Pooling Layer - Havuzlama Katmanı
* havuzlama katmanı, özellik haritalarını boyutlandırmak ve önemli bilgileri korumak için kullanılır.
* Convolution layerdan sonra sıkla eklenen bir katmandır
* amacı vonvolution layerden sonra oluşan tabloyu özgün bir şekilde minimize etkmektedir
* yani gerkesiz özellikler yok sayılır ve işlem gücünden tasarıf sağlanır
* en çok kullanılan pooling max pooling dir
* max pooling belirlenen sizeleradki matrislere denk gelen kısımlardaki en büyük sayıyı bulup başka bir tabloya işlemektedir
* max pooling dışında average pooling ve min pooling gibi havuzlama türleri de vardır

## Flattening Layer - Düzleştirme Katmanı
* matris in vektörleştirildiği yani düzleştirildiği katmandır
* bu katmanın görevi sonraki katmanda olan fully connect yapay sinir ağına işleyebbilecğei veriler oluşturmakır
* yapay sinir ağı yapısı gereği tek boyutlu dizlilerle yani vektörlerle çalısır
* bu katman matris olarak glen veriler düzleştirerek vektör haline getirip bir sobraki katmana hazır hale getirir.

## Fully Connected Layer - Tam Bağlantılı Katman
* mimarinin son bölümüdür
* bu bölüm klasik yapay sinir ağında oluşmuştur
* en son layer ı vcalssification yapılan kısmdır
* dropout ve batch normalization fully connect layer da uygulanmaktadır
* genellikle son aşamasında aktivasyon fonkisyonu olarak softmax uygulanmaktadır.

### Dropout
* bazrn fully connect bölümü moldei overfitting olmaya zorlar
* bunu önüne geçemk için bazı bağlantıarın unutuup ağın yeibden eğitilmesi gerekbilir
* dropput ile bazı bağklantılar silinir ve fully connect özelliği kaldırılır
* bu tip durumlarda dropout kullanılır
* fine tning için 0.5 ten başlayarak yaval yaval değer azakktılabilir
* sistem stabil olduğunda değer azaltması durdurulur.

### Batch Normalization
* batch normalization, her bir katmanın çıktısını normalize ederek ağı daha hızlı ve daha stabil hale getirir.
* aslında verielr preprocesisng sürecinde normlize edelir
* ancak conv sürecinde dağılm bozukluğu olabilir bu da eğtiim huzu ve kararlığını etkileyebilir
* fully connect bölümünde batch normlization işlemi ile veriler yeniden dengeli hale getireileiblir
* bu işlem sistemin öğrenme hızını ve stabilitesini olumlu yönde etkilemektedir
* kullanıldığında loss değerlribin düstüğ ügözlemlenmiştir
