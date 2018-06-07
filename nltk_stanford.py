path_to_jar = '/Users/wang/dev/stanford-corenlp-full-2018-02-27/stanford-corenlp-3.9.1.jar'
path_to_model_jar = '/Users/wang/dev/stanford-corenlp-full-2018-02-27/stanford-corenlp-3.9.1-models.jar'
model_path = '/Users/wang/dev/stanford-chinese-corenlp-2018-02-27-models/edu/stanford/nlp/models/lexparser/chinesePCFG.ser.gz'

#s = u"你 有个 优惠券 快要 过期 了"
s = u"王其龙 是 一个 优秀 的 程序员，他 喜欢 江曦"

# 依存分析
from nltk.parse.stanford import StanfordDependencyParser
parser = StanfordDependencyParser(path_to_jar, path_to_model_jar, model_path)
result = list(parser.parse(s.split()))
for row in result[0].triples():
    print(row)

# 句法结构分析
from nltk.parse.stanford import StanfordParser
parser = StanfordParser(path_to_jar, path_to_model_jar, model_path)
result = list(parser.parse(s.split()))
for r in result:
    print (r)
    print (r.draw())