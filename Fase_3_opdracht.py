# Python Script.py microarray probes sample cutoff hersenplek1 hersenplek2 gene_symbol

"""
Een aantal stappen doorlopen om de probe IDs om te zetten naar gen-informatie en vervolgens analyses uit te voeren

1. Write code that will translate any given probe id to a gene name, gene symbol, entrez id and chromosome.
2. Bereken het gemiddelde van de probe-expressies en selecteer per gen de meest representatieve probe.
3. Zoek de unieke en gedeelde probes tussen hersenregio's (LHM en PHA).
4. Filter op basis van een cutoff-waarde voor expressie.

De laterale hypothalamus (LHA) is een hersengebied dat betrokken is bij verschillende functies, zoals het reguleren van eetgedrag, motivatie, en beloningsprocessen. 
Dit gebied speelt een belangrijke rol in het integreren van signalen die te maken hebben met honger en verzadiging.

Het posterior hypothalamusgebied (PHA) is een gebied in de achterste hypothalamus, dat betrokken is bij autonome functies, 
zoals het reguleren van lichaamstemperatuur, bloeddruk en andere homeostatische processen. Het speelt ook een rol bij de stressreactie.

stap 1:
Laad de gegevens: De CSV wordt geladen in een DataFrame.
Vertaal functie: De functie translate_probe neemt een probe_id, zoekt het in de DataFrame en retourneert de bijbehorende geninformatie.
Voorbeeld van gebruik: Je kunt de functie aanroepen met een specifieke probe-ID om de geninformatie te verkrijgen.

"""

import sys


def lines_van_bestand(data):

    lijst = []

    with open(data, "r") as tekstbestand:
        for line in tekstbestand:
            line = line.strip("\n")
            lijst.append(line)
    return lijst


def probe_id_lijst_maken(lijst):

    probe_id_lijst = []
    for line in lijst
        probe_id_lijst.append(float(line[2]))

    return probe_id_lijst



def main():

    data = "Probes.csv"
    probe_id_lijst_maken(data)
    print(data)
    print(probe_id_lijst)


main()