#!/usr/bin/python
# -*- coding: utf-8 -*-
import User
import Librarian


class MemberManager:
    librarian = Librarian.Librarian()
    members = [librarian]

    def updateStatus(self, changes, data=None, id=None):
        # 회원 등록
        if changes == 'enroll':
            if self.searchMember(data[0]) is False:
                member = User.User()
                member.id = data[0]
                member.pw = data[1]
                member.name = data[2]
                self.members.append(member)
            else:
                print('중복된 아이디 입니다.')
        # 책 대출
        elif changes == 'borrow':
            member = self.searchMember(id)
            if isinstance(member, User.User) and self.checkRentable(id):
                member.borrowedList.append(data)
            else:
                '대출이 불가능합니다.'
        # 책 반납
        elif changes == 'return':
            member = self.searchMember(id)
            if isinstance(member, User.User):
                member.borrowedList.remove(data)

    def validateMember(self, id=None, pw=None):
        for member in self.members:
            if id == member.id and pw == member.pw:
                return member
        print('일치하는 회원 정보가 없습니다')
        return False

    def searchMember(self, id):
        for member in self.members:
            if id == member.id:
                return member
        return False

    def getBorrowedList(self, id):
        member = self.searchMember(id)
        if isinstance(member, User.User):
            return member.borrowedList

    def checkRentable(self, id):
        member = self.searchMember(id)
        if isinstance(member, User.User):
            return len(member.borrowedList) <= 5


