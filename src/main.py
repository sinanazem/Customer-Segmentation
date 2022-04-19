import pandas as pd
import numpy as np



from src.feature_engineering.feature_engineering import CustomerSegmentation



if __name__ == "__main__":
    obj = CustomerSegmentation()
    df = obj.get_features()
    df.to_csv('result.csv')
    print('Successed')