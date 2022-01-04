import pygal
from die import Die

die = Die()





frequencies = []
for value in range(1,die.num_sides+1):
    frequency = results.count(value)
    frequencies.append(frequency)

hist = pygal.Bar()

hist.title = "Results of rolling one D6 1000 times"
hist.x_labels = [1,2,3,4,5,6,7,8]
hist.x_title = "result"
hist._y_title = "Frequency of Results"

hist.add('D6',frequencies)
hist.render_to_file('die_visual.svg')


