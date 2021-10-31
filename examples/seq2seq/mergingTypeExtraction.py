from nltk import word_tokenize
import numpy as np
from nltk.corpus import stopwords
import string
from nltk.stem import PorterStemmer



ps = PorterStemmer()

stop_words = set(stopwords.words('english'))
punct = string.punctuation

def IsMerging(sys_pred, sents):

    sents_words = [[word.lower() for word in word_tokenize(sent)] for sent in sents]
    sys_pred_words = [word.lower() for word in word_tokenize(sys_pred)]

    sents_words_stem = [[ps.stem(word)  for word in sent_words] for sent_words in sents_words]
    sys_pred_words_stem = [ps.stem(word)  for word in sys_pred_words]

    sent_overlap = []
    for sent_words in sents_words_stem:
        sum = 0
        for sys_word in sys_pred_words_stem:
            if (sys_word in sent_words):
                sum += 1
        sent_overlap.append(sum)
    max_idx = np.argmax(sent_overlap)
    max_overlap_words = sents_words_stem[max_idx]
    max_overlap_words_org = sents_words[max_idx]


    # all_words_except_max_sent = []
    # for sent_idx, sent_words in enumerate(sents_words):
    #     if sent_idx == max_idx:
    #         continue
    #     all_words_except_max_sent += sent_words
    # all_words_except_max_sent = list(set(all_words_except_max_sent))

    # [word for sent_words in sents_words for word in sent_words if ]

    for sys_word in sys_pred_words_stem:
        if sys_word not in max_overlap_words:
            for sent_idx, sent_words in enumerate(sents_words_stem):
                if sent_idx == max_idx:
                    continue
                if (sys_word in sent_words) and (sys_word not in stop_words) and (sys_word not in punct):
                    print(line_idx)
                    print('system sent: ', sys_pred)
                    print('max overlap sent: ', ' '.join(max_overlap_words_org))
                    print('uncovered word: ', sys_word)
                    print('complement sent: ', ' '.join(sents_words[sent_idx]))
                    print('\n')
                    return 1

    return 0


input_path = './thadani_#1/test.source'  #test input text

with open(input_path, "r") as f:
    input_lines = f.readlines()

sumA_list = []
sumB_list = []
for sys_idx in range(1,21):
    print ('system #{}'.format(sys_idx))
    sumA = 0
    sumB = 0
    sysA_path = '../../../output_models/thadani_#{}/test_generations.txt'.format(sys_idx)   #path to model_A output
    sysB_path = '../../../output_models/align_wnums_#{}/test_generations.txt'.format(sys_idx)  #path to model_B output
    with open(sysA_path, "r") as f:
        sysA_lines = f.readlines()
    with open(sysB_path, "r") as f:
        sysB_lines = f.readlines()
    for line_idx, line in enumerate(input_lines[:-1]):
        # print(line_idx)
        sents = line.split('</s>')


        sysA_pred = sysA_lines[line_idx]
        sysB_pred = sysB_lines[line_idx]
        sumA += IsMerging(sysA_pred, sents)
        sumB += IsMerging(sysB_pred, sents)
    sumA_list.append(sumA)
    sumB_list.append(sumB)

print('baseline merging: ', np.mean(sumA_list))
print('alignment merging: ',np.mean(sumB_list))
print('out of ',len(sysA_lines))
