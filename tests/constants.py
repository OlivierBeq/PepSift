# -*- coding: utf-8 -*-

"""Constants for unit tests."""
import os.path

from rdkit import Chem
from rdkit.Chem.SaltRemover import SaltRemover


MOLECULES = {
    '5N1NAPHT': Chem.MolFromSmiles("NC1=CC=CC2=C1C=CC=C2C(=O)O"),
    'NAPHT': Chem.MolFromSmiles("C1=CC=C2C=CC=CC2=C1 ")
}

STANDARD_AA = {
  'Ala': Chem.MolFromSmiles("C[C@@H](C(=O)O)N"),
  'Arg': Chem.MolFromSmiles("C(C[C@@H](C(=O)O)N)CN=C(N)N"),
  'Asn': Chem.MolFromSmiles("C([C@@H](C(=O)O)N)C(=O)N"),
  'Asp': Chem.MolFromSmiles("C([C@@H](C(=O)O)N)C(=O)O"),
  'Cys': Chem.MolFromSmiles("C([C@@H](C(=O)O)N)S"),
  'Gln': Chem.MolFromSmiles("C(CC(=O)N)[C@@H](C(=O)O)N"),
  'Glu': Chem.MolFromSmiles("C(CC(=O)O)[C@@H](C(=O)O)N"),
  'Gly': Chem.MolFromSmiles("C(C(=O)O)N"),
  'Hid': Chem.MolFromSmiles("C1=C(NC=N1)C[C@@H](C(=O)O)N"),
  'Hie': Chem.MolFromSmiles("C1=C(N=CN1)C[C@@H](C(=O)O)N"),
  'Hip': Chem.MolFromSmiles("C1=C([N+]=CN1)C[C@@H](C(=O)O)N"),
  'Ile': Chem.MolFromSmiles("CC[C@H](C)[C@@H](C(=O)O)N"),
  'Leu': Chem.MolFromSmiles("CC(C)C[C@@H](C(=O)O)N"),
  'Lys': Chem.MolFromSmiles("C(CCN)C[C@@H](C(=O)O)N"),
  'Met': Chem.MolFromSmiles("CSCC[C@@H](C(=O)O)N"),
  'Phe': Chem.MolFromSmiles("C1=CC=C(C=C1)C[C@@H](C(=O)O)N"),
  'Pro': Chem.MolFromSmiles("C1C[C@H](NC1)C(=O)O"),
  'Ser': Chem.MolFromSmiles("C([C@@H](C(=O)O)N)O"),
  'Thr': Chem.MolFromSmiles("C[C@H]([C@@H](C(=O)O)N)O"),
  'Trp': Chem.MolFromSmiles("C1=CC=C2C(=C1)C(=CN2)C[C@@H](C(=O)O)N"),
  'Tyr': Chem.MolFromSmiles("C1=CC(=CC=C1C[C@@H](C(=O)O)N)O"),
  'Val': Chem.MolFromSmiles("CC(C)[C@@H](C(=O)O)N"),
}

LBHOMO_AA = {
    'LBhomo-Ala': Chem.MolFromSmiles("C[C@@H](CN)C(=O)O"),
    'LBhomo-Arg': Chem.MolFromSmiles("[H][C@](CN)(CCCN=C(N)N)C(=O)O"),
    'LBhomo-Asn': Chem.MolFromSmiles("[H][C@](CN)(CC(N)=O)C(=O)O"),
    'LBhomo-Asp': Chem.MolFromSmiles("[H][C@](CN)(CC(=O)O)C(=O)O"),
    'LBhomo-Cys': Chem.MolFromSmiles("[H][C@](CN)(CS)C(=O)O"),
    'LBhomo-Gln': Chem.MolFromSmiles("[H][C@](CN)(CCC(N)=O)C(=O)O"),
    'LBhomo-Glu': Chem.MolFromSmiles("[H][C@](CN)(CCC(=O)O)C(=O)O"),
    'LBhomo-Gly': Chem.MolFromSmiles("NCCC(=O)O"),
    'LBhomo-Hid': Chem.MolFromSmiles("[H][C@](CN)(CC1=CN=CN1)C(=O)O"),
    'LBhomo-Hie': Chem.MolFromSmiles("[H][C@](CN)(CC1=CNC=N1)C(=O)O"),
    'LBhomo-Hip': Chem.MolFromSmiles("[H][C@](CN)(CC1=CNC=[NH+]1)C(=O)O"),
    'LBhomo-Ile': Chem.MolFromSmiles("[H][C@@](CN)(C(=O)O)[C@@H](C)CC"),
    'LBhomo-Leu': Chem.MolFromSmiles("[H][C@](CN)(CC(C)C)C(=O)O"),
    'LBhomo-Lys': Chem.MolFromSmiles("[H][C@](CN)(CCCCN)C(=O)O"),
    'LBhomo-Met': Chem.MolFromSmiles("[H][C@](CN)(CCSC)C(=O)O"),
    'LBhomo-Phe': Chem.MolFromSmiles("[H][C@](CN)(CC1=CC=CC=C1)C(=O)O"),
    'LBhomo-Pro': Chem.MolFromSmiles("[H][C@@]1(CC(=O)O)CCCN1"),
    'LBhomo-Ser': Chem.MolFromSmiles("[H][C@](CN)(CO)C(=O)O"),
    'LBhomo-Thr': Chem.MolFromSmiles("[H][C@@](CN)(C(=O)O)[C@@H](C)O"),
    'LBhomo-Trp': Chem.MolFromSmiles("[H][C@](CN)(CC1=CNC2=C1C=CC=C2)C(=O)O"),
    'LBhomo-Tyr': Chem.MolFromSmiles("[H][C@](CN)(CC1=CC=C(O)C=C1)C(=O)O"),
    'LBhomo-Val': Chem.MolFromSmiles("[H][C@@](CN)(C(=O)O)C(C)C"),
}

