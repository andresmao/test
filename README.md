
<p align="center">
  <img src="https://github.com/andresmao/test/blob/master/pandas_glue_logo_2.png" width="450" title="Pandas Glue">
</p>

# Pandas Glue

[Amazon Glue](https://aws.amazon.com/glue/) is an [AWS](https://aws.amazon.com/) simple, flexible, and cost-effective ETL service and [Pandas](https://pandas.pydata.org/) is a Python library which provides high-performance, easy-to-use data structures and data analysis tools.

The goal of this package is to provide an easy way to integrate Pandas with the AWS Glue service allowing loading the content of a DataFrame (**Write**) directly in the Glue Data Catalog and also execute Athena queries (**Read**) returning the result directly in a Pandas DataFrame.

## Use cases

This package is recommended for ETL purposes which loads and transforms small to medium size datasets without requiring to create Spark jobs. Saving costs in the operation. 

<p align="center">
  <img src="https://github.com/andresmao/test/blob/master/PandasGlue_ETL_workflow.png" width="700"  title="ETL Workflow">
</p>



## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

### Prerequisites

What things you need to install the software and how to install them

```
Give examples
```

### Installing

A step by step series of examples that tell you how to get a development env running

Say what the step will be

```
Give the example
```

And repeat

```
until finished
```

End with an example of getting some data out of the system or using it for a little demo

## Running the tests

Explain how to run the automated tests for this system

### Break down into end to end tests

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
