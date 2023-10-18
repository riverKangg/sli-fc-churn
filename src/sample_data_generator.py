import os
import random
import pandas as pd

from utils import *


class DataGenerator:
    def __init__(self, num_samples=1000, yyyymm='202304'):
        """
        Initialize the DataGenerator.

        :param num_samples: The number of samples to generate.
        :param yyyymm: The year and month (e.g., '202304').
        """
        self.num_samples = num_samples
        self.yyyymm = yyyymm
        self.df = None

    def generate_key_data(self):
        """
        Generate sample data with '마감년월', '코드'.
        """
        # Generate unique '코드' (unique numbers) with 11
        ids = list(map(lambda x: str(x).rjust(11, "0"), range(1, self.num_samples + 1)))

        # Generate Target data
        targets = [random.choice([0, 1]) for _ in range(self.num_samples)]

        # Create a DataFrame
        data = {
            '마감년월': self.yyyymm,
            '코드': ids,
            target_variable: targets,
        }
        self.df = pd.DataFrame(data)

    def generate_variable_data(self):
        for feature in feature_names:
            self.df[feature] = [random.uniform(-1, 1) for _ in range(self.num_samples)]

    def save_data_to_csv(self, filepath=data_path):
        """
        Save generated data to a CSV file.

        :param filepath: The path to save the CSV file (default is data_path).
        """
        if not os.path.exists(data_path):
            os.makedirs(data_path)
        filename = f'{filepath}/sample_data_{self.yyyymm}.csv'
        self.df.to_csv(filename, index=False)

    def save_scoring_data_to_csv(self, filepath=data_path):
        """
        Save the scoring data (without 'PERF') to a CSV file.

        :param filepath: The path to save the CSV file (default is data_path).
        """
        self.df = self.df.drop(columns=target_variable)
        filename = f'{filepath}/sample_score_data_{self.yyyymm}.csv'
        self.df.to_csv(filename, index=False)


if __name__ == "__main__":
    data_generator = DataGenerator(num_samples=500, yyyymm='202211')
    data_generator.generate_key_data()
    data_generator.generate_variable_data()
    data_generator.save_data_to_csv()
