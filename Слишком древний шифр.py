number = int(input("Число которое ты видишь на стене: "))
def get_key(n):
    password = ""
    for i in range(1, (int(number/2)+1)):
        for j in range(1, 20):
            ost = n % (i + j)
            if ost == False and i != j and j > i:
                password += str(i) + "+" + str(j) + " "
            else:
                continue
    return password
print(get_key(number))