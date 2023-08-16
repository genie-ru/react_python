from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/calculate', methods=['POST'])
def calculate():
    data = request.get_json()
    print(data)
    x = int(data['x'])
    y = int(data['y'])
    z = int(data['z'])
    result = x + y + z
    return jsonify({'result': result})

@app.route('/process_data', methods=['POST'])
def process_data():
    data = request.get_json()
    print(data)
    n = int(data['n'])
    m = int(data['m'])
    matrix = data['matrix']

    C = [[0] * m for _ in range(n)]  # Cを宣言して初期化
    V = [(1, 1)]
    C[1][1] = 2
    while V:
        x, y = V.pop()
        for p, q in ((-1, 0), (0, -1), (1, 0), (0, 1)):
            i, j = x, y
            while matrix[i + p][j + q] == '.':
                C[i][j] = max(C[i][j], 1)
                i, j = i + p, j + q
            if C[i][j] < 2:
                C[i][j] = 2
                V.append((i, j))

    result = sum(C[i][j] > 0 for i in range(n) for j in range(m))
    return jsonify({"result": result})


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)