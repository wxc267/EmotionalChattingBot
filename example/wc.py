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

with open('tone.json') as tone_json:
  tone = tone_analyzer.tone(json.load(tone_json)['text'], tones='emotion',
    content_type='text/plain')

print(json.dumps(tone, indent=2))
