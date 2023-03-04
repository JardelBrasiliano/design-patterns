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
const FabricaBotao: React.FC<BotaoProps> = (props: BotaoProps) => {
  switch (props.tipo) {
    case 'padrao':
      return <BotaoPadrao {...props} />;
    case 'primario':
      return <BotaoPrimario {...props} />;
    case 'secundario':
      return <BotaoSecundario {...props} />;
    default:
      throw new Error('Tipo de botão inválido');
  }
};

const MeuComponente = React.memo(FabricaBotao);

// Exemplo de uso
function onClickBotao() {
  console.log('Botão clicado');
}

<MeuComponente tipo="padrao" onClick={onClickBotao} />;
