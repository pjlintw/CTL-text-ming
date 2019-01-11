import codecs
import re
import jieba

"""
1. processing ctl txt
2. save as txt
3. save as csv
"""


class TextLoader():
    """A text object which contains features to process textual data

    Features:
        1. cut               : Using jieba segmentation tool
        2. load_dict_from_txt: Build Dictionary for tagging, segment..
        3. removal_comment   :   ［word...］
        4. removal_modify    :   〈word...〉 and 【word..】

    """
    def __init__(self, data_dir, output=None, segment=None, tags_dir=None):
        self.data_dir = data_dir
        self.output = output
        self.segment_dir = segment
        self.tags_dir = tags_dir
        self.preprocess(data_dir)
        self.len = self.__len__()

        if output:
            self.txt_to_excel(self.output, self.segment_dir, self.tags_dir)

    def __repr__(self):
        return f"TextLoad('{self.data_dir}', output='{self.output}', segment='{self.segment_dir}')"

    def __str__(self):
        return self.content

    def __len__(self):
        return len(self.content)

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

    @staticmethod
    def load_dict_from_txt(fname):
        return [ i for i in open(fname,'r', encoding='utf-8').read().split('\n') if i != '']


    def save_txt(self):
        # !!!!!! not finish yet !!!!!
        # write jieba txt
        with open('chu_jieba_cut.txt','w',encoding='utf-8') as f:
            f.write(self.cut(self.content))

    def txt2sentence(self, txt):
        pass

    def txt_to_excel(self, output, segment_dir, tags_dir):
        # self.removal_comment()
        # self.removal_modify()
        self.content = self.content.replace('\n\n','\n')


        writer = open(output, 'w', encoding='utf-8-sig')

        segment_list = self.load_dict_from_txt(segment_dir)
        tags_list = self.load_dict_from_txt(tags_dir)
        ind = 0
        for line in self.cut(dict_name=segment_list).split('\n'):

            new_line = [i for i in line.split(' ') if i != '' and i !='\r']

            for word in new_line:
                if word in tags_list:
                    writer.write(str(ind) + ', ' + word + ', ' + 'LOC' + '\n')
                else:
                    writer.write(str(ind) + ', ' + word + '\n')
                ind += 1
            writer.write('\n')
        writer.close()


