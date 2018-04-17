import svmMLiA
from numpy import *
import operator
dataArr, labelArr = svmMLiA.loadDataSet('testSet.txt')
b,alphas = svmMLiA.smoSimple(dataArr, labelArr, 0.6, 0.001, 40)
