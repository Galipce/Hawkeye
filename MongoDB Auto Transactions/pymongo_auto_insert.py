import pymongo
from pymongo import mongo_client
import json

#Link of JSON File.

with open("Hawkeye.json") as Hawkeye:
  data=json.load(Hawkeye)

#The section where the database connection is located.
  
myclient = pymongo.MongoClient(data["ConnectingURL"])
mydb = myclient [data["DBName"]]
user_table = mydb[data["CollectionName"]]

#The section where transactions are made automatically.

while True:
 print("====================================")
 print("Select Action To Do.")
 print("====================================")
 print("1.Insert")
 print("2.Delete")
 print("3.Update")
 print("====================================")
 option = input("Your choice (1/2/3):")

 if option == '1':
   Insert = input("How many data do you want to insert? ")  
   for i in range(int(Insert)):
    mydict = { "email": "test_try@araskargo.com", "name": "Test_User", "password": "r=X2KM6+~w;Z)x{K", "rememberMe": "remember-me", "role": "Customer" }
    x = user_table.insert_one(mydict)
    print(x)

 elif option == '2':
   Delete = input("How many data do you want deleted? ")  
   for i in range(int(Delete)):
    mydict = { "email": "test_try@araskargo.com", "name": "Test_User", "password": "r=X2KM6+~w;Z)x{K", "rememberMe": "remember-me", "role": "Customer" }
    x = user_table.delete_one(mydict)
    print(x)
 
 elif option == '3':
   Update = input("How much would you like to update? ")  
   for i in range(int(Update)):
    myquery = { "password": "r=X2KM6+~w;Z)x{K", }
    newvalues = { "$set": { "password": "/fx;[JQ59tXmg7!x" } }
    x = user_table.update_one(myquery,newvalues)
    print(x)
