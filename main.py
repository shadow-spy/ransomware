#!/usr/bin/python3
# coding: utf-8

import os
from NomDuDossierModule.Network import yohann_smtp
from NomDuDossierModule.Chiffrement import yohann_crypt

utilisateur_courant = os.environ["USERNAME"]

# MAIN SCRIPT HERE !
yohann_crypt.creation_de_la_clef(utilisateur_courant)
