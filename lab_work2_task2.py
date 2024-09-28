from datetime import datetime
from airflow import DAG
from airflow.providers.docker.operators.docker import DockerOperator
from airflow.sensors.filesystem import FileSensor
from docker.types import Mount

default_args = {
    'owner': 'IlyaSwallow',
    'start_date': datetime(2024, 9, 28),
}

dag = DAG(
    'dagestan_learning',
    default_args=default_args,
    schedule_interval=None,
)

load_data_train_model = DockerOperator(
    task_id='load_data_train_model',
    image='ilyaswallow/my-app:1.0',
    command='python /data/train_model.py',
    mounts=[Mount(source='/data', target='/data', type='bind')],
    docker_url="tcp://docker-proxy:2375",
    dag=dag,
)

load_data_train_model