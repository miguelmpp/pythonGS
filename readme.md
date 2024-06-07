# 🌊 Computational Thinking With Python - Projeto de Monitoramento da Qualidade da Água dos Oceanos

## 👥 Alunos
- **Matheus Farias de Lima** - RM554254
- **Miguel Mauricio Parrado Patarroyo** – RM554007

## 📜 Descrição do Projeto
O nosso trabalho de Python é um protótipo para o "Ocean Health Tracker", uma ferramenta avançada projetada para integrar e analisar dados de múltiplas fontes, proporcionando insights críticos para a tomada de decisões estratégicas na conservação dos oceanos. Utilizando tecnologias avançadas de coleta de dados, análise preditiva e visualização, a plataforma visa monitorar a saúde dos oceanos em tempo real, identificar áreas de risco e promover ações de conservação informadas por dados.

> A outra parte do trabalho, que inclui o desenvolvimento Front-end e Web Development, pode ser encontrada em outro repositório: [https://github.com/miguelmpp/GSFrontWebBranch](https://github.com/miguelmpp/GSFrontWebBranch).

## 🛠️ Instruções de Uso
1. **Clonar o repositório**:
   ```sh
   git clone <URL do repositório>
   cd gs_python
   ```

2. **Instalar as dependências**:
   ```sh
   pip install -r requirements.txt
   ```

3. **Executar o script principal**:
   ```sh
   python main.py
   ```

4. **Gerar e visualizar os gráficos**:
   - Os gráficos serão gerados automaticamente e exibidos na tela ao executar o script `main.py`.

## 📋 Requisitos
- Python 3.6 ou superior
- Bibliotecas Python:
  - `requests`
  - `pandas`
  - `matplotlib`
  - `scikit-learn`
  - `numpy`

## 📦 Dependências
As dependências podem ser instaladas utilizando o arquivo `requirements.txt` com o seguinte comando:
```sh
pip install -r requirements.txt
```

## 🗂️ Estrutura do Projeto
- `main.py`: Script principal que contém o código do projeto.
- `ocean_data.csv`: Arquivo CSV gerado com os dados processados.
- `readme.md`: Documentação do projeto.

## 🚀 Funcionalidades
1. **Coleta de Dados**:
   - Utilização da biblioteca `requests` para coletar dados de uma API pública.
   - Tratamento de exceções para lidar com erros na coleta de dados.

2. **Processamento de Dados**:
   - Conversão de tipos de dados utilizando `pandas`.
   - Manipulação de listas e strings.
   - Análise e cálculo de métricas de qualidade da água.

3. **Visualização de Dados**:
   - Geração de gráficos utilizando `matplotlib` para visualizar a qualidade da água ao longo do tempo.

4. **Machine Learning**:
   - Aplicação de um modelo de regressão linear utilizando `scikit-learn` para prever a qualidade da água.

5. **Manipulação de Arquivos**:
   - Leitura e escrita de dados em arquivos CSV.

6. **Tratamento de Exceções**:
   - Implementação de tratamento de exceções para garantir robustez no sistema.

## 📚 Atendendo aos Requisitos

### 📖 Conhecimentos básicos em Python
O projeto demonstra conhecimentos básicos em Python através do uso de variáveis, tipos de dados e estruturas de controle. Exemplos incluem:
- **Variáveis e tipos de dados**: Uso de strings, inteiros, floats e datas.
- **Estruturas de controle**: Uso de `if`, `elif`, `else` e `for` loops para controle de fluxo e iteração de dados.

### 📜 Manipulação de Listas e Strings
A manipulação de listas e strings é exemplificada pela função `process_locations`, que processa uma lista de localizações:
```python
def process_locations(locations):
    processed = [loc.strip().upper() for loc in locations if isinstance(loc, str)]
    return processed
```

### 🔍 Conhecimento em Funções
O projeto utiliza diversas funções definidas pelos alunos, que incluem parâmetros e retornos de valores. Exemplos:
- `fetch_data(api_url)`: Coleta dados da API.
- `analyze_data(df)`: Analisa os dados coletados.
- `machine_learning_example(df)`: Aplica um modelo de machine learning aos dados.

### 📊 Noções de Estruturas de Dados
O projeto demonstra entendimento sobre estruturas de dados como listas, dicionários e DataFrames do `pandas`. Exemplos:
- **Listas**: Utilizadas para armazenar as localizações processadas.
- **Dicionários**: Utilizados para armazenar os dados coletados da API.
- **DataFrames**: Utilizados para manipulação e análise de dados.

### 🗃️ Manipulação de Arquivos
O projeto inclui a leitura e escrita de arquivos CSV para armazenamento e recuperação de dados:
```python
def save_to_csv(df, filename):
    df.to_csv(filename, index=False)
    print(f"Dados salvos em {filename}")

def read_from_csv(filename):
    df = pd.read_csv(filename)
    print(f"Dados lidos de {filename}")
    return df
```

### 🔐 Tratamento de Exceções
O tratamento de exceções é implementado para garantir que o sistema lide com erros de forma robusta:
```python
def fetch_data(api_url):
    try:
        response = requests.get(api_url, timeout=10)
        response.raise_for_status()
        data = response.json()
        return data
    except requests.exceptions.RequestException as e:
        print(f"Error fetching data: {e}")
        return []
```

## 🖥️ Detalhes do Código

### 📥 Coleta de Dados
```python
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
```

### 🔄 Processamento de Dados
```python
df = pd.DataFrame(data)
df['date'] = pd.to_datetime(df['date'], errors='coerce')
df['water_quality'] = pd.to_numeric(df['water_quality'], errors='coerce')
df['date'] = pd.date_range(start='2023-01-01', periods=len(df), freq='D')

def analyze_data(df):
    df['average_quality'] = df['water_quality'].mean()
    return df
```

### 📈 Visualização de Dados
```python
def plot_data(df):
    plt.figure(figsize=(10, 5))
    plt.plot(df['date'], df['water_quality'], label='Water Quality')
    plt.xlabel('Date')
    plt.ylabel('Water Quality')
    plt.title('Water Quality Over Time')
    plt.legend()
    plt.show()
```

### 🤖 Machine Learning
```python
def machine_learning_example(df):
    df = df.dropna(subset=['date', 'water_quality'])
    df['timestamp'] = df['date'].astype('int64') / 10**9
    X = df[['timestamp']]
    y = df['water_quality']
    model = LinearRegression()
    model.fit(X, y)
    df['predicted_quality'] = model.predict(X)
    return df, model

def plot_predictions(df):
    plt.figure(figsize=(10, 5))
    plt.plot(df['date'], df['water_quality'], label='Actual Water Quality')
    plt.plot(df['date'], df['predicted_quality'], label='Predicted Water Quality')
    plt.xlabel('Date')
    plt.ylabel('Water Quality')
    plt.title('Actual vs Predicted Water Quality')
    plt.legend()
    plt.show()
```

### 📂 Manipulação de Arquivos
```python
def save_to_csv(df, filename):
    df.to_csv(filename, index=False)
    print(f"Dados salvos em {filename}")

def read_from_csv(filename):
    df = pd.read_csv(filename)
    print(f"Dados lidos de {filename}")
    return df

save_to_csv(df_analyzed, 'ocean_data.csv')
df_from_file = read_from_csv('ocean_data.csv')
```

### 🔒 Segurança e Privacidade
```python
def secure_data(df):
    df.drop(columns=['sensitive_column'], inplace=True, errors='ignore')
    return df
```

### 📚 Educação e Engajamento
```python
def educational_content():
    print("Este script coleta dados ambientais de uma API pública, realiza análises simples e aplica técnicas básicas de machine learning.")
    print("É importante entender cada parte do código para apreciar como os dados são coletados, analisados e visualizados.")

educational_content()
```