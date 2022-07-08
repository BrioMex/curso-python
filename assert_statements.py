"""
Este código devuelve los divisores enteros de un número entero positivo (si el número es decimal lo trunca).
Para usarlo escriba python3 assert_statements.py
Los asserts son para errores del programador, no errores del usuario
"""

def divisors(num):
    divisors_list=[i for i in range(1,int(num/2+1)) if num%i ==0]
    if len(divisors_list):
        divisors_list.append(num)
        return divisors_list
    
    
def main():
    num=input("Número del que se ha de encontrar el divisor: ")
    assert num.isnumeric(), "El valor debe ser unnúmero positivo"
    divisors_list = divisors(int(num))
    print(divisors_list)


if __name__ == '__main__':
    main()