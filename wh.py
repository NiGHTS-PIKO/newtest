from flask import Flask, request

app = Flask(__name__)

@app.route('/webhook', methods=['POST'])
def webhook():
    data = request.json
    print("Webhook受信:", data)
    # 任意の処理をここに書く（例: shell実行, GPIO制御）
    return 'OK', 200

app.run(host='0.0.0.0', port=8080)