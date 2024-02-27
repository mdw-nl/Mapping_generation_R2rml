# R2RML Mapping Generator with KG Lab

## Overview
This repository contains a Python utility designed to generate R2RML mappings, which facilitate the conversion of relational database content into RDF (Resource Description Framework) data. By applying these mappings, users can seamlessly transition to and integrate within Semantic Web technologies. This tool employs the functionalities provided by the KG Lab library to execute the R2RML mappings. Included are source code and configuration files essential for defining both the mappings and data source details.

## Configuration Files
This project maintains a dedicated `config_file` folder that hosts two distinct YAML configuration files:

- `config_r2rml.yml`: Specifies the configurations for R2RML mapping file generation, defining the relationships between database tables/columns and RDF ontology components such as classes and properties.

- `config_r2rml_data.yml`: Used during the data conversion process, this file supplies detailed information regarding the data source and its format, including database connection settings like database type, credentials, and other pertinent parameters.

## Installation

Before utilizing this utility, please ensure you have met the following requirements:

- Python 3.x
- All requisite Python packages listed in `requirements.txt`

To install the necessary dependencies, execute the following command:

```bash
pip install -r requirements.txt