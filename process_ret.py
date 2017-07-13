# coding: utf-8
import sys
import json

reload(sys)
sys.setdefaultencoding('utf-8')


def strip_word_in_list(word):
    word = word.strip()
    word = word.strip("[")
    word = word.strip("]")
    word = word.strip('"')
    word = word.strip(';')
    return word


def replace_three_title(line,title):
    line = line.replace(title[0], "/")
    line = line.replace(title[1], "/")
    line = line.replace(title[2], "/")
    return line


def replace_eng_title(line, title):
    line = line.replace(title[0], "/")
    line = line.replace(title[1],"/")
    return line


def replace_syn_title(line, title):
    line = line.replace(title[0], "/")
    line = line.replace(title[2],"/")
    return line


def get_syn_three(line, file):
    all = line[1].split("/")
    for i in range(len(all)):
        if i != 2:  # 不加英文名
            if line[0] != all[i]:
                if all[i] != "":
                    if "，" in all[i]:
                        tmp = all[i].split("，")
                        for t in tmp:
                            strip_word_in_list(t)
                            file.write(line[0])
                            file.write("=")
                            file.write(t)
                            file.write("\n")
                    elif "、" in all[i]:
                        tmp = all[i].split("、")
                        for t in tmp:
                            strip_word_in_list(t)
                            file.write(line[0])
                            file.write("=")
                            file.write(t)
                            file.write("\n")
                    elif " " in all[i]:
                        tmp = all[i].split(" ")
                        for t in tmp:
                            strip_word_in_list(t)
                            file.write(line[0])
                            file.write("=")
                            file.write(t)
                            file.write("\n")
                    else:
                        strip_word_in_list(all[i])
                        file.write(line[0])
                        file.write("=")
                        file.write(all[i])
                        file.write("\n")


def get_syn_two(line, file):
    for seg_syn in line[1].split("/"):
        if line[0] != seg_syn:
            if seg_syn != "":
                if "，" in seg_syn:
                    tmp = seg_syn.split("，")
                    for t in tmp:
                        strip_word_in_list(t)
                        file.write(line[0])
                        file.write("=")
                        file.write(t)
                        file.write("\n")
                elif "、" in seg_syn:
                    tmp = seg_syn.split("、")
                    for t in tmp:
                        strip_word_in_list(t)
                        file.write(line[0])
                        file.write("=")
                        file.write(t)
                        file.write("\n")
                elif " " in seg_syn:
                    tmp = seg_syn.split(" ")
                    for t in tmp:
                        strip_word_in_list(t)
                        file.write(line[0])
                        file.write("=")
                        file.write(t)
                        file.write("\n")
                else:
                    strip_word_in_list(seg_syn)
                    file.write(line[0])
                    file.write("=")
                    file.write(seg_syn)
                    file.write("\n")


check_title = ["中文名", "外文名", "别名"]
singer_info = []
with open("/home/lulu/Desktop/vinci/svm/test/v2/歌手信息/singer_info.txt") as f:
    for line in f:
        each_singer_info = line.split('"')
        each_singer_info[1] = strip_word_in_list(each_singer_info[1])
        each_singer_info[3] = strip_word_in_list(each_singer_info[3])
        singer_info.append([each_singer_info[1], each_singer_info[3]])

for line in singer_info:
    print json.dumps(line, ensure_ascii=False)

with open("/home/lulu/Desktop/vinci/svm/test/v2/歌手信息/syn_info.txt", "w") as syn:
    for line in singer_info:
        if "国籍" in line[1]:
            line[1] = line[1].replace("国籍","/")
            replace_res = line[1].split("/")
            line[1] = replace_res[0]
            if check_title[0] in line[1] and check_title[1] in line[1] and check_title[2] in line[1]:
                line[1] = replace_three_title(line[1], check_title)
                get_syn_three(line, syn)
            elif check_title[0] in line[1] and check_title[1] in line[1]:
                pass
            elif check_title[0] in line[1] and check_title[2] in line[1]:
                line[1] = replace_syn_title(line[1], check_title)
                get_syn_two(line, syn)
            elif check_title[0] in line[1]:
                line[1] = line[1].replace(check_title[0], "/")
                get_syn_two(line, syn)
            else:
                print "singer %s has no chinese name in baike" %(line[0])

        else:
            print "singer %s has no nationality in baike" %(line[0])





# badcase = ["阿鲲","林志炫", "白银河", "萧煌奇", "蔡幸娟", "飞轮海", "黄建为","墨明棋妙","逃跑计划", "霹雳英雄"]
# split_tag = ["", "", "", "民族", "星座", "经纪公司", "出生地", "无", "主唱", "无"]
# 阿鲲 = 陈鲲
# 阿鲲 = Roc
# Chen
# 林志炫 = Terry
# Lin
# 白银河 = 白银河乐团
# 萧煌奇 = Ricky
# 蔡幸娟 = 东方云雀
# 飞轮海 = Fahrenheit
# 黄建为 = Europa
# Huang
# 黄建为 = 油罗巴
# 黄建为 = 黄箭口香糖
# 墨明棋妙 = 墨村
# 逃跑计划 = escape
# plan
# 霹雳英雄 = Knight
# hero