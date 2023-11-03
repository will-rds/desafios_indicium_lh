
# Desafio Airflow Indicium

Esse desafio é parte do programa da trilha "Orquestração com Airflow" e é pré-requisito para obtenção da competência de nível Trainee em Airflow.

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

#3. Limpando Dags de Exemplo

Para deixar a visualizacao mais limpa e criar a nossa dag basta acessar o arquivo airflow.cfg, trocando:
```
load_examples = True
``` 
para
```
load_examples = True
``` 

Depois disso, precisamos configurar o ambiente para dizer onde os arquivos de config do airflow irao ficar. Na janela do seu terminal
```
export AIRFLOW_HOME=seu/caminho/completo/airflow-data
```

# 4. Dags

Voce ira encontrar uma repositorio com as dags, copie esta pasta para dentro da pasta ```airflow-data```

# 5. Validando projeto


## Instalação

Instale my-project com npm

```bash
  npm install my-project
  cd my-project
```
    
## Licença

[MIT](https://choosealicense.com/licenses/mit/)

