from abc import ABC, abstractmethod

# Create an interface (IWorker) to define the abstraction for the Worker classes
class IWorker(ABC):

    @abstractmethod
    def work(self):
        pass

# Modify the Worker class to inherit from IWorker, ensuring it implements the work method
class Worker(IWorker):

    def work(self):
        print("I'm working!!")

# Modify the SuperWorker class to inherit from IWorker, ensuring it implements the work method
class SuperWorker(IWorker):

    def work(self):
        print("I work very hard!!!")

class Manager:

    def __init__(self):
        self.worker = None

    # Update the set_worker method to check if the worker is an instance of IWorker, not Worker
    def set_worker(self, worker):
        assert isinstance(worker, IWorker), '`worker` must be of type {}'.format(IWorker)

        self.worker = worker

    def manage(self):
        if self.worker is not None:
            self.worker.work()


# worker = Worker()
# manager = Manager()
# manager.set_worker(worker)
# manager.manage()
#
# super_worker = SuperWorker()
# try:
#     manager.set_worker(super_worker)
# except AssertionError:
#     print("manager fails to support super_worker....")

worker = Worker()
manager = Manager()
manager.set_worker(worker)
manager.manage()

super_worker = SuperWorker()
try:
    manager.set_worker(super_worker)
    manager.manage()
except AssertionError:
    print("manager fails to support super_worker....")
