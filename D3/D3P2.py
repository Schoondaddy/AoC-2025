data = open("input.txt", "r").read().split("\n")

summation = 0
for bank in data:
    bank = list(bank)
    for i in range(len(bank)):
        bank[i] = int(bank[i])
    
    
    
print(summation)

