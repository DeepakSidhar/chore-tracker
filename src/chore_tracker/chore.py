
'''

'''
from datetime import datetime
chore_list = []
completed_chore ={}
NOT_ALLOWED = ['make bed', 'sleep', 'test']

class Chore:


    def create_chore(self,chore):
        print('Create')
        chore_list.append(chore)


    def list_chores(self):
        print('List of chores ')
        for chore in chore_list:

            print(f'{chore} \n' )


    def complete_chore(self,chore):
        if self.chore_allowed(chore) and self.chore_present(chore) :
            completed_chore.update({'chore_name' : chore, 'is_completed' : True})
            print(completed_chore)
        else :
            print(f'{chore} not found - Please add it !!')

        print('Complete chore')

    def chore_allowed(self,chore):
        if chore.lower in NOT_ALLOWED:
            return False
        else:
            return True
    
    def chore_present(self,chore):
        if chore  in chore_list:
            return True
        else:
            return False

class Chore2:

    @classmethod
    def from_dict(cls,data :dict):
        print(data)
        chore = cls(data['owner'], data['description'], data['value'])
        chore.created = datetime.fromisoformat(data['created'])
        if data['finished']:
            chore.finished = datetime.fromisoformat(data['finished'])
        else :
            chore.finished = None

        if data['started']:
            chore.started = datetime.fromisoformat(data['started'])
        else :
            chore.started = None

        return chore



    def __init__(self, owner: str, description: str, value: float=2.0 ):
        self.owner = owner
        self.description = description
        self.value = value
        self.created = datetime.now()
        self.finished = None
        self.started = None



    def __str__(self):
        return f'{self.owner} {self.status} {self.description} {self.value:.02f} '

    def start(self):
        self.started = datetime.now()

    def finish(self):
        self.finished = datetime.now()

    def as_dict(self):
        if self.finished:
            finished = self.finished.isoformat()
        else :
            finished = ''
        if self.started:
            started = self.started.isoformat()
        else:
            started = ''
        return {'owner' : self.owner, 'description' : self.description, 'value': self.value, 'created': self.created.isoformat(), 'started' : started, 'finished': finished}

    @property
    def status(self):
        if not self.started:
            return 'Created'
        if not self.finished:
            return 'In Progress'
        return 'Completed'
