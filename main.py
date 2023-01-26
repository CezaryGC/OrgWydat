from datetime import date
import matplotlib.pyplot as plt
import matplotlib as mpl

today = date.today()
first = input('czy to pierwszy raz jak uruchamiasz program? (y/n)')
if first == 'y':
    with open('zapis.txt', 'w') as save:
        za = input('ile zarobiłeś w tym miesącu?')

        print('podaj swoje wydatki z tego miesiąca')
        jedz = input('Ile pieniędzy wydałeś na jedzenie?')
        pr = input("Ile pieniędzy wydałeś na prąd?")
        gaz = input("Ile pieniędzy wydałeś na gaz?")
        mie = input("Ile pieniędzy wydałeś na czynsz?")
        ubr = input("Ile pieniędzy wydałeś na ubrania?")
        inn = input("Ile pieniędzy wydałeś na różne inne rzeczy?")

        suma = int(jedz)+int(pr)+int(gaz)+int(mie)+int(ubr)+int(inn)
        osz = int(za)-suma

        print(f'łącznie w wym miesiącu wydałeś {suma}')
        if osz <= 0:
            print('w tym miesiącu nie zaoszczędziłeś nic :(')
        elif osz >= 0:
            print(f'w tym miesiącu zaoszczędziłeś {osz}')

        save.write(f'{today.strftime("%B")} {osz} {suma}')
        save.write("\n")
    with open('lastzapis.txt', 'w') as save:
        save.write(str(osz))
        input('aby stworzyć zestawienie w formie tabeli potrzebne są dane z więcej niż jednego miesiąca tutaj to już koniec (wciścnij enter by zakończyć)')

elif first == 'n':
    with open('lastzapis.txt', 'r') as save:
        content = save.readlines()
        za = input('ile zarobiłeś w tym miesącu?')

        print('podaj swoje wydatki z tego miesiąca')
        jedz = input('Ile pieniędzy wydałeś na jedzenie?')
        pr = input("Ile pieniędzy wydałeś na prąd?")
        gaz = input("Ile pieniędzy wydałeś na gaz?")
        mie = input("Ile pieniędzy wydałeś na czynsz?")
        ubr = input("Ile pieniędzy wydałeś na ubrania?")
        inn = input("Ile pieniędzy wydałeś na różne inne rzeczy?")

        suma = int(jedz)+int(pr)+int(gaz)+int(mie)+int(ubr)+int(inn)
        osz = int(za)-suma
        oszt = int(content[0]) + osz

        print(f'łącznie w wym miesiącu wydałeś {suma}')
        if osz <= 0:
            print('w tym miesiącu nie zaoszczędziłeś nic :(')
        elif osz >= 0:
            print(f'w tym miesiącu zaoszczędziłeś {osz}')

        print(f'twoje ogólne oszczędności to teraz {oszt}')

    with open('lastzapis.txt', 'w') as save:
        save.write(str(oszt))

    with open('zapis.txt', 'a') as save:
        save.write('\n')
        save.write(f'{today.strftime("%B")} {osz} {suma}')

    wyk = input('czy chcesz otrzymać wykres zestawiający wydatki w ostatnim miesiącu? (y/n)')

    if wyk == 'y':
        with open('zapis.txt', 'r') as save:
            m=[]
            s=[]
            w=[]
            for line in save:
                mi = line.split()
                m.append(mi[0])
                s.append(mi[1])
                w.append(mi[2])
                
            
            mpl.rcParams['figure.dpi'] = 100
            plt.title('Zestawienie oszczędności w ostatnich miesiącach')
            plt.xlabel('Miesiąc')
            plt.ylabel('Oszczędności')
            plt.ylim(min(s), max(s))
            plt.plot(m, s)
            plt.xticks(rotation = 45)
            plt.show()


    elif wyk == 'n':
        input('to już wszystko wciśnij enter aby zamknąć')




