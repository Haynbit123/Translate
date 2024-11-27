from flask import Flask, request, jsonify
from cryptography.fernet import Fernet

app = Flask(__name__)

# Generate a key for encryption/decryption (save this key securely!)
key = Fernet.generate_key()
cipher_suite = Fernet(key)

@app.route('/encrypt', methods=['POST'])
def encrypt():
    data = request.json.get('text', '')
    encrypted_text = cipher_suite.encrypt(data.encode()).decode()
    return jsonify({'encrypted': encrypted_text})

@app.route('/decrypt', methods=['POST'])
def decrypt():
    data = request.json.get('text', '')
    decrypted_text = cipher_suite.decrypt(data.encode()).decode()
    return jsonify({'decrypted': decrypted_text})

if __name__ == '__main__':
    app.run(debug=True)
