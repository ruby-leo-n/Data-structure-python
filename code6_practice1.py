class ListNode:  # 답지 참조: 꼭 복기해볼것!
    class Node:
        def __init__(self, coef, expon, link):
            self.coef = coef
            self.expon = expon
            self.link = link

    def __init__(self):
        self.Ahead = None
        self.Asize = 0
        self.Bhead = None
        self.Bsize = 0
        self.Chead = None
        self.Csize = 0

    def Ais_empty(self):
        return self.Asize == 0

    def Bis_empty(self):
        return self.Bsize == 0

    def Cis_empty(self):
        return self.Csize == 0

    def A_insert(self, coef, expon):
        if self.Ais_empty():
            self.Ahead = self.Node(coef, expon, None)
        else:
            self.Ahead = self.Node(coef, expon, self.Ahead)
        self.Asize += 1

    def B_insert(self, coef, expon):
        if self.Bis_empty():
            self.Bhead = self.Node(coef, expon, None)
        else:
            self.Bhead = self.Node(coef, expon, self.Bhead)
        self.Bsize += 1

    def C_insert(self, coef, expon):
        if self.Cis_empty():
            self.Chead = self.Node(coef, expon, None)
        else:
            self.Chead = self.Node(coef, expon, self.Chead)
        self.Csize += 1

    def poly_add(self):
        print("다항식 계산중...")
        a = self.Ahead
        b = self.Bhead
        self.sum = 0
        while a != None and b != None:
            if a.expon == b.expon:
                self.sum = a.coef + b.coef
                self.C_insert(self.sum, a.expon)
                a = a.link
                b = b.link
            elif a.expon > b.expon:
                self.C_insert(a.coef, a.expon)
                a = a.link
            elif a.expon < b.expon:
                self.C_insert(b.coef, b.expon)
                b = b.link

        if a is None:
            self.poly_add2(b)
        elif b is None:
            self.poly_add2(a)
        else:
            return

    def poly_add2(self, p):
        while p is not None:
            c_pointer = self.Chead
            flag = True
            while c_pointer is not None:
                if c_pointer.expon == p.expon:
                    c_pointer.coef += p.coef
                    flag = False
                c_pointer = c_pointer.link
            if flag == True:
                self.C_insert(p.coef, p.expon)
            p = p.link

    def sorted_List(self):
        follow_pointer = None
        C_pointer = self.Chead
        leading_pointer = self.Chead.link
        flag = False

        while True:
            while leading_pointer is not None:
                if C_pointer.expon < leading_pointer.expon:
                    if follow_pointer is not None:
                        follow_pointer.link = leading_pointer
                    C_pointer.link = leading_pointer.link
                    leading_pointer.link = C_pointer
                    flag = True

                    if C_pointer == self.Chead:
                        self.Chead = leading_pointer

                if flag:
                    C_pointer, leading_pointer = leading_pointer, C_pointer
                    flag = False

                leading_pointer = leading_pointer.link

            if C_pointer.link is None:
                break
            follow_pointer = C_pointer
            C_pointer = C_pointer.link
            leading_pointer = C_pointer.link

    def print_Clist(self):
        c = self.Chead
        while c:
            if c.link != None:
                print(c.coef, "^", c.expon, "+", end=" ")
            else:
                print(c.coef, "^", c.expon)
            c = c.link


s = ListNode()
s.A_insert(3, 12)
s.A_insert(5, 6)
s.A_insert(1, 2)

s.B_insert(3, 12)
s.B_insert(4, 5)
s.B_insert(2, 2)

s.poly_add()
s.sorted_List()
s.print_Clist()
