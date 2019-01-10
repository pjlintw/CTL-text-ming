import codecs
import re
import jieba

"""
1. processing ctl txt
2. save as txt
3. save as csv
"""


class TextLoader():
    def __init__(self, data_dir, output=None, segment=None):
        self.data_dir = data_dir
        self.output = output
        self.segment_dir = segment
        self.preprocess(data_dir)

        if output:
            self.txt_to_excel(self.output, self.segment_dir)

    def preprocess(self, data_dir):
        with codecs.open(data_dir, 'r', encoding='utf-8') as file:
            self.content = file.read()

    def removal_comment(self):
        comment_pattern = u'［[^&].+］'
        comment_lst = re.findall(comment_pattern, self.content)
        for i in comment_lst:
            self.content = self.content.replace(i, '')

    def removal_modify(self):
        modify_pattern = u'〈[^〉]+〉|【[^】]+】'
        modify_lst = re.findall(modify_pattern, self.content)
        for i in modify_lst:
            self.content = self.content.replace(i, '')

    def cut(self, dict_name=None):
        jieba.load_userdict(dict_name)
        return ' '.join(jieba.cut(self.content))

    def load_dict_from_txt(self, fname):
        return [ i for i in open(fname,'r', encoding='utf-8').read().split('\n') if i != '']


    def save_txt(self):
        # !!!!!! not finish yet !!!!!
        # write jieba txt
        with open('chu_jieba_cut.txt','w',encoding='utf-8') as f:
            f.write(self.cut(self.content))

    def txt2sentence(self, txt):
        pass

    def txt_to_excel(self, output, segment_dir):
        self.removal_comment()
        self.removal_modify()
        print(self.content)


        writer = open(output, 'w', encoding='utf-8-sig')

        segment_list = self.load_dict_from_txt(segment_dir)
        for ind, line in enumerate(self.cut(dict_name=segment_list).split('\n')):
            new_line = [i for i in line.split(' ') if i != '']

            for word in new_line:
                if word in segment_list:
                    writer.write(str(ind) + ', ' + word + ', ' + 'LOC' + '\n')
                else:
                    writer.write(str(ind) + ', ' + word + '\n')
                ind += 1
            writer.write('\n')
        writer.close()