AMHETYL_AA = {
    'Amethyl-Ala': Chem.MolFromSmiles("CC(C)(C(=O)O)N"),
    'Amethyl-Arg': Chem.MolFromSmiles("C(CC(C)(C(=O)O)N)CN=C(N)N"),
    'Amethyl-Asn': Chem.MolFromSmiles("C(C(C)(C(=O)O)N)C(=O)N"),
    'Amethyl-Asp': Chem.MolFromSmiles("C(C(C)(C(=O)O)N)C(=O)O"),
    'Amethyl-Cys': Chem.MolFromSmiles("C(C(C)(C(=O)O)N)S"),
    'Amethyl-Gln': Chem.MolFromSmiles("C(CC(=O)N)C(C)(C(=O)O)N"),
    'Amethyl-Glu': Chem.MolFromSmiles("C(CC(=O)O)C(C)(C(=O)O)N"),
    'Amethyl-Hid': Chem.MolFromSmiles("C1=C(NC=N1)CC(C)(C(=O)O)N"),
    'Amethyl-Hie': Chem.MolFromSmiles("C1=C(N=CN1)CC(C)(C(=O)O)N"),
    'Amethyl-Hip': Chem.MolFromSmiles("C1=C([N+]=CN1)CC(C)(C(=O)O)N"),
    'Amethyl-Ile': Chem.MolFromSmiles("CC[C@H](C)C(C)(C(=O)O)N"),
    'Amethyl-Leu': Chem.MolFromSmiles("CC(C)CC(C)(C(=O)O)N"),
    'Amethyl-Lys': Chem.MolFromSmiles("C(CCN)CC(C)(C(=O)O)N"),
    'Amethyl-Met': Chem.MolFromSmiles("CSCCC(C)(C(=O)O)N"),
    'Amethyl-Phe': Chem.MolFromSmiles("C1=CC=C(C=C1)CC(C)(C(=O)O)N"),
    'Amethyl-Pro': Chem.MolFromSmiles("C1CC(C)(NC1)C(=O)O"),
    'Amethyl-Ser': Chem.MolFromSmiles("C(C(C)(C(=O)O)N)O"),
    'Amethyl-Thr': Chem.MolFromSmiles("C[C@H](C(C)(C(=O)O)N)O"),
    'Amethyl-Trp': Chem.MolFromSmiles("C1=CC=C2C(=C1)C(=CN2)CC(C)(C(=O)O)N"),
    'Amethyl-Tyr': Chem.MolFromSmiles("C1=CC(=CC=C1CC(C)(C(=O)O)N)O"),
    'Amethyl-Val': Chem.MolFromSmiles("CC(C)C(C)(C(=O)O)N"),
}

