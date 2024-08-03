#Press Shift+Enter to run the code
givenstring="Lorem ipsum dolor! diam amet, lorem consetetur Lorem magna. sed diam nonumy eirmod tempor. diam et labore? et diam magna. et diam amet."

class TextAnalizer(object):
    
    def __init__(self, text):
        #remove punctuaction
  # remove punctuation
        formattedText = text.replace('.','').replace('!','').replace('?','').replace(',','')
        
        # make text lowercase
        formattedText = formattedText.lower()
        
        self.fmtText = formattedText

    def freqAll(self):
        #split text into words
        wordList = self.fmtText.split(" ")

        #create dictionary
        freqMap = {}
        for word in set (wordList): # use set to remove duplicates in list
            freqMap[word]= wordList.count(word)

            return freqMap
        
    def freqOf (self,word):
        #get frequency map
        freqDict = self.freqAll()
        if word in freqDict:
            return freqDict[word]
        else:
            return 0
    
analyzed = TextAnalizer(givenstring)

print('Formatted Text', analyzed.fmtText)

freqMap = analyzed.freqAll()
print(freqMap)

word = 'lorem'
frequency  = analyzed.freqOf(word)
print('the word,', word, 'appears', frequency,'times')

