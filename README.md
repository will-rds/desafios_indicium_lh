
# Desafio Airflow Indicium

Esse desafio é parte do programa da trilha "Orquestração com Airflow".

# Objetivos

1. Criar uma task que le os dados da tabala 'Order' do banco de dados disponivel em ```data/Northwind_small.sqlite```. Sendo que o banco e um sqlite, essa taks deve escrever um arquivo chamado "output_orders.csv".

2. Criar outra taks que le os dados da tabela 'OrderDetail' do mesmo banco, e fazer um ```join``` com o arquivo "output_orders.csv" exportado da task anterior. Essa task deve calcular qual a soma da quantidade vendida (Quantity) com destino (ShipCity) para o Rio de Janeiro.

3. Exportar essa contagem em arquivo "count.txt" que contenha somente esse valor em formato texto.

4. Criar uma ordenacao de execucao das tasks que a ultima taks precisa ser ```export_final_output```. 
   

# Instruções 

Siga as instruções abaixo para poder realizar o desafio corretamente.

>  As instruções utilizam comandos do Linux. Usuários do Windows deverão procurar comandos correspondentes.

# 1. Clone o repositório

O primeiro passo é clonar o repositório para um novo repositório no seu computador:

```
git clone https://github.com/will-rds/desafios_indicium_lh_airflow.git

cd desafios_indicium_lh_airflow
```
# 2. Instalar o Airflow

Voce pode usar o proprio site offial do Airflow.

Lembrando que o Airflow sera executado localmente, tenha ciencia que ira consumir recursos de seu computador.

Para instalar o Airflow primeiro iremos criar um ambiente virtual e depois rodar o script abaixo. O arquivo install.sh, tem as intrucoes, basta executar.

```
virtualenv venv -p python3
source venv/bin/activate
bash install.sh
```

Se tudo der certo em seu terminal ira aparecer a segunte mensage: 
```
standalone | 
standalone | Airflow is ready
standalone | Login with username: admin  password: ******
standalone | Airflow Standalone is for development purposes only. Do not use this in production!
standalone |
```

A senha do Airflow e gerara automaticamente, procure nos logs a senha correspondente.

Airflow iniciado basta abrir um navegador e acessar http://localhost:8080.

No console pressione ctrl+c para encerrar o processo do Airflow, depois disso, pegue o caminho completo de onde o projeto esta e digite no terminal:
```
export AIRFLOW_HOME=/seu/caminho/completo/desafios_indicium_lh_airflow/airflow-data

```
> Lembre-se de colocar o caminho correto

# 3. Arrumando caminho na DAG
Na pasta dags, voce vai encontrar um arquivo chamado elt_dag.py, vc precisa alterar 3 caminhos para melhor funcionalidade.
Mude as linhas: 34,35 e 61, abaixo as linhas correspondentes:

```
df_file = ('/seu/caminho/completo/desafios_indicium_lh_airflow/data/Northwind_small.sqlite')
output_csv_file = ('/seu/caminho/completo/desafios_indicium_lh_airflow/data/output_orders.csv')
with open('/seu/caminho/completo/desafios_indicium_lh_airflow/data/count.txt', 'w') as file:
 ```
Mude o caminho antes de desafios_indicium....


# 4. Limpando Dags de Exemplo

Para deixar a visualizacao mais limpa e criar a nossa dag basta acessar o arquivo airflow.cfg que fica dentro da pasta airflow-data, trocando:
```
load_examples = True
``` 
para
```
load_examples = True
``` 

Depois disso, precisamos configurar o ambiente para dizer onde os arquivos de config do airflow irao ficar. Na janela do seu terminal
```
export AIRFLOW_HOME=seu/caminho/completo/desafios_indicium_lh_airflow/airflow-data
```
Mude o caminho antes de desafios_indicium....

# 4. Dags

Voce ira encontrar uma repositorio com as dags, copie esta pasta para dentro da pasta ```airflow-data```

# 5. Validando projeto

Depois de executar todos os passos voce deve encontrar na pasta ```data``` dois arquivos, um chamado ```output_orders.csv``` e ```count.txt```.


[![LinkedIn](https://img.shields.io/badge/LinkedIn-%230077B5.svg?logo=linkedin&logoColor=white)](https://www.linkedin.com/in/willianrsantos/) 

    
## Licença

[MIT](https://choosealicense.com/licenses/mit/)

