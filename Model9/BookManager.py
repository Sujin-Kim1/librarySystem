#!/usr/bin/python
# -*- coding: utf-8 -*-
import Book


class BookManager:
    dummy1 = Book.Book('돌이킬 수 없는 약속', '야쿠마루 가쿠', 3)
    dummy2 = Book.Book('죽고 싶지만 떡볶이는 먹고 싶어', '백세희', 2)
    dummy3 = Book.Book('열두 발자국', '정재승', 4)
    books = [dummy1, dummy2, dummy3]

    # 책이 대출 가능한지 확인해준다.
    def checkBookAvailable(self, bookId):
        return self.books[bookId].status

    # 책의 내용을 변경한다.
    def updateStatus(self, changes=None, data=None):
        # 책 등록
        if changes == 'register':
            book = Book.Book(data[0], data[1], data[2])
            self.books.append(book)
        # 책 대출
        if changes == 'borrow':
            if self.checkBookAvailable(data):
                self.decreaseNumOfBooks(data)
            else:
                print('대출 불가능한 책입니다.')
                return
        # 책 반납
        if changes == 'return':
            self.increaseNumOfBooks(data)

    # 저자나 책 이름으로 검색했을 때 결과값을 출력하고 book 의 index 와 book 을 반환한다.
    def searchData(self, data):
        for i, book in enumerate(self.books):
            if (data in book.author) or (data in book.name == data):
                print('책 이름 :', self.books[i].name)
                print('저자 :', self.books[i].author)
                print('대출 가능한 책의 개수 :', self.books[i].numOfBooks)
                return i, book
        print('검색 결과가 없습니다.')
        return False

    def decreaseNumOfBooks(self, bookIndex):
        self.books[bookIndex].numOfBooks -= 1
        if self.books[bookIndex].numOfBooks <= 0:
            self.books[bookIndex].status = False

    def increaseNumOfBooks(self, bookIndex):
        self.books[bookIndex].numOfBooks += 1

