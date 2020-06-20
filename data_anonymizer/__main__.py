import sys
import os.path
import argparse
import data_anonymizer as data
from .ConfigReader import config

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    
    parser.add_argument('-c', '--config', dest='configfile', 
                        required=True, help="Configuration file")
    parser.add_argument('-i', '--input', dest='inputfile', 
                        required=True, help="SQL dump from database")
    parser.add_argument('-o', '--output', dest='outputfile', 
                        required=True, help="Anonymized SQL dump")

    args = parser.parse_args()

    configfile = args.configfile
    infile = args.inputfile
    outfile = args.outputfile

    if not os.path.isfile(infile):
        print(str(infile) + " is not a valid file")
        sys.exit()

    if not os.path.isfile(configfile):
        print(str(configfile) + " is not a valid file")
        sys.exit()

    configreader = config(open(configfile, 'r'))

    host = configreader.storage()['host']
    username = configreader.storage()['username']
    password = configreader.storage()['password']
    database = configreader.storage()['database']

    anonymizer = data.Anonymize(host=host, username=username, 
                                password=password, database=database,
                                configfile=configfile, infile=infile, 
                                outfile=outfile)
    anonymizer.populate_database()
    anonymizer.anonymize_database()
    anonymizer.export_database()
