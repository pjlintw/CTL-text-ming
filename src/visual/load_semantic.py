from src.preprocessing.txt_reader import TextLoader

semantic = TextLoader.load_dict_from_txt('../data/semantic/semantic2.txt')
semantic = [ i.split('\t') for i in semantic if i != '']


dict = {}
for i_pair in semantic:
    word = i_pair[0]
    word_semantic = i_pair[1]

    if word not in dict:
        dict[word] = [0, 0, 0]

    if word_semantic == '-1':
        dict[word][0] += 1
    elif word_semantic == '0':
        dict[word][1] += 1
    elif word_semantic == '1':
        dict[word][2] += 1

    #print(word, dict[word])

def get_semantic(word):
    try:
        max_value = max(dict[word])
        return dict[word].index(max_value) - 1

    except:
        return None

# print(get_semantic('向後'))
# print(get_semantic('靈芝'))
# print(get_semantic('歿'))