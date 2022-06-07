import sqlite3
import tkinter as tk
import pandas as pd


janela = tk.Tk()
janela.title('Cadastro de Produtos')
janela.geometry("330x350")
janela.configure(bg='gray')

#Criando o Banco de Dados:

# conexao = sqlite3.connect ('cadastro.db')
#
# # Criando o cursor:
# c = conexao.cursor ()
#
# # Criando a tabela:
#
# c.execute ("""CREATE TABLE  Produtos (
#        codigo integer,
#        produto text,
#        valor integer,
#        quantidade integer,
#        fornecedor text
#    )""")
#
# # Commit as mudanças:
# conexao.commit ()
#
# # Fechar o banco de dados:
# conexao.close ()

def cadastrar_produtos():
     conexao = sqlite3.connect('cadastro.db')
     c = conexao.cursor()

     # Inserir dados na tabela:
     c.execute("INSERT INTO produtos VALUES (:codigo,:produto,:valor,:quantidade,:fornecedor)",
               {
                   'codigo': entry_codigo.get(),
                   'produto': entry_produto.get(),
                   'valor': entry_valor.get(),
                   'quantidade': entry_quantidade.get(),
                   'fornecedor': entry_fornecedor.get()

               })

     # Commit as mudanças:
     conexao.commit()

     # Fechar o banco de dados:
     conexao.close()

     # #Apaga os valores das caixas de entrada
     entry_codigo.delete(0, "end")
     entry_produto.delete(0, "end")
     entry_valor.delete(0, "end")
     entry_quantidade.delete(0, "end")
     entry_fornecedor.delete(0, "end")

def exporta_produtos():
     conexao = sqlite3.connect('cadastro.db')
     c = conexao.cursor()

     # Inserir dados na tabela:
     c.execute("SELECT *, oid FROM produtos")
     produtos_cadastrados = c.fetchall()
     # print(produtos_cadastrados)
     produtos_cadastrados = pd.DataFrame(produtos_cadastrados,
                                     columns=['codigo', 'produto', 'valor', 'quantidade', 'fornecedor', ])
     produtos_cadastrados.to_excel('produtos.xlsx')

     # Commit as mudanças:
     conexao.commit()

     # Fechar o banco de dados:
     conexao.close()


 # Rótulos Entradas:

label_codigo = tk.Label(janela, text='codigo')
label_codigo.grid(row=0, column=0, padx=10, pady=10)

label_produto = tk.Label(janela, text='produto')
label_produto.grid(row=1, column=0, padx=10, pady=10)

label_valor = tk.Label(janela, text='valor')
label_valor.grid(row=2, column=0, padx=10, pady=10)

label_quantidade = tk.Label(janela, text='quantidade')
label_quantidade.grid(row=3, column=0, padx=10, pady=10)

label_fornecedor = tk.Label(janela, text='fornecedor')
label_fornecedor.grid(row=4, column=0, padx=10, pady=10)

 # Caixas Entradas:
entry_codigo = tk.Entry(janela, width=35)
entry_codigo.grid(row=0, column=1, padx=10, pady=10)

entry_produto = tk.Entry(janela, width=35)
entry_produto.grid(row=1, column=1, padx=10, pady=10)

entry_valor = tk.Entry(janela, width=35)
entry_valor.grid(row=2, column=1, padx=10, pady=10)

entry_quantidade = tk.Entry(janela, width=35)
entry_quantidade.grid(row=3, column=1, padx=10, pady=10)

entry_fornecedor = tk.Entry(janela, width=35)
entry_fornecedor.grid(row=4, column=1, padx=10, pady=10)

# # Botão de Cadastrar

botao_cadastrar = tk.Button(text='Cadastrar Produto', command=cadastrar_produtos)
botao_cadastrar.grid(row=5, column=0, columnspan=2, padx=10, pady=10, ipadx=80)

 # Botão de Exportar
botao_exportar = tk.Button(text='Exportar para Excel', command=exporta_produtos)
botao_exportar.grid(row=6, column=0, columnspan=2, padx=10, pady=10, ipadx=80)

janela.mainloop()
