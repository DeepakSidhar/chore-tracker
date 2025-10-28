from datetime import datetime, time, timedelta

from chore_tracker.data import Data


TOTAL_AMOUNT = 4000

class Reward:
    def init (self, name, filename):
        self.name = name
        self.filename = filename


    def reward_status(name, file_name):
        status = 0
        chores = Data.load_chores(file_name)


        for chore in chores:
            if chore.owner == name and chore.finished != None:
                status += 2


        total_status = TOTAL_AMOUNT - status
        today = datetime.now()
        ten_HKD = timedelta(total_status/10)
        eight_HKD = timedelta(total_status / 8)
        six_HKD = timedelta(total_status / 6)
        four_HKD = timedelta(total_status / 4)
        two_HKD = timedelta(total_status / 2)






        return (f""" The current award is {status} dollars.\n
                If ypu complete five chores each day it will take you {ten_HKD} \n 
                If ypu complete four chores each day it will take you {eight_HKD} \n 
                If ypu complete three chores each day it will take you {six_HKD} \n  
                If ypu complete two chores each day it will take you {four_HKD} \n  
                If ypu complete one chores each day it will take you {two_HKD} \n  """

                )



