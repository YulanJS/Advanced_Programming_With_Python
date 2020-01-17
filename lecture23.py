# ----------------------------------------------------------------------
# Name:        lecture23
# Purpose:     Demonstrate the use of Pandas
#
# Author:      Rula Khayrallah
# ----------------------------------------------------------------------
"""
Skeleton module to be used in lecture 23.

Demonstrate using Pandas to answer the following questions about
National Parks.
What state is Glacier National Park in?
What is the park code and acreage of Yosemite National Park?
What is the largest national park in the US?
What state is home to the smallest national park?
How many national parks are there in Washington State?
How many national parks are there in California?
What is the average acreage of National parks?
What is the total area occupied by national parks in each state and
between which latitudes/longitudes are these parks located?
"""
import pandas as pd
import numpy as np
import re


def q1(df):
    """
    What state is Glacier National Park in?
    :param df: Pandas DataFrame representing the data in parks.csv
    :return: string - the name of the state where Glacier National Park
            is located
    """
    return df.loc['Glacier National Park', 'State']


def q2(df):
    """
    What is the park code and acreage of Yosemite National Park?
    :param df: Pandas DataFrame representing the data in parks.csv
    :return: tuple (string, integer) Park code and acreage
    """
    # Your code here
    yosemite = df.loc['Yosemite National Park']
    return yosemite['Park Code'], yosemite['Acres']


def q3(df):
    """
    What is the largest national park in the US?
    :param df: Pandas DataFrame representing the data in parks.csv
    :return: string - name of the largest park.
    """
    return df['Acres'].idxmax()


def q4(df):
    """
    What state is home to the smallest national park?
    :param df: Pandas DataFrame representing the data in parks.csv
    :return: string - name of the state home to the smallest park.
    """
    return df.loc[df['Acres'].idxmin(), 'State']


def q5(df):
    """
    How many national parks are there in Washington State?
    :param df: Pandas DataFrame representing the data in parks.csv
    :return: integer
    """
    return len(df[df['State'] == 'WA'])


def q6(df):
    """
    How many national parks are there in California?
    :param df: Pandas DataFrame representing the data in parks.csv
    :return: integer
    """
    # The state of Death Valley is stored as "CA NV"
    return len(df[df['State'].str.contains('CA')])


def q7(df):
    """
    What is the average acreage of National parks?
    :param df: Pandas DataFrame representing the data in parks.csv
    :return: float
    """
    return df['Acres'].mean()


def q8(df):
    """
    What is the total area occupied by national parks in each state and
    between which latitudes/longitudes are these parks located?
    :param df: Pandas DataFrame representing the data in parks.csv
    :return: : Pandas DataFrame
    """
    result = df.groupby("State").agg({"Acres": np.sum,
                                      "Latitude": (np.max, np.min),
                                      "Longitude": (np.max, np.min)})
    print(result)


def question1(df):
    """
    How many total species (species ids) are there?
    :param df: Pandas DataFrame representing the data in species.csv
    :return: integer
    """
    return len(df)


def question2(df):
    """
    How many unique species (by 'Scientific Name') are there?
    :param df: Pandas DataFrame representing the data in species.csv
    :return: integer
    """
    return len(df['Scientific Name'].unique())


def question3(df):
    """
    How many endangered species are there?
    :param df: Pandas DataFrame representing the data in species.csv
    :return: integer
    """
    return len(df[df['Conservation Status'] == 'Endangered'])


def question4(df):
    # each boolean mask need to be in parentheses
    # can also use df.loc[several boolean masks]
    return len(df[(df['Conservation Status'] == 'Endangered') &
                  (df['Nativeness'] == 'Native')])


def question5(df):
    return len(df[(df['Conservation Status'] == 'Species of Concern') &
                  (df['Category'] == 'Bird')])


def question6(df):
    # don't use chain [][]
    return df.loc[(df['Park Name'] == 'Yosemite National Park') &
                  (df['Conservation Status'] == 'Threatened') &
                  (df['Category'] == 'Fish'), 'Common Names']


def question7(df):
    # common name contains bear
    # Bulb-Bearing ...
    # to deal with that, use regex with str.contains
    # bear on the word boundary
    # unique() act on Series to get a numpy array
    # There is a insect whose name contains bear, use category = mammal
    # to filter it out
    return df.loc[(df['Common Names'].str.contains(r'\bBear\b',
                                                   flags=re.IGNORECASE)) &
                  (df['Category'] == 'Mammal'), 'Park Name'].unique()


def qb1(df):
    # use boolean mask with new df_wa
    # access by index is faster
    # if state is regular col, we can use two boolean masks
    df_wa = df.loc['WA']
    return len(df_wa[df_wa['Conservation Status'] == 'Endangered'])


def qb2(df):
    # ignore the park belongs to two states
    # only count for one particular col instead of counting all cols
    # will count all non-NaN values
    result = df.groupby('State').count()['Common Names']
    # will get a Series
    return result.idxmax()


def qb3(df):
    # str.contains doesn't know what to do with NaN
    endangered_df = df.loc[df['Conservation Status'].str.contains('Endangered',
                                                                  na=False)]
    return endangered_df.groupby('State').count()['Common Names'].idxmax()


def main():
    # Read the csv file and use column 0 (Park Name) as our index
    df_parks = pd.read_csv('parks.csv', index_col=1)
    # Question 1
    print(f'Glacier National Park is in {q1(df_parks)}.')
    print(q2(df_parks))
    print(q3(df_parks))
    print(q4(df_parks))
    print(q5(df_parks))
    print(q6(df_parks))
    print(q7(df_parks))
    q8(df_parks)
    df_species = pd.read_csv('species.csv', index_col=0, usecols=range(13))
    # load col 0 to 12
    print(question1(df_species))
    print(question2(df_species))
    print(question3(df_species))
    print(question4(df_species))
    print(question5(df_species))
    print(question6(df_species))
    print(question7(df_species))
    df_both = pd.merge(df_parks, df_species, on='Park Name')
    # set state col as index, it is not a regular col any more
    # don't return a copy, change in place, save in the same DataFrame
    df_both.set_index('State', inplace=True)
    print(qb1(df_both))
    print(qb2(df_both))
    print(qb3(df_both))
    df_multi = pd.merge(df_parks, df_species, on='Park Name')


if __name__ == "__main__":
    main()
