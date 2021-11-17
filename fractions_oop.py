def gcd(n, d):
    while n != d:
        if n > d:
            n = n - d
        else:
            d = d - n
    return n


class Fraction:
    def __init__(self, n, d):
        self.num = int(n / gcd(abs(n), abs(d)))
        self.denom = int(d / gcd(abs(n), abs(d)))
        if self.denom < 0:
            self.denom = abs(self.denom)
            self.num = -1*self.num
        elif self.denom == 0:
            raise ZeroDivisionError

    def Add(self, other):
        return Fraction(self.num * other.denom + self.denom * other.num, self.denom * other.denom)

    def Sub(self, other):
        return Fraction(self.num * other.denom - self.denom * other.num, self.denom * other.denom)

    def Mul(self, other):
        return Fraction(self.num * other.num, self.denom * other.denom)

    def Div(self, other):
        return Fraction(self.num * other.denom, self.denom * other.num)

    def __str__(self):
        return f"{self.num} / {self.denom}"



def main():
    f1 = Fraction(2,-2)
    f2 = Fraction(3,-4)
    f3 = Fraction.Add(f1,f2)
    f4 = Fraction.Sub(f1,f2)
    f5 = Fraction.Mul(f1,f2)
    f6 = Fraction.Div(f1,f2)
    print(f3)
    print(f4)
    print(f5)
    print(f6)


if __name__ == '__main__':
    main()