#!/usr/env/bin python3
# -*- coding: utf-8 -*-
"""
Questions for the evaluation of the questionnaire
"""

from classes import Question


G04Q01 = Question(
    'G04Q01',
    'Primary mode of transportation',
    {
        'AO01': 'Car',
        'AO02': 'By foot',
        'AO03': 'Public transportation',
        'AO04': 'Bicycle',
        'AO05': 'Carpooled'
    }
)

G01Q02 = Question(
    'G01Q02',
    'Faculty',
    {
        'AO01': 'INF',
        'AO02': 'LS',
        'AO03': 'ESB',
        'AO04': 'TEC',
        'AO05': 'TEX',
        'AO06': 'other'
    }
)

G04Q07 = Question(
    'G04Q07',
    'Do you currently have one of the following tickets?',
    {
        'AO01': 'Deutschlandticket',
        'AO02': 'JugendBW-Ticket',
        'AO03': 'Naldo Semesterticket',
        'AO04': 'Kein vergleichbares Ticket',
        'AO05': 'Sonstiges'
    }
)