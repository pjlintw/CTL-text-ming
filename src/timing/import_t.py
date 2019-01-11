from src.preprocessing.txt_reader import TextLoader
from src.timing.timing import Time


# start
Time.start()

txt_data_dir = '../data/origin_text_data/周氏冥通記 書本 二校 無註本.txt'

# init text class
f = TextLoader(txt_data_dir)


loc_list_dir = '../data/anno_dict/data_loc.txt'
jieba_dict_dir = '../data/jieba_dict/CHU_jieba_dict.txt'


# processing and save it: cut,
TextLoader.txt_to_excel(f, output='../data/new.txt', segment_dir=jieba_dict_dir, tags_dir=loc_list_dir)