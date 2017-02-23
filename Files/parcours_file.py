#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Module parcours de fichier
----------------------------------------


"""
import calendar
from datetime import datetime

montant_max = 0
montant_max_jeudi = 0
jours_semaine = {
    calendar.MONDAY : 'Lundi', calendar.TUESDAY : 'Mardi', calendar.WEDNESDAY : 'Mercredi',
    calendar.THURSDAY : 'Jeudi', calendar.FRIDAY : 'Vendredi', calendar.SATURDAY : 'Samedi',
    calendar.SUNDAY : 'Dimanche'
}


with open('/home/stagiaire/PycharmProjects/perso/Python-perso/assets/comptage-voyageurs-trains-transilien.csv', 'r') as file:
    file.readline() # Exclude the Header line from process
    for line in file:
        #print(line)
        list_chanmp = line.replace('\n', '').split(';')
        montant = 0 if list_chanmp[-1] == 'Montants' else int(list_chanmp[-1])
        if montant > montant_max:
            montant_max = montant
            result = line
        line_date = datetime.strptime(list_chanmp[3], '%Y-%m-%d')
        week_day = calendar.weekday(line_date.year,line_date.month, line_date.day)
        if week_day == 3:
            print(jours_semaine[week_day])
            montant_jeudi = int(list_chanmp[-1])
            if montant_jeudi > montant_max_jeudi:
                montant_max_jeudi = montant_jeudi
                result_jeudi = line

print(result)
print(result_jeudi)