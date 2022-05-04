import time
import os
from functions import *

passcode = 2301
unlocked = False
tries = 3
penalty = 0

while unlocked is False:
    if penalty <= 3:
        if tries > 0:
            if get_user_entry() != passcode:
                tries -= 1
                print(f'You have entered an incorrect passcode. You have {tries} attempts remaining.')
            else:
                print('You have entered the correct passcode.')
                unlocked = True
        else:
            clear = lambda: os.system('cls')
            clear()
            penalty += 1
            for i in range(penalty,0,-1):
                print(f"'You have made 3 wrong guesses and must wait for {i} seconds.", end="\r", flush=True)
                time.sleep(1)
            clear = lambda: os.system('cls')
            clear()
            tries = 3
            continue
    else:
        print('You have made too many attempts. System locked permenantly!!')
        break
if unlocked is True:
    print('Unlocked.')
