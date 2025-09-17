bike = {'Bike Name':'Bullet','Engine capacity':'350cc','Price':'250000'}

#bike.clear()
bike2 = bike.copy()
print(bike2)
print(bike.get('Which brand','Key not found'))
print(bike['Price'])
print(bike.items())
print(bike.keys())
print(bike.pop('Price'))
print(bike.popitem())
bike.update({'Brand':'Royal Enfield'})
print(bike.values())