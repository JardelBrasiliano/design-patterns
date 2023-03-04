import React, { useMemo } from 'react';

// PRODUTOS
interface BotaoProps {
  tipo: 'padrao' | 'primario' | 'secundario';
  onClick: () => void;
}

const BotaoPadrao: React.FC<BotaoProps> = (props: BotaoProps) => {
  return <button onClick={props.onClick}>Botão Padrão</button>;
};

const BotaoPrimario: React.FC<BotaoProps> = (props: BotaoProps) => {
  return <button onClick={props.onClick}>Botão Primário</button>;
};

const BotaoSecundario: React.FC<BotaoProps> = (props: BotaoProps) => {
  return <button onClick={props.onClick}>Botão Secundário</button>;
};

// FABRICA
interface Botao {
  renderizar(): React.ReactElement;
}

class FabricaBotao {
  criarBotao(props: BotaoProps): Botao {
    switch (props.tipo) {
      case 'padrao':
        return { renderizar: () => <BotaoPadrao {...props} /> };
      case 'primario':
        return { renderizar: () => <BotaoPrimario {...props} /> };
      case 'secundario':
        return { renderizar: () => <BotaoSecundario {...props} /> };
      default:
        throw new Error('Tipo de botão inválido');
    }
  }
}

const MeuComponente: React.FC<BotaoProps> = (props: BotaoProps) => {
  const botao = useMemo(() => {
    const fabricaBotao = new FabricaBotao();
    return fabricaBotao.criarBotao(props);
  }, [props]);

  return <div>{botao.renderizar()}</div>;
};

// Exemplo de uso
function onClickBotao() {
  console.log('Botão clicado');
}

<MeuComponente tipo="padrao" onClick={onClickBotao} />;
