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

def imprime_menu_principal():
    print("""
           ╔═══════════════════════════════╗
           ║       Bem-vindo ao Help       ║
           ║ Escolha uma de nossas opções: ║
           ║  1. Médico                    ║
           ║  2. Paciente                  ║
           ║  3. Administrativo            ║
           ║  4. Sair                      ║
           ╚═══════════════════════════════╝ """)
def imprime_menu_medico():
    print(""" 
        ╔═════════════════════════════════════╗
        ║ Escolha uma de nossas opções:       ║
        ║                                     ║
        ║  1. Cadastrar médico                ║
        ║  2. Pesquisar médico por CRM        ║
        ║  3. Excluir médico por CRM          ║
        ║  4. Voltar ao menu anterior         ║
        ╚═════════════════════════════════════╝ """) 
def imprime_menu_paciente():
    print( """
        ╔═══════════════════════════════════════╗
        ║ Escolha uma de nossas opções:         ║
        ║                                       ║
        ║  1. Cadastrar paciente                ║
        ║  2. Pesquisar paciente por CPF        ║
        ║  3. Excluir paciente por CPF          ║
        ║  4. Voltar ao menu principal          ║
        ╚═══════════════════════════════════════╝ """)
def imprime_menu_administrativo():
    print( """
        ╔═══════════════════════════════════════╗
        ║ Escolha uma de nossas opções:         ║
        ║                                       ║
        ║  1. Agendamentos                      ║
        ║  2. Registro de procedimentos         ║
        ║  3. Voltar ao menu principal          ║
        ╚═══════════════════════════════════════╝ """)
def imprime_menu_agendamentos():
    print( """
        ╔═══════════════════════════════════════╗
        ║ Escolha uma de nossas opções:         ║
        ║                                       ║
        ║  1. Adicionar agendamentos            ║
        ║  2. Visualizar agendamentos           ║
        ║  3. Cancelar agendamento              ║
        ║  4. Voltar ao menu principal          ║
        ╚═══════════════════════════════════════╝ """)
def imprime_menu_procedimentos():
    print( """
        ╔═══════════════════════════════════════╗
        ║ Escolha uma de nossas opções:         ║
        ║                                       ║
        ║  1. Registrar um procedimento         ║
        ║  2. Listar procedimentos              ║
        ║  3. Voltar ao menu principal          ║
        ╚═══════════════════════════════════════╝ """)