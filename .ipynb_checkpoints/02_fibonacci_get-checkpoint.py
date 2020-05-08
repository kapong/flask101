from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/', methods=['GET']) 
def calc_fibo(): 
    num = request.args.get("num", "0")
    try:
        num = int(num)
    except:
        return 'Error this is not a number', 400
    return 'Fib(%d) = %d! ' % (num, fibo(num))

@app.route('/json', methods=['GET']) 
def calc_fibo_json(): 
    num = request.args.get("num", "0")
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
