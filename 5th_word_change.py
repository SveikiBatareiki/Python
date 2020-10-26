# Uzrakstīt programmu teksta pārveidošanai
# Saglabā lietotāja ievadu
# Izdrukā ievadīto tekstu bez izmaiņām
# Izņēmums: ja ievadā ir vārdi nav .... slikts, TAD izvadā nav ... slikts posms jānomaina uz ir labs
# Laiks nav slikts -> Laiks ir labs
# Auto nav jauns -> Auto nav jauns
# Tas biezpiens nav nemaz tik slikts -> Tas biezpiens ir labs
# Droši vien noderēs find (vai index, vai pat rfind), tāpat arī in operātors var noderēt. Tāpat slice sintakse būs noderīga.
# Ja uzdevums risinās raiti, tad varam uzlabot un meklēt gan nav ... slikts -> ir labs, gan nav ... slikta -> ir laba
# Diānas

fraze = input("Ievadiet savu tekstu: ")
ir_nav = fraze.find("nav")
ir_slikts = fraze.rfind("slikts")
#print(ir_nav, ir_slikts)
if ir_nav == -1 or ir_slikts == -1 or ir_nav > ir_slikts:
    print(fraze)
else:
    new_fraze = fraze[:ir_nav] + "ir labs " + fraze[ir_slikts+6+1:]
    print(new_fraze)
