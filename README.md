Sesli Kitap Uygulaması <br>
Bu Python tabanlı uygulama, bir PDF dosyasındaki metni alır ve bu metni sese dönüştürerek bir sesli kitap oluşturur. Kullanıcılar basit bir grafik kullanıcı arayüzü (GUI) üzerinden PDF dosyasını seçebilir ve bu dosyanın içeriğini sesli dosya olarak kaydedebilir.

Özellikler <br>
PDF Okuma: Seçilen PDF dosyasındaki metni çıkarır.<br>
Metni Sese Çevirme: Çıkarılan metni Google Text-to-Speech (gTTS) kullanarak sese dönüştürür.<br>
Sesli Kitap Oluşturma: Metni bir MP3 dosyasına kaydeder ve sesli kitap olarak kullanılabilir hale getirir.<br><br>
Gereksinimler<br>
Bu uygulamayı çalıştırmak için aşağıdaki Python kütüphanelerine ihtiyacınız var:<br>

PyPDF2: PDF dosyalarını okumak için kullanılır.<br>
gTTS: Metni sese çevirmek için kullanılır.<br>
tkinter: Grafik kullanıcı arayüzü (GUI) oluşturmak için kullanılır.<br><br>
Bu kütüphaneleri yüklemek için aşağıdaki komutu çalıştırabilirsiniz:<br>

pip install PyPDF2 <br>
pip install gtts <br>
pip install tkinter <br>
Kullanım
Uygulamayı başlattıktan sonra, PDF Dosyası Seç butonuna tıklayın.<br>
Sesli kitap oluşturmak istediğiniz PDF dosyasını seçin.<br>
Uygulama, PDF dosyasındaki metni MP3 dosyası olarak kaydeder ve dosya otomatik olarak oynatılır.<br>
