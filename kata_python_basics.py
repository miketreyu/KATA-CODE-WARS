
#funcion que devuelve un hello world
def greet():
    return "Hello, world!"

#funcion que devuelve un numero int en str
def int_to_string(number):
    return str(number)

#funcion que convierte los numeros positivos en negativos, pero si sale uno negativo o 0 no se modifica
def make_negative(number):
    if number > 0:  # Check if the number is positive
        return -number  # Return the negative of the number
    else:
        return number  # Return the number itself (it's already negative or zero)


#lo mismo que el anterior pero de forma distinta
def make_negative( number ):
    return -abs(number)


#funcion que multiplica el string por el numero de veces que hayas puesto de int
def repeat_str(repeat, string):
    return string * repeat



