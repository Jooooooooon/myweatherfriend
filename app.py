from flask import Flask, jsonify, request
app = Flask(__name__)

from slack import WebClient
client = WebClient(token='xoxb-1370016697107-1376065690948-A3RRW6FIiBRptuK3GDyLGtAB')


## API 역할을 하는 부분
@app.route('/slack', methods=['POST'])
def test_get():
    message = request.json['event']['blocks'][0]['elements'][0]['elements'][1]['text']
    channel = request.json['event']['channel']

    if '안녕' in message:
        client.chat_postMessage(channel=channel, text='나도 안녕!')
    else:
        client.chat_postMessage(channel=channel, text='뭐라고?')

    return jsonify({'result':'success'})

if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)