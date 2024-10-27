# Python Script.py microarray probes sample cutoff hersenplek1 hersenplek2 gene_symbol


import sys


def lines_van_bestand(data):
    lijst = []

    with open(data, "r") as tekstbestand:
        tekstbestand.readline()  # haalt header eruit

        for line in tekstbestand:
            line = line.strip("\n")
            line = line.split(",")
            lijst.append(line)

    return lijst


def gene_probe_pairs_maken(lijst):
    pairs_lijst = []

    for line in lijst:
        pairs_lijst.append([line[0], line[2]])

    return pairs_lijst


def dict_gene_en_zijn_probes(gene_probe_pairs):
    gene_dict = {}


    for probe_id, gene_id in gene_probe_pairs:
        if gene_id in gene_dict:
            # Voeg de probe_id toe aan de bestaande lijst
            gene_dict[gene_id].append(probe_id)
        else:
            # Maak een nieuwe lijst aan met de eerste probe_id
            gene_dict[gene_id] = [probe_id]

    return gene_dict


def main():
    print("test")
    data = "Probes.csv"
    lijst = lines_van_bestand(data)

    geneprobe_pairs = gene_probe_pairs_maken(lijst)
    gene_dict = dict_gene_en_zijn_probes(geneprobe_pairs)

    print(gene_dict)

main()

