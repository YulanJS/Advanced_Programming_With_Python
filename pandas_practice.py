import pandas as pd
import numpy as np
prices = pd.Series([2.25, 1.59, 1.75, 3])
print(prices)
print(prices.index)
print(prices.values)
type(prices.values)
fruits = ['apples', 'oranges', 'bananas', 'strawberries']
prices = pd.Series([2.25, 1.59, 1.75, 3], index=fruits, name='SpartanFresh')
# associate with name to convenient concatenating columns
print(prices)
print(type(prices))
print(prices.index)
print(prices.name)
gradebook = {'Zoe': 8, 'Alex': 20, 'Dan': 9.5, 'Anna': 19}
midterm = pd.Series(gradebook)
print(midterm)
print(midterm.iloc[2])  # numeric index position
#  print(midterm[2])  # not recommended, gives 9.5 in this case
print(midterm.loc['Dan'])
puzzle = pd.Series([10, 20, 30], index=[1, 2, 3])
print(puzzle)
# print(puzzle[2])  # 20
# print(puzzle[0])  # KeyError
# index value: use loc, index position: use iloc
print(midterm.mean())
print(midterm.idxmin())  # similar to python min, returns key
print(midterm.idxmax())
final = pd.Series({'Zoe': 18, 'Alex': 29, 'Dan': 15, 'Anna': 30})
exams = midterm + final
print(exams)
final = pd.Series({'Zoe': 18, 'Alex': 29, 'Dave': 15, 'Anna': 30})
exams = midterm + final
print(exams)
# index: NaN when an index appears in one series but not the other
first = np.NaN
second = np.NaN
print(first == second)
print(exams.isnull())  # to detect NaN
print(exams.dropna())  # not to present rows with NaN as data
print(exams)  # exams are not modified
print(exams.dropna(inplace=True))  # returns None here
print(exams)  # rows with NaN are deleted
exams = midterm + final
print(exams.fillna(0))  # replace NaN data with 0
print(exams)  # exams are not modified
exams = midterm + final
print(exams.fillna(midterm))  # when NaN, replace it with midterm value
print(exams.fillna(midterm).fillna(final))
new_grades = midterm.apply(lambda grade: grade + 0.5 if grade < 10 else grade)
print(new_grades)
print(midterm)  # not modified
midterm += 1  # add 1 to each values
print(midterm)
prices *= 0.6
final.loc['Lynn'] = 20.5  # add a index value pair to Series
print(final)
# series indexes don't have to be unique
fruits = ['apples', 'oranges', 'bananas', 'strawberries', 'apples', 'apples']
prices = pd.Series([2.25, 1.59, 1.75, 3, 2, 1.99], index=fruits)
print(prices.loc['apples'])
print(type(prices.loc['apples']))  # if single value, type: float
# if multiple values in Series, type: pd.Series
gradebook = {'Zoe': 8, 'Alex': 20, 'Dan': 9.5, 'Anna': 19}
midterm = pd.Series(gradebook, name='midterm grade')
final = pd.Series({'Zoe': 18, 'Alex': 29, 'Dan': 15, 'Anna': 30},
                  name='final grade')
cs122 = pd.concat([midterm, final], axis=1)  # axis=0: row, axis=1: col
print(cs122)
print(type(cs122))  # pandas.DataFrame #if axis=0, type: Series
# each row of DataFrame is a Series
print(cs122.loc['Dan'])  # type: pd.Series
# print(cs122['Dan'])  # [] are reserved for cols, KeyError
print(cs122['final grade'])  # pd.Series
print(cs122.loc['Dan', 'final grade'])  # returns a view
#  view: original data will be changed as change to view
#  efficiency: don't have to make a copy every time to keep the original
#  data structure, so use view
#  print(cs122['Dan']['final grade'])  # Not efficient, wrong way,
#  it makes a copy
print(cs122.loc['Dan':, 'final grade'])
new_cs122 = cs122.drop('Dan', inplace=True)
print(new_cs122)
print(cs122)  # original data not changed
# need to use inplace=True
# drop axis=1
cs122.loc['Dave'] = 0
print(cs122)  # add the value to both cols
cs122['Homework'] = None
print(cs122)  # add a column


