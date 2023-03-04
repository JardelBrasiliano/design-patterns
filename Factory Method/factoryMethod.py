from abc import ABC, abstractmethod
from enum import Enum


class PerfilUsuario(ABC):
    def __init__(self, nome):
        self.nome = nome


class Convidado(PerfilUsuario):
    def __init__(self, nome):
        super().__init__(nome)
        self.tipo_perfil = "Convidado"


class PessoaJuridica(PerfilUsuario):
    def __init__(self, nome):
        super().__init__(nome)
        self.tipo_perfil = "Pessoa Jurídica"


class PessoaFisica(PerfilUsuario):
    def __init__(self, nome):
        super().__init__(nome)
        self.tipo_perfil = "Pessoa Física"


class FabricaUsuario(ABC):
    @abstractmethod
    def criar_perfil(self, nome):
        pass


class Usuario(FabricaUsuario):
    def __init__(self, nome):
        self.nome = nome

    def criar_perfil(self, tipo_perfil):
        if tipo_perfil == "convidado":
            return Convidado(self.nome)
        elif tipo_perfil == "pessoa_juridica":
            return PessoaJuridica(self.nome)
        elif tipo_perfil == "pessoa_fisica":
            return PessoaFisica(self.nome)
        else:
            raise ValueError("Tipo de perfil inválido")


# USANDO


nome_usuario = input("Digite seu nome: ")
usuario = Usuario(nome_usuario)

print("\nEscolha o tipo de perfil que deseja criar:")
print("1. Convidado")
print("2. Pessoa Jurídica")
print("3. Pessoa Física\n")

opcao = int(input("Digite a opção desejada: "))

if opcao == 1:
    perfil = usuario.criar_perfil("convidado")
elif opcao == 2:
    perfil = usuario.criar_perfil("pessoa_juridica")
elif opcao == 3:
    perfil = usuario.criar_perfil("pessoa_fisica")
else:
    print("Opção inválida")
    exit()


if perfil:
    print(f"\nPerfil criado: {perfil.tipo_perfil} - {perfil.nome}\n")
