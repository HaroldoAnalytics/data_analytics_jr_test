Desafio - Analista de dados júnior

OBS: devido ao tamanho da base sql tratada e do Jupyter notebook serem muito grandes para o github, ou seja ultrapassar os 100 mb permitidos pelo git, os arquivos foram salvos em um drive e seram compartilhados atraves do link,

link do Jupyter notebook https://drive.google.com/file/d/1zdvsM2RIQ6N_bdLMuSN2KAUe0SJYfhoC/view?usp=sharing

link da base SQL https://drive.google.com/file/d/1F0epmV9d1VOAJQANYA396V1nDC1oU2k1/view?usp=sharing

Neste desafio, tivemos 5 desafios que consistiram em:

Utilizar o Python para conectar aos nossos arquivos CSV e, em seguida, transformá-los em SQLite. Para isso, utilizamos as bibliotecas zipfile e os.
O zipfile nos permite acessar arquivos zipados, e o os nos fornece o caminho dinâmico. Assim, iteramos sobre os arquivos CSV, criando tabelas no banco de dados caso não existam, e carregamos dados do CSV para o SQLite. Realizamos o código de forma que respeitasse a tipagem dos dados presentes nos arquivos e importasse de maneira efetiva as colunas com tipagem data. Além disso, o código é protegido por um bloco if __name__ == '__main__': para garantir que o script seja executado apenas se for chamado diretamente, não se for importado como um módulo.

Após a importação, partimos para o passo 2.

Utilizar SQL
Para realizar o tratamento e junção das tabelas, utilizamos o DB Browser (SQLite), onde usamos códigos para realizar os seguintes pré-tratamentos:

Reordenar colunas.
Alterar valores usando UPDATE + SET + WHERE, especificando qual valor desejamos alterar.
Alterar nomes de colunas.
CREATE TABLE para criar a tabela escolas_alunos solicitada pelo tópico 2, usando INNER JOIN, ou seja, trazendo os elementos presentes em ambas as tabelas e formando uma única tabela.
Além disso, foram utilizados os dicionários presentes no banco de dados para realizar conferências e alguns tratamentos adicionais, além dos realizados nos tópicos anteriores, visando trazer maior veracidade para os dados.

OBS: Seria interessante não realizar a junção em uma única tabela, e sim realizar a normalização dos dados, tendo assim tabelas dimensões e fatos, deixando a base mais performática.

Os passos 3 e 4 foram realizados simultaneamente, onde realizamos uma análise exploratória, retirando valores nulos, dados duplicados, entre outros processos de ETL. Durante a análise, chegamos a alguns insights relevantes, tais como:

Proporção de alunos, oferecendo uma visão mais detalhada da distribuição demográfica dos alunos em termos de idade, sexo e raça. Isso pode ser crucial para entender quem são os principais consumidores, permitindo à empresa personalizar suas estratégias de marketing para atender melhor às preferências e características específicas de diferentes grupos, algo extremamente importante nos dias de hoje.

Densidade de perfis sobre as escolas, analisando como a composição demográfica dos alunos varia entre as diferentes escolas. Essa informação é crucial para entender se há diferenças significativas nas características dos alunos em diferentes contextos escolares.

Distribuição de alunos por escola, sendo este o ponto mais importante. Aqui, identificamos nossos top 3 outliers, o que nos permite saber quais escolas já estão consolidadas em nossa carteira de clientes. Além disso, isso influencia decisões sobre alocação de recursos, investimentos e desenvolvimento de estratégias específicas para outras escolas.

Modalidade, vinculada aos fatos anteriores. A análise fornece uma visão clara das modalidades de ensino mais comuns, permitindo à empresa identificar as tendências educacionais predominantes. Isso é crucial para alinhar os serviços educacionais oferecidos com as demandas do mercado.

Todas as análises feitas já trouxeram consigo seu storytelling, contando visualmente o insight gerado por elas. Dessa forma, conseguimos concentrar as informações em um único lugar, facilitando para o sênior que irá corrigir e verificar a veracidade do insight.

Diante mão, gostaria de agradecer à USE e toda a sua equipe pela oportunidade de vir a ingressar no quadro de colaboradores e de participar de um desafio tão enriquecedor.
