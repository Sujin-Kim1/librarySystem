#!/usr/bin/python
# -*- coding: utf-8 -*-
import BookManager


class BookSystem:
    def borrow(self, index):
        bookManger = BookManager.BookManager()
        bookManger.updateStatus('borrow', index)

    def returnBook(self, index):
        bookManger = BookManager.BookManager()
        bookManger.updateStatus('return', index)
        pass

    # BookManager 의 searchData 를 호출한다.
    def searchData(self, data):
        bookManger = BookManager.BookManager()
        return bookManger.searchData(data)

    def registerBook(self, data):
        bookManger = BookManager.BookManager()
        bookManger.updateStatus('register', data)
