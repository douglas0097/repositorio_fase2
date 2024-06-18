from banco_dados1 import *

#======================== Banco de Dados =======================

endereco = "localhost"
usuario = "root"
senha = "12345678"

conexao = criarConexaoInicial(endereco, usuario, senha)

sql_criar_bd = "CREATE DATABASE IF NOT EXISTS hospital"
criarBancoDados(conexao, sql_criar_bd)

sql_criar_tabela_medico = """
    CREATE TABLE IF NOT EXISTS medico(
        crm INT AUTO_INCREMENT PRIMARY KEY,
        nome VARCHAR(45),
        especialidade VARCHAR(45),
        telefone VARCHAR(45)
    )
"""
sql_criar_tabela_paciente = """
    CREATE TABLE IF NOT EXISTS paciente(
        cpf INT AUTO_INCREMENT PRIMARY KEY,
        nome VARCHAR(45),
        idade VARCHAR(45),
        endereco VARCHAR(45),
        telefone VARCHAR(45)
    )
"""
sql_criar_tabela_agendamentos = """
    CREATE TABLE IF NOT EXISTS agendamento(
        id INT AUTO_INCREMENT PRIMARY KEY,
        cpf VARCHAR(45),
        consulta VARCHAR(45)
    )
"""
sql_criar_tabela_procedimentos = """
    CREATE TABLE IF NOT EXISTS procedimento(
        id INT AUTO_INCREMENT PRIMARY KEY,
        cpf VARCHAR(45),
        consulta VARCHAR(45)
    )
"""

criarTabela(conexao, "hospital", sql_criar_tabela_medico)
criarTabela(conexao, "hospital", sql_criar_tabela_paciente)
criarTabela(conexao, "hospital", sql_criar_tabela_agendamentos)
criarTabela(conexao, "hospital", sql_criar_tabela_procedimentos)

sql_listar_medicos = "SELECT * FROM medico"
sql_listar_pacientes = "SELECT * FROM paciente"
sql_listar_agendamentos = "SELECT * FROM agendamento"
sql_listar_procedimentos = "SELECT * FROM procedimento"