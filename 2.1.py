x = input('Name:')

print('Welcome, ' + x)

name = input("What is your company's name?")

feet = int(input('Enter # of feet of fiber optic needed?'))

if feet > 500:
  print(name)
  print(feet * 0.5)
elif feet > 250:
  print(name)
  print(feet * 0.7)

elif feet > 100:
  print(name)
  print(feet * 0.8)
  

