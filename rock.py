import random
uc = ''
cc = ''

t = random.randint(1,3)
if t==1:
    cc='Rock'
elif t==2:
    cc='Paper'
elif t==3:
    cc='Scissors'

uc = input('Enter Rock, Paper or Scissors: ')

if uc=='Rock':
    if cc=='Rock':
        print('Its a tie') 
    elif cc=='Paper':
        print('Computer wins')
    elif cc=='Scissors':
        print('User wins')
elif uc=='Paper':
    if cc=='Rock':
        print('User wins')
    elif cc=='Paper':
        print('Its a tie')
    elif cc=='Scissors':
        print('Computer wins')
elif uc=='Scissors':
    if cc=='Rock':
        print('Computer wins')
    elif cc=='Paper':
        print('User wins')
    elif cc=='Scissors':
        print('Its a tie')
print('Computer choice was', cc)
