from src.visual.semantic_preprocessing import neg_list
from src.visual.load_semantic import get_semantic

print(neg_list)
neg_list.append('不能')
neg_list.append('死')
neg_list.append('劫')
neg_list.append('未報')

f = open('sen_in_line.txt','r',encoding='utf-8').read()

sentence_list = [ i.split(' ') for i in f.split('\n') if i != '']

writer = open('sen_with_value.txt', 'w',encoding='utf-8')
lst = list()
for i in sentence_list:
    v = 0
    for word in i:
        if word in neg_list:
            v -= 1
        try:
            v += get_semantic(word)
        except:
            pass
            #print('no word {}'.format(word))
    writer.write(str(v) + ', ')
    writer.write(' '.join(i)+'\n')
writer.close()
