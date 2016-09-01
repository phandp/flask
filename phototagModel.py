#!/usr/bin/python
# Filename: phototagModel.py

from sklearn.externals import joblib
import random
import json
import time

from sklearn.datasets import load_boston
dataB = load_boston()

from sklearn.linear_model import LinearRegression
clf = LinearRegression()
clf.fit(dataB.data, dataB.target)


def doPrediction(data):
	
	# do some ML here
	print "JSON Object received from the FE client  ", data

	answer = [
	[0.96, 0.16, 0.08, 0.04, 0.02, 0.012],
	[0.21, 0.86, 0.08, 0.04, 0.02, 0.012],
	[0.91, 0.26, 0.18, 0.04, 0.02, 0.012],
	[0.91, 0.26, 0.18, 0.04, 0.02, 0.012],
	[0.91, 0.26, 0.18, 0.04, 0.02, 0.012],
	[0.91, 0.26, 0.18, 0.04, 0.02, 0.012],
	[0.91, 0.26, 0.18, 0.04, 0.02, 0.012],
	[0.91, 0.26, 0.18, 0.04, 0.02, 0.012],
	[0.91, 0.26, 0.18, 0.04, 0.02, 0.012],
	[0.91, 0.26, 0.18, 0.04, 0.02, 0.012],
	[0.04, 0.26, 0.18, 0.04, 0.91, 0.012],
	[0.91, 0.26, 0.18, 0.04, 0.02, 0.012],
	[0.91, 0.26, 0.18, 0.04, 0.02, 0.012],
	[0.1, 0.26, 0.18, 0.96, 0.02, 0.012],
	[0.91, 0.26, 0.18, 0.04, 0.02, 0.012],
	[0.91, 0.26, 0.18, 0.04, 0.02, 0.012],
	[0.91, 0.26, 0.18, 0.04, 0.02, 0.012],
	[0.91, 0.26, 0.18, 0.04, 0.02, 0.012],
	[0.91, 0.26, 0.18, 0.04, 0.02, 0.012],
	[0.91, 0.26, 0.18, 0.04, 0.02, 0.012],
	[0.91, 0.26, 0.18, 0.04, 0.02, 0.012],
	[0.91, 0.26, 0.18, 0.04, 0.02, 0.012],
	]

	predictionObject = [{ "label": "healthy", "confidence": str(answer[data][0]) },
	 { "label": "fibrosis", "confidence": str(answer[data][1]) }, 
	 { "label": "ground_glass", "confidence": str(answer[data][2]) }, 
	 { "label": "consolidation", "confidence": str(answer[data][3]) },
	 { "label": "reticulation", "confidence": str(answer[data][4]) },
	 { "label": "micronodules", "confidence": str(answer[data][5]) }
	 ]


	time.sleep(0.5)	

	return predictionObject



# End of phototagModel.py


			