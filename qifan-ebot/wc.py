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

##with open('tone.json') as tone_json:
####    print type(json.load(tone_json)['utterances'])
##  tone = tone_analyzer.tone("good bye!", tones='emotion', content_type='text/plain')

##in_str = "goodbye my friend"

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
