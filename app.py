from flask import Flask, render_template, request

app = Flask(__name__)

def caesar_encrypt(text, shift):
    encrypted = []
    for char in text:
        if char.isalpha():
            shift_amount = 65 if char.isupper() else 97
            encrypted.append(chr((ord(char) + shift - shift_amount) % 26 + shift_amount))
        else:
            encrypted.append(char)
    return ''.join(encrypted)

def caesar_decrypt(text, shift):
    return caesar_encrypt(text, -shift)

@app.route('/', methods=['GET', 'POST'])
def index():
    result = ''
    if request.method == 'POST':
        text = request.form['text']
        shift = int(request.form['shift'])
        action = request.form['action']
        if action == 'encrypt':
            result = caesar_encrypt(text, shift)
        elif action == 'decrypt':
            result = caesar_decrypt(text, shift)
    return render_template('index.html', result=result)

if __name__ == '__main__':
    app.run(debug=True)

