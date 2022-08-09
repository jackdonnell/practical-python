current_movies = {'the grinch':'11:00am',
                  'Rudolf':'1:00pm',
                  'frosty the snowman': '3:00pm',
                  }
print('we got:\n')
for i in current_movies:
    print(i)
movie = input('whatchu wanna see')

showtime = current_movies.get(movie)
if showtime == None:
    print('that shits not playing here hun')
else:
    print(movie, 'is playing at', showtime)