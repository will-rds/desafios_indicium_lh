from datetime import datetime, timedelta
from textwrap import dedent
from airflow import DAG
import sqlite3
from airflow.utils.dates import days_ago
from airflow.operators.python import PythonOperator
import pandas as pd

# These args will get passed on to each operator
# You can override them on a per-task basis during operator initialization
default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'email': ['my_email'],
    'email_on_failure': True,
    'email_on_retry': True,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

with DAG(
    'NorthwindELT',
    default_args=default_args,
    description='A ELT dag for the Northwind ECommerceData',
    schedule_interval=timedelta(days=1),
    start_date=datetime(2021, 1, 1),
    catchup=False,
    tags=['example'],
) as dag:
    dag.doc_md = """
        ELT Diária do banco de dados de ecommerce Northwind,
        começando em 2022-02-07. 
    """ 
    df_file = ('/seu/caminho/completo/desafios_indicium_lh_airflow/data/Northwind_small.sqlite')
    output_csv_file = ('/seu/caminho/completo/desafios_indicium_lh_airflow/data/output_orders.csv')
    
    # essa task conecta-se e extrai a tabela order do banco de dados e salva em um arquivo csv

    def extract_order():
        conn = sqlite3.connect(df_file)
        query = f" SELECT * FROM 'Order'"
        df = pd.read_sql_query(query, conn) 
        conn.close()
        df.to_csv(output_csv_file, index=False)
    
    # Essa tesk faz a uniao das tabelas order (arquivo csv) e orderdetail, para fazer uma consulta e gerar resultado

    def join_tables():
        conn = sqlite3.connect(df_file)
        query = "SELECT * FROM OrderDetail"
        order_detail_df = pd.read_sql_query(query, conn)
        csv_df = pd.read_csv(output_csv_file)
        marged = pd.merge(left=csv_df, right=order_detail_df, how='inner', left_on='Id', right_on='OrderId')
        
        rio_de_janeiro_quantity = marged[marged['ShipCity'] =='Rio de Janeiro']['Quantity'].sum()
                    
        conn.close()
        return rio_de_janeiro_quantity
    
    def export_count_to_file(rio_de_janeiro_quantity, ti):
        with open('/seu/caminho/completo/desafios_indicium_lh_airflow/data/count.txt', 'w') as file:
            file.write(str(rio_de_janeiro_quantity))




    extract_order_db = PythonOperator(
        task_id='taks1',
        python_callable=extract_order,
        provide_context=True,
        dag=dag,
    )
      
    join_task = PythonOperator(
        task_id='task2',
        python_callable=join_tables,
        dag=dag
    )
    output = PythonOperator(
        task_id='export_final_output',
        python_callable=export_count_to_file,
        op_args=[join_tables()],
        provide_context=True,
        dag=dag,
    )

    extract_order_db >> join_task >> output



    extract_order.doc_md = dedent(
        """\
    #### Task Documentation

    Essa task extrai os dados do banco de dados postgres, parte de baixo do step 1 da imagem:

    ![img](https://user-images.githubusercontent.com/49417424/105993225-e2aefb00-6084-11eb-96af-3ec3716b151a.png)

    """

    )


    
