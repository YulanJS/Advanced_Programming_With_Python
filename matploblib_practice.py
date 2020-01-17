import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
# compare to slides to get complete example code
# plt.plot(1, 2, 'mo')
# plt.plot(3, 1, 'b+')
# plt.plot(2, 1, 'xg')
# plt.plot([1, 2, 3], [2, 4, 1], '-or')
# plt.plot([2, 4, 1], '-gD')  # x coordinate is the index of list
# x_values = np.arange(3, 9, 2)
# y_values = x_values + 2
# plt.plot(x_values, y_values, '--p')
'''
songs_df = pd.read_csv('top2018.csv')
# plt.plot(songs_df['duration_ms']) # x axis is the index position
songs_df['rank'] = songs_df.index + 1  # create a rank column
songs_df.set_index('rank', inplace=True)
# plt.plot(songs_df['duration_ms'])
plt.xlabel('Song Rank')  # position(rank) in the top 99 songs
plt.ylabel('Spotify Attributes')
songs_df['energy'].plot(c='m', marker='.')
songs_df['danceability'].plot(c='g')
# plt.plot(songs_df['energy'], 'b')
# plt.plot(songs_df['danceability'], 'r')
plt.legend()
# right up corner stating which curve representing which characteristic
ax = plt.gca()
ax.axis([1, 99, 0.2, 1])
plt.tick_params(bottom=False, top=False,
                left=False, right=False,
                labelleft=False, labelbottom=False)
plt.title('Characteristics of Popular Songs')
plt.fill_between(range(1, 100), songs_df['danceability'],
                 songs_df['energy'], color='yellow')
plt.show()
'''

'''
lang_pop = {'Python': 27.35, 'Java': 20.64, 'Javascript': 8.4,
                'C#': 7.45, 'PHP': 7.18, 'C/C++': 6.08,
                'others': 22.9}
# plt.bar
plt.pie(lang_pop.values(), explode=(0.1, 0, 0, 0, 0, 0, 0),
        labels=lang_pop.keys())
# highlight one key of dict in explode
plt.show()
'''