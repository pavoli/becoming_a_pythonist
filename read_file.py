# -*- coding: utf-8 -*-
#! /usr/local/bin/python3
__author__ = 'p.olifer'


import os
import io

PRC_15 = 'PR_GCS_015'
PRC_19 = 'PR_GCS_019'
FILE_NAME = 'C:/git/pda/RFHMR/Backup/CKDCase/CaseFeeding.asp'

try:
    with open(FILE_NAME, encoding="utf-8", errors='ignore') as file:
        # print(file.readlines())
        for i in file.readlines():
            if i.rstrip():
                print(i)
except FileNotFoundError as e:
    pass