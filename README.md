
<p align="center">
  <img src="https://github.com/andresmao/test/blob/master/pandas_glue_logo_2.png" width="450" title="Pandas Glue">
</p>

# Pandas Glue

[Amazon Glue](https://aws.amazon.com/glue/) is an [AWS](https://aws.amazon.com/) simple, flexible, and cost-effective ETL service and [Pandas](https://pandas.pydata.org/) is a Python library which provides high-performance, easy-to-use data structures and data analysis tools.

The goal of this package is help in the usage of serverless compute services ([Lambda](https://aws.amazon.com/glue/), [Glue](https://aws.amazon.com/lambda/), [Athena](https://aws.amazon.com/athena/)) in order to provide an easy way to integrate Pandas with  AWS Glue,  allowing upload the content of a DataFrame (**Write function**) directly in a table (parquet format) in the Glue Data Catalog and also execute Athena queries (**Read function**) returning the result directly in a Pandas DataFrame.

## Use cases

This package is recommended for ETL purposes which loads and transforms small to medium size datasets without requiring to create Spark jobs, helping reduce infrastructure costs.

It could be used within [Lambda functions](https://docs.aws.amazon.com/lambda/latest/dg/lambda-introduction-function.html)  or [Glue scripts](https://docs.aws.amazon.com/glue/latest/dg/aws-glue-programming-python.html).

<p align="center">
  <img src="https://github.com/andresmao/test/blob/master/PandasGlue_ETL_workflow.png" width="700"  title="ETL Workflow">
</p>

### Prerequisites

```
pip install pandas
pip install boto3
pip install pyarrow 
```

### Installing the package

```
pip install pandasglue
```

## Usage 

**Read method:**

***read_glue()***

To retrieve the result of an Athena Query in a Pandas DataFrame.

Quick example:

```
import pandas as pd
import pandasglue as pg

#Parameters
sql_query = "SELECT * FROM table_name LIMIT 20" 
db_name = "DB_NAME"
s3_output_bucket = "s3://bucket-url/"

df = pg.read_glue(sql_query,db_name,s3_output_bucket)

print(df)

```

**Write method:**

***write_glue()***

Convert a given Pandas Dataframe to a Glue Parquet table

Quick example:

```
import pandas as pd
import pandasglue as pg

#Parameters
sql_query = "SELECT * FROM table_name LIMIT 20" 
database = "DB_NAME"
table_name = "TB_NAME"
s3_path = "s3://bucket-url/"

#Sample DF
source_data = {'name': ['Sarah', 'Renata', 'Erika', 'Fernanda', 'Diana'], 
        'city': ['Seattle', 'Sao Paulo', 'Seattle', 'Santiago', 'Lima'],
         'test_score': [82, 52, 56, 234, 254]}
         
df = pd.DataFrame(source_data, columns = ['name', 'city', 'test_score'])


pg.write_glue(df, database, table_name, s3_path, partition_cols=['city'])


```

## Built With

* [Dropwizard](http://www.dropwizard.io/1.0.2/docs/) - The web framework used
* [Maven](https://maven.apache.org/) - Dependency Management
* [ROME](https://rometools.github.io/rome/) - Used to generate RSS Feeds

## Contributing

Please read [CONTRIBUTING.md](https://gist.github.com/PurpleBooth/b24679402957c63ec426) for details on our code of conduct, and the process for submitting pull requests to us.

## Authors

* **Billie Thompson** - *Initial work* - [PurpleBooth](https://github.com/PurpleBooth)

See also the list of [contributors](https://github.com/your/project/contributors) who participated in this project.

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgments

* Hat tip to anyone whose code was used
* Inspiration
* etc
