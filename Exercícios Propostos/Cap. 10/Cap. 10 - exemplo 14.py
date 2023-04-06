def ExibeClassificacao(): 
    global Times, Torneio
    MontaClassificacao()
    sfmt = "{:>3} {:<16}" + "{:>6}"*8
    print("-" * LargTela)
    s = "Pos;Time;PG;J;V;E;D;GP;GC;SG"
    print(sfmt.format(*s.split(";")))
    print("-" * LargTela)
    Pos = 1
    for time in Times:
        dados = (Pos,) + tuple(time)
        print(sfmt.format(*dados))
        Pos += 1
    print("-" * LargTela)