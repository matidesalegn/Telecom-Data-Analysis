import unittest
import pandas as pd
import psycopg2
from configparser import ConfigParser

# Function to read PostgreSQL connection details from Secrets.toml
def config(filename='Secrets.toml', section='connections.postgresql'):
    # Create a parser
    parser = ConfigParser()
    # Read the configuration file
    parser.read(filename)

    # Get section, default to postgresql
    db_params = {}
    if parser.has_section(section):
        params = parser.items(section)
        for param in params:
            db_params[param[0]] = param[1]
    else:
        raise Exception(f'Section {section} not found in the {filename} file')

    return db_params

# Function to connect to PostgreSQL database and fetch data
def fetch_data_from_postgres(query):
    try:
        # Read PostgreSQL connection details from Secrets.toml
        params = config()
        # Connect to PostgreSQL database
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        # Execute SQL query
        cur.execute(query)
        # Fetch data
        data = cur.fetchall()
        cur.close()
        conn.close()
        return data
    except Exception as e:
        print(f"Error fetching data from PostgreSQL: {e}")
        return None

# Define your SQL query to fetch the data
sql_query = "SELECT * FROM xdr_data"

# Fetch data from PostgreSQL database
data = fetch_data_from_postgres(sql_query)

# Convert fetched data into a pandas DataFrame
df = pd.DataFrame(data, columns=['Start', 'Bearer Id', 'Last Location Name', ...])

class TestCleaTelco(unittest.TestCase):
    
    def setUp(self):
        self.clean_telco = clean_dataframe.CleanTelco()
    
    def test_convert_to_datetime(self):
        self.assertEqual(self.clean_telco.convert_to_datetime(df, 'Start')['Start'].dtype, "datetime64[ns]")
    
    def test_convert_to_integer(self):
        self.assertEqual(self.clean_telco.convert_to_integer(df, 'Bearer Id')['Bearer Id'].dtype, "int64")

    def test_convert_to_string(self):
        self.assertEqual(self.clean_telco.convert_to_string(df, 'Last Location Name')['Last Location Name'].dtype, 'string')

if __name__ == "__main__":
    unittest.main()
