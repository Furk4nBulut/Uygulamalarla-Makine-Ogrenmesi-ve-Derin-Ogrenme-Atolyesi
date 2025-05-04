4 May 2025 Day 10

# RNN (Recurrent Neural Networks) , LSTM (Long Short-Term Memory) ve GRU (Gated Recurrent Unit) Nedir?
- RNN, LSTM ve GRU, sıralı veriler üzerinde çalışan derin öğrenme modelleridir.
# RNN (Recurrent Neural Networks)
- RNN(yinelemeli sinir ağı)  ,sıralı veriler üzerinde çalışan özel bir derşn öğrenme modelidir.
- önceki girdileri hatırlayarak ve bu bilgileri kullanrrak sonraki çıktıları tahmin edder
- bu sayede doğal dil işleme (metin çeviri, duygu analizi), konuşma tanıma ve zaman serisi analizi gibi alanlarda yaygın olarak kullanılır
- sıralı veriye okdaklanma: rnn ler metinler , esler gibi sırasal yapıa sahip verilerle çalışmya özel olarak tasarlanmıştır
- hafıza mekanızması: bu ağlar, önceki bilgileri bir tğr hafıza hücresinde saklar ve bu sayede uzun süreli bağımlılıkalr yakalayabilir
- geniş uygulama alanları: doğal dil işleme, makine çevirsi,duygu analizi,konuşma tanıma ve hatta müzik besteleme gibi birçok alanda kullanılır
- zaman serisi, metin serisi, ses gibi sıralı verilerle kullanılır
- aynı ağırlıkarla zaman içinde tekrar eden yaoılaar(ağ belleği gibi)
- matematiksel olarak: ht = tanh(W * xt + U * ht-1 + b)
- özetle rnn ler sıralı veriler üzerindeki karmaşık yapıları anlamak ve tahmin etmek için kullanılan güçlü bir araçtır


# LSTM
- lstm derin öğrenme alanında kullanılan özel bir rnn mimarisidir
- standart ileri beslemeli

neden lstm
- uzun vadeli bağımlılıklar
- sıralı veri işleem: zaman serisi...
- gradyan kaybolma problemi: lstm ler gelenbeksel rnn lerde görüken gradyan kaybolma pronlemine karşı dsha dirençlidir
lstm ler hücre adı verilen özel birimlerden oluşur. bu hücreler bilgiyi uzun süre saklayabilir ve geektiğinde bu bilgiyi kullanabilirlwr...
- forhget gate: hücredeki bilgilerin unutulup unutulmayacağına karar verir
- input gate: yeni bilgilerin hücreye eklenip eklenmeyeceğine karar verir
- output gate: hüzreden hangi bilginin çıkacağına karar verir

- doğal dil işleme, zaman serisi analizi,makine çevirisi gibi birçok alanda kullanılır
- özetle , lstm uzun süreli bağımlılıkları öğrenebilen ve sırlı verileri işşleyebilen güçlü bir derin öğrenme modelidir. doğal dil işleme, zaman serisi analizi ve diğer sıralı veri uygulamalarında yaygın olarak kullanılır
- lstmler rnn lerin gelişmiş bir versiyonudur ve sıralı veriler üzerinde daha iyi performans gösterirler
- uzun süreli modellemek etkilidir
- çeşitli alanlarda yaygın olarak kullanılır

# GRU
- gru, derin öğrenme alanında kullanılan , özellikle sırlaı verieler üzerinde çalışan bir rnn türüdür
- lstm ile benzer işlevlere sahip olsa da , daha basit yapıya sahiptir
-lstm e göre daha basit yapı:  daha az parametreye sahip oludüüu için daha hızlı eğitilir
- uzun vadeli bağımlılıkları yakalama: lstm gibi uzun vadeli bağımlılıklaı öprenme konusunda başarılıdırüü
- gradyan ...
- hru iki geriş kapısı vardır: güncelleme ve sıfırlama kapıları
- sıfıtlsms geçidi: bu geçit, önceki gizli durumun ne jadarını yeni bilfgilere göre gğncelleyeceine karar verr
- güncelleme kapısı: yeni bilgilerin ne kadarının mevcut gizli duruma eklenip eklenmeyeceğine karar verir
- bu ikigeçit sayesinde  , gru lar hangi ilgileri hatırlayacakalrına ve hangi bilgileri unutacaklarına dah iyi karar verirler
- kullanı  alanları : doğal dil işleme, zaman serisi analizi, konuşma yanıma ve diğer sıralı veri uygulamaları
- lstm ile;
- bezerlikler: ikisi de sıralı veriler üzeride çalışır, uzun vadeli bağımlılıkları yakalayabilir
- farklılıklar: gru , lstm e göre daha az parametre için hızlı. ancak duruma göre değişir
- özetle,  gru sıralı veriler üzerinde çalışan ve uzun vadeli bağımlılıkları yakalayabilen güçlü bir derin öğrenme modelidir. lstm e göre daha basit yapıya sahiptir ve daha hızlı eğitilir. doğal dil işleme, zaman serisi analizi ve diğer sıralı veri uygulamalarında yaygın olarak kullanılır

M RIK Projektdr Ads: EB6O4259 
RNN Varyantları 
a.Bidirectional RNN (Bi-RNN) .Veriyi hem ileri hem geri okur. ◦NLP gibi bağlamın önemli olduğu yerlerde kullanılır. • Yine de vanishing gradient e karşı LSTM kadar dayanıklı değildir. b. Deep RNN .RNN hücreleri katmanlar halinde üst üste konur. ◦Daha karmaşık örüntüler öğrenebilir ancak eğitim zordur. c. Echo State Networks (ESN) .RNNin ağırlıkları sabit bırakılır; sadece çıkış ağırlıkları öğrenilir. ◦Eğitim çok hızlıdir ama kapasitesi sınırlıdır. d. IndRNN (Independent RNN) ◦Her nöronun kendi ağırlıkları vardır, vanishing gradient problemi azaltılır. ◦Daha derin RNN'ler oluşturulabilir.


