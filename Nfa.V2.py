"""
 AFN tabel :
        1   l
A  [A, B]  [A]
B  [B, C]  [B]
C      []   []
"""
tabel = {
    ("A","l"):("A",),
    ("A","1"): ("A","B",),
    ("B","l"): ("B",),
    ("B","1"): ("B","C",),
    ("C","l"):(),
    ("C","1"):(),

}

def automat(input,stareacurenta=("A")):
    print(tuple(stareacurenta),end=" + ")
    counter = len(input)
    for i in input:
        counter-=1
        print(i,end = " --> ")
        stareaNoua = tuple()
        for stare in stareacurenta:
            stareaNoua+=tabel[stare,i]
            stareaNoua=set(stareaNoua)
            stareaNoua=tuple(stareaNoua)
        stareacurenta=stareaNoua
        print(stareaNoua,end=" ")
        if ("B" in stareacurenta or "C" in stareacurenta) and counter ==0:
            return "Recunoscut"
    return 0
cuvant = input("Alege un cuvant: ")

if automat(cuvant) == "Recunoscut":
    print("Cuvantul a fost Recunoscut")
else:print("Cuvantul nu a fost recunoscut")
