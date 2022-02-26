from os import system
from flask import Flask

app = Flask(__name__)

@app.errorhandler(404)
def page_not_found(error):
	return "<h1>404 Not Found</h1>"

@app.route("/close_kakaotalk")
def close_kakaotalk():
    kakaotalk_win_count = 0

    while 1:
        i = system("taskkill /im KakaoTalk.exe")
        if i == 0:
            kakaotalk_win_count += 1
        elif i == 128:
            break

    if kakaotalk_win_count == 0:
        return "<h1>The KaKaoTalk.exe was already off.</h1>"
    else:
        return f"<h1>Successfully off the KaKaoTalk.exe in {kakaotalk_win_count}time<h1>"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
