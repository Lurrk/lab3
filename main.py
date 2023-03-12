from random import randint


def proc1():
    slovo = []
    while (new_word := str(input())) != "stop":
        slovo.append(new_word)
    print(" ".join(slovo))


proc1()


def proc2():
 word = input("введите слово:")
 for i in range(len(word)):
     if word[i] == "Ф" or word[i] == "ф":
         print("Слово редкое")
         break
     else:
        print("Слово обычное")
        break


proc2()


def proc3():
    k = 0
    print("Чтобы завершенить игру, введите stop")
    while True:
        a = randint(1, 100)
        b = randint(1, 100)
        print(f"{a} + {b} = ", end="")
        res = input()

        if res == "stop":
            break

        res = int(res)
        if a+b == res:
            print("Правильно!")
        else:
            print("Ответ неправильный :(")
            k += 1
        if k == 3:
           print('игра окончена')
           break


proc3()