from random import randint
TRAIN_SET_LIMIT = 10
TRAIN_SET_COUNT = 10

TRAIN_INPUT = list()
TRAIN_OUTPUT = list()
for i in range(TRAIN_SET_COUNT):
    a = randint(0, TRAIN_SET_LIMIT)
    b = randint(0, TRAIN_SET_LIMIT)
    c = randint(0, TRAIN_SET_LIMIT)
    op = a + (2*b) + (3*c)
    TRAIN_INPUT.append([a, b, c])
    TRAIN_OUTPUT.append(op)

from sklearn.linear_model import LinearRegression

predictor = LinearRegression(n_jobs=-1)
predictor.fit(X=TRAIN_INPUT, y=TRAIN_OUTPUT)

import sys

x1=int(sys.argv[1])
x2=int(sys.argv[2])
x3=int(sys.argv[3])

X_TEST = [[x1,x2,x3]]
outcome = predictor.predict(X=X_TEST)
print ('Result :: ', outcome)
