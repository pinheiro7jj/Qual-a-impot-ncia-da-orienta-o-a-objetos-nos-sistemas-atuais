import tkinter as tk
from tkinter import messagebox

class Usuario:
    def __init__(self, nome, email, idade):
        self.nome = nome
        self.email = email
        self.idade = idade
    
    def __str__(self):
        return f"{self.nome} - {self.email} - {self.idade} anos"

class Cadastro:
    def __init__(self):
        self.usuarios = []

    def adicionar_usuario(self, nome, email, idade):
        usuario = Usuario(nome, email, idade)
        self.usuarios.append(usuario)

    def listar_usuarios(self):
        return "\n".join(str(usuario) for usuario in self.usuarios)

class Aplicacao:
    def __init__(self, root):
        self.root = root
        self.root.title("Cadastro de Usuários")

        self.cadastro = Cadastro()

        # Configuração da interface gráfica
        self.label_nome = tk.Label(root, text="Nome:")
        self.label_nome.grid(row=0, column=0, padx=10, pady=10)

        self.entry_nome = tk.Entry(root)
        self.entry_nome.grid(row=0, column=1, padx=10, pady=10)

        self.label_email = tk.Label(root, text="Email:")
        self.label_email.grid(row=1, column=0, padx=10, pady=10)

        self.entry_email = tk.Entry(root)
        self.entry_email.grid(row=1, column=1, padx=10, pady=10)

        self.label_idade = tk.Label(root, text="Idade:")
        self.label_idade.grid(row=2, column=0, padx=10, pady=10)

        self.entry_idade = tk.Entry(root)
        self.entry_idade.grid(row=2, column=1, padx=10, pady=10)

        self.button_cadastrar = tk.Button(root, text="Cadastrar", command=self.cadastrar_usuario)
        self.button_cadastrar.grid(row=3, column=0, columnspan=2, pady=10)

        self.button_listar = tk.Button(root, text="Listar Usuários", command=self.listar_usuarios)
        self.button_listar.grid(row=4, column=0, columnspan=2, pady=10)

        self.text_usuarios = tk.Text(root, width=40, height=10)
        self.text_usuarios.grid(row=5, column=0, columnspan=2, padx=10, pady=10)

    def cadastrar_usuario(self):
        nome = self.entry_nome.get()
        email = self.entry_email.get()
        idade = self.entry_idade.get()

        # Validação simples
        if not nome or not email or not idade:
            messagebox.showwarning("Entrada inválida", "Por favor, preencha todos os campos.")
            return
        
        # Adicionando o usuário ao cadastro
        try:
            idade = int(idade)  # Garantindo que idade seja um número
            self.cadastro.adicionar_usuario(nome, email, idade)
            messagebox.showinfo("Sucesso", f"Usuário {nome} cadastrado com sucesso!")
            self.entry_nome.delete(0, tk.END)
            self.entry_email.delete(0, tk.END)
            self.entry_idade.delete(0, tk.END)
        except ValueError:
            messagebox.showwarning("Entrada inválida", "Por favor, insira um valor válido para idade.")

    def listar_usuarios(self):
        usuarios = self.cadastro.listar_usuarios()
        if usuarios:
            self.text_usuarios.delete(1.0, tk.END)  # Limpa o texto antes de adicionar
            self.text_usuarios.insert(tk.END, usuarios)
        else:
            messagebox.showinfo("Sem usuários", "Não há usuários cadastrados.")

# Criando a janela principal
root = tk.Tk()

# Criando a aplicação
app = Aplicacao(root)

# Iniciando o loop da interface gráfica
root.mainloop()
