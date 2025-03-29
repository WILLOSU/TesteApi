from flask import Flask, request, jsonify
import pandas as pd
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Habilita o CORS para evitar problemas de requisição no frontend

# Caminho do CSV no seu diretório
csv_path = r"D:\Intuitive\d-teste\TesteApi\backend\data\Relatorio_cadop.csv"

# Carregando o CSV
try:
    df = pd.read_csv(csv_path, sep=None, engine="python", encoding="utf-8", on_bad_lines="skip")
except UnicodeDecodeError:
    df = pd.read_csv(csv_path, sep=None, engine="python", encoding="latin1", on_bad_lines="skip")

# Rota para buscar operadoras por nome
@app.route('/buscar', methods=['GET'])
def buscar_operadoras():
    termo = request.args.get('termo', '').lower()  # Obtém o termo da URL
    if not termo or len(termo) < 3:  
        return jsonify([])  # Retorna lista vazia se o termo for muito curto

    # Filtra os dados baseando-se no nome da operadora
    resultados = df[df['Nome_Fantasia'].str.lower().str.contains(termo, na=False)]

    # Retorna os resultados em formato JSON
    return jsonify(resultados[['Nome_Fantasia', 'CNPJ']].to_dict(orient='records'))

if __name__ == "__main__":
    app.run(debug=True)
