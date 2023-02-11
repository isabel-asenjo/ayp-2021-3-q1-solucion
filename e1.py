import random

def random_number():
    return str(random.randint(100,999))

def camarada(n):
    return len(set(n)) == 1

def ondulado(n):
    return len(set(n)) == 2 and n[0] == n[2]

def main():
    j1 = input("Rol del J1 ('C'amarada u 'O'ndulado): ").upper()
    while j1 != 'C' and j1 != 'O':
        j1 = input("Ingreso inválido. Rol del J1 ('C'amarada u 'O'ndulado): ").upper()
    j2 = 'C' if j1 == 'O' else 'O'

    scores = {'J1': [], 'J2': []}

    while len(scores['J1']) < 3 or len(scores['J2']) < 3:
        n = random_number()
        if camarada(n):
            if j1 == 'C':
                scores['J1'].append(int(n))
            else:
                scores['J2'].append(int(n))
        elif ondulado(n):
            if j1 == 'O':
                scores['J1'].append(int(n))
            else:
                scores['J2'].append(int(n))

    if sum(scores['J1']) > sum(scores['J2']):
        print("Ganó J1")
    elif sum(scores['J1']) < sum(scores['J2']):
        print("Ganó J2")
    else:
        print("Empate")
    

main()
