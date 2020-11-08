#!/usr/bin/python
# coding=utf-8
import os


class BakiciMod:

    def __init__(self):
        self.uzantilarGrup = []
        self.konum = os.getcwd()
        self.konumunuz = "Konumunuz: " + self.konum

    def dosyalar_set(self):
        gelen_adres = raw_input("Kontrol edilecek dizin yolu giriniz: ")

        gelen_uzanti = raw_input("Aranacak dosya uzantısı: ")
        dosyalar = os.listdir(gelen_adres)

        for dosya in dosyalar:
            if dosya.endswith(gelen_uzanti):
                self.uzantilarGrup.append(dosya)

    def dosyalar_get(self):
        self.dosyalar_set()

        for bulunan_dosyalar in self.uzantilarGrup:
            print bulunan_dosyalar
