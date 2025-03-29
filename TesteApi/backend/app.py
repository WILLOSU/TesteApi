from flask import Flask
import pandas as pd

app = Flask(__name__)

# Caminho do CSV no seu diretório
csv_path = r"D:\Intuitive\d-teste\TesteApi\backend\data\Relatorio_cadop.csv"

# Tentando carregar o CSV com diferentes estratégias para evitar erros
try:
    # Tenta detectar automaticamente o delimitador
    df = pd.read_csv(csv_path, sep=None, engine="python", encoding="utf-8", on_bad_lines="skip")
except UnicodeDecodeError:
    # Se houver erro de encoding, tenta com outro encoding
    df = pd.read_csv(csv_path, sep=None, engine="python", encoding="latin1", on_bad_lines="skip")

# Exibir as primeiras linhas no terminal para verificar
print(df.head())

if __name__ == "__main__":
    app.run(debug=True)

