"""
Este código devuelve los divisores enteros de un número entero positivo (si el número es decimal lo trunca).
Para usarlo escriba python3 debuggin.py
"""

def divisors(num):
    divisors_list=[i for i in range(1,int(num/2+1)) if num%i ==0]
    if len(divisors_list):
        divisors_list.append(num)
        return divisors_list

def num_type(num):
    try:
        
        num=int(num)
        if num < 1:
            raise Exception("El número debe ser entero positivo.")
    except ValueError:
            print("El valor debe ser numérico")
            num=0
    except Exception as ee:
            print(ee)
            num=0
    finally:
        return num
    
    
def main():
    num=input("Número del que se ha de encontrar el divisor: ")
    divisors_list = divisors(num_type(num))
    print(divisors_list)


if __name__ == '__main__':
    main()