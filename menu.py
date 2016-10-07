import sys
import csv


print """ menu
-----------------
1)Leer
2)Insertar
3)Exit"""
opcion=int(input("Insertar "))    
if opcion == 1:
    with open('data.csv','r')as file:
              data = csv.reader(file, delimiter=',')
              for line in data:
                  print line
        
if opcion == 2:
      nombre = raw_input("Nombre:")
      email = raw_input("E-mail: ")
      with open('data.csv','a')as file:
       data = csv.writer(file, delimiter=',')
       data.writerow([nombre, email])

       
if opcion == 3:
       sys.exit(0)
