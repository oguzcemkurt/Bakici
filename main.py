#!/usr/bin/python
import os
gelenAdres = raw_input("Dizin Yolu Giriniz: ")


gelenUzanti = raw_input("Uzanti Giriniz: ")
dosyalar = os.listdir(gelenAdres)

for dosya in dosyalar:
    if dosya.endswith(gelenUzanti):
        print dosya


