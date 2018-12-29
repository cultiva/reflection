from slackbot.bot import Bot

# プラグイン追加用に読み込み
# リファレンスはhttps://github.com/lins05/slackbot#create-plugins

from slackbot.bot import respond_to
from slackbot.bot import listen_to
import re

def main():
    bot = Bot()
    bot.run()

    # ここから追加プラグイン
    @respond_to('I love you')
    def love(message):
        message.reply('I love you too!')

if __name__ == "__main__":
    main()
