import pandas as pd
import boto3

#Customer Variables
customer_query = "SELECT name, local_price FROM big_mac where iso_a3 = 'ARG'"
customer_db = "default"
customer_s3_output = "s3://rserafim/"

#TO-DO REVIEW
client = boto3.client('athena')

#query executing
def run_query(query, database, s3_output):
    response = client.start_query_execution(
        QueryString=query,
        QueryExecutionContext={
            'Database': database
            },
        ResultConfiguration={
            'OutputLocation': s3_output,
            }
        )
    return response['QueryExecutionId']

#query_validation
def query_validation(query_exec):
    resp=["FAILED","SUCCEEDED","CANCELLED"]
    response = client.get_query_execution(QueryExecutionId=query_exec)
    while response['QueryExecution']['Status']['State'] not in resp:
        response = client.get_query_execution(QueryExecutionId=query_exec)
    return response

#main program
def read_glue(query,db,s3_output):
    qe=run_query(query,db,s3_output)
    validation=query_validation(qe)
    if validation == "FAILED":
        message_error = "Your query is not valid: "+response['QueryExecution']['Status']['StateChangeReason']
        raise Exception(message_error)
    else:
        file=customer_s3_output+qe+".csv"
        df = pd.read_csv(file)
    return df

teste=read_glue(customer_query,customer_db,customer_s3_output)
print(teste)
