#мы отгадываем число от 1 до 100, загаданное компьютером
import numpy as np
number=np.random.randint(1,101)
count=0
while True:
    count += 1
    predict_number = int(input('Guess the num from 1 to 100'))
    
    if predict_number>number:
        print('Try lower')
    elif predict_number<number:
        print('Try bigger')
    else:
        print(f"You're right! The number is {number}, guessed for {count} attempts")
        break
