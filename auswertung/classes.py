#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Classes for the evaluation of the questionnaire
"""

from typing import Any, Dict

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

# Labels for the groups
class Question:
    __answers: Dict[str, Option] = {}
    __text: str = ''
    __code: str = ''

    def __init__(self, code: str, text: str, answers: Dict[str, str]):
        self.__answers = {key: Option(key, text) for key, text in answers.items()}
        self.__text = text
        self.__code = code

    def __getitem__(self, key: str) -> str:
        # If Key is like 'AO{XX}' or an integer, return the text of the option
        if key in self.__answers:
            return self.__answers[key]
        elif key.isdigit() and (key := f'AO{int(key):02}') in self.__answers:
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
    
    def ranking_nth(self, nth: int) -> str:
        return f'{self.code}[{nth}]'
    
    def __getattribute__(self, name: str) -> Any:
        try:
            return self[name]
        except KeyError:
            return super().__getattribute__(name)