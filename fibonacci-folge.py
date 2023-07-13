def fibonacci(n):
    folge = [0, 1]

    for i in range(2, n):
        folge.append(folge[i - 1] + folge[i - 2])

    return folge[:n]

def ist_primzahl(eingabe_zahl):
    if eingabe_zahl < 2:
        return False
    
    for i in range(2, int(eingabe_zahl ** 0.5) + 1):
        if eingabe_zahl % i == 0:
            return False
        
    return True

def erhalte_primzahlen(folge):
    primzahlen = []

    for nummer in folge:
        if ist_primzahl(nummer):
            primzahlen.append(nummer)

    return primzahlen

n = int(input("Bitte gib eine Zahl ein, um die Fibo-Folge zu generieren: "))
fib_folge = fibonacci(n)
primzahlen = erhalte_primzahlen(fib_folge)

print(f"\nDie ersten {n} Fibo-Zahlen lauten:")
print(fib_folge)

print("Die Primzahlen in der Fibo-Folge sind:")
print(primzahlen, "\n")
