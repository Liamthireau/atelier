import logging

import pytz
import json
import requests
import pandas as pd
from airflow import DAG
from datetime import datetime
from sqlalchemy import create_engine
from vacances_scolaires_france  import SchoolHolidayDates
from airflow.operators.python_operator import PythonOperator
from airflow.providers.postgres.hooks.postgres import PostgresHook


default_args = {
    'owner': 'airflow',
    'start_date': datetime(2025, 3, 18)
}

dag = DAG(
    'extract_data_dag',
    default_args=default_args,
    description="DAG qui permet de collecter les données de l'API Enedis afin d'alimenter le DWH",
    schedule_interval='* * * * *'
)


# Fonction principale qui sera exécutée par le PythonOperator
def extract_load_school_holidays():
    # Récupération des données de vacances scolaires
    logging.info("-- Extraction des données des vacances scolaires --")
    holiday_dates = SchoolHolidayDates()
    holiday_dates_data = holiday_dates.holidays_for_year(2025)

    # Création du DataFrame
    holidayDf = pd.DataFrame(holiday_dates_data).T

    # Connexion à PostgreSQL
    logging.info("-- Connexion à la base de données PostgreSQL --")
    pg_hook = PostgresHook(postgres_conn_id="POSTGRES_DEFAULT")
    conn = pg_hook.get_conn()
    cursor = conn.cursor()






