# -*- coding: utf-8 -*-
import svmMLiA
from numpy import *
import matplotlib
import matplotlib.pyplot as plt

zhFont1 = matplotlib.font_manager.FontProperties(fname='C:\Windows\Fonts\STXINWEI.TTF')
dataArr, labelArr = svmMLiA.loadDataSet('testSet.txt')
b, alphas = svmMLiA.smoSimple(dataArr, labelArr, 0.6, 0.001, 40)

type1_x = []
type1_y = []
type2_x = []
type2_y = []

plt.figure(figsize=(8,5))
ax = plt.subplot(111)
print 'range(len(labelArr)):'
print range(len(labelArr))
for i in range(len(labelArr)):
	if labelArr[i] == 1:
		type1_x.append(dataArr[i][0])
		type1_y.append(dataArr[i][1])

	if labelArr[i] == -1:
		type2_x.append(dataArr[i][0])
		type2_y.append(dataArr[i][1])

plt.title(u'用圆圈标记的支持向量',fontproperties = zhFont1)
type1 = ax.scatter(type1_x, type1_y, s=20, c='red', marker='.', alpha=0.5)
type2 = ax.scatter(type2_x, type2_y, s=40, c='blue', marker='*', alpha=0.7)	
ax.legend((type1, type2), (u'+1', u' -1'), loc=2, prop=zhFont1)

for i in range(100):
	if(labelArr[i]==1 and alphas[i]>0.0):
		ax.scatter(dataArr[i][0], dataArr[i][1], color='', edgecolors='g', s=200)
	if(labelArr[i]==-1 and alphas[i]>0.0):
		ax.scatter(dataArr[i][0], dataArr[i][1], color='', edgecolors='g', s=200)		
 	
plt.show()