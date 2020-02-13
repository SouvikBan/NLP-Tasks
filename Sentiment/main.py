from cltk.tokenize.sentence import TokenizeSentence
from nltk.corpus import sentiwordnet as swn
import nltk
import re

'''Finds the part of the string which comes after the delimiter'''
def substring_after(s, delim):
    return s.partition(delim)[2]

'''Finds the part of the string which comes before the delimiter'''
def substring_before(s, delim):
    return s.partition(delim)[0]

'''Finds the part of the string which comes between the two delimiter'''
def substring_before_after(s, delim1, delim2):
    temp = s.partition(delim1)[2]
    return temp.partition(delim2)[0]

tokenizer = TokenizeSentence('bengali')
f = open("data.txt","r")

lines = f.readlines()
lines = [x.rstrip() for x in lines] 
i = 0
tokenized_list = []
pattern = "^([0-9])*\)"
bengali_text_tokenize = []

for line in lines:
    if re.search(pattern,line):
        tokenized_list.append(bengali_text_tokenize)
        bengali_text_tokenize = []
    
    bengali_text_tokenize += tokenizer.tokenize(line)

tokenized_list.append(bengali_text_tokenize)

f1 = open("new.txt","r")
lines1 = f1.readlines()

i=0
list_matched = []
for tweet in tokenized_list:
    for word in tweet:
        for delimited_word in lines1:
            if  word == substring_after(delimited_word, "#").rstrip("\n\r"):
                list_matched.append([word,substring_before(delimited_word,":"),i,substring_before_after(delimited_word,":","#")])
    i += 1

# print(list_matched)
count = 0

score_list = [[0,0] for i in range(len(tokenized_list))]
num_negative = [ 0 for i in range(len(tokenized_list))]
num_positive = [ 0 for i in range(len(tokenized_list))]
for word in list_matched:
    # print(word[3])
    # print(word[2], word[3])
    if word[3]  == 'NN' or word[3] == 'NNS' or word[3] == 'NP':
        count+=1
        try:
            breakdown = swn.senti_synset(word[1] + '.n.01')
            if breakdown.pos_score() > breakdown.neg_score():
                num_positive[word[2]-1] += 1                
            elif breakdown.pos_score() < breakdown.neg_score():
                num_negative[word[2]-1] += 1        
            else:
                num_positive[word[2]-1] += 1                            
                num_negative[word[2]-1] += 1                          
        except:
            # print("n",word[2])
            pass
    
    if word[3]  == 'VV' or word[3] == 'VBP' or word[3] == 'VVP':
        count+=1
        try:
            breakdown = swn.senti_synset(word[1] + '.v.01')
            if breakdown.pos_score() > breakdown.neg_score():
                num_positive[word[2]-1] += 1                
            elif breakdown.pos_score() < breakdown.neg_score():
                num_negative[word[2]-1] += 1    
            else:
                num_positive[word[2]-1] += 1                            
                num_negative[word[2]-1] += 1                              
            # print(breakdown.pos_score())
        except:
            # print("v",word[2])
            pass

    if word[3]  == 'JJ':
        count+=1
        try:
            breakdown = swn.senti_synset(word[1] + '.a.01')
            if breakdown.pos_score() > breakdown.neg_score():
                num_positive[word[2]-1] += 1                
            elif breakdown.pos_score() < breakdown.neg_score():
                num_negative[word[2]-1] += 1         
            else:
                num_positive[word[2]-1] += 1                            
                num_negative[word[2]-1] += 1                         
            #print(breakdown)
        except:
            # print("a",word[2])
            pass

    if word[3]  == 'RB':
        count+=1
        try:
            breakdown = swn.senti_synset(word[1] + '.r.01')
            if breakdown.pos_score() > breakdown.neg_score():
                num_positive[word[2]-1] += 1                
            elif breakdown.pos_score() < breakdown.neg_score():
                num_negative[word[2]-1] += 1
            else:
                num_positive[word[2]-1] += 1                            
                num_negative[word[2]-1] += 1                            
            #print(breakdown)
        except:
            # print("r",word[2])
            pass

    score_list[word[2]-1] = [num_positive[word[2]-1],num_negative[word[2]-1]]

answer = []
count = 0
for i in score_list:
    if i[0] > i[1]:
        print("POSITIVE", count)
    if i[1] > i[0]:
        print("NEGATIVE", count)
    else:
        print("NEUTRAL", count)
    count+=1
    
#print(score_list)