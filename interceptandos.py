import sys
def resolver():
    input_data = sys.stdin.read().split()
    lista_N = [int(x) for x in input_data]
    total_nove = 0
    if not lista_N:
        return   
    for i in lista_N:
        if i == 9:
            total_nove += 1
            return
    if total_nove == 0:
        print("F")
    else:
        print("S")
if __name__ == "__main__":
    resolver()