# Question 1
file = open("text.txt", "w+")
try:
    file.write("Bonjour Mes Amis")
except IOError as e:
    print("Erreur d'écriture")

file.close()

# Question 2
file = open("text2.txt", "w+")
try:
    for i in range(101):
        file.write(f"Bonjour Mes Amis\n")
except IOError as e:
    print("Erreur d'écriture")

file.close()

# Question 3
file = open("text2.txt", "r")
try:
    print(file.read())
except IOError as e:
    print("Erreur de lecture")
file.close()