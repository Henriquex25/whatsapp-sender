# WhatsApp Sender

## Descrição
Script em Python que envia mensagens em massa pelo WhatsApp.


## Requisitos
- Python 3.8+
- Git
- Conta no Supabase
- Conta no Z-API


## Instalação

### Clone o repositório
No diretório desejado, clone o repositório do projeto:
```bash
git clone https://github.com/Henriquex25/whatsapp-sender.git
```

Acesse a pasta criada na etapa anterior:
```bash
cd ./whatsapp-sender
```

### Prepare o ambiente
Agora vamos criar e ativar o ambiente virtual:
```bash
# Criar ambiente virtual
python -m venv venv

# Ativar o ambiente virtual (Linux/Mac)
source venv/bin/activate

# Ativar o ambiente virtual (Windows)
venv\Scripts\activate
```

### Instale as dependências
Para que o projeto funcione corretamente, devemos instalar as dependências executando o seguinte comando:
```bash
pip install -r requirements.txt
```

## Configuração
Copie o arquivo `.env.example` para `.env`
```bash
cp .env.example .env
```
Preencha com as suas credenciais

## Uso
Execute o script principal:
```bash
python main.py

# Ou

python3 main.py
```

## Funcionalidades
- Conexão com API do Supabase
- Tratamento de dados
- Envio de mensagens via Z-API