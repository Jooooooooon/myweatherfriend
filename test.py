import requests
import schedule
import time
from pandas import json_normalize

slack_token = 'xoxb-1370016697107-1376065690948-A3RRW6FIiBRptuK3GDyLGtAB'

# 채널 이름
ChannelName = "slack-bot-test"

# 채널 조회 API 메소드: conversations.list
URL = 'https://slack.com/api/conversations.list'

# 파라미터
params = {
    'Content-Type': 'application/x-www-form-urlencoded',
    'token': slack_token
}

# API 호출
res = requests.get(URL, params=params)

channel_list = json_normalize(res.json()['channels'])
channel_id = list(channel_list.loc[channel_list['name'] == ChannelName, 'id'])[0]

# print(f"""
# 채널 이름: {ChannelName}
# 채널 id: {channel_id}
# """)

# 글 내용
Text = "슬랙 봇 테스트"

# 채널 내 문구 조회 API 메소드: conversations.list
URL = 'https://slack.com/api/conversations.history'

# 파라미터
params = {
    'Content-Type': 'application/x-www-form-urlencoded',
    'token': slack_token,
    'channel': channel_id
         }

# API 호출
res = requests.get(URL, params = params)

chat_data = json_normalize(res.json()['messages'])
chat_data['text'] = chat_data['text'].apply(lambda x: x.replace("\xa0"," "))
ts = chat_data.loc[chat_data['text'] == Text, 'ts'].to_list()[0]

# print(f"""
# 글 내용: {Text}
# ts: {ts}
# """)

def job():
print("I'm working...")
# Bot으로 등록할 댓글 메시지 문구
message = f"""
저 부르셨어요?
"""

# 파라미터
data = {'Content-Type': 'application/x-www-form-urlencoded',
        'token': slack_token,
        'channel': channel_id,
        'text': message,
        'reply_broadcast': 'True',
        'thread_ts': ts
        }

# 메시지 등록 API 메소드: chat.postMessage
URL = "https://slack.com/api/chat.postMessage"
res = requests.post(URL, data=data)

schedule.every(1).minute.do(job)
# schedule.every().hour.do(job)
# schedule.every().day.at("10:30").do(job)
# schedule.every(5).to(10).minutes.do(job)
# schedule.every().monday.do(job)
# schedule.every().wednesday.at("13:15").do(job)
# schedule.every().minute.at(":17").do(job)

while True:
    schedule.run_pending()
    time.sleep(1)