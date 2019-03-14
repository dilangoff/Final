'''
Hi my name is Dilan Goff and this is my finale exam project I made a drawing with turtle graphics and asked the
reviewers about it
'''

#This is my code for the survey questions

like = -5
while like <1 or like >3:
    try:
        like = float(input('Did you like my Drawing?(1 = yes 2 = No) '))

    except ValueError:
        print('1 or 2')


if like == 1:
    print('Thank you')

if like == 2:
    print('Thank you for your input, I hope you will like are next drawing')



