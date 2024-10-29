# Resumidor de Vídeos do YouTube

Este projeto é um script Python que permite baixar áudio de vídeos do YouTube, transcrevê-lo e gerar resumos do conteúdo transcrito. Ele utiliza bibliotecas como `yt-dlp` para download de vídeos, `whisper` para transcrição e a API do OpenAI para geração de resumos.

## Funcionalidades

-   **Download de Áudio**: Baixa o áudio do vídeo do YouTube no formato MP3.
-   **Transcrição**: Converte o áudio baixado em texto usando o modelo Whisper.
-   **Geração de Resumo**: Gera um resumo do texto transcrito usando a API do OpenAI.

## Tecnologias Utilizadas

-   [Python](https://www.python.org/) - Linguagem de programação.
-   [yt-dlp](https://github.com/yt-dlp/yt-dlp) - Biblioteca para baixar vídeos do YouTube.
-   [Whisper](https://github.com/openai/whisper) - Modelo de transcrição de áudio.
-   [OpenAI API](https://beta.openai.com/) - API para geração de resumos.

## Pré-requisitos

Antes de executar o projeto, você precisa ter instalado:

-   Python 3.7 ou superior
-   Pip (gerenciador de pacotes do Python)

### Instalação das Dependências

Instale as bibliotecas necessárias com o seguinte comando:

```bash
pip install requirements.txt
```

## Configuração

1. Clone este repositório em sua máquina local:

    ```bash
    git clone https://github.com/seu_usuario/seu_repositorio.git
    ```

2. Navegue até o diretório do projeto:

    ```bash
    cd seu_repositorio
    ```

3. Configure a chave da API do OpenAI no arquivo `gerar_resumo.py`:

    ```python
    openai.api_key = 'sua_chave_de_api'
    ```

## Como Usar

1. Execute o script `main.py`:

    ```bash
    python main.py
    ```

2. Quando solicitado, insira a URL do vídeo do YouTube que deseja resumir.

3. O script irá baixar o áudio do vídeo, transcrevê-lo e gerar um resumo.

## Estrutura do Projeto

```plaintext
├── data/                 # Diretório onde os áudios serão salvos
├── download_audio.py     # Script para baixar o áudio do YouTube
├── transcribe_audio.py   # Script para transcrever o áudio
├── gerar_resumo.py       # Script para gerar o resumo do texto
└── main.py               # Script principal para executar o projeto
```

## Contribuição

Sinta-se à vontade para contribuir com melhorias ou correções. Para isso, siga os passos abaixo:

1. Faça um fork do repositório.
2. Crie uma nova branch (`git checkout -b feature/nome-da-feature`).
3. Faça suas alterações e commit (`git commit -m 'Adiciona nova feature'`).
4. Envie a branch (`git push origin feature/nome-da-feature`).
5. Abra um Pull Request.

## Licença

Este projeto é licenciado sob a MIT License - consulte o arquivo [LICENSE](LICENSE) para mais detalhes.

## Contato

Se você tiver alguma dúvida ou sugestão, sinta-se à vontade para entrar em contato.
