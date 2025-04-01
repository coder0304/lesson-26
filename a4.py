class dog:
    animal='dog'
def __init__(self,breed,color):
  self.breed=breed
  self.color=color
rodger=dog("Pug","Brown")
buzo=dog("Bulldog","black")
print('rodger details:')
print('rodger is a',rodger.animal)
print('breed: ',rodger.breed)
print('color: ',rodger.color)

print('\nbuzo details: ')
print('buzo is a',buzo.animal)
print('breed: ',buzo.breed)