data = open("input.txt", "r").read().split("\n")

summation = 0
for bank in data:
    bank = list(bank)
    for i in range(len(bank)):
        bank[i] = int(bank[i])
    
    max1 = bank.index(max(bank))
    if max1 == len(bank) - 1:
        max2 = max1
        max1 = bank.index(max(bank[:len(bank) - 1]))
    else:
        range2 = bank[max1 + 1:]
        max2 = max1 + range2.index(max(range2)) + 1
    summation += 10 * bank[max1] + bank[max2]

    
print(summation)


    