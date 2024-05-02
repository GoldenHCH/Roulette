import random

table = {
    'even': 2,
    'odd': 2,
    'black': 2,
    'red': 2,
    'half1': 2,
    'half2': 2,
    'col1': 3,
    'col2': 3,
    'col3': 3,
    'doz1': 3,
    'doz2': 3,
    'doz3': 3
}

wheel = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18',
         '19', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '31', '32', '33', '34', '35', '36',
         '0', '00']
red_slots = [1, 3, 5, 7, 9, 12, 14, 16, 18, 19, 21, 23, 25, 27, 30, 32, 34, 36]
black_slots = [2, 4, 6, 8, 10, 11, 13, 15, 17, 20, 22, 24, 26, 28, 29, 31, 33, 35]


class bet:
    def __init__(self, slot, amount):
        self.slot = slot
        self.amount = amount


class spin:
    def __init__(self, *bets):
        self.cost = None
        self.earn = None
        self.win_slot = None
        self.bets = bets

    def play(self, win_slot=[], cost=0, earn=0):
        self.cost = cost
        self.earn = earn
        self.win_slot = win_slot
        i = random.randint(0, 37)
        land = wheel[i]
        print(f'the wheel landed on {land}')
        self.win_slot = [land]
        # dozens
        if 0 <= i <= 11:
            self.win_slot.append('doz1')
        elif 12 <= i <= 23:
            self.win_slot.append("doz2")
        elif 24 <= i <= 36:
            self.win_slot.append("doz3")
        # halfs
        if 0 <= i <= 17:
            self.win_slot.append('half1')
        elif 18 <= i <= 35:
            self.win_slot.append('half2')
        # even/odd
        if land not in ['0', '00'] and (int(land) % 2) == 0:
            self.win_slot.append('even')
        elif land not in ['0', '00'] and (int(land) % 2) == 1:
            self.win_slot.append('odd')
        # red/black
        if int(land) in red_slots:
            self.win_slot.append("red")
        elif int(land) in black_slots:
            self.win_slot.append('black')
        # column
        if land not in ['0', '00'] and int(land) % 3 == 1:
            self.win_slot.append("col1")
        elif land not in ['0', '00'] and int(land) % 3 == 2:
            self.win_slot.append('col2')
        elif land not in ['0', '00'] and int(land) % 3 == 0:
            self.win_slot.append('col3')

        for bet in self.bets:
            self.cost += bet.amount
            if bet.slot in self.win_slot:
                if bet.slot in table:
                    self.earn += bet.amount * table[bet.slot]
                else:
                    self.earn += bet.amount * 36
