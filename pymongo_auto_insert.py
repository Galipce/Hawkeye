import pymongo
from pymongo import mongo_client

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["Hawkeye"]
user_table = mydb["users"]

while True:
 print("====================================")
 print("Select Action To Do.")
 print("====================================")
 print("1.Insert")
 print("2.Delete")
 print("3.Delete")

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

