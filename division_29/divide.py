"""�������������������� dividend �ͳ��� divisor�������������Ҫ��ʹ�ó˷��������� mod �������

���ر����� dividend ���Գ��� divisor �õ����̡�"""
class Solution(object):
##    def __init__(self,dividend=1,divisor=1):
##        pass
####        self.dividend = dividend
####        self.divisor = divisor
    def divide(self,dividend,divisor):
##        self.dividend = dividend
##        self.divisor = divisor
        if dividend == 0:
            return 0
        elif dividend == divisor:
            return 1
        elif dividend > 0:
            if divisor > 0:
                d = self.de(dividend,divisor)
                return d[0]
            else:
                d = self.de(dividend,-divisor)
                return -d[0]
        else:
            if divisor > 0:
                d = self.de(-dividend,divisor)
                return -d[0]
            else:
                d = self.de(-dividend,-divisor)
                if d[1] != 1:
                    return d[0]
                else:
                    return d[0]-1
    def de(self,a,b):
        self.a = a
        self.b = b
        i = 0
        s = 0
        for j in range(150000,0,-149999):
            while a - b*j >= 0:
                a = a - b*j
                i = i + 1*j
            d = i
            if a == 0:
                s = 1
        return [d,s]
b = Solution()
a = b.divide(-214748,-12)
print a
