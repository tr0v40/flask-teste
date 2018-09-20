from Server import App
from flask import jsonify
from Services import Listar
from Models import Resposta

@App.route("/alunos", methods=["GET"])

def ListarRoute():
    Resposta.Resposta["Status"] = "Sucesso"
    Resposta.Resposta["Dados"] = Listar.Listar()
    Resposta.Resposta["Mensagem"] = "Alunos Enviados."
    Retorno = jsonify(Resposta.Resposta)
    return Retorno