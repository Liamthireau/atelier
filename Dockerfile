# Use the official Airflow image as the base image
FROM apache/airflow:2.7.2

# Install the required Python libraries
#RUN pip install apache-airflow-providers-postgres
RUN pip install vacances_scolaires_france holidays
 