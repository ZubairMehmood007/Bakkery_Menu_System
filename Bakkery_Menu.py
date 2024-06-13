import pandas as pd
import numpy as np
import datetime

print('-' * 38)
print("WELCOME TO OUR BAKKERY KINGS BAKKER ")
print('-' * 38)

info = []

while True:
    A = int(input("Press 1 for menu list: "))

    if A == 1:
        print('-' * 30)
        print('''SELECT THE ITEM WHICH YOU WANT TO BUY: 
        1: CAKE
        2: BISCUITS
        3: TEA ITEMS
        4: CHOCLATES
        5: INFO ABOUT SHOPPING
        6: EXIT''')

        print('-' * 30)
        a = int(input("Enter the item number: "))
        print('-' * 30)

        if a == 1:
            print('''Cakes types
            1: Chocolate cake : 
            2: Pine Apple cake: 
            3: Cream cake:
            4: Fruit cake:
            5: Jelly cake:
            6: Birthday cake: ''')

            b = int(input("Press item number: "))
            if b == 1:
                print(f"Thanks for selecting {b} Chocolate Cake: ")
                print('here the information about requiremnets and cake price = 2000/-: \n')

                b_ = input('Enter you name:')
                b1 = input('Entr the adress: ')
                b2 = int(input('Enter the Phone number: '))
                b4 = int(input("How many items u want to buy: "))
                b3 = int(input(f"Enter amount {b4*2000} of your cake: "))
                if b3 == 2000*b4:
                    b3 = b3
                    date = datetime.datetime.now()
                    info_preson = b_, b1, b2, b3, date
                    info.append(info_preson)
                    print("Here is your information:: ")
                    print("-" * 65)
                    df = pd.DataFrame(info, columns=["Name", "Adress", "Phone Number", "Amount paid", "Date"])

                    print(f"Mr/Ms {b_} Your order is confirmed at {date}: ")
                    print("-" * 65)
                else:
                    print(f"Kindly pay {b4*2000} amount only:\n your order is not confirmed:  ")


            elif b == 2:
                print(f"Thanks for selecting {b} Pine Apple cake: ")
                print('here the information about requiremnets and cake price = 2700/-: \n')

                c_ = input('Enter you name:')
                c1 = input('Entr the adress: ')
                c2 = int(input('Enter the Phone number: '))
                b4 = int(input("How many items u want to buy: "))
                c3 = int(input(f"Enter amount {b4*2700}/- of your cake: "))

                if c3 == 2700*b4:
                    c3 = c3
                    date = datetime.datetime.now()
                    info_preson = c_, c1, c2, c3, date
                    info.append(info_preson)
                    print("Here is your information:: ")
                    print("-" * 65)
                    df = pd.DataFrame(info, columns=["Name", "Adress", "Phone Number", "Amount paid", "Date"])

                    print(f"Mr/Ms {c_} Your order is confirmed at {date}: ")
                    print("-" * 65)
                else:
                    print(f"Kindly pay {b4*2700} amount only:\n your order is not confirmed:  ")


            elif b == 3:
                print(f"Thanks for selecting {b} Cream Cake: ")
                print('here the information about requirements and cake price = 2500/-: \n')

                d_ = input('Enter you name:')
                d1 = input('Entr the adress: ')
                d2 = int(input('Enter the Phone number: '))
                b4 = int(input("How many items u want to buy: "))
                d3 = int(input(f"Enter amount {b4*2500}/- of your cake: "))

                if d3 == 2500*b4:
                    d3 = d3
                    date = datetime.datetime.now()
                    info_preson = d_, d1, d2, d3, date
                    info.append(info_preson)
                    print("Here is your information:: ")
                    print("-" * 65)
                    df = pd.DataFrame(info, columns=["Name", "Adress", "Phone Number", "Amount paid", "Date"])

                    print(f"Mr/Ms {d_} Your order is confirmed at {date}:")
                    print("-" * 65)
                else:
                    print(f"Kindly pay {b4*2500} amount only:\n your order is not confirmed:  ")


            elif b == 4:
                print(f"Thanks for selecting {b} Fruit Cake: ")
                print('here the information about requirements and cake price = 3400/-: \n')

                e_ = input('Enter you name:')
                e1 = input('Entr the adress: ')
                e2 = int(input('Enter the Phone number: '))
                b4 = int(input("How many items u want to buy: "))
                e3 = int(input(f"Enter amount {b4*3400}/- of your cake: "))

                if e3 == 3400*b4:
                    e3 = e3
                    date = datetime.datetime.now()
                    info_preson = e_, e1, e2, e3, date
                    info.append(info_preson)
                    print("Here is your information:: ")
                    print("-" * 65)
                    df = pd.DataFrame(info, columns=["Name", "Adress", "Phone Number", "Amount paid", "Date"])

                    print(f"Mr/Ms {e_} Your order is confirmed at {date}: ")
                    print("-" * 65)
                else:
                    print(f"Kindly pay {b4*3400} amount only:\n your order is not confirmed:  ")




            elif b == 5:
                print(f"Thanks for selecting {b} Jelly Cake: ")
                print('here the information about requirements and cake price = 3600/-: \n')

                f_ = input('Enter you name:')
                f1 = input('Entr the adress: ')
                f2 = int(input('Enter the Phone number: '))
                b4 = int(input("How many items u want to buy: "))
                f3 = int(input(f"Enter amount {b4*3600}/- of your cake: "))

                if f3 == 3600*b4:
                    f3 = f3
                    date = datetime.datetime.now()
                    info_preson = f_, f1, f2, f3, date
                    info.append(info_preson)
                    print("Here is your information:: ")
                    print("-" * 65)
                    df = pd.DataFrame(info, columns=["Name", "Adress", "Phone Number", "Amount paid", "Date"])

                    print(f"Mr/Ms {f_} Your order is confirmed at {date}:")
                    print("-" * 65)
                else:
                    print(f"Kindly pay {b4*3600} amount only:\n your order is not confirmed:  ")

            elif b == 6:
                print(f"Thanks for selecting {b} Birthday Cake: ")
                print('here the information about requirements and cake price = 4000/-: \n')

                j_ = input('Enter you name:')
                j1 = input('Entr the adress: ')
                j2 = int(input('Enter the Phone number: '))
                b4 = int(input("How many items u want to buy: "))
                j3 = int(input(f"Enter amount {b4*4000}/- of your cake: "))

                if j3 == 4000*b4:
                    j3 = j3
                    date = datetime.datetime.now()
                    time_now = datetime.time()

                    info_preson = j_, j1, j2, j3, date
                    info.append(info_preson)
                    print("Here is your information:: ")
                    print("-" * 65)
                    df = pd.DataFrame(info, columns=["Name", "Adress", "Phone Number", "Amount paid", "Date"])

                    print(f"Mr/Ms {j_} Your order is confirmed at {date}: ")
                    print("-" * 65)
                else:
                    print(f"Kindly pay {b4*4000} amount only:\n your order is not confirmed:  ")

        elif a == 2:

            print('''Biscuits types
                1: Choclate Biscuits: 
                2: Pine Apple Biscuits: 
                3: Cream Biscuits:
                4: Fruit Biscuits:
                5: Jelly Biscuits:
                6: Special Biscuits: ''')

            b = int(input("Press item number: "))
            if b == 1:
                print(f"Thanks for selecting {b} Chocolate Biscuits: ")
                print('here the information about requiremnets and cake price 1KG=  2000/-: \n')

                b_ = input('Enter you name:')
                b1 = input('Entr the adress: ')
                b2 = int(input('Enter the Phone number: '))
                b4 = int(input("How many items u want to buy: "))
                b3 = int(input(f"Enter amount {b4*2000} of your cake: "))

                if b3 == 2000*b4:
                    b3 = b3
                    date = datetime.datetime.now()
                    info_preson = b_, b1, b2, b3, date
                    info.append(info_preson)
                    print("Here is your information:: ")
                    print("-" * 65)
                    df = pd.DataFrame(info, columns=["Name", "Adress", "Phone Number", "Amount paid", "Date"])

                    print(f"Mr/Ms {b_} Your order is confirmed at {date}: You will receive your order after one hour")
                    print("-" * 65)
                else:
                    print("Kindly pay {b4*2000} amount only:\n your order is not confirmed:  ")

            elif b == 2:
                print(f"Thanks for selecting {b} Pine Apple Biscuits : ")
                print('here the information about requirements and cake price 1KG= 3400/-: \n')

                c_ = input('Enter you name:')
                c1 = input('Entr the adress: ')
                c2 = int(input('Enter the Phone number: '))
                b4 = int(input("How many items u want to buy: "))
                c3 = int(input(f"Enter amount {b4*3400}/- of your cake: "))

                if c3 == 3400*b4:
                    c3 = c3
                    date = datetime.datetime.now()
                    time_now = datetime.time()

                    info_preson = c_, c1, c2, c3, date
                    info.append(info_preson)
                    print("Here is your information:: ")
                    print("-" * 65)
                    df = pd.DataFrame(info, columns=["Name", "Adress", "Phone Number", "Amount paid", "Date"])

                    print(f"Mr/Ms {c_} Your order is confirmed at {date} You will receive your order after one hour")
                    print("-" * 65)
                else:
                    print(f"Kindly pay {b4*3400} amount only:\n your order is not confirmed:  ")

            elif b == 3:
                print(f"Thanks for selecting {b} Cream Biscuits: ")
                print('here the information about requirements and cake price = 3200/-: \n')

                d_ = input('Enter you name:')
                d1 = input('Entr the adress: ')
                d2 = int(input('Enter the Phone number: '))
                b4 = int(input("How many items u want to buy: "))
                d3 = int(input(f"Enter amount {b4*3200} of your cake: "))

                if d3 == 3200*b4:
                    d3 = d3
                    date = datetime.datetime.now()
                    time_now = datetime.time()

                    info_preson = d_, d1, d2, d3, date
                    info.append(info_preson)
                    print("Here is your information:: ")
                    print("-" * 65)
                    df = pd.DataFrame(info, columns=["Name", "Adress", "Phone Number", "Amount paid", "Date"])

                    print(f"Mr/Ms {d_} Your order is confirmed at {date} ")
                    print("-" * 65)
                else:
                    print(f"Kindly pay {b4*3200} amount only:\n your order is not confirmed:  ")

            elif b == 4:
                print(f"Thanks for selecting {b} Fruit Biscuits: ")
                print('here the information about requirements and cake price = 3900/-: \n')

                e_ = input('Enter you name:')
                e1 = input('Entr the adress: ')
                e2 = int(input('Enter the Phone number: '))
                b4 = int(input("How many items u want to buy: "))
                e3 = int(input(f"Enter amount {b4*3900}/- of your cake: "))

                if e3 == 3900*b4:
                    e3 = e3
                    date = datetime.datetime.now()
                    time_now = datetime.time()

                    info_preson = e_, e1, e2, e3, date
                    info.append(info_preson)
                    print("Here is your information:: ")
                    print("-" * 65)
                    df = pd.DataFrame(info, columns=["Name", "Adress", "Phone Number", "Amount paid", "Date"])

                    print(f"Mr/Ms {e_} Your order is confirmed at {date} ")
                    print("-" * 65)
                else:
                    print(f"Kindly pay {b4*3900} amount only:\n your order is not confirmed:  ")

            elif b == 5:
                print(f"Thanks for selecting {b} Jelly Biscuits: ")
                print('here the information about requirements and cake price = 3000/-: \n')

                f_ = input('Enter you name:')
                f1 = input('Entr the adress: ')
                f2 = int(input('Enter the Phone number: '))
                b4 = int(input("How many items u want to buy: "))
                f3 = int(input(f"Enter amount {b4*3000}/- of your cake: "))

                if f3 == 3000*b4:
                    f3 = f3
                    date = datetime.datetime.now()
                    time_now = datetime.time()

                    info_preson = f_, f1, f2, f3, date
                    info.append(info_preson)
                    print("Here is your information:: ")
                    print("-" * 65)
                    df = pd.DataFrame(info, columns=["Name", "Adress", "Phone Number", "Amount paid", "Date"])

                    print(f"Mr/Ms {f_} Your order is confirmed at {date} ")
                    print("-" * 65)
                else:
                    print(f"Kindly pay {b4*3000} amount only:\n your order is not confirmed:  ")

            elif b == 6:
                print(f"Thanks for selecting {b} Special Biscuits: ")
                print('here the information about requirements and cake price = 4500/-: \n')

                j_ = input('Enter you name:')
                j1 = input('Entr the adress: ')
                j2 = int(input('Enter the Phone number: '))
                b4 = int(input("How many items u want to buy: "))
                j3 = int(input(f"Enter amount {b4*4500}/- of your cake: "))

                if j3 == 4500*b4:
                    j3 = j3
                    date = datetime.datetime.now()
                    time_now = datetime.time()

                    info_preson = j_, j1, j2, j3, date
                    info.append(info_preson)
                    print("Here is your information:: ")
                    print("-" * 65)
                    df = pd.DataFrame(info, columns=["Name", "Adress", "Phone Number", "Amount paid", "Date"])

                    print(f"Mr/Ms {j_} Your order is confirmed at {date} ")
                    print("-" * 65)
                else:
                    print(f"Kindly pay {b4*4500} amount only:\n your order is not confirmed:  ")



        elif a == 3:

            print('''Tea Items types
                    1: Dry cake cut: 
                    2: Petties: 
                    3: Cream petties:
                    4: Fruit and mix types patties:
                    5: Jelly and strawberry items:
                    6: Nimko: ''')

            b = int(input("Press item number: "))
            if b == 1:
                print(f"Thanks for selecting {b} Dry Cake cut: ")
                print('here the information about requiremnets and cake price = 1200/-: \n')

                b_ = input('Enter you name:')
                b1 = input('Entr the adress: ')
                b2 = int(input('Enter the Phone number: '))
                b4 = int(input("How many items u want to buy: "))
                b3 = int(input(f"Enter amount {b4*1200}/- of your cake: "))

                if b3 == 1200*b4:
                    b3 = b3
                    date = datetime.datetime.now()
                    info_preson = b_, b1, b2, b3, date
                    info.append(info_preson)
                    print("Here is your information:: ")
                    print("-" * 65)
                    df = pd.DataFrame(info, columns=["Name", "Adress", "Phone Number", "Amount paid", "Date"])

                    print(f"Mr/Ms {b_} Your order is confirmed at {date}: ")
                    print("-" * 65)
                else:
                    print(f"Kindly pay {b4*1200} amount only:\n your order is not confirmed:  ")


            elif b == 2:
                print(f"Thanks for selecting {b} Petties: ")
                print('here the information about requiremnets and cake price 1KG= 2700/-: \n')

                c_ = input('Enter you name:')
                c1 = input('Entr the adress: ')
                c2 = int(input('Enter the Phone number: '))
                b4 = int(input("How many items u want to buy: "))
                c3 = int(input(f"Enter amount {b4*2700}/- of your cake: "))

                if c3 == 2700*b4:
                    c3 = c3
                    date = datetime.datetime.now()
                    info_preson = c_, c1, c2, c3, date
                    info.append(info_preson)
                    print("Here is your information:: ")
                    print("-" * 65)
                    df = pd.DataFrame(info, columns=["Name", "Adress", "Phone Number", "Amount paid", "Date"])

                    print(f"Mr/Ms {c_} Your order is confirmed at {date}: ")
                    print("-" * 65)
                else:
                    print(f"Kindly pay {b4*2700} amount only:\n your order is not confirmed:  ")


            elif b == 3:
                print(f"Thanks for selecting {b} Cream Petties: ")
                print('here the information about requirements and cake price 1KG = 4300/-: \n')

                d_ = input('Enter you name:')
                d1 = input('Entr the adress: ')
                d2 = int(input('Enter the Phone number: '))
                b4 = int(input("How many items u want to buy: "))
                d3 = int(input(f"Enter amount {b4*4300}/- of your cake: "))

                if d3 == 4300*b4:
                    d3 = d3
                    date = datetime.datetime.now()
                    info_preson = d_, d1, d2, d3, date
                    info.append(info_preson)
                    print("Here is your information:: ")
                    print("-" * 65)
                    df = pd.DataFrame(info, columns=["Name", "Adress", "Phone Number", "Amount paid", "Date"])

                    print(f"Mr/Ms {d_} Your order is confirmed {date}: ")
                    print("-" * 65)
                else:
                    print(f"Kindly pay {b4*4300} amount only:\n your order is not confirmed:  ")


            elif b == 4:
                print(f"Thanks for selecting {b} Fruit and mix types patties: ")
                print('here the information about requirements and cake price 1KG= 5200/-: \n')

                e_ = input('Enter you name:')
                e1 = input('Entr the adress: ')
                e2 = int(input('Enter the Phone number: '))
                b4 = int(input("How many items u want to buy: "))
                e3 = int(input(f"Enter amount {b4*5200}/- of your cake: "))

                if e3 == 5200*b4:
                    e3 = e3
                    date = datetime.datetime.now()
                    info_preson = e_, e1, e2, e3, date
                    info.append(info_preson)
                    print("Here is your information:: ")
                    print("-" * 65)
                    df = pd.DataFrame(info, columns=["Name", "Adress", "Phone Number", "Amount paid", "Date"])

                    print(f"Mr/Ms {e_} Your order is confirmed at {date}: ")
                    print("-" * 65)
                else:
                    print(f"Kindly pay {b4*5200} amount only:\n your order is not confirmed:  ")




            elif b == 5:
                print(f"Thanks for selecting {b} Jelly and strawberry items: ")
                print('here the information about requirements and cake price 1KG = 2650/-: \n')

                f_ = input('Enter you name:')
                f1 = input('Entr the adress: ')
                f2 = int(input('Enter the Phone number: '))
                b4 = int(input("How many items u want to buy: "))
                f3 = int(input(f"Enter amount {b4*2650}/- of your cake: "))

                if f3 == 2650*b4:
                    f3 = f3
                    date = datetime.datetime.now()
                    info_preson = f_, f1, f2, f3, date
                    info.append(info_preson)
                    print("Here is your information:: ")
                    print("-" * 65)
                    df = pd.DataFrame(info, columns=["Name", "Adress", "Phone Number", "Amount paid", "Date"])

                    print(f"Mr/Ms {f_} Your order is confirmed at {date}: ")
                    print("-" * 65)
                else:
                    print(f"Kindly pay {b4*2650} amount only:\n your order is not confirmed:  ")

            elif b == 6:
                print(f"Thanks for selecting {b} Nimko: ")
                print('here the information about requirements and cake price = 2100/-: \n')

                j_ = input('Enter you name:')
                j1 = input('Entr the adress: ')
                j2 = int(input('Enter the Phone number: '))
                b4 = int(input("How many items u want to buy: "))
                j3 = int(input(f"Enter amount {b4*2100}/- of your cake: "))

                if j3 == 2100*b4:
                    j3 = j3
                    date = datetime.datetime.now()
                    time_now = datetime.time()

                    info_preson = j_, j1, j2, j3, date
                    info.append(info_preson)
                    print("Here is your information:: ")
                    print("-" * 65)
                    df = pd.DataFrame(info, columns=["Name", "Adress", "Phone Number", "Amount paid", "Date"])

                    print(
                        f"Mr/Ms {j_} Your order is confirmed at {date} ")
                    print("-" * 65)
                else:
                    print(f"Kindly pay {b4*2100} amount only:\n your order is not confirmed:  ")




        elif a == 4:

            print('''CHOCOLATES types
                1: Chocolate mix: 
                2: Dairy milk chocolate: 
                3: Twist chocolate:
                4: Fruit chocolate:
                5: Jelly chocolate:
                6: Birthday chocolate special''')

            b = int(input("Press item number: "))
            if b == 1:
                print(f"Thanks for selecting {b} Chocolate mix: ")
                print('here the information about requiremnets and cake price = 5300/-: \n')

                b_ = input('Enter you name:')
                b1 = input('Entr the adress: ')
                b2 = int(input('Enter the Phone number: '))
                b4 = int(input("How many items u want to buy: "))
                b3 = int(input(f"Enter amount {b4*5300}/- of your cake: "))

                if b3 == 5300*b4:
                    b3 = b3
                    date = datetime.datetime.now()
                    info_preson = b_, b1, b2, b3, date
                    info.append(info_preson)
                    print("Here is your information:: ")
                    print("-" * 65)
                    df = pd.DataFrame(info, columns=["Name", "Adress", "Phone Number", "Amount paid", "Date"])

                    print(f"Mr/Ms {b_} Your order is confirmed at {date}: ")
                    print("-" * 65)
                else:
                    print(f"Kindly pay {b4*5300} amount only:\n your order is not confirmed:  ")


            elif b == 2:
                print(f"Thanks for selecting {b} Dairy Milk chocolate: ")
                print('here the information about requiremnets and cake price = 5970/-: \n')

                c_ = input('Enter you name:')
                c1 = input('Entr the adress: ')
                c2 = int(input('Enter the Phone number: '))
                b4 = int(input("How many items u want to buy: "))
                c3 = int(input(f"Enter amount {b4*5970}/- of your cake: "))

                if c3 == 5970*b4:
                    c3 = c3
                    date = datetime.datetime.now()
                    info_preson = c_, c1, c2, c3, date
                    info.append(info_preson)
                    print("Here is your information:: ")
                    print("-" * 65)
                    df = pd.DataFrame(info, columns=["Name", "Adress", "Phone Number", "Amount paid", "Date"])

                    print(f"Mr/Ms {c_} Your order is confirmed at {date}: ")
                    print("-" * 65)
                else:
                    print(f"Kindly pay {b4*5970} amount only:\n your order is not confirmed:  ")


            elif b == 3:
                print(f"Thanks for selecting {b} Twist chocolate: ")
                print('here the information about requirements and cake price = 5500/-: \n')

                d_ = input('Enter you name:')
                d1 = input('Entr the adress: ')
                d2 = int(input('Enter the Phone number: '))
                b4 = int(input("How many items u want to buy: "))
                d3 = int(input(f"Enter amount {b4*5500}/- of your cake: "))

                if d3 == 5500*b4:
                    d3 = d3
                    date = datetime.datetime.now()
                    info_preson = d_, d1, d2, d3, date
                    info.append(info_preson)
                    print("Here is your information:: ")
                    print("-" * 65)
                    df = pd.DataFrame(info, columns=["Name", "Adress", "Phone Number", "Amount paid", "Date"])

                    print(f"Mr/Ms {d_} Your order is confirmed at {date} ")
                    print("-" * 65)
                else:
                    print(f"Kindly pay {b4*5500} amount only:\n your order is not confirmed:  ")


            elif b == 4:
                print(f"Thanks for selecting {b} Fruit chocolate: ")
                print('here the information about requirements and cake price = 6540/-: \n')

                e_ = input('Enter you name:')
                e1 = input('Entr the adress: ')
                e2 = int(input('Enter the Phone number: '))
                b4 = int(input("How many items u want to buy: "))
                e3 = int(input(f"Enter amount {b4*6540}/- of your cake: "))

                if e3 == 6540*b4:
                    e3 = e3
                    date = datetime.datetime.now()
                    info_preson = e_, e1, e2, e3, date
                    info.append(info_preson)
                    print("Here is your information:: ")
                    print("-" * 65)
                    df = pd.DataFrame(info, columns=["Name", "Adress", "Phone Number", "Amount paid", "Date"])

                    print(f"Mr/Ms {e_} Your order is confirmed at {date}: ")
                    print("-" * 65)
                else:
                    print(f"Kindly pay {b4*6540} amount only:\n your order is not confirmed:  ")




            elif b == 5:
                print(f"Thanks for selecting {b} Jelly chocolate: ")
                print('here the information about requirements and cake price = 6980/-: \n')

                f_ = input('Enter you name:')
                f1 = input('Entr the adress: ')
                f2 = int(input('Enter the Phone number: '))
                b4 = int(input("How many items u want to buy: "))
                f3 = int(input(f"Enter amount {b4*6980}/- of your cake: "))

                if f3 == 6980*b4:
                    f3 = f3
                    date = datetime.datetime.now()
                    info_preson = f_, f1, f2, f3, date
                    info.append(info_preson)
                    print("Here is your information:: ")
                    print("-" * 65)
                    df = pd.DataFrame(info, columns=["Name", "Adress", "Phone Number", "Amount paid", "Date"])

                    print(f"Mr/Ms {f_} Your order is confirmed at {date}: ")
                    print("-" * 65)
                else:
                    print(f"Kindly pay {b4*6980} amount only:\n your order is not confirmed:  ")

            elif b == 6:
                print(f"Thanks for selecting {b} Birthday chocolate special: ")
                print('here the information about requirements and cake price = 9900/-: \n')

                j_ = input('Enter you name:')
                j1 = input('Entr the adress: ')
                j2 = int(input('Enter the Phone number: '))
                b4 = int(input("How many items u want to buy: "))
                j3 = int(input(f"Enter amount {b4*9900}/- of your cake: "))

                if j3 == 9900*b4:
                    j3 = j3
                    date = datetime.datetime.now()
                    time_now = datetime.time()

                    info_preson = j_, j1, j2, j3, date
                    info.append(info_preson)
                    print("Here is your information:: ")
                    print("-" * 65)
                    df = pd.DataFrame(info, columns=["Name", "Adress", "Phone Number", "Amount paid", "Date"])

                    print(f"Mr/Ms {j_} Your order is confirmed at {date} ")
                    print("-" * 65)
                else:
                    print(f"Kindly pay {b4*9900} amount only:\n your order is not confirmed:  ")






        elif a == 5:
            try:

                print('Thanks for visiting \n')
                print('*' * 27)
                print(' Below is your information about shopping::')
                print('*' * 27)

                print('-' * 45)
                m = np.sum(df['Amount paid'])
                df["Total bill"] = pd.Series(m)
                print(df)

                print('-' * 45)

                with pd.ExcelWriter(r"C:\Users\LENOVO\Desktop\Bakkery_System\database.xlsx") as writer:
                    df.to_excel(writer, sheet_name='customer_data', index = False)
                    print("Your data is stored into excel")

            except:
                print("You have not recored yet..")



        if a == 6:
            print("Thanks for visiting: ")


            break




else:
    print('Wrong entry: ')


