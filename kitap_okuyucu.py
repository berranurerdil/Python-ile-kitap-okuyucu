import PyPDF2  # PDF dosyalarını okumak için kullanılan kütüphane
from gtts import gTTS  # Metni sese çevirmek için kullanılan kütüphane
import os  # İşletim sistemi ile ilgili işlemler için kullanılan kütüphane
import tkinter as tk  # GUI (Grafik Kullanıcı Arayüzü) oluşturmak için kullanılan kütüphane
from tkinter import filedialog  # Dosya seçme penceresi oluşturmak için kullanılan modül

# PDF dosyasını okumak için bir fonksiyon tanımlıyoruz
def pdf_reader(filename):
    metin = ""  # PDF'den çıkarılan metnin saklanacağı değişken
    pdf_reader_filename = PyPDF2.PdfReader(open(filename,'rb'))  # PDF dosyasını açıp, bir PdfReader nesnesi oluşturuyoruz

    # PDF'in her sayfasını okuyarak, metin değişkenine ekliyoruz
    for i in range(len(pdf_reader_filename.pages)):
        metin += pdf_reader_filename.pages[i].extract_text()
    
    return metin  # Çıkarılan metni döndürüyoruz


def pdf_sound_convert(metin, speaker):
    # Metni sese çevirmek için bir Google Text-to-Speech (GTTS) nesnesi oluşturuyoruz
    speech = gTTS(text=metin, lang='tr')

    # Sese çevrilen metin dosyasına kaydediyoruz
    filename = f"{speaker}.mp3"
    speech.save(filename)
    
    return filename  # Dosya adını döndürüyoruz

def pdf_sec():
    file_path = filedialog.askopenfilename(filetype=[("PDF Dosyaları","*pdf")])
    if file_path:
        pdf_metin = pdf_reader(file_path)
        mp3_file = pdf_sound_convert(pdf_metin, "kaydet")  # "kaydet" olarak kaydediliyor
        os.system(f"Start {mp3_file}")  # Dosyanın açılması


# Tkinter ile GUI (Grafik Kullanıcı Arayüzü) oluşturuyoruz

app = tk.Tk()
app.title("Sesli Kitap Uygulaması")
app.geometry("250x150")


pdf_buton = tk.Button(app, text="PDF Dosyası Seç", command=pdf_sec, padx=20, pady=20)
pdf_buton.pack(pady=20)


app.mainloop()