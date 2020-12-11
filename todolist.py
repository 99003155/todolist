# import the sys modules

import sys

# global variable declared to count each of the work to be done

count = 0


# creating subuser class

class SubUser:

    # constructor

    def __init__(self, name):

        self.name = name

    # to display name

    def display_name(self):

        print self.name


# Inherited class

class MainUser(SubUser):

    pass


# display user

n = MainUser('Hello User')

n.display_name()


# create Work class

class Work:

    # constructor

    def __init__(self, work_todo):
        self.work_todo = work_todo
        global count
        count += 1
        self.id = count


# create class with functions to be performed

class WorkToDo:

    # constructor

    def __init__(self):
        self.work = []

# insert a new task

    def start_work(self, work_todo):
        self.work.append(Work(work_todo))

        # find the completed task

    def find(self, cnt):
        for work_todo in self.work:
            if str(work_todo.id) == str(work_todo.id):
                return work_todo
        return None

    # complete a task

    def end_work(self, cnt):
        task = self.find(cnt)


# main class

class Main:

    # constructor

    def __init__(self):
        self.worktodo = WorkToDo()
        self.options = {'1': self.start, '2': self.end, '3': self.exit}

        # display the list

    def choose(self):
        print ("""
            WELCOME TO THE TO-DO LIST
            Please choose your option
            1. Work to do today
            2. Work completed
            3. Exit application
            """)
# run the functions

    def begin(self):

        while True:
            self.choose()
            number = input('Choose your option ')
            task = self.options.get(number)
            if task:
                task()
            else:
                print 'Invalid'.format(number)

                # add the work to be done

    def start(self):
        work_todo = input('What do you want to do today? ')
        self.worktodo.start_work(work_todo)
        print 'Task entered'

        # enter the completed task

    def end(self):
        id = input('Enter option number: ')
        print 'Hurray! Work done'

        # exit the application

    def exit(self):
        print 'Thank you. Have a great day'
        sys.exit(0)


if __name__ == '__main__':
    Main().begin()

    
