abstract class PerfilUsuario {
  nome: string;

  constructor(nome: string) {
    this.nome = nome;
  }
}

class Convidado extends PerfilUsuario {
  tipo_perfil: string;

  constructor(nome: string) {
    super(nome);
    this.tipo_perfil = 'Convidado';
  }
}

class PessoaJuridica extends PerfilUsuario {
  tipo_perfil: string;

  constructor(nome: string) {
    super(nome);
    this.tipo_perfil = 'Pessoa Jurídica';
  }
}

class PessoaFisica extends PerfilUsuario {
  tipo_perfil: string;

  constructor(nome: string) {
    super(nome);
    this.tipo_perfil = 'Pessoa Física';
  }
}

interface FabricaUsuario {
  criar_perfil(nome: string): PerfilUsuario;
}

class Usuario implements FabricaUsuario {
  nome: string;

  constructor(nome: string) {
    this.nome = nome;
  }

  criar_perfil(tipo_perfil: string) {
    if (tipo_perfil === 'convidado') {
      return new Convidado(this.nome);
    } else if (tipo_perfil === 'pessoa_juridica') {
      return new PessoaJuridica(this.nome);
    } else if (tipo_perfil === 'pessoa_fisica') {
      return new PessoaFisica(this.nome);
    } else {
      throw new Error('Tipo de perfil inválido');
    }
  }
}

// USO

const nome_usuario = 'Jardel';
const usuario = new Usuario(nome_usuario);

const novoPerfil = usuario.criar_perfil('pessoa_fisica');

console.log(
  `\nPerfil criado:  ${novoPerfil.tipo_perfil} - ${novoPerfil.nome}\n`
);
