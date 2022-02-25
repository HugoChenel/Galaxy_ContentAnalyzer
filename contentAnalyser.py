#!/bin/env python

import argparse
import csv

parser = argparse.ArgumentParser(description='Count occurences of either nucleotides or peptides in fasta files containing multiple sequences. This tool also provides information about purine and pyrimidine rates for nucleotides files or amino acid counts in groups. ')
parser.add_argument('--input', '-i', type=str, help="input file", required = True)
parser.add_argument('--output', '-o', type=str, help="output file", required = True)
parser.add_argument('--type', '-t', type=str, help="input type : nucleotide or peptide", required = True)
args = parser.parse_args()


if args.type == 'nucleotide':
    with open(args.input, 'r') as inputfile:
            contents = inputfile.readlines()
            dico = {}
            for line in contents:
                if line[0] == '>':
                    dicoSequence = {}
                    sequenceName = line.strip()
                    countA, countT, countC, countG, countPurines, countPyrimidines, countAT, countCG, countU = 0, 0, 0, 0, 0, 0, 0, 0, 0
                if line[0] != '>':
                    for el in line:
                        if el == 'a' or el == 'A' : countA += 1
                        elif el == 't' or el == 'T' : countT += 1
                        elif el == 'c' or el == 'C' : countC += 1
                        elif el == 'g' or el == 'G' : countG += 1
                        elif el == 'u' or el == 'U' : countU += 1
                    dicoSequence['name'] = sequenceName
                    dicoSequence['a'] = countA
                    dicoSequence['t'] = countT
                    dicoSequence['c'] = countC
                    dicoSequence['g'] = countG
                    dicoSequence['u'] = countU
                    dicoSequence['length'] = countA + countT + countC + countG + countU
                    dicoSequence['at'] = ( countA + countT + countU) / (countA + countT + countC + countG + countU) 
                    dicoSequence['cg'] = ( countC + countG ) / (countA + countT + countC + countG + countU)
                    dicoSequence['purines'] = countA + countG
                    dicoSequence['pyrimidines'] = countT + countC + countU
                dico[sequenceName] = dicoSequence


    with open(args.output, 'wt') as out_file:
        out_file.write("Seq_name\tA\tT\tC\tG\tU\tlength\tat\tcg\tpurines\tpyrimidines\n")        
        for seq in dico.keys():
            out_file.write("%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\n"%(dico[seq]['name'], dico[seq]['a'], dico[seq]['t'], dico[seq]['c'], dico[seq]['g'], 
            dico[seq]['u'], dico[seq]['length'], dico[seq]['at'], dico[seq]['cg'], dico[seq]['purines'], dico[seq]['pyrimidines']))

if args.type == 'peptide':
    with open(args.input, 'r') as inputfile:
            contents = inputfile.readlines()
            dico = {}
            for line in contents:
                if line[0] == '>':
                    dicoSequence = {}
                    sequenceName = line.strip()
                    countA, countR, countN, countD, countC, countQ, countE, countG, countH, countI, countL, countK, countM, countF, countP, countS, countT, countW, countY, countV = 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0
                if line[0] != '>':
                    for el in line:
                        if el == 'A': countA += 1
                        elif el == 'R': countR += 1
                        elif el == 'N': countN += 1
                        elif el == 'D' : countD += 1
                        elif el == 'C' : countC += 1
                        elif el == 'Q': countQ += 1
                        elif el == 'E': countE += 1
                        elif el == 'G' : countG += 1
                        elif el == 'H' : countH += 1
                        elif el == 'I': countI += 1
                        elif el == 'L': countL += 1
                        elif el == 'K' : countK += 1
                        elif el == 'M' : countM += 1
                        elif el == 'F': countF += 1
                        elif el == 'P': countP += 1
                        elif el == 'S' : countS += 1
                        elif el == 'T' : countT += 1
                        elif el == 'W': countW += 1
                        elif el == 'Y': countY += 1
                        elif el == 'V' : countV += 1
                    dicoSequence['name'] = sequenceName
                    dicoSequence['A'] = countA
                    dicoSequence['R'] = countR
                    dicoSequence['N'] = countN
                    dicoSequence['D'] = countD
                    dicoSequence['C'] = countC
                    dicoSequence['Q'] = countQ
                    dicoSequence['E'] = countE
                    dicoSequence['G'] = countG
                    dicoSequence['H'] = countH
                    dicoSequence['I'] = countI
                    dicoSequence['L'] = countL
                    dicoSequence['K'] = countK
                    dicoSequence['M'] = countM
                    dicoSequence['F'] = countF
                    dicoSequence['P'] = countP
                    dicoSequence['S'] = countS
                    dicoSequence['T'] = countT
                    dicoSequence['W'] = countW
                    dicoSequence['Y'] = countY
                    dicoSequence['V'] = countV
                    dicoSequence['Nonpolar'] = countG + countA + countV + countL + countI + countM + countP + countF 
                    dicoSequence['Aliphatic'] = countL + countI + countV
                    dicoSequence['Aromatic'] = countF + countY + countW + countH
                    dicoSequence['Acidic'] = countN + countQ
                    dicoSequence['Basic'] = countR + countK + countH
                    dicoSequence['Hydroxylic'] = countS + countT                    
                    dicoSequence['Sulphuric'] = countM + countC
                    dicoSequence['Amide'] = countN + countQ
                    dicoSequence['Hydrophobic'] = countA + countV + countL + countI + countM + countY + countW + countF
                    dicoSequence['Polar'] = countC + countS + countT + countN + countQ + countD + countE + countH + countK + countR + countY + countW
                    dicoSequence['Charged'] = countH + countK + countR + countD + countE
                    dicoSequence['Length'] = countA + countR + countN + countD+ countC+ countQ+ countE+ countG+ countH+ countI+ countL+ countK+ countM+ countF+ countP+ countS+ countT+ countW+ countY+ countV
                dico[sequenceName] = dicoSequence

    with open(args.output, 'wt') as out_file:
        out_file.write("Seq_name\tA\tR\tN\tD\tC\tQ\tE\tG\tH\tI\tL\tK\tM\tF\tP\tS\tT\tW\tY\tV\tAliphatic\tAromatic\tAcidic\tBasic\tHydroxylic\tSulphuric\tAmide\tHydrophobic\tPolar\tNonpolar\tCharged\tLength\n")        
        for seq in dico.keys():
            out_file.write("%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\n"
            %(dico[seq]['name'], dico[seq]['A'], dico[seq]['R'], dico[seq]['N'], dico[seq]['D'], dico[seq]['C'], dico[seq]['Q'], dico[seq]['E'], dico[seq]['G'], dico[seq]['H'], dico[seq]['I'], dico[seq]['L'], 
            dico[seq]['K'], dico[seq]['M'], dico[seq]['F'], dico[seq]['P'], dico[seq]['S'], dico[seq]['T'], dico[seq]['W'], dico[seq]['Y'], dico[seq]['V'], 
            dico[seq]['Aliphatic'], dico[seq]['Aromatic'], dico[seq]['Acidic'], dico[seq]['Basic'], dico[seq]['Hydroxylic'], dico[seq]['Sulphuric'], dico[seq]['Amide'], dico[seq]['Hydrophobic'], 
            dico[seq]['Polar'], dico[seq]['Nonpolar'], dico[seq]['Charged'], dico[seq]['Length']))