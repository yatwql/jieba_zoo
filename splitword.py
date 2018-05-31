# -*- coding:utf-8 -*-
import sys
import os
import jieba #导入结巴分词库
import jieba.analyse

#设置utf-8输出环境
#reload(sys)
#sys.setdefaultencoding('utf-8')
#结巴分词--全模式
jieba.load_userdict('/Users/wang/work/jieba/userdict.txt')
sent='天善智能是一个专注于商业智能BI、数据分析、数据挖掘和大数据技术领域的技术社区 www.hellobi.com 。内容从最初的商业智能 BI 领域也扩充到了数据分析、数据挖掘和大数据相关 的技术领域，包括 R、Python、SPSS、Hadoop、Spark、Hive、Kylin等，成为一个专注于数据领域的垂直社区。天善智能致力于构建一个基于数据领域的生态圈，通过社区链接一切 与数据相关的资源:例如数据本身、人、数据方案供应商和企业，与大家一起共同努力推动大数据、商业智能BI在国内的普及和发展。'
#wordlist=jieba.cut(sent,cut_all=True)
wordlist=jieba.cut(sent,cut_all=False)
#wordlist=jieba.cut_for_search(sent)
print("|".join(wordlist))
print("----------------")
keywords = jieba.analyse.extract_tags(sent, topK=20, withWeight=True, allowPOS=())
# 访问提取结果
for item in keywords:
    # 分别为关键词和相应的权重
    print (item[0], item[1])
print("----------------")
# 同样是四个参数，但allowPOS默认为('ns', 'n', 'vn', 'v')
# 即仅提取地名、名词、动名词、动词
keywords = jieba.analyse.textrank(sent, topK=20, withWeight=True, allowPOS=('ns', 'n', 'vn', 'v'))
# 访问提取结果
for item in keywords:
    # 分别为关键词和相应的权重
    print (item[0], item[1])
