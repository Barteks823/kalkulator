def dodaj(a, b):
    return a + b

def odejmij(a, b):
    return a - b

def mnoz(a, b):
    return a * b

def dziel(a, b):
    if b == 0:
        return "Nie można dzielić przez zero!"
    return a / b

def main():
    print("Prosty kalkulator - wybierz operację:")
    print("1. Dodawanie")
    print("2. Odejmowanie")
    print("3. Mnożenie")
    print("4. Dzielenie")

    wybor = input("Wybierz (1/2/3/4): ")
    a = float(input("Podaj pierwszą liczbę: "))
    b = float(input("Podaj drugą liczbę: "))

    if wybor == '1':
        print("Wynik:", dodaj(a, b))
    elif wybor == '2':
        print("Wynik:", odejmij(a, b))
    elif wybor == '3':
        print("Wynik:", mnoz(a, b))
    elif wybor == '4':
        print("Wynik:", dziel(a, b))
    else:
        print("Niepoprawny wybór.")

if __name__ == "__main__":
    main()
