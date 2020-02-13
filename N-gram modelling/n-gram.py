from __future__ import unicode_literals
import operator
import re
import numpy as np
import matplotlib.pyplot as plt
from scipy import special

# http://lucumr.pocoo.org/2015/11/18/pythons-hidden-re-gems/

input_s = "This is the shop where I bought my bike.\n The driver drinks liquor, I think someone else ought to drive. I would go with you, only I have no money. She studies grammar. Was she writing a letter ? I do not like fish. Do not come in front of me. I also had only about $2.55. \n Let's see how this goes. following: (1)asdasd (2)sdaasd 3.asdsad 4. #tokenize #nlp_sucks #ax.bx priyankmodi99@gmail.com John M. Mr. Asda @pmodi99 http://regexlib.com/Search.aspx?k=email&AspxAutoDetectCookieSupport=1 name(aka asdad)\n 'How are you?'"

# reg_nospace_word = '\w+|\$[\d\.]+|\S+' #alphabetic sequences, money expressions, and any other non-whitespace sequences
# reg2 = '\s*\n\s*\n\s*'     #
# reg_email = '^\w+@[a-zA-Z_]+?\.[a-zA-Z]{2,3}$'
# reg_punct2 = '''[!"\#$%&'()*+,\-./:;<=>?@\[\\\]^_`{|}~]'''
# reg_punct = '\('
# reg_punct3 = '\)'
# punct_arr = list(reg_punct2)
# reg_sal = '^(Dr|Mrs?|Ms)\.'
# reg_sal2 = '[A-Z]+\.'

scanner = re.Scanner([
        (b"[\x80-\xff]+", lambda scanner,token: ("EMOJI",token)),
        (r"[a-zA-Z0-9]+@([a-zA-Z0-9]+\.*){2,3}",lambda scanner,token: ("EMAIL",token)),
        (r"https?:\/\/(www\.)?[-a-zA-Z0-9@:%._\+~#=]{1,256}\.[a-zA-Z0-9()]{1,6}\b([-a-zA-Z0-9()@:%_\+.~#?&//=]*)",lambda scanner,token: ("LINK",token)),
        (r"#\S+",lambda scanner,token: ("HASHTAG",token)),
        (r"@\S+",lambda scanner,token: ("MENTION",token)),
        (r'[A-Z]\.', lambda scanner, token: ("NNP",token)),
        (r"[0-9]+%", lambda scanner,token: ("PERCENT",token)),
        (r"[0-9.]+", lambda scanner,token: ("DECIMAL",token)),
        (r"([\w]+['][\w]+)", lambda scanner,token: ("APOS",token)),
        (b"(Mr.|Dr.|Ms.|Prof.|Doc.)", lambda scanner,token: ("SAL",token)),
        (r"\w+", lambda scanner,token: ("WORD",token)),
        (r"\$[0-9]+(.[0-9]+)*",lambda scanner,token: ("CURRENCY",token)),
        (r"\s+",lambda scanner,token: None),
        (r"\\n",lambda scanner,token: None),
        (r"[0-9]+", lambda scanner,token: ("NUMBERS",token)),
        (r"'", lambda scanner,token: ("QUOTE",token)),
        (r"[,.?!\-@&;\(\):\/#$\*\|=]+", lambda scanner,token: ("PUNC",token)),
    ])

reg_emoji = "[\x80-\xff]+"
reg_email = "[a-zA-Z0-9]+@([a-zA-Z0-9]+\.*){2,3}"
reg_link = "http[s]*://[A-Z0-9a-z./]*"
reg_hashtag = "#\S+"
reg_mention = "@\S+"
reg_nnp = '[A-Z]\.$'
reg_percent = "[0-9]+%"
reg_decimal = "[0-9.]+"
reg_word = "\w+"
reg_currency = "$[0-9]+(.[0-9]+)*"
reg_space = "\s+"
reg_new_line = "\\n"
reg_numbers = "[0-9]+"
reg_punc = "[,.?!`'’\-@&;\(\):\/#$\*\|=]+"


def ngram(n, list_words):
        ngram_dict = {}
        for i in range(0,len(list_words)-n):
                temp = []
                for j in range(i,i+n):
                        temp.append(list_words[j])
                ngram_dict.append(temp)
        # ngrams = zip(*[list_words[i:] for i in range(n)])
        # return [" ".join(ngram) for ngram in ngrams]

        return ngram_dict


def main():
        frequency = {}
        list_words = []
        fp=open("test.txt","r")
        for line in fp.readlines():
                x,y = scanner.scan(line)
                for i in range(len(x)):
                        list_words.append(x[i][1])
                        # print(x[i][1], end= " ")
                # print("")
                # tokenise(line)
        print(list_words)
        for word in list_words:
                count = frequency.get(word,0)
                frequency[word] = count + 1
        # for key, value in reversed(sorted(frequency.items(), key = operator.itemgetter(1))):
        #         print(key, value)
        # n = 1000
        # frequency = {key:value for key,value in list(frequency.items())[0:n]}
        #convert value of frequency to numpy array
        s = frequency.values()
        s = np.array(list(s))
        # print(s2)
        #Calculate zipf and plot the data
        a = 2. #  distribution parameter
        counts, bins, ignored = plt.hist(s, 50, density=None)
        x = np.arange(1., 50.)
        y = x**(-a) / special.zetac(a)
        plt.plot(x, y/max(y), linewidth=2, color='r')
        plt.show()
        print(ngram(4, list_words))
main()


    
