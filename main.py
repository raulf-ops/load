age = int(input("Quel âge avez-vous ? "))
nom = input("Quel est votre nom ? ")


if age < 18:
    print("bonjour", nom, "vous êtes mineur.")

elif age >= 13 and age < 18:
    print("bonjour", nom, "vous êtes un enfant.")

else:
    print("bonjour", nom, "vous êtes majeur.")