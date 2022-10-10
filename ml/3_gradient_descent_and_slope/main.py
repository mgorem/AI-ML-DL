# program to demonstrate GRADIENT DESCENT:
# having values of x and y, find the best fit line through
# gradient descent.

import numpy as np

def gradient_descent(x,y):
    m_curr = b_curr = 0
    n = len(x)
    learning_rate = 0.001

    # take baby steps to reach global minimum
    # steps to take
    iterations = 1000
    for i in range(iterations):
        # for each step calculate the y_predicted
        y_predicted = m_curr * x + b_curr

        # checking the cost:
        cost = (1/n) * sum([val ** 2 for val in (y-y_predicted)])

        # calculate the derivatives i.e m_deriv and b_deriv
        m_deriv = - (2/n) * sum(x * (y - y_predicted))
        b_deriv = - (2/n) * sum(y - y_predicted)
        m_curr = m_curr - learning_rate * m_deriv
        b_curr = b_curr - learning_rate * b_deriv

        # print the values of m and b at each iteration
        print("m {}, b {}, cost {}, iteration {}".format(m_curr, b_curr, cost, i))

x = np.array([1, 2, 3, 4, 5])
y = np.array([5, 7, 9, 11, 13])

gradient_descent(x, y)
