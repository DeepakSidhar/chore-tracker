import sys

from chore_tracker.chore import Chore, Chore2
import json

"""


chore_list = []
def create_chore(chore):
    print('Create')
    chore_list.append(chore)

def list_chores():
    print('List of chores ')
    for chore in chore_list:
        print(chore)
def complete_chore():
    print('Complete chore')
"""
def menu() -> str:
    print('Create Chore 1')
    print('List Chores 2')
    print('Completed Chore 3')
    print('Exit the app 4 ')
    choice  = input('Please enter a number :')
    return choice

def load_chores(file_name:str) -> list:
    try:
        with open(file_name) as f:
            items = json.load(f)
            chores = [Chore2.from_dict(item) for item in items]

    except Exception as error:
        print(error)
        chores = []

    return chores

def save_chores(chores : list, file_name):
    with open(file_name, 'w') as f:
        json.dump([chore.as_dict() for chore in chores ], f)



def main():
    file_name = 'chores.json'
    chores = load_chores(file_name)
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
            index = int(chore) # try and except type error
            chores[index].finish()  # try catch of indeix out of bound

            continue
        if choice == '4':
            save_chores(chores, file_name)
            print(f'Saved to {file_name}')

            break






if __name__ == "__main__":

    main()


'''
Add a chore 
complete a chore 
each chore completed needs to have 2 HKD  a max of 10 HKD per day
minus the number from the total 


'''