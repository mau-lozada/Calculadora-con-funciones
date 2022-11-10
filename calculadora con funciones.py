# -*- coding: utf-8 -*-
"""
Created on Tue Dec 17 20:56:37 2019

@author: vecin
"""
def ingreso ():
    global n1,n2 
    n1 = float(input("primer numero: "))
    n2 = float(input("segundo numero: "))
    
def suma ():
    print ("El resultado es: ", n1+n2)
    input()

def resta ():
    print ("El resultado es: ", n1-n2)
    input()

def multiplicacion ():
    print ("El resultado es: ", n1*n2)
    input()

def division ():
    if n2 == 0:
        print("No se puede dividir")
        input()
    else:
        print("El resultado es: ",n1/n2)
        input()
               
        
while True: 
    print("\tMenú calculadora")
    print("1. Sumar")
    print("2. Restar")
    print("3. Multiplicar")
    print("4. Dividir")
    print("5. Salir")

    
    opcion = input("->")
    
    if opcion == '1':
        ingreso()
        suma ()
        
    elif opcion == '2':
        ingreso()
        resta()
        
    elif opcion == '3':
        ingreso()
        multiplicacion()
        
    elif opcion == '4':
        ingreso()
        division()
        
    elif opcion == '5':
        break
        
        
        