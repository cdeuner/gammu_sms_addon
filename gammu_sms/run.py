from flask import Flask, request, jsonify
import subprocess
import datetime
import os
import threading

app = Flask(__name__)
LOG_FILE = "/config/addons/gammu_sms/log/sms.log"

def log_sms(number, message, status, error=None):
    now = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    with open(LOG_FILE, "a") as f:
        f.write(f"[{now}] To: {number} | Status: {status}\n")
        f.write(f"Message: {message}\n")
        if error:
            f.write(f"Error: {error}\n")
        f.write("-" * 50 + "\n")

def send_sms_to_numbers(numbers, message):
    os.makedirs("/config/addons/gammu_sms/log", exist_ok=True)
    for number in numbers:
        try:
            result = subprocess.run(
                ['gammu', 'sendsms', 'TEXT', number, '-text', message],
                capture_output=True,
                text=True,
                timeout=20
            )
            if result.returncode == 0:
                log_sms(number, message, "Success")
            else:
                err_msg = result.stderr.strip()
                log_sms(number, message, "Failed", err_msg)
        except subprocess.TimeoutExpired as e:
            err_msg = f"Timeout expired: {str(e)}"
            log_sms(number, message, "Timeout", err_msg)
        except Exception as e:
            err_msg = str(e)
            log_sms(number, message, "Exception", err_msg)

@app.route('/send_sms', methods=['POST'])
def send_sms():
    data = request.json
    numbers = data.get('numbers')
    message = data.get('message')

    if not numbers or not message:
        return jsonify({'error': 'Missing numbers or message'}), 400

    if not isinstance(numbers, list):
        return jsonify({'error': 'numbers must be a list'}), 400

    # Lancement de l'envoi en arrière-plan
    thread = threading.Thread(target=send_sms_to_numbers, args=(numbers, message))
    thread.start()

    # Réponse immédiate
    return jsonify({'status': 'sending', 'numbers': numbers, 'message': message}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5005)
