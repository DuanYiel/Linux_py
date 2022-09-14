str='X-DSPAM-Confidence: 0.8475'

place=str.find(':')

print(place)

place1=str[place+1:]

print(place1)

print(float(place))
