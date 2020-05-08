from flask import Flask, request, jsonify

app = Flask(__name__) 

@app.route('/', methods=['POST']) 
def calc_fibo_json():
    num = request.form['num']
    try:
        num = int(num)
    except:
        return jsonify({
            "error": "Not a number",
        }), 400
    return jsonify({
        "input": num,
        "output": fibo(num)
    })

def fibo(num):
    if num <= 1:
        return 0
    elif num == 2:
        return 1
    else:
        return fibo(num - 1) + fibo(num - 2)

if __name__ == '__main__':
    app.run()
