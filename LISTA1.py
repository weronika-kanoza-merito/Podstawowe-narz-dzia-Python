
# Zad 1
wysokosc = float(input("Podaj wysokość trójkąta: "))
bok = float(input("Podaj długość boku trójkąta: "))
pole = 0.5 * bok * wysokosc
print(f"Pole trójkąta wynosi: {pole}")

# Zad 2
celsius = float(input("Podaj temperaturę w Celsjuszach: "))
fahrenheit = (celsius * 9/5) + 32
print(f"Temperatura: {fahrenheit} stopni Fahrenheita")

# Zad 3
def dlugosc_imienia(imie):
    return len(imie)

imie = input("Podaj swoje imię: ")
print(f"Długość imienia: {dlugosc_imienia(imie)}")

# Zad 4
def roznica_dlugosci(imie1, imie2):
    print(f"Różnica długości: {abs(len(imie1) - len(imie2))}")

imie1 = input("Podaj pierwsze imię: ")
imie2 = input("Podaj drugie imię: ")
roznica_dlugosci(imie1, imie2)

# Zad 5
def typ_argumentu(argument):
    print(f"Typ argumentu: {type(argument)}")

# Przykład użycia:
typ_argumentu(10)  # int
typ_argumentu("Hello")  # str
typ_argumentu([1, 2, 3])  # list




