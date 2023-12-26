from koalanlp.Util import initialize, finalize
from koalanlp.proc import Tagger
from koalanlp import API

from koalanlp.jvm import JVM
JVM.start_jvm("-Xmx4g -Dfile.encoding=utf-8", callback_server_parameters={"port": 25335})
initialize(java_options="-Xmx4g -Dfile.encoding=utf-8", EUNJEON="2.1.6")

print("**** finish initialize ****")

tagger = Tagger(API.EUNJEON)
tagged = tagger.tag("안녕하세요. 눈이 오는 설날 아침입니다.")
print(tagged)
exit(1)
while True:
    text = input("분석할 문장을 입력하세요>> ").strip()
    print(text)

    if len(text) == 0:
        break

    sentences = tagger.tagSentence(text)
    print(sentences)
    exit(1)
    print("===== Sentence =====")
    for i, sent in enumerate(sentences):
        print("===== Sentence #$i =====")
        print(sent.surfaceString())

        print("# Analysis Result")
        # print(sent.singleLineString())

        for word in sent:
            print("Word [%s] %s = " % (word.getId(), word.getSurface()), end='')

            for morph in word:
                print("%s/%s " % (morph.getSurface(), morph.getTag()), end='')

            print()

finalize()