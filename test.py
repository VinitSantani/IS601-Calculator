import unittest
import Function
import csv
from Calculator import Calculator;


class Test(unittest.TestCase) :
    
    def setUp(self) -> None:
        self.calculator = Calculator()

    def test_instantiate_calculator(self):
        self.assertIsInstance(self.calculator, Calculator)
    
    def test_add(self):
        with open('./data/Unit Test Addition.csv', mode='r') as csv_file:
            csv_reader= csv.DictReader(csv_file)
            for row in csv_reader:
                self.assertEqual( self.calculator.add(int(row['Value 1']), int(row['Value 2'])), int(row['Result']))
    
    def test_sub(self):
        with open('./data/Unit Test Subtraction.csv', mode='r') as csv_file:
            csv_reader= csv.DictReader(csv_file)
            for row in csv_reader:
                self.assertEqual(self.calculator.subtract(int(row['Value 2']), int(row['Value 1'])), int(row['Result']))

    def test_multiply(self):
        with open('./data/Unit Test Multiplication.csv', mode='r') as csv_file:
            csv_reader= csv.DictReader(csv_file)
            for row in csv_reader:
                self.assertEqual(self.calculator.multiply(int(row['Value 1']), int(row['Value 2'])), int(row['Result']))

    def test_divide(self):
        with open('./data/Unit Test Division.csv', mode='r') as csv_file:
            csv_reader= csv.DictReader(csv_file)
            for row in csv_reader:
                self.assertEqual(self.calculator.divide(int(row['Value 2']), int(row['Value 1'])),float(row['Result'])) 

    def test_square(self):
        with open('./data/Unit Test Square.csv', mode='r') as csv_file:
            csv_reader= csv.DictReader(csv_file)
            for row in csv_reader:
                self.assertEqual(self.calculator.square(int(row['Value 1'])), float(row['Result']))

    def test_sqrt(self):
        with open('./data/Unit Test Square Root.csv', mode='r') as csv_file:
            csv_reader= csv.DictReader(csv_file)
            for row in csv_reader:
                self.assertEqual(self.calculator.sqrt(int(row['Value 1'])), round(float(row['Result']),8))  
                
                    
if __name__ == '__main__':
    unittest.main()