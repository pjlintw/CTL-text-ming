from txt_reader import TextLoader

# read data
path = '../data/origin_text_data/y.txt'

# , output='myoutput.txt', tags_dir='../data/jieba_dict/CHU_jieba_dict.txt'
f = TextLoader(data_dir=path, output='myoutput.csv', segment='../data/jieba_dict/CHU_jieba_dict.txt',
               tags_dir='../data/anno_dict/data_loc.txt')


