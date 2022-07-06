def main():
    dict_numbers={i:i**3 for i in range(1,101) if i%3!=0}
    for key, value in dict_numbers.items():
        print(key,"-",value)

    root_numbers={i:round(i**0.5,2) for i in range(1,1000)}
    for key, value in root_numbers.items():
        print(key,"-",value)
    

if __name__=='__main__':
    main()
