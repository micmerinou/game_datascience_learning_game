"""A game in which computer makes a random number and tries to guess it"""
import numpy as np
def random_predict(number:int=1) -> int:
    """Randomly set and guess the number
    Args:
        number (int,optional):seted num. Default=1
    
    Returns:
        int:counter of tries
    """
    count=0
    zonea=0
    zoneb=101
    predict_number = 50
    while True:
        count+=1
        if predict_number>number:
            #Try lower
            dist=round((predict_number-zonea)/2)
            zoneb=predict_number
            predict_number-=dist
        elif predict_number<number:
            #Try bigger
            dist=round((zoneb-predict_number)/2)
            zonea=predict_number
            predict_number+=dist
        else:
            #You're right!
            break
    return(count)

def score_game(random_predict) -> int:
    """How many tries out of 1000 will be done to guess on average
    
    Args:
        random_predict([type]):function of guessing
        
    Returns:
        int:mean number of attempts
    """
    count_ls=[]
    np.random.seed(1)
    random_array=np.random.randint(1,101,size=(1000))
    for number in random_array:
        count_ls.append(random_predict(number))
        
    score=int(np.mean(count_ls))
    
    print(f"Your algorythm guesses the number for {score} attempts on average")
    return(score)
