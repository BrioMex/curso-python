from operator import and_


def main():
    square_numbers=[i**2 for i in range(1,101) if(i%3)!=0]
    print(square_numbers)

    divisibles=[i for i in range(1,10000) if i%4==0 and i%6==0 and i%9==0]
    print(divisibles)

if __name__=='__main__':
    main()