# a = {'a': '1', 'b': '2', 'c': '3'}
# for key,value in a.items():
#        print(key+':'+value)


#-*- encoding=utf-8 -*-
import requests

url = "https://client.raysync.cloud/raysync/api/auth/login"
my_login = {"username":"test_gc","password":"pdLQRYEwePDdW2AJ85rKpMaoZ4q9vk50VYNWynXByxQGObvk6L10V9zN3ljmoOP5","loginType":1}
my_hearders = {"Content-Type": "application/json",
            "Authorization": "Bearer "}
response2 = requests.post(url,json=my_login,headers = my_hearders)

# print("test_json:",response2.json())
# print("test_code:",response2.status_code)

a = response2.json()

print("-"*100)
for key,value in a.items():
    print(key,":",value)

print("-"*100)
list = [{"username":"test_gc","age":"18"},{"username":"test_gy","age":"30"}]
list1 = sorted(list,key=lambda i:i['age'],reverse=True)
print(list1)