#!/usr/env/bin python3
# -*- coding: utf-8 -*-
"""
Questions for the evaluation of the questionnaire
"""

from classes import Question, QuestionType

# Category (Student, Employee, Professor, External)
G01Q01 = Question(
    'G01Q01',
    'Category',
    {
        'AO01': 'Student',
        'AO02': 'Employee',
        'AO03': 'Professor',
        'AO04': 'External'
    },
    QuestionType.OPTIONS
)

# Faculty (INF, LS, ESB, TEC, TEX, other)
G01Q02 = Question(
    'G01Q02',
    'Faculty',
    {
        'AO01': 'INF',
        'AO02': 'LS',
        'AO03': 'ESB',
        'AO04': 'TEC',
        'AO05': 'TEX',
        '-oth-': 'Other'
    },
    QuestionType.OPTIONS
)

# Exchange-Program (Yes, No)
G01Q03 = Question(
    'G01Q03',
    'Exchange-Program',
    {
        'Y': 'Yes',
        'N': 'No'
    },
    QuestionType.OPTIONS
)

# Older than 26 (Yes, No)
G01Q04 = Question(
    'G01Q04',
    'Older than 26',
    {
        'Y': 'Yes',
        'N': 'No'
    },
    QuestionType.OPTIONS
)

# Knowledge of Deutschlandticket (Very bad to Very good; 4 Options)
G02Q01 = Question(
    'G02Q01',
    'Knowledge of Deutschlandticket',
    {
        'AO01': 'Very bad',
        'AO02': 'Bad',
        'AO03': 'Good',
        'AO04': 'Very good'
    },
    QuestionType.OPTIONS
)

# Knowledge of Vollsolidarmodell (Very bad to Very good; 4 Options)
G02Q02 = Question(
    'G02Q02',
    'Knowledge of Vollsolidarmodell',
    {
        'AO01': 'Very bad',
        'AO02': 'Bad',
        'AO03': 'Good',
        'AO04': 'Very good'
    },
    QuestionType.OPTIONS
)

# Your informed stance on the Deutschlandticket in the full solidarity model (Very opposed to Very supportive; 4 Options)
G03Q01 = Question(
    'G03Q01',
    'Informed opinion on Deutschlandticket',
    {
        'AO01': 'Strongly opposed',
        'AO02': 'Opposed',
        'AO03': 'Supportive',
        'AO04': 'Very supportive'
    },
    QuestionType.OPTIONS
)

# Primary mode of transportation (Car, By foot, Public transportation, Bicycle, Carpooled)
G04Q01 = Question(
    'G04Q01',
    'Primary mode of transportation',
    {
        'AO01': 'Car',
        'AO02': 'By foot',
        'AO03': 'Public transportation',
        'AO04': 'Bicycle',
        'AO05': 'Carpooled'
    },
    type=QuestionType.RANKING,
    ranking_slots=3
)

# Frequency of using public transportation to get to university (Never to Always; 5 Options)
G04Q02 = Question(
    'G04Q02',
    'Frequency of using public transportation to get to university',
    {
        'AO01': 'Never',
        'AO02': 'Fewer than once a week',
        'AO03': 'Once a week',
        'AO04': 'Several times a week',
        'AO05': 'Daily'
    },
    QuestionType.OPTIONS
)

# Frequency of using public transportation otherwise (Never to Always; 5 Options)
G04Q03 = Question(
    'G04Q03',
    'Frequency of using public transportation otherwise',
    {
        'AO01': 'Never',
        'AO02': 'Fewer than once a week',
        'AO03': 'Once a week',
        'AO04': 'Several times a week',
        'AO05': 'Daily'
    },
    QuestionType.OPTIONS
)

# Amount of money spent on transportation per month (0 to 100+; 5 Options)
G04Q04 = Question(
    'G04Q04[SQ001]',
    'Amount of money spent on transportation per month',
    {},
    QuestionType.NUMBER
)

# Distance between home and university (0 to 100+; 5 Options)
G04Q05 = Question(
    'G04Q05[SQ001]',
    'Distance between home and university',
    {},
    QuestionType.NUMBER
)

# Time from home to university (0 to 360+; 5 Options)
G04Q06 = Question(
    'G04Q06[SQ001]',
    'Time from home to university',
    {},
    QuestionType.NUMBER
)

# Current ticket (Deutschlandticket, JugendBW-Ticket, Naldo Semesterticket, Kein vergleichbares Ticket, Sonstiges)
G04Q07 = Question(
    'G04Q07',
    'Do you currently have one of the following tickets?',
    {
        'AO01': 'Deutschlandticket',
        'AO02': 'JugendBW-Ticket',
        'AO03': 'Naldo Semester Ticket',
        'AO04': 'No comparable ticket',
        '-oth-': 'Other'
    },
    QuestionType.OPTIONS
)

# How important is the climate friendliness of your mode of transportation to you? (Not important to Very important; 4 Options)
G05Q01 = Question(
    'G05Q01',
    'How important is the climate friendliness of your mode of transportation to you?',
    {
        'AO01': 'Not important',
        'AO02': 'Less important',
        'AO03': 'Important',
        'AO04': 'Very important'
    },
    QuestionType.OPTIONS
)

# Stance on the named conditions for the full solidarity model: Amount justified?
G06Q01 = Question(
    'G06Q01',
    'Is the Amount reasonable?',
    {
        'Y': 'Yes',
        'N': 'No'
    },
    QuestionType.OPTIONS
)

# Stance on the named conditions for the full solidarity model: What amount is justified?
G06Q02 = Question(
    'G06Q02[SQ001]',
    'Justified amount for the full solidarity model',
    {},
    QuestionType.NUMBER
)

# Stance on the named conditions for the full solidarity model: Fairness (Very unfair to Very fair; 4 Options)
G06Q03 = Question(
    'G06Q03',
    'Stance on the fairness of the full solidarity model',
    {
        'AO01': 'Very unfair',
        'AO02': 'Unfair',
        'AO03': 'Fair',
        'AO04': 'Very fair'
    },
    QuestionType.OPTIONS
)

# Expected impact of having a Deutschlandticket on your mode of transportation (Not at all, A little, Very much; 3 Options)
G07Q01 = Question(
    'G07Q01',
    'Expected impact of having a Deutschlandticket on your mode of transportation',
    {
        'AO01': 'Not at all',
        'AO02': 'A little',
        'AO03': 'Very much'
    },
    QuestionType.OPTIONS
)

# Your idea for an alternative
G08Q01 = Question(
    'G08Q01',
    'Your idea for an alternative',
    {},
    QuestionType.TEXT
)
