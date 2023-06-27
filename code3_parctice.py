class Polynomial:

    def __init__(self):
        self.poly = []

    def polynomial(self):
        degree = int(input("최고차항계수를 입력:"))
        for i in range(degree+1):
            self.poly.append(int(input("{0}차수의 계수를 입력".format(i))))

    def degree(self):
        return len(self.poly)-1

    def add(self, rhs):
        rhsN = Polynomial()
        for i in range(0, len(self.poly)):
            rhsN.poly.append(rhs.poly[i] + self.poly[i])
        return print(rhsN.poly)

    def sub(self, rhs):
        rhsN = Polynomial()
        for i in range(0, len(self.poly)):
            rhsN.poly.append(-rhs.poly[i] + self.poly[i])
        return print(rhsN.poly)

    def display(self):
        print(self.poly)

    def evaluate(self, scalar):
        rhs = Polynomial()
        print("\n")
        for i in range(0, len(self.poly)):
            rhs.poly.append(self.poly[i]*(pow(scalar, i)))
            print(self.poly[i]*(pow(scalar, i)), end=" ")
        print("\n")
        return print(sum(rhs.poly))

    def multiply(self, rhs):
        rhsN = Polynomial()
        sizeone = self.degree()
        sizetwo = rhs.degree()
        rhsN.poly = [0 for _ in range(sizeone+sizetwo+1)]

        if (sizeone == sizetwo):
            for i in range(sizeone+1):
                for j in range(sizetwo+1):
                    rhsN.poly[i+j] = rhsN.poly[i+j] + rhs.poly[i]*self.poly[j]
            return print(rhsN.poly)

        elif (sizeone != sizetwo):
            for i in range(sizetwo+1):
                for j in range(sizeone+1):
                    rhsN.poly[i+j] = rhsN.poly[i+j] + rhs.poly[i]*self.poly[j]
            return print(rhsN.poly)


px = Polynomial()
rhs = Polynomial()

rhs.polynomial()
px.polynomial()

rhs.display()
px.display()


# px.degree()
# rhs.degree()

# rhs.add(px)
# rhs.sub(px)

# rhs.evaluate(-1)
# px.evaluate(2)

rhs.multiply(px)
