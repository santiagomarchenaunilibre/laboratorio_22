#lista
frutas = ["Pera","Manzana","Uvas","Banano","Fresa"]
print("Lista original",frutas)

fruta_ingreso = input("Ingrese fruta: ")
frutas.append(fruta_ingreso)
print("Lista nueva: ",frutas)
print("La tercera fruta es: ",frutas[2])