#Definition: Matplotlib is a Python library used to visualize data through graphs and charts

# 1)Write a Python program to draw a line graph.
import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y = [10, 20, 15, 30, 25]

plt.plot(x, y)
plt.title("Line Graph")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.show()

# 2)Write a Python program to draw a bar chart.
import matplotlib.pyplot as plt

names = ["Amit", "Priya", "Rahul"]
marks = [80, 90, 75]

plt.bar(names, marks)
plt.title("Student Marks")
plt.xlabel("Students")
plt.ylabel("Marks")
plt.show()

# 3)Write a Python program to draw a pie chart.
import matplotlib.pyplot as plt

values = [40, 30, 20, 10]
labels = ["Python", "Java", "C", "C++"]

plt.pie(values, labels=labels, autopct="%1.1f%%")
plt.title("Programming Languages")
plt.show()

# 4)Write a Python program to draw a scatter plot.
import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y = [10, 15, 12, 20, 25]

plt.scatter(x, y)
plt.title("Scatter Plot")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.show()

# 5)Write a Python program to draw a histogram
import matplotlib.pyplot as plt

marks = [40, 50, 50, 60, 60, 60, 70, 80, 90]

plt.hist(marks, bins=5)
plt.title("Marks Distribution")
plt.xlabel("Marks")
plt.ylabel("Frequency")
plt.show()

# 6)Write a Python program to draw two lines on the same graph with a legend.
import matplotlib.pyplot as plt

x = [1, 2, 3, 4]
y1 = [10, 20, 30, 40]
y2 = [15, 25, 20, 35]

plt.plot(x, y1, label="Line 1")
plt.plot(x, y2, label="Line 2")

plt.title("Multiple Line Graph")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.legend()
plt.show()