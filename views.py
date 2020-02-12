from flask import request, render_template, flash, send_from_directory
import os

from app import app


@app.route('/')
def index():
    return render_template('fichasSearch.html', titulo='Fichas de Numeração')


# -------------------------------------------------------------------------------------------------------------------
@app.route('/search_fichas', methods=['POST', ])
def search_fichas():
    flash('Para documentos com extensão .tif confira a pasta de download!')

    codlog = request.form['cd_codlog']

    path = r"\\nas.prodam\SL0104_Fichas_Numeracao"
    # path = r"C:\Users\x369482\Desktop\DLE_Fichas_renomeadas"

    main_folder_files = os.listdir(path)
    result_list = list()
    inside_files_list = list()
    pdf_dict = {}

    # lista com o nome dos arquivos e das pastas que estao dentro da pasta principal que estao de acordo com a pesquisa
    for file in main_folder_files:
        if file[:8] == codlog:
            result_list.append(file)

    # lista os items que foram encontrados na pesquisa e separa .pdf das Pastas
    for item in result_list:
        if item.endswith('.pdf'):
            pdf_dict = {item: item}
        else:
            # quando é pasta deve abrir a pasta e listar os arquivos contidos la dentro
            path2 = r"\\nas.prodam\SL0104_Fichas_Numeracao\{}".format(item)
            # path2 = r"C:\Users\x369482\Desktop\DLE_Fichas_renomeadas\{}".format(item)
            inside_files = os.listdir(path2)
            for i in inside_files:
                if not i.endswith('.db'):
                    teste = {item: inside_files}
                    inside_files_list.append(teste)
    inside_files_list.append(pdf_dict)

# refaz a lista para tirar itens que estao repetidos> função futura
    unique_list = list()
    for i in range(len(inside_files_list)):
        if inside_files_list[i] not in inside_files_list[i + 1:]:
            unique_list.append(inside_files_list[i])

    return render_template('fichasList.html', titulo='Fichas de Numeração', path=path,
                           inside_files_list=unique_list)


@app.route('/view_fichas', methods=['GET', ])
def view_fichas():
    path = request.args['path']
    file = request.args['file']
    folder = request.args['folder']

    if file.endswith('.tif'):
        path = path + r'/' + folder
        return send_from_directory(path, file)

    return send_from_directory(path, file)
