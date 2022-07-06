def main():
    my_list = [1,'Hello',True,4.5]
    my_dict = {"firstname": "Manuel", "lastname":"Briones"}

    super_list = [
        {"firstname": "Manuel", "lastname":"Briones"},
        {"firstname": "Diana", "lastname":"Rodríguez"},
        {"firstname": "Karen", "lastname":"Briones"},
        {"firstname": "Karina", "lastname":"Briones"}
    ]
    super_dict = {
        'natural_nums': [1,2,3,4,5],
        'integer_nums': [-1,-2,0,1,2],
        'floating_nums':[1.4,0.3,-1.2]
    }

    for key, value in super_dict.items():
        print(key,"-",value)

    for element in super_list:
        print(element['firstname'],'-',element['lastname'])

    


if __name__=='__main__':
    main()