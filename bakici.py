#!/usr/bin/python
# coding=utf-8
import os
konum = os.getcwd();
print "Konumunuz: " + konum
gelenAdres = raw_input("Kontrol edilecek dizin yolu giriniz: ")


gelenUzanti = raw_input("Aranacak dosya uzantısı: ")
dosyalar = os.listdir(gelenAdres)

for dosya in dosyalar:
    if dosya.endswith(gelenUzanti):
        print dosya


