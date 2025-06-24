from flask import Flask, request, jsonify
import subprocess
import datetime
import os

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

@app.route('/send_sms', methods=['POST'])
def send_sms():
    data = request.json
    numbers = data.get('numbers')
    message = data.get('message')

    if not numbers or not message:
        return jsonify({'error': 'Missing numbers or message'}), 400

    if not isinstance(numbers, list):
        return jsonify({'error': 'numbers must be a list'}), 400

    os.makedirs("/config/addons/gammu_sms/log", exist_ok=True)
    success = []
    errors = []

    for number in numbers:
        try:
            result = subprocess.run(
                ['gammu', 'sendsms', 'TEXT', number, '-text', message],
                capture_output=True,
                text=True
            )
            if result.returncode == 0:
                success.append(number)
                log_sms(number, message, "Success")
            else:
                err_msg = result.stderr.strip()
                errors.append({'number': number, 'error': err_msg})
                log_sms(number, message, "Failed", err_msg)
        except Exception as e:
            err_msg = str(e)
            errors.append({'number': number, 'error': err_msg})
            log_sms(number, message, "Exception", err_msg)

    response = {
        'status': 'ok' if not errors else 'partial failure',
        'success': success,
        'errors': errors
    }

    return jsonify(response), 200 if not errors else 207

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5005)
