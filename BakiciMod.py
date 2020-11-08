#!/usr/bin/python
# coding=utf-8
import os


class BakiciMod:

    def __init__(self):
        self.uzantilarGrup = []
        self.konum = os.getcwd()
        self.konumunuz = "Konumunuz: " + self.konum

    def dosyalarSet(self):
        gelenAdres = raw_input("Kontrol edilecek dizin yolu giriniz: ")

        gelenUzanti = raw_input("Aranacak dosya uzantısı: ")
        dosyalar = os.listdir(gelenAdres)

        for dosya in dosyalar:
            if dosya.endswith(gelenUzanti):
                self.uzantilarGrup.append(dosya)

    def dosyalarGet(self):
        self.dosyalarSet()

        for bulunanDosyalar in self.uzantilarGrup:
            print bulunanDosyalar
