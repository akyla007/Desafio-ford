# Desafio Ford

## Instalação das Dependências

Siga os passos abaixo para instalar as dependências do projeto a partir do arquivo `pyproject.toml`.

### Pré-requisitos

- Python 3.12 ou superior
- `pip` (gerenciador de pacotes do Python)
- `virtualenv` (opcional, mas recomendado)

### Passo a Passo

1. **Clone o repositório:**

    ```bash
    git clone https://github.com/akyla007/Desafio-ford.git
    cd Desafio-ford
    ```

2. **Crie um ambiente virtual (opcional, mas recomendado):**

    ```bash
    python -m venv venv
    source venv/bin/activate  # No Windows use `venv\Scripts\activate`
    ```

3. **Instale o `pip-tools`:**

    ```bash
    pip install pip-tools
    ```

4. **Compile as dependências do `pyproject.toml`:**

    ```bash
    pip-compile
    ```

5. **Instale as dependências:**

    ```bash
    pip install -r requirements.txt
    ```

### Executando o Projeto

Após instalar as dependências, você pode executar o projeto com o comando:

```bash
python main.py
```

### Contribuindo

Se você deseja contribuir com o projeto, por favor, faça um fork do repositório e envie um pull request com suas alterações.
