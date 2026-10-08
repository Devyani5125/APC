# # # 1)numpy
# # import numpy as np

# # a = np.array([1, 2, 3])
# # b = np.array([[1, 2], [3, 4]])
# # c = np.array([[[1, 2], [3, 4]]])

# # print("1D Array:")
# # print(a)

# # print("2D Array:")
# # print(b)

# # print("3D Array:")
# # print(c)

# # 2)print 1d and 3d  array
# # import numpy as np

# # a = np.array([10, 20, 30, 40])

# # b = np.array([
# #     [[1, 2], [3, 4]],
# #     [[5, 6], [7, 8]]
# # ])

# # print("1D Array:")
# # print(a)

# # print("3D Array:")
# # print(b)

# # 3)transpose of 
# # import numpy as np

# # a = np.array([[1, 2, 3],
# #               [4, 5, 6]])

# # print("Original Array:")
# # print(a)

# # print("Transpose:")
# # print(a.T)


# # 4)add elements in array
# # import numpy as np

# # a = np.array([10, 20, 30])

# # print("Original Array:")
# # print(a)

# # a = np.append(a, 40)

# # print("After adding element:")
# # print(a)


# #5) Matrix Operations (+, -, *, /)
# # import numpy as np

# # a = np.array([[10, 20],
# #               [30, 40]])

# # b = np.array([[2, 4],
# #               [5, 8]])

# # print("Addition:")
# # print(a + b)

# # print("Subtraction:")
# # print(a - b)

# # print("Multiplication:")
# # print(a * b)

# # print("Division:")
# # print(a / b)


# # 6)exponential function
# # import numpy as np

# # a = np.array([1, 2, 3, 4])

# # print("Array:")
# # print(a)

# # print("Exponential:")
# # print(np.exp(a))

# # 7)pandas
# # import pandas as pd

# # data = [10, 20, 30]

# # s = pd.Series(data, index=["A", "B", "C"])

# # print(s)



# #8) Pandas DataFrame
# import pandas as pd

# data = {
#     "Name": ["Amit", "Rahul", "Priya"],
#     "Marks": [80, 75, 90]
# }

# df = pd.DataFrame(data)

# print(df)
# # 9)create a csv file
# # import pandas as pd

# # data = {
# #     "Name": ["Amit", "Rahul", "Priya"],
# #     "Marks": [80, 75, 90]
# # }

# # df = pd.DataFrame(data)

# # df.to_csv("student.csv", index=False)

# # print("CSV file created successfully")

# # 10)read csv file
# # import pandas as pd

# # df = pd.read_csv("student.csv")

# # print("CSV File Data:")
# # print(df)