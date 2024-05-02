import random

table = {
    0: 1
}


wheel = ['1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16','17','18','19','20','21','22',"23",'24','25','26','27',
         '28','29','30','31','32','33','34','35','36','0','00']


class bet:
    def __init__(self, slot, amount):
        self.slot = slot
        self.amount = amount


class spin:
    def __init__(self, *bet):
        self.bet = bet

    def play():
        i = random.randint(0, 37)
        land = wheel[i]
        doz1 = 0<=i<=11
        doz2 = 12<=i<=23
        doz3 = 24<=i<=35
        half1 = 0<=i<=17
        half2 = 18<=i<=35
        even = land != '0' and land != '00' and int(land)%2 == 0
        odd = land != '0' and land != '00' and (int(land)-1)%2 == 0
        red = 
        black = d