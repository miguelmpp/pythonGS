import requests
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
import numpy as np

# Coleta de Dados usando API real
API_URL = 'https://services3.arcgis.com/pI4ewELlDKS2OpCN/arcgis/rest/services/SDG_6_3_2_Proportion_of_bodies_of_water_with_good_ambient_water_quality/FeatureServer/0/query?where=1%3D1&outFields=*&geometry=-138.297%2C31.345%2C-100.592%2C43.510&geometryType=esriGeometryEnvelope&inSR=4326&spatialRel=esriSpatialRelIntersects&outSR=4326&f=json&resultRecordCount=8'

def fetch_data(api_url):
    try:
        response = requests.get(api_url, timeout=10)
        response.raise_for_status()
        data = response.json()
        
        features = data.get('features', [])
        processed_data = [
            {
                'location': feature['attributes'].get('ROMNAM', 'N/A'),
                'water_quality': feature['attributes'].get('obsValue', 'N/A'),
                'date': feature['attributes'].get('DATA_LAST_UPDATE', 'N/A')
            }
            for feature in features
        ]
        return processed_data
    except requests.exceptions.RequestException as e:
        print(f"Error fetching data: {e}")
        return []

data = fetch_data(API_URL)

# Transformar dados em DataFrame do pandas
df = pd.DataFrame(data)
print("Dados coletados:")
print(df.head())

# Ajustar formato da data
df['date'] = pd.to_datetime(df['date'], errors='coerce')
df['water_quality'] = pd.to_numeric(df['water_quality'], errors='coerce')

# Simular diferentes datas para visualização
df['date'] = pd.date_range(start='2023-01-01', periods=len(df), freq='D')

print("Dados após conversão de tipos:")
print(df.head())

# Verificar distribuição das datas e qualidades da água
print("Datas únicas:", df['date'].unique())
print("Qualidades da água únicas:", df['water_quality'].unique())

# Análise de Dados
def analyze_data(df):
    df['average_quality'] = df['water_quality'].mean()
    return df

df_analyzed = analyze_data(df)

# Função adicional para manipulação de listas e strings
def process_locations(locations):
    processed = [loc.strip().upper() for loc in locations if isinstance(loc, str)]
    return processed

locations = process_locations(df['location'].tolist())
print("Processed Locations:", locations)

# Manipulação de Arquivos: Salvar e ler dados
def save_to_csv(df, filename):
    df.to_csv(filename, index=False)
    print(f"Dados salvos em {filename}")

def read_from_csv(filename):
    df = pd.read_csv(filename)
    print(f"Dados lidos de {filename}")
    return df

save_to_csv(df_analyzed, 'ocean_data.csv')
df_from_file = read_from_csv('ocean_data.csv')

# Visualização de Dados
def plot_data(df):
    plt.figure(figsize=(10, 5))
    plt.plot(df['date'], df['water_quality'], label='Water Quality')
    plt.xlabel('Date')
    plt.ylabel('Water Quality')
    plt.title('Water Quality Over Time')
    plt.legend()
    plt.show()

plot_data(df_analyzed)

# Machine Learning - Exemplo simples de regressão linear
def machine_learning_example(df):
    df = df.dropna(subset=['date', 'water_quality'])
    print("Dados após remoção de valores nulos:")
    print(df.head())
    
    df['timestamp'] = df['date'].astype('int64') / 10**9
    X = df[['timestamp']]
    y = df['water_quality']
    model = LinearRegression()
    model.fit(X, y)
    df['predicted_quality'] = model.predict(X)
    return df, model

df_ml, model = machine_learning_example(df_analyzed)

# Visualizar predições
def plot_predictions(df):
    plt.figure(figsize=(10, 5))
    plt.plot(df['date'], df['water_quality'], label='Actual Water Quality')
    plt.plot(df['date'], df['predicted_quality'], label='Predicted Water Quality')
    plt.xlabel('Date')
    plt.ylabel('Water Quality')
    plt.title('Actual vs Predicted Water Quality')
    plt.legend()
    plt.show()

plot_predictions(df_ml)

# Segurança e Privacidade
def secure_data(df):
    # Exemplo simples: remover dados sensíveis
    df.drop(columns=['sensitive_column'], inplace=True, errors='ignore')
    return df

df_secure = secure_data(df_ml)

# Educação e Engajamento
def educational_content():
    print("Este script coleta dados ambientais de uma API pública, realiza análises simples e aplica técnicas básicas de machine learning.")
    print("É importante entender cada parte do código para apreciar como os dados são coletados, analisados e visualizados.")

educational_content()
