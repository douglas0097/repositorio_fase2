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


#======================== Métodos =======================

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
    

#===============================================


def criar_medico_principal():
    def cria_medico():
                    
        testa = True

        while testa: 
            nome = input("\nInforme o nome do médico: ")
            especialidade = input("Informe a especialidade do médico: ")
            telefone = input("Informe o telefone do médico: ")

            if not nome or not especialidade or not telefone:
                print("\nInforme todos os dados solicitados!") 
            else:
                medico = { "nome": nome, "especialidade": especialidade, "telefone": telefone}
                testa = False
                return medico

    medico = cria_medico()

    nome = medico["nome"]
    especialidade = medico["especialidade"]
    telefone = medico["telefone"]

    #insere o medico na tabela
    sql_inserir_medico = "INSERT INTO medico (nome, especialidade, telefone) VALUES (%s, %s, %s)"
    dados_insert = (nome, especialidade, telefone)
    insertNaTabela(conexao, sql_inserir_medico, dados_insert)
    print("Médico cadastrado com sucesso!")
    print(listarTabelas(conexao, sql_listar_medicos))
def busca_medico_pelo_crm():

    crm = input("Informe o crm do medico que você deseja buscar: ")
    cursor = conexao.cursor()
    sql_buscar_medico = "SELECT * FROM medico WHERE crm = %s"
    cursor.execute(sql_buscar_medico, (crm,))
    medico = cursor.fetchone()
    
    if medico:
        print(f"\nMédico encontrado:\n"
          f"Nome: {medico[1]}\n"
          f"especialidade: {medico[2]}\n"
          f"telefone: {medico[3]}\n")
    else:
        print("Nenhum médico encontrado com o CRM informado.")
def exclui_medico_pelo_crm():
    #mostra os medicos cadastrados antes de excluir
    print(listarTabelas(conexao, sql_listar_medicos))
        
    #remove um medico pelo crm 
    crm = input("Informe o crm do medico que você deseja remover: ")
    cursor = conexao.cursor()

    # SQL para buscar o médico pelo CRM antes de excluir
    sql_buscar_medico = "SELECT * FROM medico WHERE crm = %s"
    cursor.execute(sql_buscar_medico, (crm,))
    medico = cursor.fetchone()

    # Verifica se o médico com o CRM existe
    if not medico:
        print(f"Médico com CRM {crm} não encontrado.")
    else:
        sql_remover = "DELETE FROM medico WHERE crm = %s"
        dados_remover = (crm,)
        excluirDadosTabela(conexao, sql_remover, dados_remover)
        print("Médico removido com sucesso!")
    #---------------------------------------------------
