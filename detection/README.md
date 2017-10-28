# Detection

## meaningcloud.com

Clickbait title detection via a API for text classification (meaningcloud.com)

The plugin sends a HTTP POST request to api.meaningcloud.com where we set up a text classification model to detect clickbait

We did this by collecting lots of clickbait titles and pasting them all into the training text field.

We also added some specific relevent terms (extreme, pranks, gone wrong,..) and some irrelevant ones (music video etc.)

## weka

### learning about weka

- training weka: http://ashrafsau.blogspot.ch/2015/03/text-classification-in-weka-with.html?view=sidebar
- https://stackoverflow.com/questions/13432781/how-to-use-weka-for-predict-results
  - https://stackoverflow.com/questions/13432781/how-to-use-weka-for-predict-results
  - http://weka.wikispaces.com/Making+predictions
- predicting with weka
  - how to create a arff file
    - https://weka.wikispaces.com/ARFF+(stable+version)#Examples-The%20@attribute%20Declarations-String%20attributes
