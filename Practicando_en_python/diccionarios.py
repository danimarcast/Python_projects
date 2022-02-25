diccionario={
    'Programar':'organizar ideas o tareas :p',
    'POO':'Programacion orientada a objetos',
    'MVC':'Modelo vista controlador'

}
print(diccionario['POO'])


numeros={
    "0":"cero",
    "1":"uno",
    "2":"dos",
    "3":"tres",
    "4":"cuatro",
    "5":"cinco",
    "6":"seis",
    "7":"siete",
    "8":"ocho",
    "9":"nueve"
}
texto=input("Digite un numero entero")
textofinal = ""
for letra in texto:
    textofinal += numeros[letra] + " "
print(textofinal)
