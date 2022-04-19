import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

from src.data_processing.data_processing import DataProcessing

class CustomerSegmentation:

    @staticmethod
    def gen_feature(df):

        df["Dt_Customer"] = pd.to_datetime(df["Dt_Customer"])

        dates = []
        for v in  df["Dt_Customer"]:
            v = v.date()
            dates.append(v)

        days = []

        d1 = max(dates)
        for i in dates:
            delta = d1 - i
            days.append(delta)

        df["Customer_For"] = days
        df["Customer_For"] = pd.to_numeric(df["Customer_For"], errors="coerce")

        df["Age"] = max(dates).year-df["Year_Birth"]

        df["spend"] = df[["MntWines",
                                          "MntFruits",
                                          "MntMeatProducts",
                                          "MntFishProducts",
                                          "MntSweetProducts",
                                          "MntGoldProds"]].sum(axis=1)

        df["Living_With"]=df["Marital_Status"].replace(
                                                    {"Married":"Partner",
                                                     "Together":"Partner",
                                                     "Absurd":"Alone",
                                                     "Widow":"Alone",
                                                     "YOLO":"Alone",
                                                     "Divorced":"Alone",
                                                     "Single":"Alone",})

        df["Children"] = df["Kidhome"]+df["Teenhome"]

        df['Family_Size'] = df['Living_With'].replace({'Alone':1,'Partner':2}) + df["Children"]

        df['Is_Parent'] = np.where(df.Children > 0 , 1,0)

        df["Education"]=df["Education"].replace(
                                            {"Basic":"Undergraduate",
                                             "2n Cycle":"Undergraduate",
                                             "Graduation":"Graduate",
                                             "Master":"Postgraduate",
                                             "PhD":"Postgraduate"})

        df=df.rename(
                columns={"MntWines": "Wines",
                         "MntFruits":"Fruits",
                         "MntMeatProducts":"Meat",
                         "MntFishProducts":"Fish",
                         "MntSweetProducts":"Sweets",
                         "MntGoldProds":"Gold"})

        to_drop = ["Marital_Status", "Dt_Customer", "Z_CostContact", "Z_Revenue", "Year_Birth", "ID"]
        df = df.drop(to_drop, axis=1)

        return df

    def get_features(self):
        obj = DataProcessing()
        df = obj.get_data()


        df_result = self.gen_feature(df)
        return df_result