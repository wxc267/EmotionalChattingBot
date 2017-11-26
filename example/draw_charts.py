import os
import json
from watson_developer_cloud import ToneAnalyzerV3 
from glob import glob
from highcharts import Highchart
H_area = Highchart(width=750, height=600)
H_column = Highchart(width=750, height=600)

tone_analyzer = ToneAnalyzerV3(
  url= "https://gateway.watsonplatform.net/tone-analyzer/api",
  username="a060ad99-e713-464c-baa8-141156535b8a",
  password= "rIzF3FpYwy1a",
  version="2016-05-19"
)

with open('tone.json') as tone_json:
  tone = tone_analyzer.tone(json.load(tone_json)['text'], tones='emotion',
    content_type='text/plain')


output = json.dumps(tone, indent=2)

outputdata = json.loads(output)
Xcategory = []
Joy = [] # data for Joy
Anger = [] # data for Anger
Disgust = [] # data for Disgust
Fear = [] # data for Fear
Sadness = [] # data for Sadness
i=0
j=0

sentence = outputdata["sentences_tone"]
while i<len(sentence) :
	Xcategory.append(str(sentence[i]["text"]))
	Tones = sentence[i]["tone_categories"][0]["tones"]
	Anger.append(Tones[0]["score"])
	Disgust.append(Tones[1]["score"])
	Fear.append(Tones[2]["score"])
	Joy.append(Tones[3]["score"])
	Sadness.append(Tones[4]["score"])
	i=i+1
#print Xcategory



#output_filename = 'output.json'
#fo = open(output_filename, "w")
#fo.write(json.dumps(tone, indent=2))
#fo.close()
#print(json.dumps(tone, indent=2))
#
options = {
    'chart': {
        'type': 'area',
		'renderTo': 'container_area'
    },
    'title': {
        'text': 'Changes in Percentage of Emotions'
    },
    'xAxis': {
        'categories': Xcategory,
        'tickmarkPlacement': 'on',
        'title': {
            'enabled': False
        }
    },
    'yAxis': {
        'title': {
            'text': 'Percent'
        },
        'labels': {
            'formatter': 'function () {\
                                return this.value ;\
                            }'
        }
    },
    'tooltip': {
        'shared': True,

    },

    'plotOptions': {
        'area': {
            'stacking': 'percent',
            'lineColor': '#666666',
            'lineWidth': 1,
            'marker': {
                'lineWidth': 1,
                'lineColor': '#666666'
            },
            'credits': {'enabled': True},
            "legend": {}
        },

        'series': {
            'label': {
                'minFontSize': 5,
                'maxFontSize': 15,
                'enabled':True,
                'style': {
                    'color': 'blue'
                },
                'onArea':True
            }
        }
    }
}

H_area.set_dict_options(options)

H_area.add_data_set(Joy, 'area', 'joy',color = 'rgb(241,199,28)')
H_area.add_data_set(Anger, 'area', 'anger',color ='rgb(207,46,17)')
H_area.add_data_set(Disgust, 'area', 'disgust',color ='rgb(118,181,92)')
H_area.add_data_set(Fear, 'area', 'fear',color ='rgb(151,77,193)')
H_area.add_data_set(Sadness, 'area', 'sadness',color ='rgb(46,116,213)')
H_area.save_file('output_charts_area')

options_column = {
    'chart': {
        'type': 'column',
		'renderTo': 'container_column',
        'options3d': {
            'enabled': True,
            'alpha': 15,
            'beta': 15,
            'viewDistance': 25,
            'depth': 40
        }
    },
    'title': {
        'text': 'Percentage of Emotions to Each Sentence'
    },
    'xAxis': {
        'categories': Xcategory,
        'tickmarkPlacement': 'on',
        'title': {
            'enabled': False
        }
    },
    'yAxis': {
        'title': {
            'text': 'Percent'
        },
        'labels': {
            'formatter': 'function () {\
                                return this.value ;\
                            }'
        }
    },
    'tooltip': {
        'shared': True,

    },

    'plotOptions': {
        'area': {
            'stacking': 'percent',
            'lineColor': '#666666',
            'lineWidth': 1,
            'marker': {
                'lineWidth': 1,
                'lineColor': '#666666'
            },
            'credits': {'enabled': True},
            "legend": {}
        },

        'series': {
            'label': {
                'minFontSize': 5,
                'maxFontSize': 15,
                'enabled':True,
                'style': {
                    'color': 'blue'
                },
                'onArea':True
            }
        }
    }
}

H_column.set_dict_options(options_column)

H_column.add_data_set(Joy, 'column', 'joy',color = 'rgb(241,199,28)')
H_column.add_data_set(Anger, 'column', 'anger',color ='rgb(207,46,17)')
H_column.add_data_set(Disgust, 'column', 'disgust',color ='rgb(118,181,92)')
H_column.add_data_set(Fear, 'column', 'fear',color ='rgb(151,77,193)')
H_column.add_data_set(Sadness, 'column', 'sadness',color ='rgb(46,116,213)')
H_column.save_file('output_charts_column')