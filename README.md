# Data Anonymizer

A Python module that anonymizes SQL dumps

## Installation

Install the Python module using the setup.py

```
python setup.py install
```

 or with pip

 ```
 pip install .
 ```

## Usage

First we will need to generate a configuration file using the GUI.

```bash
python -m data_anonymizer -g --host 127.0.0.1 --user root --pass toor --db anonymize
```

This will open a local webserver at <http://127.0.0.1:8000>, follow the instructions onscreen and download the configuration file.

Now we can create an anonymized using the configuration file we just generated

```bash
python -m data_anonymizer -c config.yml -i dump.sql -o anonymized.sql
```

### Options

- `-h` Help

Command Line Interface (for anonymizing database)

- `-c <CONFIGFILE>` Configuration file
- `-i <INPUTFILE>` SQL dump file
- `-o <OUTPUTFILE>` SQL dump output anonymized

Graphical User Interface (for generating configuration file)

- `-g` GUI (starts Flask server)
- `--host <HOST>` Host of MariaDB/MySQL server
- `--user <USERNAME>` Username of MariaDB/MySQL server
- `--pass <PASSWORD>` Password of MariaDB/MySQL server
- `--db <DATABASE>` Temporary database
