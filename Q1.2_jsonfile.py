import json
dictionary= {"Assam":"Dispur"
             ,"Goa"  : "Panaji", 
             "Bihar":"Patna",
             "Madhya Pradesh":"Bhopal",
             "Manipur":"Imphal",
             "Rajasthan":"Jaipur",
            "UttaraKhand":"Dehradun"}
print(type(dictionary))
with open("captials.json","w") as outfile:
 json.dump(dictionary,outfile)
 print("print successfully")