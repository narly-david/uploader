# uploader
Create a PostgresDB table from one or more CSV files.

Optionally analyze the data prior to exporting.

Built using Streamlit:
https://docs.streamlit.io/library/api-reference

# Installation
```
pip install virtualenv
sudo apt-get install virtualenv
cd /workspaces
virtualenv venv
source ./venv/bin/activate
pip install pandas
pip install streamlit
pip install streamlit-pandas-profiling
```

# Startup
```
source /workspaces/venv/bin/activate
```

# Run
```
streamlit run app.py
```