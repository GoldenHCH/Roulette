from game import *

amounts = [i for i in range(1,101)]
slots = [int(i) for i in range(0,37)]+['even', 'odd', 'black', 'red', 'half1', 'half2', 'col1', 'col2', 'col3',
                                        'doz1', 'doz2', 'doz3']
cross = []

for slot in slots:
    for amount in amounts:
        cross.append(bet(slot,amount))

print(len(slots))
