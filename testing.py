import psycopg2
import pandas as pd
import matplotlib.pyplot as plt

def get_connection():
    try:
        return psycopg2.connect(
            database="accounts",
            user='postgres',
            password='password',
            host='127.0.0.1',
            port='5432'
        )
    except:
        return False

database = get_connection()
if database:
    print(f"Database connected successfully")
else:
    print(f"Failed to connect database.")

curr = database.cursor()
def get_data():
    curr.execute("SELECT region, SUM(amount) as total_amount FROM sale_register WHERE crop_name like 'Paddy%' GROUP BY region ORDER BY total_amount DESC")
    data = curr.fetchall()
    columns = [desc[0] for desc in curr.description]
    return data, columns
data, columns = get_data()
df = pd.DataFrame(data, columns=columns)
plt.barh(df.iloc[:,0],df.iloc[:,1])
plt.xlabel("total sales")
plt.ylabel("Region")
plt.title("Region wise Gross Sale Paddy")
plt.show()