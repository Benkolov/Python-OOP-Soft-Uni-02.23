class Worker:

    def __init__(self, name, salary, energy):
        self.name = name
        self.salary = salary
        self.energy = energy
        self.money = 0

    def work(self):
        if self.energy <= 0:
            raise Exception('Not enough energy.')

        self.money += self.salary
        self.energy -= 1

    def rest(self):
        self.energy += 1

    def get_info(self):
        return f'{self.name} has saved {self.money} money.'


import unittest


class WorkerTests(unittest.TestCase):

    def test_worker_initialization(self):
        worker = Worker("John Doe", 100, 10)
        self.assertEqual(worker.name, "John Doe")
        self.assertEqual(worker.salary, 100)
        self.assertEqual(worker.energy, 10)

    def test_rest_method(self):
        worker = Worker("John Doe", 100, 10)
        worker.rest()
        self.assertEqual(worker.energy, 11)

    def test_work_method_error(self):
        worker = Worker("John Doe", 100, 0)
        with self.assertRaises(Exception) as context:
            worker.work()
        self.assertEqual(str(context.exception), "Not enough energy.")

    def test_work_method_money_increment(self):
        worker = Worker("John Doe", 100, 10)
        worker.work()
        self.assertEqual(worker.money, 100)

    def test_work_method_energy_decrement(self):
        worker = Worker("John Doe", 100, 10)
        worker.work()
        self.assertEqual(worker.energy, 9)

    def test_get_info_method(self):
        worker = Worker("John Doe", 100, 10)
        worker.work()
        worker.work()
        self.assertEqual(worker.get_info(), "John Doe has saved 200 money.")


if __name__ == '__main__':
    unittest.main()
