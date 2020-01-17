import pandas as pd
import numpy as np
# better way of expressing: q4, q6, q8
"""
This assignment practices using pandas on '2019 FE GUIDE.csv'.

It answers eleven queries about car information in csv file. The data 
will be stored in pandas dataframe. 
"""


def q1(df):
    """
    How many cars are made by the manufacturer Honda?
    :param df: Pandas DataFrame representing data in '2019 FE GUIDE.csv'
    :return: integer representing number of cars made by Honda
    """
    return len(df[df['Mfr Name'] == 'Honda'])


def q2(df):
    """
    How many 'Guzzlers' are there (as indicated by the column
    # 'Guzzler?')
    :param df: Pandas DataFrame representing data in '2019 FE GUIDE.csv'
    :return: integer representing number of 'Guzzlers'
    """
    return len(df[df['Guzzler?'] == 'G'])


def q3(df):
    """
    What is the value of the highest combined Fuel Efficiency as given
    by "Comb FE (Guide) - Conventional Fuel"?
    :param df: Pandas DataFrame representing data in '2019 FE GUIDE.csv'
    :return: float representing the highest combined Fuel Efficiency
    """
    return df['Comb FE (Guide) - Conventional Fuel'].max()


def q4(df):
    """
    Which division and car line has the lowest combined FE
    - Conventional Fuel? The function must return a tuple of strings.
    :param df: Pandas DataFrame representing data in '2019 FE GUIDE.csv'
    :return: a tuple of strings representing division and carline
    """
    # Just return one of the pairs
    carline = df['Comb FE (Guide) - Conventional Fuel'].idxmin()
    return df.loc[carline, 'Division'], carline


def q5(df):
    """
    # What is the highest combined FE - Conventional Fuel among all
    # wheel drives.
    :param df: Pandas DataFrame representing data in '2019 FE GUIDE.csv'
    :return: float representing highest combined FE -conventional fuel
    """
    # Use 'Drive Desc'.
    return df.loc[df['Drive Desc'] == 'All Wheel Drive',
                  'Comb FE (Guide) - Conventional Fuel'].max()


def q6(df):
    """
    Which car line has the largest difference between Highway
    and City Fuel efficiency - Conventional Fuel? Col K - J
    :param df: Pandas DataFrame representing data in '2019 FE GUIDE.csv'
    :return: string representing carline
    """
    # axis=1, apply function to each row
    return df.apply(lambda row: row['Hwy FE (Guide) - Conventional Fuel'] -
                    row['City FE (Guide) - Conventional Fuel'], axis=1)\
        .idxmax()


def q7(df):
    """
    What is the average annual fuel cost (Annual Fuel1 Cost -
    Conventional Fuel) of supercharged cars?
    :param df: Pandas DataFrame representing data in '2019 FE GUIDE.csv'
    :return: float representing average annual fuel cost
    """
    # Annual Fuel1 Cost - Conventional Fuel
    # Air Aspiration Method Desc
    return df.loc[df['Air Aspiration Method Desc'] == 'Supercharged'
                  , 'Annual Fuel1 Cost - Conventional Fuel'].mean()


def q8(df):
    """
    What SUV has the lowest annual fuel cost?
    :param df: Pandas DataFrame representing data in '2019 FE GUIDE.csv'
    :return: a string representing the carline
    """
    # Use "Carline Class Desc" to identify SUVs. Col AS, BR
    df_suv = df[df['Carline Class Desc'].str.contains('SUV', na=False)]
    return df_suv['Annual Fuel1 Cost - Conventional Fuel'].idxmin()


def q9(df):
    """
    Which manufacturer has the most cars with manual transmission?
    :param df: Pandas DataFrame representing data in '2019 FE GUIDE.csv'
    :return: string representing manufacturer
    """
    # find the group with the largest members using .size()
    return df[df['Trans Desc'] == 'Manual'].groupby('Mfr Name').size().idxmax()


def q10(df):
    """
    What is the average annual fuel cost by car division?
    :param df: Pandas DataFrame representing data in '2019 FE GUIDE.csv'
    :return: Pandas Series containing car division and average annual fuel cost
    """
    # it returns a Series with one element in agg. If multiple elements
    # in agg, it returns a dataframe.
    return df.groupby('Division').agg({'Annual Fuel1 Cost - Conventional Fuel':
                                       np.mean})


def q11(df):
    """
    The criteria I use to buy a car: 4-Wheel Drive with highest combined
    fuel efficiency.
    :param df: Pandas DataFrame representing data in '2019 FE GUIDE.csv'
    :return: a string representing the perfect carline for me.
    """
    # Drive Desc: '4-Wheel Drive'.
    # Combined Fuel Efficiency: 'Comb FE (Guide) - Conventional Fuel'
    df_wheel = df[df['Drive Desc'] == '4-Wheel Drive']
    return df_wheel['Comb FE (Guide) - Conventional Fuel'].idxmax()


def main():
    # pick index to facilitate answering questions
    df_2019_FE = pd.read_csv('2019 FE Guide.csv', index_col=3).\
        dropna(how='all').dropna(axis=1, how='all')
    # remove rows and cols whose values are all NaN using how='all'
    print(q1(df_2019_FE))
    print(q2(df_2019_FE))
    print(q3(df_2019_FE))
    print(q4(df_2019_FE))
    print(q5(df_2019_FE))
    print(q6(df_2019_FE))
    print(q7(df_2019_FE))
    print(q8(df_2019_FE))
    print(q9(df_2019_FE))
    print(q10(df_2019_FE))
    print(q11(df_2019_FE))


if __name__ == "__main__":
    main()
