import matplotlib.pyplot as plt
import numpy as np
import matplotlib.pyplot as plt

test_names = ["Jayden", "Brent", "Jason", "Yamkela", "Jason 2"]
test_scores = [12, 99, 65, 85, 42]
x_pos = [i for i, _ in enumerate(test_names)]    # labels on the x-axis
# labeling and visuals
plt.bar(x_pos, test_scores, color='black')
plt.xlabel("Names")
plt.ylabel("Marks (%)")
plt.title("Python Marks For 5 Students")
plt.xticks(x_pos, test_names)
plt.show()

"""import numpy
from scipy import stats

test_scores = [12, 99, 86, 87, 88, 45, 87, 94, 78, 77, 85, 86]
my_mean = numpy.mean(test_scores)
print("the mean is: ", mymean)

my_mode = stats.mode(test_scores)
print("the mode is: ", my_mode)

x = numpy.percentile(test_scores, 75)
print("The 75% percentile for the marks is ", x)"""
