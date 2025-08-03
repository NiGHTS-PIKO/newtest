import subprocess
from flask import Flask, request

app = Flask(__name__)

@app.route('/webhook', methods=['POST'])
def webhook():
    data = request.json
    if data and data.get('event') == 'push':
        print("✅ Push event received. Executing auto.sh...")
        result = subprocess.run(
            ["/bin/bash", "/home/nights/Desktop/newtest/auto.sh"],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        )
        print("stdout:", result.stdout)
        print("stderr:", result.stderr)
        return "Executed auto.sh", 200
    return "Ignored", 204

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080)
