# Instron_to_SQL_to_Kintone
Repo for SQL, Python, and HTTP scripts. Querying data within the server (SQL), processing data (Python), and pushing data to Kintone (HTTP).

File information:
* BN_file.csv: BN data to use with parse.data.py
* SQL parse data.py: Python script to parse data from SQL_export.csv
* SQL_export.csv: Exported data to use with SQL parse data.py
* instron_SQL_query.sql: SQL script to query data from various tables and output as one table
* kintone_rest_api.http: API script to PUSH data to Kintone
* parse.data.py: Python script to parse data from BN_file.csv
* parse_json.js: JSON script to parse data from SQL server (to be used right before kintone_rest_api.http)
