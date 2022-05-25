import pymongo
from pymongo import mongo_client

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["OnurAkduman"]
kullanicilar_tablosu = mydb["kullanicilar"]
urunler_tablosu = mydb["urunler"]
sepet_urunleri_tablosu = mydb["sepet_urunleri"]
mesajlar_tablosu = mydb["mesajlar"]


insert = input("Kaç adet veri girilmesini istersiniz? ") 

for i in range(int(insert)):
 mydict = { "email": "denemetest@hotmail.com", "ad": "Ciguli", "sifre": "123123", "rememberMe": "remember-me", "rol": "musteri" }
 x = kullanicilar_tablosu.insert_one(mydict)

print(x)
