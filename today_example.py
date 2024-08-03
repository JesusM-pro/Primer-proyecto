string = "Mary had a little lamb Little lamb, little lamb Mary had a little lamb.Its fleece was white as snow And everywhere that Mary went Mary went, Mary went Everywhere that Mary went The lamb was sure to go"


def freq(string):
    words=[]

    words= string.lower().split()

    Dict={}

    for key in words:
        Dict[key] = words.count(key)

    print('the frecuenqcy of words is ', Dict)

freq(string)
print(freq)