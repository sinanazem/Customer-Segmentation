import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


class DataProcessing:

    def read_data(self,file_path):

        self.data = pd.read_csv(file_path,sep='\t')
        return self.data

    def cleaning_data(self,df):

        df = df.dropna()
        return df

    def get_data(self):

        data = self.read_data('src/data/marketing_campaign.csv')
        result = self.cleaning_data(data)
        return result