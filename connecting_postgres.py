import psycopg2

#establishing the connection
conn = psycopg2.connect(
   database="postgres", user='postgres', password='postgres', host='localhost', port= '5432'
)
#Creating a cursor object using the cursor() method
cursor = conn.cursor()

#Executing an MYSQL function using the execute() method
cursor.execute("select version()")

# Fetch a single row using fetchone() method.
data = cursor.fetchone()
print("Connection established to: ",data)

#Executing an MYSQL function using the execute() method
cursor.execute("select * from employee")
result=cursor.fetchall()
print("Emp table has below data: \n",result)

#Closing the connection
conn.close()