# Amino acids from Sandberg M. et al. (1998), J. Med. Chem., 41(14)
ADDITIONAL_AA = {
    "alpha-aminocaprylic acid": Chem.MolFromSmiles("CCCCCCC(C(=O)O)N"),
    "(S)-2-aminoethyl-L-cysteine": Chem.MolFromSmiles("C(CSC[C@@H](C(=O)O)N)N"),
    "aminophenylacetate": Chem.MolFromSmiles("OC(=O)CC1=CC=C(C=C1)N"),
    "alpha-aminoisobytyric acid": Chem.MolFromSmiles("CC(C)(C(=O)O)N"),
    "alloisoleucine": Chem.MolFromSmiles("CC[C@@H](C)[C@@H](C(=O)O)N"),
    "L-allylglycine": Chem.MolFromSmiles("C=CC[C@@H](C(=O)O)N"),
    "alpha-aminobutyric acid": Chem.MolFromSmiles("CCC(C(=O)O)N"),
    "p-aminophenylalanine": Chem.MolFromSmiles("C1=CC(=CC=C1C[C@@H](C(=O)O)N)N"),
    "beta-alanine": Chem.MolFromSmiles("C(CN)C(=O)O"),
    "p-bromophenylalanine": Chem.MolFromSmiles("C1=CC(=CC=C1C[C@@H](C(=O)O)N)Br"),
    "cyclohexylalanine": Chem.MolFromSmiles("C[C@@H](C(=O)O)NC1CCCCC1"),
    "citrulline": Chem.MolFromSmiles("C(C[C@@H](C(=O)O)N)CNC(=O)N"),
    "beta-chloroalanine": Chem.MolFromSmiles("C(C(C(=O)O)N)Cl"),
    "cycloleucine": Chem.MolFromSmiles("C1CCC(C1)(C(=O)O)N"),
    "p-chlorophenylalanine": Chem.MolFromSmiles("C1=CC(=CC=C1CC(C(=O)O)N)Cl"),
    "cysteic acid": Chem.MolFromSmiles("C(C(C(=O)O)N)S(=O)(=O)O"),
    "2,4-diaminobutyric acid": Chem.MolFromSmiles("C(CN)C(C(=O)O)N"),
    "2,3-diaminopropionic acid": Chem.MolFromSmiles("C(C(C(=O)O)N)N"),
    "3,4-dehydroproline": Chem.MolFromSmiles("C1C=CC(N1)C(=O)O"),
    "3,4-dihydroxyphenylalanine": Chem.MolFromSmiles("C1=CC(=C(C=C1C[C@@H](C(=O)O)N)O)O"),
    "p-fluorophenylalanine": Chem.MolFromSmiles("C1=CC(=CC=C1CC(C(=O)O)N)F"),
    "D-glucosaminic acid": Chem.MolFromSmiles("C([C@H]([C@H]([C@@H]([C@H](C(=O)O)N)O)O)O)O  "),
    "homoarginine": Chem.MolFromSmiles("C(CCN=C(N)N)C[C@@H](C(=O)O)N"),
    "delta-hydroxylysine": Chem.MolFromSmiles("C(C[C@@H](C(=O)O)N)[C@H](CN)O"),
    "DL-beta-hydroxynorvaline": Chem.MolFromSmiles("CCC(C(C(=O)O)N)O"),
    "homoglutamine": Chem.MolFromSmiles("C(CC(C(=O)O)N)CC(=O)N"),
    "homophenylalanine": Chem.MolFromSmiles("C1=CC=C(C=C1)CC[C@@H](C(=O)O)N"),
    "homoserine": Chem.MolFromSmiles("C(CO)C(C(=O)O)N"),
    "hydroxyproline": Chem.MolFromSmiles("C1[C@H](CN[C@@H]1C(=O)O)O"),
    "p-iodophenylalanine": Chem.MolFromSmiles("C1=CC(=CC=C1C[C@@H](C(=O)O)N)I"),
    "isoserine": Chem.MolFromSmiles("C(C(C(=O)O)O)N"),
    "alpha-methylleucine": Chem.MolFromSmiles("CC(C)C[C@@](C)(C(=O)O)N"),
    "DL-methionine-s-methylsulfoniumchloride": Chem.MolFromSmiles("C[S+](C)CCC(C(=O)O)N"),
    "3-(1-naphthyl)alanine": Chem.MolFromSmiles("C1=CC=C2C(=C1)C=CC=C2CC(C(=O)O)N"),
    "3-(2-naphthyl)alanine": Chem.MolFromSmiles("C1=CC=C2C=C(C=CC2=C1)C[C@@H](C(=O)O)N"),
    "norleucine": Chem.MolFromSmiles("CCCC[C@@H](C(=O)O)N"),
    "N-methylalanine": Chem.MolFromSmiles("C[C@@H](C(=O)O)NC"),
    "norvaline": Chem.MolFromSmiles("CCC[C@@H](C(=O)O)N"),
    "O-benzylserine": Chem.MolFromSmiles("C1=CC=C(C=C1)COCC(C(=O)O)N"),
    "O-benzyltyrosine": Chem.MolFromSmiles("C1=CC=C(C=C1)COC2=CC=C(C=C2)CC(C(=O)O)N"),
    "O-ethyltyrosine": Chem.MolFromSmiles("CCC1=C(C=CC(=C1)O)C[C@@H](C(=O)O)N"),
    "O-methylserine": Chem.MolFromSmiles("COC[C@@H](C(=O)O)N"),
    "O-methylthreonine": Chem.MolFromSmiles("C[C@H]([C@@H](C(=O)O)N)OC"),
    "O-methyltyrosine": Chem.MolFromSmiles("COC1=CC=C(C=C1)CC(C(=O)O)N"),
    "ornithine": Chem.MolFromSmiles("C(C[C@@H](C(=O)O)N)CN"),
    "penicillamine": Chem.MolFromSmiles("CC(C)([C@H](C(=O)O)N)S"),
    "pyroglutamic acid": Chem.MolFromSmiles("C1CC(=O)N[C@@H]1C(=O)O"),
    "pipecolic acid": Chem.MolFromSmiles("C1CCNC(C1)C(=O)O"),
    "sarcosine": Chem.MolFromSmiles("CNCC(=O)O"),
    "3,3,3-trifluoroalanine": Chem.MolFromSmiles("C(C(=O)O)(C(F)(F)F)N"),
    "6-hydroxydopa": Chem.MolFromSmiles("C1=C(C(=CC(=C1O)O)O)CC(C(=O)O)N"),
    "L-vinylglycine": Chem.MolFromSmiles("C=C[C@@H](C(=O)O)N"),
    "(-)-(2R)-2-amino-3-(2-aminoethylsulfonyl)propanoic acid dihydrochloride": Chem.MolFromSmiles("C(CS(=O)(=O)C[C@@H](C(=O)O)N)N"),
    "(2S)-2-amino-9-hydroxy-4,7-dioxanonanoic acid": Chem.MolFromSmiles("N[C@H](C(=O)O)COCCOCCO"),
    "(2S)-2-amino-6-hydroxy-4-oxahexanoic acid": Chem.MolFromSmiles("N[C@H](C(=O)O)COCCO"),
    "(-)-(2R)-2-amino-3-(2-hydroxyethylsulfonyl)propanoic acid": Chem.MolFromSmiles("C(CS(=O)(=O)C[C@@H](C(=O)O)N)O"),
    "(-)-(2R)-2-amino-3-(2-hydroxyethylsulfanyl)propanoic acid": Chem.MolFromSmiles("N[C@H](C(=O)O)CSCCO"),
    "(2S)-2-amino-12-hydroxy-4,7,10-trioxadodecanoic acid": Chem.MolFromSmiles("N[C@H](C(=O)O)COCCOCCOCCO"),
    "(2S)-2,9-diamino-4,7- dioxanonanoic acid": Chem.MolFromSmiles("N[C@H](C(=O)O)COCCOCCN"),
    "(2S)-2,12-diamino-4,7,10- trioxadodecanoic acid": Chem.MolFromSmiles("N[C@H](C(=O)O)COCCOCCOCCN"),
    "(S)-5,5-difluoronorleucine": Chem.MolFromSmiles("FC(CC[C@H](N)C(=O)O)(C)F"),
    "(S)-4,4-difluoronorvaline": Chem.MolFromSmiles("FC(C[C@H](N)C(=O)O)(C)F"),
    "(3R)-1-1-dioxo-[1,4]thiaziane-3-carboxylic acid": Chem.MolFromSmiles("C1CS(=O)CC(N1)C(=O)O"),
    "(S)-4,4,5,5,6,6,6-heptafluoronorleucine": Chem.MolFromSmiles("FC(C[C@H](N)C(=O)O)(C(C(F)(F)F)(F)F)F"),
    "(S)-5,5,6,6,6-pentafluoronorleucine": Chem.MolFromSmiles("FC(CC[C@H](N)C(=O)O)(C(F)(F)F)F"),
    "(S)-4,4,5,5,5-pentafluoronorvaline": Chem.MolFromSmiles("FC(C[C@H](N)C(=O)O)(C(F)(F)F)F"),
    "(3R)-1,4-thiazinane-3-carboxylic acid": Chem.MolFromSmiles("S1C[C@H](NCC1)C(=O)O"),
}

# Pat Walters's HIV molecule list from https://github.com/PatWalters/rd_filters/
ADDITIONAL_MOLECULES = [mol for mol in Chem.SmilesMolSupplier(os.path.abspath(os.path.join(__file__,
                                                                                           os.pardir,
                                                                                        './HIV.smi')))
                       if mol is not None]
