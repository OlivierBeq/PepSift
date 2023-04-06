# -*- coding: utf-8 -*-

"""Constants for unit tests."""

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