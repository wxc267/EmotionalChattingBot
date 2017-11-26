import os
import json
from watson import *
from glob import glob
from highcharts import Highchart
from options import *


'''
chatLog is the list of user inputs
["hello! Ebot!","good bye ebot. I will miss you."]
'''
def chatlogAnalyze(chatLog):
	Joy = [] # data for Joy
	Anger = [] # data for Anger
	Disgust = [] # data for Disgust
	Fear = [] # data for Fear
	Sadness = [] # data for Sadness	
	for sentence in chatLog:
		output=analyzeSentence(sentence)
		outputdata = json.loads(output)
		doc=outputdata["document_tone"]
		Tones = doc["tone_categories"][0]["tones"]
		Anger.append(Tones[0]["score"])
		Disgust.append(Tones[1]["score"])
		Fear.append(Tones[2]["score"])
		Joy.append(Tones[3]["score"])
		Sadness.append(Tones[4]["score"])
	return [Joy,Anger,Disgust,Fear,Sadness]
	

def drawChart(options,Hchart,chartType,emotions,fileName):
	Joy = emotions[0] # data for Joy
	Anger = emotions[1] # data for Anger
	Disgust = emotions[2] # data for Disgust
	Fear = emotions[3] # data for Fear
	Sadness = emotions[4] # data for Sadness		
	Hchart.set_dict_options(options)
	Hchart.add_data_set(Joy, chartType, 'joy',color = 'rgb(241,199,28)')
	Hchart.add_data_set(Anger, chartType, 'anger',color ='rgb(207,46,17)')
	Hchart.add_data_set(Disgust, chartType, 'disgust',color ='rgb(118,181,92)')
	Hchart.add_data_set(Fear, chartType, 'fear',color ='rgb(151,77,193)')
	Hchart.add_data_set(Sadness, chartType, 'sadness',color ='rgb(46,116,213)')
	Hchart.save_file(fileName)

'''
emotions are the list of emotion
emotions=[Joy,Anger,Disgust,Fear,Sadness]
'''
def drawAreaChart(emotions,chatLog):
	H_area = Highchart(width=750, height=600)
	H_area.set_options('xAxis',{'categories':chatLog})
	drawChart(options_area,H_area,'area',emotions,'output_charts_area')
	

def drawColumnChart(emotions):
	H_column = Highchart(width=750, height=600)
	H_column.set_options('xAxis',{'categories':['Before','After']})
	drawChart(options_column,H_column,'column',emotions,'output_charts_column')


