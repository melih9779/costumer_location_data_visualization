<img width="640" alt="costumer location data visualization" src="https://user-images.githubusercontent.com/9290445/166223818-bf9ce70c-8685-400c-957e-6f613aaf994f.png">

# Proje Hedefi:
- Müşteri konumlarından elde edilen verinin görselleştirilmesi(Data visualization).
- Elde edilen görseller ile müşteri yoğunluğu çıkartılarak hedeflenen bölgelerin müşteri sıklığına göre negatif yoğunlukta kalan bölgelere özel kampanya planlanması.
- Farklı zamanlar ile alınan konumların karşılaştırılması.
- Farklı zamanlarda konum karşılaştırmaları ile baz alınan mesafe çevresinde Ağızdan ağıza pazarlama tahminleri

### Gerekli Python Paketleri
* pandas 
* geoplotlib

Yazıda örnek data kullanabilmek için IBB Açık Veri Portalından aldığım [Akaryakıt İstasyonları Veri Seti](https://data.ibb.gov.tr/dataset/akaryakit-istasyonlari/resource/5625860c-d79a-446f-898e-2aa2b9099bc8 "Akaryakıt İstasyonları Veri Seti")'ni kullandım.

<img width="779" alt="code_preview" src="https://user-images.githubusercontent.com/9290445/166224084-dfdd5b45-7365-41c6-8fe4-2d5f3ebc9b3c.png">
Farklı görselleştirme seçenekleri için bazı kısımları yorum satırı olarak ekledim.
Sonuç olarak aşağıda ekleyeceğim görseller Istanbulda bulunan akaryakıt istasyonlarının haritada yoğunluğunu görebilirsiniz. Bu konumları biz müşteri konumları gibi baz alabiliriz.

Müşteri yoğunluğuna göre aktifliğimizin az olduğu bölgeler özel reklam kampanyaları düzenlenebilir. Ek olarak yazının ilerleyen kısımlarında göstereceğim örnek görsellerde belli çaptaki konumlarda farklı zamandaki verileri karşılaştırıp aynı mahalle, aynı site içerisindeki konumların ağızdan ağıza pazarlama tahminleri yapılabilir.


Aşağıda oluşturduğum görselde yeşil konumları 2022, turuncuları 2021 datası gibi baz alanabilirsiniz. Konumları random örneklendirmek için oluşturdum gerçek konum verileri içermemektedir.

Belirli bir çaptaki müşterileri baz alarak zamana dayalı değişim yüzdelerini hesaplayabiliriz. Yoğun pazarlama gerçekleşmeyen bir bölgedeki mağaza veya online ticaret olan bi bölgede yakınındaki müşterilerinizin değişimini, müşterileriniz çok olduğu bölgeye ulaşılabilirliği arttırmak için ihtiyaç doğrultusunda fiziksel konum ile destekleme ve bölgedeki pazara özel çalışmalar yapılabilir. Sektör ve hizmetlere göre bir çok analiz ve pazarlamayı desteleyecek kurgular oluşturulabilir.

<img width="744" alt="maps_example" src="https://user-images.githubusercontent.com/9290445/166224080-459ea97f-be88-4d9b-8579-cee7ade4597f.png">
