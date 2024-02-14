import unittest
from analysis import load_and_preprocess_data

class TestLoadAndPreprocessData(unittest.TestCase):
    def test_data_loading_and_preprocessing(self):
      
        test_data = 'Ming_Kirsten-python_assignment2_orig.csv'
        result = load_and_preprocess_data(test_data)

       
        self.assertIsNotNone(result)
   

if __name__ == '__main__':
    unittest.main()
