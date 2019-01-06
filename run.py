from slackbot.bot import Bot

# 以下、I love you プラグイン追加用に読み込み
# リファレンスはhttps://github.com/lins05/slackbot#create-plugins

from slackbot.bot import respond_to
from slackbot.bot import listen_to
import re


# 以下、振り返り文プラグイン追加用に読み込み
import os
from slackbot.utils import download_file, create_tmp_file

# sleepメソッド用
from time import sleep

# この部分がI love youプラグイン追加
@respond_to('I love you')
def love(message):
    message.reply('I love you too!')

# この部分が振り返り文プラグイン追加
@respond_to('今日の分')
def upload_content(message):
    sleep(1)
    message.reply('How was your day today?')
    sleep(1)
    message.send('それじゃあ、今日の振り返りを始めようか。')
    sleep(1)
    # message.channel.upload_content(slack_filename, content,
    #                                initial_comment='')
    message.send('これがculivaのライフパーパスだね。') #sendに切り替えられないか検討
    content=u"雄大な振れ幅を活かして、\n人類の可能性を拡げるコロンブス"
    message.channel.upload_content('content.txt', content)

    message.reply('じゃあ、1つ目の質問だ。雄大な振れ幅を出すためのアクションをとれたかい？')

@respond_to('2つ目')
def second_question(second_answer):
        second_answer.reply('オッケー、2つ目の質問だ。その振れ幅を何かに活かすことはできたかい？')

@respond_to('3つ目')
def third_question(third_answer):
        third_answer.reply('それでは、3つ目の質問だ。それは誰かの可能性を拡げるものかい？')

@respond_to('4つ目')
def fourth_question(fourth_answer):
        fourth_answer.reply('そうかい。では、最後の質問だ。コロンブスらしい人間力を持っていたかい？')


def main():
    bot = Bot()
    bot.run()

if __name__ == "__main__":
    main()
