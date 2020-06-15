import data_anonymizer as data

if __name__ == '__main__':
    anonymizer = data.Anonymize()
    # anonymizer.populate_database()
    anonymizer.anonymize_database()
    anonymizer.export_database()
