from Server import App
from Models import Resposta
from flask import jsonify

@App.errorhandler(404)
def TratarNaoEncontrado(error):
    Resposta.Resposta["Status"] = "Erro"
    Resposta.Resposta["Mensagem"] = "Acao nao existente"
    return jsonify(Resposta.Resposta)

@App.errorhandler(500)
def TratarNaoEncontrado(error):
    Resposta.Resposta["Status"] = "Erro"
    Resposta.Resposta["Mensagem"] = "Um problema critico foi encontrado. Erro{0}".format(error)
    return jsonify(Resposta.Resposta)
