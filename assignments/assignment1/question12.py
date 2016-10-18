data = [('Jony', '17', '91'), ('Jony', '17', '93'), ('John', '20', '90'), ('Tom', '19', '80'),
        ('Json', '21', '85')]

insertData = True

while insertData:
    name = input("enter name:")

    age = input("enter age:")
    score = input("enter score:")
    data.append((name, age, score))
    insertData = input("you want to add more record Default 'Y' (Y/N):").upper() != "N"

print(data)
print(sorted(data, key=lambda element: (element[0], int(element[1]), int(element[2]))))