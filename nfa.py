cuvant = input("Alege un cuvant: ")

tabel = {
    (0, "a") : {0},
    (0, 'b') : {0,1},
    (1, 'a') : {1},
    (1, 'b') : {1,2},
        }
s_initial = {0}
s_final = {2}

def nfa(lista_stari, tabel, inputs):
    stare_noua = set()
    for stare in lista_stari:
        if (stare, inputs) in tabel:
            stare_noua = stare_noua | tabel[(stare, inputs)]
    return stare_noua

for inputs in cuvant:
    s_initial = nfa(s_initial, tabel, inputs)
    print("{} ".format(inputs), end="")
    if len(s_initial) == 0:
        print("--> {} ",end="")
        break
    else:
        print("--> {} ".format(s_initial), end="")

for stare in s_initial:
    if stare in s_final:
        print(" Cuvantul este recunoscut")
else:
    print(" Cuvantul nu este recunoscut")
