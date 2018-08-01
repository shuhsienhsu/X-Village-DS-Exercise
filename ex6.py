import json

with open('external_data/ptt_0726_s.json', 'r', encoding='utf-8') as f:
    text = json.load(f)

record = []
for i in range(len(text)):
    if(text[i]['h_推文總數']):
        record += [i]
        #print(text[i]['h_推文總數']['all'])

for i in range(1, len(record)):
    for j in range(i):
        j = i - j - 1
        if(text[record[j]]['h_推文總數']['all'] < text[record[j + 1]]['h_推文總數']['all']):
            temp = text[record[j]]
            text[record[j]] = text[record[j + 1]]
            text[record[j + 1]] = temp
        else:
            break
        #if(text[record[j]]['h_推文總數']['all'] > text[record[j - 1]]['h_推文總數']['all']):
            #temp = text[record[j]]
            #text[record[j]] = text[record[j - 1]]
            #text[record[j - 1]] = temp

for k in record:
    #print(text[k])
    print(text[k]['h_推文總數']['all'])
