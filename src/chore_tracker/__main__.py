import sys
from turtledemo.penrose import start

from chore_tracker.chore import Chore, Chore2
import json

from chore_tracker.data import Data
from chore_tracker.reward import Reward


def menu() -> str:
    print('Create Chore 1')
    print('List Chores 2')
    print('Completed Chore 3')
    print('Reward Status 4')
    print('Exit the app 5 ')
    choice  = input('Please enter a number :')
    return choice


'''

def reward_status(name, file_name):
    status = 0
    chores = load_chores(file_name)
    for chore in chores :
        if chore.owner == name and chore.finished != None :
            status +=2

    return f' The current award is {status} dollars '
'''
def main():
    file_name = 'chores.json'
    chores = Data.load_chores(file_name)
    print('The project has started')
    name = input('please enter a name :')

    while True :
        choice = menu()
        if choice == '1':
            description = input('please enter a chore:')
            chores.append(Chore2(name,description))
            chores[-1].start()

            continue
        if choice == '2':
            for index, chore in enumerate(chores, start=1):
                print(index, chore)

            continue
        if choice == '3':
            chore = input('Please enter the number for the  chore that is completed :')
            try :
                index = int(chore) - 1

            except ValueError:
                print(f'This is not a valid entry {chore}')

            try :
                chores[index].finish()  # try catch of indeix out of bound
            except IndexError :
                print('Not valid option please try again')

            continue
        if choice == '4':
            Data.save_chores(chores, file_name)
            print(Reward.reward_status(name, file_name))

            continue
        if choice == '5':
            Data.save_chores(chores, file_name)
            print(f'Saved to {file_name}')

            break






if __name__ == "__main__":

    main()


