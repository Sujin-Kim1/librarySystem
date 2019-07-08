#!/usr/bin/python
# -*- coding: utf-8 -*-

from Member import Member


class User(Member):
    def __init__(self, id=None, pw=None, name=None):
        self.id = id
        self.pw = pw
        self.name = name
        self.numOfBorrowedBooks = 0
        self.borrowedList = []
