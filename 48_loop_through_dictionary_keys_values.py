""" Looping through dictionary to get the keys and values both """


cars_details = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

for cars in cars_details.items():
    print(cars)



"""

Output :

('brand', 'Ford')
('model', 'Mustang')
('year', 1964)

"""