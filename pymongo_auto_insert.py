from ast import Delete
from tkinter import INSERT
import pymongo
from pymongo import mongo_client

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["Hawkeye"]
user_table = mydb["users"]

while True:

 print("Yapılacak İşlemi Seçin.")
 print("=======================")
 print("1.Insert")
 print("2.Delete")

 secim = input("Seçiminiz (1/2):")

 if secim == '1':
   Insert = input("Kaç adet veri girilmesini istersiniz? ")  
   for i in range(int(Insert)):
    mydict = { "email": "test_try@aaraskargo.com", "name": "Test_User", "password": "r=X2KM6+~w;Z)x{K", "rememberMe": "remember-me", "rol": "Customer" }
    x = user_table.insert_one(mydict)
    print(x)

 
 elif secim == '2':
   Delete = input("Kaç adet veri girilmesini istersiniz? ")  
   for i in range(int(Delete)):
    mydict = { "email": "test_try@aaraskargo.com", "name": "Test_User", "password": "r=X2KM6+~w;Z)x{K", "rememberMe": "remember-me", "rol": "Customer" }
    x = user_table.delete_one(mydict)
    print(x)

