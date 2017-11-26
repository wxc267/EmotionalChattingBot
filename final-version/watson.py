import os
import json
from watson_developer_cloud import ToneAnalyzerV3 
from glob import glob
tone_analyzer = ToneAnalyzerV3(
	  url= "https://gateway.watsonplatform.net/tone-analyzer/api",
	  username="a060ad99-e713-464c-baa8-141156535b8a",
	  password= "rIzF3FpYwy1a",
	  version="2016-05-19"
	)

def analyzeSentence(sentence):
	tone = tone_analyzer.tone(sentence, tones='emotion',
		content_type='text/plain')
	output=json.dumps(tone, indent=2)
	return output

def emo_ana(in_str):
    tone = tone_analyzer.tone(in_str, tones='emotion', content_type='text/plain')
    
    a = tone["document_tone"]["tone_categories"][0]['tones'][0]['score']
    d = tone["document_tone"]["tone_categories"][0]['tones'][1]['score']
    f = tone["document_tone"]["tone_categories"][0]['tones'][2]['score']
    j = tone["document_tone"]["tone_categories"][0]['tones'][3]['score']
    s = tone["document_tone"]["tone_categories"][0]['tones'][4]['score']

    rl = [a,d,f,j,s]
    print rl
    return rl
