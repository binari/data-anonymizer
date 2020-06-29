def gui(host, username, password, database, infile):
    import data_anonymizer as data
    import io
    from flask import Flask, render_template, url_for, request, session, send_file
    from ruamel.yaml import YAML
    import data_anonymizer as data

    anonymizer = data.Anonymize(host=host, username=username, 
                                password=password, database=database, infile=infile)

    anonymizer.populate_database()
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
            for column in anonymizer.get_columns(table):
                tables[table].append(column[3])

        return render_template('columnselector.html', tables=tables)

    @app.route('/action', methods=['POST'])
    def action():
        if request.method != 'POST':
            return 'no'

        # Does magic to convert stuff
        toBeModified = {}
        for element in request.form:
            if '*iterator*' in element:
                toBeModified[element.replace('*iterator*','')] = {'iterator': {'name': request.form[element]},'columns': {}}
            else:
                splitted = element.split('!?!')
                
                if request.form[element] not in ["None", ""]:
                    if splitted[1] not in toBeModified[splitted[0]]['columns']:
                        toBeModified[splitted[0]]['columns'][splitted[1]] = {}
                    toBeModified[splitted[0]]['columns'][splitted[1]][splitted[2]] = request.form[element]

        configdata = {'storage': {'host': host, 'username': username, 'password': password, 'database': database}, 'anonymize': toBeModified}
        yaml=YAML()
        yaml.default_flow_style = False
        yamlconfig = io.StringIO()
        yaml.dump(configdata, yamlconfig)

        mem = io.BytesIO()
        mem.write(yamlconfig.getvalue().encode('utf-8'))
        # seeking was necessary. Python 3.5.2, Flask 0.12.2
        mem.seek(0)

        return send_file(mem, as_attachment=True, attachment_filename='config.yml', mimetype='text/yaml')

    app.run('127.0.0.1', 8000)