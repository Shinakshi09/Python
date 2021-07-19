"""

Printing the values of the dictionary
"""



cars_details = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}


for cars in cars_details:
    print(cars_details[cars])

"""

Output :

Ford
Mustang
1964

"""

"""

Printing the values of dict. using values method

"""

for cars in cars_details.values():
    print(cars)



