"""Collection of data science helper functions"""


import pandas as pd


class LambdaClass(pd.DataFrame):

    def null_count(self):
        '''Counts total number of null values in a dataframe'''
        return self.isnull().sum().sum()

    def train_test_split(self, frac): 
        '''Split dataframe into training, test datasets'''
        frac = round(len(self)*frac)
        train_df = self[:frac]
        test_df = self[frac:]
        return train_df, test_df # instaniate 2 variables for the dataframes

    def randomize(self, seed):
        '''Randomizes dataframe order'''
        return self.sample(frac=1, random_state=seed)