# 🌦️ Weather ETL Pipeline on AWS with Airflow

<p align="center">
  <img src="https://img.shields.io/badge/Python-ETL-blue?style=for-the-badge&logo=python" />
  <img src="https://img.shields.io/badge/Apache%20Airflow-Orchestration-red?style=for-the-badge&logo=apacheairflow" />
  <img src="https://img.shields.io/badge/AWS-EC2%20%7C%20S3-orange?style=for-the-badge&logo=amazonaws" />
  <img src="https://img.shields.io/badge/OpenWeatherMap-API-yellow?style=for-the-badge&logo=icloud" />
  <img src="https://img.shields.io/badge/VS%20Code-Remote%20SSH-007ACC?style=for-the-badge&logo=visualstudiocode" />
</p>

<p align="center">
  <b>A data engineering project that builds and orchestrates an end-to-end ETL pipeline using Python, Apache Airflow, AWS EC2, and AWS S3.</b>
</p>

---

## 📌 Overview

This project demonstrates how to build a small **production-style ETL pipeline** that:

- **Extracts** weather data from the **OpenWeatherMap API**
- **Transforms** raw JSON data into a structured tabular format
- **Loads** the processed data:
  - locally as a **CSV** file
  - remotely into an **AWS S3 bucket**
- **Runs on an AWS EC2 instance**
- **Uses Apache Airflow** to orchestrate the workflow as a DAG
- **Uses VS Code Remote SSH** to develop directly on the cloud server
- **Accesses the Airflow web UI** locally through SSH port forwarding

This project combines **Python scripting**, **workflow orchestration**, **cloud deployment**, and **remote development** into one complete mini-project.

---

## 🚀 Project Architecture

```text
OpenWeatherMap API
        │
        ▼
   Extract Task
        │
        ▼
 Transform Task
        │
        ▼
    Load Task
   ┌───────────────┬───────────────┐
   ▼               ▼               │
Local CSV      AWS S3 Bucket       │
                                Airflow DAG
                                     │
                                     ▼
                           Running on AWS EC2
                                     │
                                     ▼
                    VS Code Remote SSH + Airflow UI
```

---

## 🧰 Tech Stack
- Python
- Apache Airflow
- AWS EC2
- AWS S3
- OpenWeatherMap API
- Pandas
- Boto3
- VS Code Remote SSH

---

## ✨ Features
- Modular ETL pipeline design
- API-based data ingestion
- Airflow DAG scheduling and orchestration
- Remote cloud execution on EC2
- Local and cloud storage of processed data
- Airflow UI monitoring via localhost

--- 

## 📂 Repository Structure
```bash
weather-etl-pipeline/
│
├── dags/
│   └── weather_etl_dag.py
│
├── include/
│   └── weather_pipeline/
│       ├── __init__.py
│       ├── transform.py
│       └── load.py
│
├── data/
│   └── weather_data.csv
│
├── screenshots/
│   ├── project_structure(airflow UI).png
│   ├── uploaded_csv_file.png
│   └── s3_upload.png
│
├── requirements.txt
├── .gitignore
├── LICENSE
└── README.md

```

---
## 🔄 ETL Workflow
1. Extract

The pipeline sends a request to the OpenWeatherMap API and retrieves weather data in JSON format.

Example extracted information:

- city name
- temperature
- humidity
- pressure
- weather description
- timestamp
2. Transform

The raw response is cleaned and transformed into a structured dataset.

Typical transformations include:

- selecting relevant fields
- renaming columns
- converting data types
- formatting timestamps
- creating a CSV-ready table
3. Load

The final processed data is stored in two destinations:

- Locally on the EC2 instance as a .csv file
- AWS S3 as a cloud-stored CSV object

---
## ⚙️ Airflow Orchestration

This project uses Apache Airflow to define the ETL process as a DAG.

The DAG manages:

- task dependencies
- workflow execution
- retries and scheduling
- monitoring through the Airflow UI

DAG stages:

- API check / extraction
- transformation
- local save
- S3 upload
---

## ☁️ AWS Deployment

The pipeline runs on an AWS EC2 instance, making the project closer to a real cloud workflow.

EC2 is used for:
- hosting the Airflow environment
- executing the ETL pipeline
- storing the generated local CSV output
- enabling remote development with SSH
S3 is used for:
- storing the transformed CSV output
- simulating a cloud-based data lake / storage layer

--- 

## 💻 Remote Development with VS Code SSH

To work directly on the EC2 instance, the project uses VS Code Remote SSH.

This allows:

- editing files directly on the server
- running Airflow remotely
- managing the project without manually copying files back and forth

---

## 🌐 Accessing the Airflow UI

Since Airflow runs on the EC2 instance, its web interface can be accessed locally using SSH port forwarding.

Example: 
```bash
ssh -i your-key.pem -L 8080:localhost:8080 ec2-user@your-ec2-public-ip
```

Then open in your browser:
```bash
http://localhost:8080
```

This makes it possible to view and manage DAGs from your own machine while Airflow is running remotely.
--- 

## 🛠️ Installation & Setup
1. Clone the repository
