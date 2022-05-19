'''
Unit converter: Miles and Kilometers
'''

def print_menu():
     print('1. Kilometers to Miles')
     print('2. Miles to Kilometers')
     print('3. Kilograms to Pounds')
     print('4. Pounds to Kilograms')
     print('5. Celsius to Fahrenheit')
     print('6. Fahrenheit to Celsius')
     
def km_miles():
     km = float(input('Enter distance in kilometers: '))
     miles = km / 1.609
     print('Distance in miles: {0}'.format(miles))
     
def miles_km():
     miles = float(input('Enter distance in miles: '))
     km = miles * 1.609
     print('Distance in kilometers: {0}'.format(km))

def kg_lb():
     kg = float(input('Enter mass in kilograms: '))
     lb = kg * 2.205
     print('Mass in pounds: {0}'.format(lb))

def lb_kg():
     lb = float(input('Enter mass in pounds: '))
     kg = lb / 2.205
     print('Mass in kilograms: {0}'.format(kg))

def C_F():
     C = float(input('Enter temperature in Celsius: '))
     F = (C * 9/5) + 32
     print('Temperature in Fahrenheit: {0}'.format(F))

def F_C():
     F = float(input('Enter temperature in Fahreinheit: '))
     C = (F - 32) * 5/9
     print('Temperature in Celsius: {0}'.format(C))

     
if __name__ == '__main__':
     while True:
         print_menu() 
         choice = input('Which conversion would you like to do?: ')
         match choice:
             case '1':
                  km_miles()
             case '2':
                  miles_km()
             case '3':
                 kg_lb()
             case '4':
                 lb_kg()
             case '5':
                 C_F()
             case '6':
                 F_C()

     answer = input('Do you want to exit? Type \'y\' for yes ')
     if answer == 'y':
          break
