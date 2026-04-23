from datetime import datetime, timedelta
import json

from airflow import DAG
from airflow.providers.standard.operators.python import PythonOperator
from airflow.providers.http.sensors.http import HttpSensor
from airflow.providers.http.operators.http import HttpOperator

from include.weather_pipeline.transform import transform_weather_data
from include.weather_pipeline.load import save_weather_to_s3


default_args = {
    "owner": "airflow",
    "depends_on_past": False,
    "email_on_failure": False,
    "email_on_retry": False,
    "retries": 2,
    "retry_delay": timedelta(minutes=2),
}


def transform_task(ti=None, **kwargs):
    raw_data = ti.xcom_pull(task_ids="extract_weather_data")
    transformed = transform_weather_data(raw_data)
    ti.xcom_push(key="transformed_weather_data", value=transformed)


def load_task(city_name="portland", bucket_name="apiairflow", ti=None, **kwargs):
    transformed_data = ti.xcom_pull(
        task_ids="transform_weather_data",
        key="transformed_weather_data",
    )
    save_weather_to_s3(
        transformed_data=transformed_data,
        city_name=city_name,
        bucket_name=bucket_name,
    )


with DAG(
    dag_id="weather_etl_dag",
    default_args=default_args,
    description="Extract weather data from OpenWeather, transform it, and store it in S3",
    start_date=datetime(2025, 4, 20),
    schedule="@daily",
    catchup=False,
    tags=["weather", "etl", "api", "s3"],
) as dag:

    is_weather_api_ready = HttpSensor(
        task_id="is_weather_api_ready",
        http_conn_id="weathermap_api",
        endpoint="/data/2.5/weather?q=Portland&appid={{ var.value.openweather_api_key }}",
        method="GET",
    )

    extract_weather_data = HttpOperator(
        task_id="extract_weather_data",
        http_conn_id="weathermap_api",
        endpoint="/data/2.5/weather?q=Portland&appid={{ var.value.openweather_api_key }}",
        method="GET",
        response_filter=lambda response: json.loads(response.text),
        log_response=True,
    )

    transform_weather_data_task = PythonOperator(
        task_id="transform_weather_data",
        python_callable=transform_task,
    )

    load_weather_data_task = PythonOperator(
        task_id="load_weather_data",
        python_callable=load_task,
        op_kwargs={
            "city_name": "portland",
            "bucket_name": "apiairflow",
        },
    )

    is_weather_api_ready >> extract_weather_data >> transform_weather_data_task >> load_weather_data_task
