#!/usr/bin/python
import os
gelenAdres = input("Path Giriniz: ")
gelenUzanti = input("Uzanti Giriniz: ")
dosyalar = os.listdir(gelenAdres)

for dosya in dosyalar:
    if dosya.endswith(gelenUzanti):
        print dosya

