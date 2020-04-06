import webbrowser

new = 2

URL="https://www.olx.ro/auto-masini-moto-ambarcatiuni/autoturisme/"


qmodel= input("Doresti o masina specifica?\n")
if(qmodel == "Da" or qmodel == "da" or qmodel == "dA"):
    model = input("\nCe model doresti sa cauti? (scrie cu litere mici!)\n")
    ok=1
    filtre = input("\nDoresti sa adaugi si filtre?\n")
    Link= URL+model
    if filtre == "Da" or filtre == "da" or filtre == "dA":

        qpretmin = input("\nDoresti sa pui un pret minim?\n")
        if qpretmin == "Da" or qpretmin == "da" or qpretmin == "dA":
            sq1= "search%5Bfilter_float_price%3Afrom%5D="
            pretmin = input("\nCare este pretul minim?\n")
            if(ok == 1):
                Link= Link + "?" + sq1 + pretmin + "&"
            else:
                Link= Link + sq1 + pretmin + "&"
            ok=ok+1


        qpretmax = input("\nDoresti sa pui un pret maxim?\n")
        if qpretmax == "Da" or qpretmax == "da" or qpretmax == "dA":
            sq1= "search%5Bfilter_float_price%3Ato%5D="
            pretmax = input("\nCare este pretul maxim\n")
            if(ok == 1):
                Link= Link + "?" + sq1 + pretmax + "&"
            else:
                Link= Link + sq1 + pretmax + "&"
            ok=ok+1


        qcapacitatemotormin = input("\nDoresti sa pui capacitatea minima?\n")
        if qcapacitatemotormin == "Da" or qcapacitatemotormin == "da" or qcapacitatemotormin == "dA":
            sq1= "search%5Bfilter_float_enginesize%3Afrom%5D="
            capacitatemotormin = input("\nCapacitate motor de la:\n")
            if(ok == 1):
                Link= Link + "?" + sq1 + capacitatemotormin + "&"
            else:
                Link= Link + sq1 + capacitatemotormin + "&"
            ok=ok+1


        qcapacitatemotormax = input("\nDoresti sa pui capacitatea maxima?\n")
        if qcapacitatemotormax == "Da" or qcapacitatemotormax == "da" or qcapacitatemotormax == "dA":
            sq1= "search%5Bfilter_float_enginesize%3Ato%5D="
            capacitatemotormax = input("\nCapacitate motor pana la:\n")
            if(ok == 1):
                Link= Link + "?" + sq1 + capacitatemotormax + "&"
            else:
                Link= Link + sq1 + capacitatemotormax + "&"
            ok=ok+1


        qanmin = input("\nDoresti sa pui un an minim?\n")
        if qanmin == "Da" or qanmin == "da" or qanmin == "dA":
            sq1= "search%5Bfilter_float_year%3Afrom%5D="
            anmin = input("\nAnul de la:\n")
            if(ok == 1):
                Link= Link + "?" + sq1 + anmin + "&"
            else:
                Link= Link + sq1 + anmin + "&"
            ok=ok+1


        qanmax = input("\nDoresti sa pui un an maxim?\n")
        if qanmax == "Da" or qanmax == "da" or qanmax == "dA":
            sq1= "search%5Bfilter_float_year%3Ato%5D="
            anmax = input("\nAnul pana la:\n")
            if(ok == 1):
                Link= Link + "?" + sq1 + anmax + "&"
            else:
                Link= Link + sq1 + anmax + "&"
            ok=ok+1
        

        webbrowser.open(Link[:-1], new=new)
        

    else:
        webbrowser.open(URL+model, new=new)

else:
    filtre = input("\nDoresti sa adaugi filtre?\n")
    ok=1
    Link= URL
    if filtre == "Da" or filtre == "da" or filtre == "dA":

        qpretmin = input("\nDoresti sa pui un pret minim?\n")
        if qpretmin == "Da" or qpretmin == "da" or qpretmin == "dA":
            sq1= "search%5Bfilter_float_price%3Afrom%5D="
            pretmin = input("\nCare este pretul minim?\n")
            if(ok == 1):
                Link= Link + "?" + sq1 + pretmin + "&"
            else:
                Link= Link + sq1 + pretmin + "&"
            ok=ok+1


        qpretmax = input("\nDoresti sa pui un pret maxim?\n")
        if qpretmax == "Da" or qpretmax == "da" or qpretmax == "dA":
            sq1= "search%5Bfilter_float_price%3Ato%5D="
            pretmax = input("\nCare este pretul maxim\n")
            if(ok == 1):
                Link= Link= Link + "?" + sq1 + pretmax + "&"
            else:
                Link= Link + sq1 + pretmax + "&"
            ok=ok+1


        qcapacitatemotormin = input("\nDoresti sa pui capacitatea minima?\n")
        if qcapacitatemotormin == "Da" or qcapacitatemotormin == "da" or qcapacitatemotormin == "dA":
            sq1= "search%5Bfilter_float_enginesize%3Afrom%5D="
            capacitatemotormin = input("\nCapacitate motor de la:\n")
            if(ok == 1):
                Link= Link + "?" + sq1 + capacitatemotormin + "&"
            else:
                Link= Link + sq1 + capacitatemotormin + "&"
            ok=ok+1


        qcapacitatemotormax = input("\nDoresti sa pui capacitatea maxima?\n")
        if qcapacitatemotormax == "Da" or qcapacitatemotormax == "da" or qcapacitatemotormax == "dA":
            sq1= "search%5Bfilter_float_enginesize%3Ato%5D="
            capacitatemotormax = input("\nCapacitate motor pana la:\n")
            if(ok == 1):
                Link= Link + "?" + sq1 + capacitatemotormax + "&"
            else:
                Link= Link + sq1 + capacitatemotormax + "&"
            ok=ok+1


        qanmin = input("\nDoresti sa pui un an minim?\n")
        if qanmin == "Da" or qanmin == "da" or qanmin == "dA":
            sq1= "search%5Bfilter_float_year%3Afrom%5D="
            anmin = input("\nAnul de la:\n")
            if(ok == 1):
                Link= Link + "?" + sq1 + anmin + "&"
            else:
                Link= Link + sq1 + anmin + "&"
            ok=ok+1


        qanmax = input("\nDoresti sa pui un an maxim?\n")
        if qanmax == "Da" or qanmax == "da" or qanmax == "dA":
            sq1= "search%5Bfilter_float_year%3Ato%5D="
            anmax = input("\nAnul pana la:\n")
            if(ok == 1):
                Link= Link + "?" + sq1 + anmax + "&"
            else:
                Link= Link + sq1 + anmax + "&"
            ok=ok+1
        

        webbrowser.open(Link[:-1], new=new)

    else:
        webbrowser.open(Link[:-1], new=new)
