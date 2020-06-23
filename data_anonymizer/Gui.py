def gui(host, username, password, database):
    import data_anonymizer as data
    from flask import Flask, render_template, url_for, request, session
    import data_anonymizer as data

    anonymizer = data.Anonymize(host=host, username=username, 
                                password=password, database=database)
    # anonymizer.populate_database()

    app = Flask(__name__.split('.')[0])

    app.secret_key = b'greghrwr32t54t3wrfewy34'

    @app.route('/')
    def root():
        tables = anonymizer.get_tables()
        return render_template('tableselector.html', tables=tables)

    @app.route('/columnselector', methods=['POST'])
    def columnselector():
        if request.method != 'POST':
            return 'no'

        tables = {}
        for table in request.form:
            tables[table] = []
            for column in anonymizer.get_columns('core_users'):
                tables[table].append(column[3])

        return render_template('columnselector.html', tables=tables)

    @app.route('/action', methods=['POST'])
    def action():
        if request.method != 'POST':
            return 'no'

        toBeModified = {}
        for element in request.form:
            splitted = element.split('!?!')
            if splitted[0] not in toBeModified:
                toBeModified[splitted[0]] = {}
            if request.form[element] != "None":
                toBeModified[splitted[0]][splitted[1]] = request.form[element]
        print(toBeModified)
        return toBeModified

    app.run('127.0.0.1', 8000)