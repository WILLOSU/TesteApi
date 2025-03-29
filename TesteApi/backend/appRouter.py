from flask import Flask, jsonify, request
import pandas as pd

app = Flask(__name__)

# Caminho do CSV
csv_path = r"D:\Intuitive\d-teste\TesteApi\backend\data\Relatorio_cadop.csv"

# Carregar o CSV
df = pd.read_csv(csv_path, sep=None, engine="python", encoding="utf-8", on_bad_lines="skip")

@app.route('/buscar', methods=['GET'])
def buscar():
    # Recuperar o termo de busca enviado pela query string
    termo = request.args.get('termo', '').strip()

    if not termo:
        return jsonify(df.to_dict(orient="records"))  # Retorna todos os registros quando o termo está vazio
    
    # Filtrar os dados no DataFrame com base no termo de busca
    resultado = df[df.apply(lambda row: row.astype(str).str.contains(termo, case=False).any(), axis=1)]

    if resultado.empty:
        return jsonify({"mensagem": "Nenhum resultado encontrado para o termo informado."}), 404
    
    # Retornar os resultados como um JSON
    return jsonify(resultado.to_dict(orient="records"))

if __name__ == "__main__":
    app.run(debug=True)
