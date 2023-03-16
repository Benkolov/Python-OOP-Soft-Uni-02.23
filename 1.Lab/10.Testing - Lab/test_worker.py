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


    def setUp(self):
        self.worker = Worker("John", 100, 10)


    def test_worker_initialization(self):
        self.assertEqual(self.worker.name, "John")
        self.assertEqual(self.worker.salary, 100)
        self.assertEqual(self.worker.energy, 10)


    def test_energy_increment_after_rest(self):
        initial_energy = self.worker.energy
        self.worker.rest()
        self.assertEqual(self.worker.energy, initial_energy + 1)


    def test_error_when_working_with_negative_or_zero_energy(self):
        self.worker.energy = 0
        with self.assertRaises(Exception, msg='Not enough energy.'):
            self.worker.work()
        self.worker.energy = -1
        with self.assertRaises(Exception, msg='Not enough energy.'):
            self.worker.work()


    def test_money_increase_after_work(self):
        initial_money = self.worker.money
        self.worker.work()
        self.assertEqual(self.worker.money, initial_money + self.worker.salary)


    def test_energy_decrease_after_work(self):
        initial_energy = self.worker.energy
        self.worker.work()
        self.assertEqual(self.worker.energy, initial_energy - 1)


    def test_get_info(self):
        self.worker.money = 500
        info = self.worker.get_info()
        self.assertEqual(info, "John has saved 500 money.")


if __name__ == "__main__":
    unittest.main()
