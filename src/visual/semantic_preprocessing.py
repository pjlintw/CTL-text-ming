from src.preprocessing.txt_reader import TextLoader

# read file
f = TextLoader('../preprocessing/myoutput.txt').content

tokens = [i.strip() for i in f.split('\n')]
print(f)
#print(f)

sentences_list = list()
append_list = list()
# filter token

def x(number):
    return 10 if number > 5 else 5
print()

def token_cell(token):
    if len(token) > 1:
        return token
    else:
        return None

for n in range():

for token in tokens:
    if token == '' or token == '。' or token == '！' or token == '？':
        if len(append_list) == 0:
            continue
        sentences_list.append(append_list)
        append_list = list()
    elif '#' in token:
        continue
    elif token in ['，', '「','」','（','）', '『', '『', '；','、']:
        continue
    else:
        append_list.append(token)
print(sentences_list)
# write sentences in line as file
# writer = open('sen_in_line.txt', 'w',encoding='utf-8')
# for i in file_list:
#     writer.write(' '.join(i)+'\n')
# writer.close()

# p
neg_list = ['罵','不悅','畜生','亡','禽獸','賊','身之大穢',
            '穢則','侵人','勿','不好','橫行','惡魅','輕慢',
            '極醜陋','無言','罪人','凶宅','惡魅','邪鬼']

