#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Classes for the evaluation of the questionnaire
"""

from enum import Enum
from typing import Any, Callable, Dict, List

from pandas import DataFrame, Index

class Option:
    __text: str = ''
    __key: str = ''

    def __init__(self, key: str, text: str):
        self.__key = key
        self.__text = text

    def __str__(self) -> str:
        return self.__key
    
    def __repr__(self) -> str:
        return f'Option("{self.__key}", "{self.__text}")'
    
    @property
    def text(self) -> str:
        return self.__text
    
    @property
    def key(self) -> str:
        return self.__key

class QuestionType(Enum):
    OPTIONS = 'options'
    RANKING = 'ranking'
    TEXT = 'text'
    NUMBER = 'number'

# Labels for the groups
class Question:
    __answers: Dict[str, Option] = {}
    __text: str = ''
    __code: str = ''
    __type: str = ''
    __ranking_slots: int = 0

    def __init__(self, code: str, text: str, answers: Dict[str, str], type: str = QuestionType.OPTIONS, ranking_slots: int = 0):
        self.__answers = {key: Option(key, text) for key, text in answers.items()}
        self.__text = text
        self.__code = code

        assert type in QuestionType.__members__.values(), f"Type '{type}' not found in QuestionType"
        self.__type = type

        assert type != QuestionType.RANKING or ranking_slots > 0, "Ranking questions need a number of slots"
        self.__ranking_slots = ranking_slots

    def __getitem__(self, key: str) -> str:
        # If Key is like 'AO{XX}' or an integer, return the text of the option
        if key in self.__answers:
            return self.__answers[key]
        elif isinstance(key, int) and (key := f'AO{int(key):02}') in self.__answers:
            return self.__answers[key]
        else:
            raise KeyError(f"Key '{key}' not found in question '{self.__text}'")
        
    def __str__(self) -> str:
        return self.__text
    
    def __repr__(self) -> str:
        return f'Question("{self.__code}", "{self.__text}", {self.__answers})'
    
    @property
    def text(self) -> str:
        return self.__text

    @property
    def code(self) -> str:
        return self.__code
    
    @property
    def answers(self) -> Dict[str, Option]:
        return self.__answers
    
    @property
    def type(self) -> str:
        return self.__type
    
    @property
    def ranking_slots(self) -> List[str]:
        return [
            self.ranking_nth(i) for i in range(1, self.__ranking_slots + 1)
        ]
    
    def text_of_option(self, key: str) -> str:
        if key is None or key == '':
            return None

        try:
            return self[key].text
        except KeyError:
            return key

    def group_frame(self, df: DataFrame) -> DataFrame:
        return df.groupby(self.code)
    
    def rename_index(self, df: DataFrame) -> None:
        return df.rename(index=self.__answers, inplace=True)
    
    def rename_columns(self, df: DataFrame) -> None:
        return df.rename(columns=self.__answers, inplace=True)
    
    def ranking_nth(self, nth: int) -> str:
        assert self.__type == QuestionType.RANKING, "Question is not a ranking question"
        assert 0 < nth <= self.__ranking_slots, f"Ranking slot {nth} is out of range"
        return f'{self.code}[{nth}]'
    
    def ranking_nth_question(self, nth: int) -> str:
        return Question(
            self.ranking_nth(nth),
            f'{self.text} (Ranking Slot {nth})',
            {key: option.text for key, option in self.__answers.items()},
            QuestionType.OPTIONS
        )