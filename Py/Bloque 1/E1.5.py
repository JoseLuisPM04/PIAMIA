import random

num = random.randint(1, 100)
inte = 5

while inte > 0:
    print(num)
    num_pr = int(input("Dime tu intento "))
    if num_pr == num:
        print("Acertaste")
        break
    if num != num_pr and num_pr < num:
        inte -= 1
        print("Fallo, el numero es mayor, te quedan ",inte," intentos")
    if num != num_pr and num_pr > num:
        inte -= 1
        print("Fallo, el numero es menor, te quedan ",inte," intentos")