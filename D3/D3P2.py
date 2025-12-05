data = open("input.txt", "r").read().split("\n")

summation = 0
for bank in data:
    number = ""
    bank = list(bank)
    for i in range(len(bank)):
        bank[i] = int(bank[i])
   
    maximum = max(bank[:len(bank) - 11])
    number += str(maximum)
    bank = bank[bank.index(maximum) + 1:]
    for i in range(10, -1, -1):
        maximum = max(bank[:len(bank) - i])
        number += str(maximum)
        bank = bank[bank.index(maximum) + 1:]
    summation += int(number)

print(summation)