import zipfile, os
import pandas as pd
from pathlib import Path
from sqlalchemy import create_engine, inspect, MetaData, Table, Column, String, Integer, Float, Date

pasta_zip = Path(os.getcwd()).joinpath(Path('Data/Data.zip'))

# Tirando arquivos do zip
with zipfile.ZipFile(pasta_zip, 'r') as zip:
    zip.extractall()

caminho_escolas = 'Data/Escolas'
caminho_estudantes = 'Data/Perfil dos educandos'

arquivos_escolas_csv = [arquivo for arquivo in os.listdir(caminho_escolas) if arquivo.endswith('.csv')]
arquivos_estudantes_csv = [arquivo for arquivo in os.listdir(caminho_estudantes) if arquivo.endswith('.csv')]

colunas_datas_escolas = ['dt_criacao', 'doc_criacao', 'dom_criacao', 'dt_ini_conv', 'dt_ini_func', 'dt_autoriza', 'dt_extintao', 'database']
colunas_datas_estudantes = ['database']

# Definir o nome do arquivo do banco de dados SQLite
db_filename = 'test_analytics.db'

engine = create_engine(f'sqlite:///{db_filename}', echo=True)

metadata = MetaData()
metadata.reflect(bind=engine)

# Convertendo a coluna de data para o tipo datetime, assumindo que ela está no formato %d/%m/%Y
def _converter_data(colunas_contem_datas, df):
    for coluna in df.columns:
        if coluna.lower() in colunas_contem_datas:
            df[coluna] = pd.to_datetime(df[coluna], format='%d/%m/%Y', errors='coerce')

# Função para carregar dados em csv para o banco de dados
def carregar_dados_banco(arquivos_csv, caminho_pasta, colunas_contem_datas):
    for arquivo in arquivos_csv:
        nome_tabela = os.path.splitext(arquivo)[0]

        if not inspect(engine).has_table(nome_tabela):
            df = pd.read_csv(os.path.join(caminho_pasta, arquivo), encoding='latin1', sep=';')

            _converter_data(colunas_contem_datas, df)

            tipos_de_dados = {coluna: Date if pd.api.types.is_datetime64_any_dtype(df[coluna]) else
                                      Integer if pd.api.types.is_integer_dtype(df[coluna]) else
                                      Float if pd.api.types.is_float_dtype(df[coluna]) else
                                      String for coluna in df.columns}

            tabela = Table(nome_tabela, metadata, *[Column(coluna, tipo_dado) for coluna, tipo_dado in tipos_de_dados.items()])

            tabela.create(bind=engine)

            df.to_sql(nome_tabela, engine, if_exists='replace', index=False)

    metadata.create_all(engine)

    print(f"Dados da pasta {caminho_pasta} carregados com sucesso no banco de dados SQLite.")

if __name__ == '__main__':
    carregar_dados_banco(arquivos_escolas_csv, caminho_escolas, colunas_datas_escolas)
    carregar_dados_banco(arquivos_estudantes_csv, caminho_estudantes, colunas_datas_estudantes)
