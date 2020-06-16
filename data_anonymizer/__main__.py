import sys
import os.path
import argparse
import data_anonymizer as data
from .ConfigReader import config

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    
    parser.add_argument('-c', '--config', dest='configfile')
    parser.add_argument('--host', dest='host')
    parser.add_argument('--user', dest='username')
    parser.add_argument('--pass', dest='password')
    parser.add_argument('--db', dest='database')
    parser.add_argument('-i', '--input', dest='inputfile')
    parser.add_argument('-o', '--output', dest='outputfile')

    args = parser.parse_args()

    configfile = args.configfile
    infile = args.inputfile
    outfile = args.outputfile

    if not os.path.isfile(infile):
        print(str(infile) + " is not a valid file")
        sys.exit()

    # if not os.path.isfile(configfile):
    #     print(str(configfile) + " is not a valid file")
    #     sys.exit()

    # configreader = config(open(configfile, 'r'))

    # host = configreader.storage()['host']
    # username = configreader.storage()['username']
    # password = configreader.storage()['password']
    # database = configreader.storage()['database']

    if args.host is not None:
        host = args.host
    if args.username is not None:
        username = args.username
    if args.password is not None:
        password = args.password
    if args.database is not None:
        database = args.database

    anonymizer = data.Anonymize(host=host, username=username, 
                                password=password, database=database, 
                                infile=infile, outfile=outfile)
    anonymizer.populate_database()
    anonymizer.anonymize_database()
    anonymizer.export_database()