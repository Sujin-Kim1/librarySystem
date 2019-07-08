#!/usr/bin/python
# -*- coding: utf-8 -*-
import BookSystem
import MemberSystem


class Transaction:
    def __init__(self):
        self.book = BookSystem.BookSystem()
        self.member = MemberSystem.MemberSystem()
        self.id = None

    def getInput(self):
        while True:
            print('******************')
            print('원하는 메뉴를 골라주세요')
            print('******************')
            if self.member.getUserLogInState() or self.member.getLibrarianLogInState():
                print('1 : 로그아웃')
            else:
                print('1 : 로그인')
            print('2 : 회원가입')
            print('3 : 책 검색 하기')
            print('4 : 대출')
            print('5 : 반납')
            print('6 : 대출 조회')
            print('7 : 책 등록 하기')

            try:
                event = int(input())
                # 로그아웃
                if event == 1 and (self.member.getUserLogInState() or self.member.getLibrarianLogInState()):
                    self.member.logout()
                    self.setId(None)
                # 로그인
                elif event == 1:
                    id = input('id : ')
                    pw = input('password : ')
                    self.member.login(id, pw)
                    self.setId(id)
                # 회원가입
                elif event == 2:
                    id = input('id : ')
                    pw = input('password : ')
                    name = input('name : ')
                    data = [id, pw, name]
                    self.member.signUp(data)
                # 책 검색 하기
                elif event == 3:
                    data = input('검색할 내용을 입력해주세요 : (ex. 책 이름, 저자) ')
                    result = self.book.searchData(data)
                # User 의 로그인이 필요한 서비스
                elif self.member.getUserLogInState():
                    # 대출
                    if event == 4:
                        data = input('대출할 책을 검색해주세요 : ')
                        result = self.book.searchData(data)
                        if result[1] is not False:
                            need = input('대출하시겠습니까? (ex. \'y\' or \'n\') ')
                            if need == 'y' or 'Y':
                                self.book.borrow(result[0])  # book 의 index 값
                                self.member.increaseBookIssue(result[1], self.getId())
                        else:
                            print('검색 내용이 없습니다.')
                            continue
                    # 반납
                    elif event == 5:
                        self.member.displayBorrowedList(self.getId())
                        try:
                            num = int(input('반납할 책의 번호를 입력해주세요. : '))
                        except TypeError:
                            print('번호를 입력해 주세요.')
                        self.member.decreaseBookIssue(num, self.getId())
                    # 대출 조회
                    elif event == 6:
                        self.member.displayBorrowedList(self.getId())
                    # 책 등록 : User 에게 권한이 없음
                    elif event == 7:
                        if not self.member.getLibrarianLogInState():
                            print('권한이 없습니다.')
                # 사서의 로그인이 필요한 서비스
                elif self.member.getLibrarianLogInState() and event == 7:
                    # 책 등록하기
                    name = input('책 이름을 입력해주세요 : ')
                    author = input('저자를 입력해주세요 : ')
                    num = input('수량을 입력해주세요 : ')
                    data = [name, author, num]
                    self.book.registerBook(data)
                    # Librarian 이 User 의 서비스를 이용하려고 할 때
                elif self.member.getLibrarianLogInState() and event == 4 or 5 or 6:
                    print('지원하지 않는 서비스입니다.')
                else:
                    print('로그인이 필요합니다.')
            except:
                print('입력값이 올바르지 않습니다.')
                pass

    def setId(self, id):
        self.id = id

    def getId(self):
        return self.id


if __name__ == '__main__':
    ts = Transaction()
    ts.getInput()
