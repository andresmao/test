
<p align="center">
  <img src="https://github.com/andresmao/test/blob/master/pandas_glue_logo_2.png" width="450" title="Pandas Glue">
</p>

# Pandas Glue

[Amazon Glue](https://aws.amazon.com/glue/) is an [AWS](https://aws.amazon.com/) simple, flexible, and cost-effective ETL service and [Pandas](https://pandas.pydata.org/) is a Python library which provides high-performance, easy-to-use data structures and data analysis tools.

The goal of this package is help in the usage of serverless compute services in order to provide an easy way to integrate Pandas with the AWS Glue service allowing upload the content of a DataFrame (**Write**) directly in the Glue Data Catalog and also execute Athena queries (**Read**) returning the result directly in a Pandas DataFrame.

## Use cases

This package is recommended for ETL purposes which loads and transforms small to medium size datasets without requiring to create Spark jobs, helping reduce infrastructure costs.

It could be used within [Lambda functions](https://docs.aws.amazon.com/lambda/latest/dg/lambda-introduction-function.html)  or [Glue scripts](https://docs.aws.amazon.com/glue/latest/dg/aws-glue-programming-python.html).

<p align="center">
  <img src="https://github.com/andresmao/test/blob/master/PandasGlue_ETL_workflow.png" width="700"  title="ETL Workflow">
</p>

### Prerequisites

Mandatory
```
pip install pandas
pip install boto3
```
Recommended (to transform csv into parquet files as part of the ETL process)
```
pip install pyarrow 
```

### Installing

```
pip install pandasglue
```

## Usage

**Read**

Explain what these tests test and why

```
Give an example
```

### And coding style tests

Explain what these tests test and why

```
Give an example
```

## Deployment

Add additional notes about how to deploy this on a live system

## Built With

* [Dropwizard](http://www.dropwizard.io/1.0.2/docs/) - The web framework used
* [Maven](https://maven.apache.org/) - Dependency Management
* [ROME](https://rometools.github.io/rome/) - Used to generate RSS Feeds

## Contributing

Please read [CONTRIBUTING.md](https://gist.github.com/PurpleBooth/b24679402957c63ec426) for details on our code of conduct, and the process for submitting pull requests to us.

## Versioning

We use [SemVer](http://semver.org/) for versioning. For the versions available, see the [tags on this repository](https://github.com/your/project/tags). 

## Authors

* **Billie Thompson** - *Initial work* - [PurpleBooth](https://github.com/PurpleBooth)

See also the list of [contributors](https://github.com/your/project/contributors) who participated in this project.

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgments

* Hat tip to anyone whose code was used
* Inspiration
* etc
