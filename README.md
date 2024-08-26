Sesli Kitap Uygulaması <br>
Bu Python tabanlı uygulama, bir PDF dosyasındaki metni alır ve bu metni sese dönüştürerek bir sesli kitap oluşturur. Kullanıcılar basit bir grafik kullanıcı arayüzü (GUI) üzerinden PDF dosyasını seçebilir ve bu dosyanın içeriğini sesli dosya olarak kaydedebilir.

Özellikler
PDF Okuma: Seçilen PDF dosyasındaki metni çıkarır.
Metni Sese Çevirme: Çıkarılan metni Google Text-to-Speech (gTTS) kullanarak sese dönüştürür.
Sesli Kitap Oluşturma: Metni bir MP3 dosyasına kaydeder ve sesli kitap olarak kullanılabilir hale getirir.
Gereksinimler
Bu uygulamayı çalıştırmak için aşağıdaki Python kütüphanelerine ihtiyacınız var:

PyPDF2: PDF dosyalarını okumak için kullanılır.
gTTS: Metni sese çevirmek için kullanılır.
tkinter: Grafik kullanıcı arayüzü (GUI) oluşturmak için kullanılır.
Bu kütüphaneleri yüklemek için aşağıdaki komutu çalıştırabilirsiniz:

bash
Kodu kopyala
pip install PyPDF2 gTTS tkinter
Kullanım
Uygulamayı başlattıktan sonra, PDF Dosyası Seç butonuna tıklayın.
Sesli kitap oluşturmak istediğiniz PDF dosyasını seçin.
Uygulama, PDF dosyasındaki metni MP3 dosyası olarak kaydeder ve dosya otomatik olarak oynatılır.
