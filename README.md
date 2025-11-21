# Simple Data Engineering Project

## 📄 Abstract

This project implements a complete **Data Engineering Pipeline** that covers all essential stages of modern data workflows: data ingestion, cleaning, transformation, analysis, visualization, and storage. The system retrieves data from an external **API**, converts it into a structured **DataFrame**, removes missing values, and applies multiple data-processing techniques such as summary statistics and grouped aggregations.  
The processed results are stored inside a **PostgreSQL database** and can also be exported to CSV files. The application includes structured **logging**, robust **exception handling**, a fully modularized architecture, and a **Docker Compose** environment that ensures reproducibility and portability.  
Finally, the project produces visualizations that answer five analytical questions, demonstrating how raw API data can be transformed into actionable insights.

## 📘 Introduction

Building end-to-end Data Engineering systems is a fundamental skill for modern data-driven applications. Such systems automate the process of collecting, processing, and analyzing data, enabling organizations to extract meaningful insights efficiently and reliably.  
As part of the Data Engineering training sessions, the objective of this project was to design and implement a Python-based application that simulates a real-world data pipeline—from ingestion to visualization and storage.

The developed application:
- connects to an external **API** to fetch data
- converts the response into a **pandas DataFrame**
- cleans the data by removing **NULL values**
- applies at least two data-processing methods (summary statistics, groupby, aggregations)
- generates **visualizations** to answer five analytical questions
- stores the processed data in a **PostgreSQL database** running inside a Docker container
- includes structured **logging**, exception handling, and CSV export functionality

This project represents a complete mini data engineering workflow following real industry practices: modular code structure, containerization, database integration, reproducible environments, and clear visualization of insights.

## 🚀 Features

- Modular Python Architecture
- Dockerized Python + PostgreSQL setup
- Logging & Exception Handling
- Save-to-File (CSV) functionality
- PostgreSQL integration with Docker volume for persistent data

## 🗂 Project Structure

```
project/
│── Dockerfile
│── docker-compose.yml
│── requirements.txt
│── main.py
│── db_module.py
│── fetch_module.py
│── prepare_module.py
│── features_module.py
│── save_module.py
│── plot_module.py
```

## 🛠 Installation & Setup

### 1️⃣ Clone the repository
```
git clone your-repo-url
cd project
```

### 2️⃣ Run with Docker Compose
```
docker-compose up --build
```

### 3️⃣ App execution
- The Python app starts automatically and connects to the database
- Creates the table if it doesn't exist
- Processes the data
- Stores it in PostgreSQL and CSV

## 🧪 Run Without Docker (Optional)

```
pip install -r requirements.txt
python main.py
```

## 🌐 Environment Variables

Set in `docker-compose.yml`:
```
DB_HOST=db
DB_NAME=coffee_db
DB_USER=user
DB_PASS=password
```

## 🧰 Technologies Used

| Component | Technology |
|----------|------------|
| Programming Language | Python 3.10 |
| Database | PostgreSQL 15 (Dockerized) |
| Containerization | Docker & Docker Compose |
| Logging | Python logging module |
| Data Saving | CSV exports |
| Dependencies | pandas, psycopg2 |

## 📈 Future Enhancements

- SQLAlchemy ORM & Alembic migrations
- REST API with FastAPI
- Kafka real-time streaming
- Airflow ETL pipelines
- Monitoring dashboards with Grafana / Prometheus
