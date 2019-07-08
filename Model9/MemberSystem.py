#!/usr/bin/python
# -*- coding: utf-8 -*-
import MemberManager
import User
import Librarian


class MemberSystem:
    def __init__(self):
        self.isUserLoggedIn = False
        self.isLibrarianLoggedIn = False

    def login(self, id, pw):
        memberManager = MemberManager.MemberManager()
        result = memberManager.validateMember(id, pw)
        if isinstance(result, Librarian.Librarian):
            self.setLibrarianLogInState()
        elif isinstance(result, User.User):
            self.setUserLogInState()
        else:
            print('로그인 실패')
            pass

    def logout(self):
        self.isUserLoggedIn = False
        self.isLibrarianLoggedIn = False

    def signUp(self, data):
        memberManager = MemberManager.MemberManager()
        memberManager.updateStatus('enroll', data)

    def displayBorrowedList(self, id):
        memberManager = MemberManager.MemberManager()
        borrowedList = memberManager.getBorrowedList(id)
        for i, book in enumerate(borrowedList):
            print(i+1, ': 책 제목 : ', book.name, '/ 저자 : ', book.author)

    def getUserLogInState(self):
        return self.isUserLoggedIn

    def getLibrarianLogInState(self):
        return self.isLibrarianLoggedIn

    def setUserLogInState(self):
        self.isUserLoggedIn = True if self.isUserLoggedIn is False else True

    def setLibrarianLogInState(self):
        self.isLibrarianLoggedIn = True if self.isLibrarianLoggedIn is False else True

    def increaseBookIssue(self, book, id):
        memberManager = MemberManager.MemberManager()
        memberManager.updateStatus('borrow', book, id)

    def decreaseBookIssue(self, num, id):
        memberManager = MemberManager.MemberManager()
        bookList = memberManager.getBorrowedList(id)
        book = bookList[num - 1]
        memberManager.updateStatus('return', book, id)
