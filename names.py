name= "Monika"
print("Mam na imię", name)

char = input("Podaj znak:")
size = int(input("Podaj rozmiar macierzy:"))
for i in range(size):
    for j in range(size):
        print(char, end=" ")
    print()

