# Gaussian Convolution

Este projeto é uma ferramenta para processar arquivos de log gerados pelo software Gaussian e tem como objetivo colocar uma gaussiana sobre cada par de transição lambda, força de oscilador.


## Pré-requisitos

Antes de começar, certifique-se de ter o Python instalado em sua máquina. Você pode baixar a versão mais recente do Python aqui: https://www.python.org/downloads/

## Passos para criar um ambiente virtual e instalar as bibliotecas

### 1. Criação do Ambiente Virtual

Um ambiente virtual é uma ferramenta que ajuda a manter os projetos Python isolados uns dos outros, especialmente com relação às suas dependências.

1. Abra o terminal (ou cmd/powershell no Windows).
2. Navegue até o diretório para clonar o projeto. Por exemplo:

    ```sh
    cd caminho/para/o/seu/projeto
    ```


3. Clone o projeto:
    ```sh
    git clone https://github.com/labcc-control/gaussian-convolve.git
    ```

4. Navegue até o diretório do projeto:

    ```sh
    cd ./gaussian-convolve
    ```


5. Crie um novo ambiente virtual com o comando:

    ```sh
    python -m venv .venv
    ```

6. Ative o ambiente virtual:

    - No Windows:

        ```sh
        .venv\Scripts\activate
        ```

    - No macOS/Linux:

        ```sh
        source .venv/bin/activate
        ```

    Quando o ambiente virtual estiver ativado, você verá o nome do ambiente entre parênteses na linha de comando, por exemplo `(.venv)`.

### 2. Instalação das Bibliotecas

Após ativar o ambiente virtual, você pode instalar as bibliotecas necessárias para o seu projeto listadas no `requirements.txt` usando o comando:

    ```sh
    pip install -r requirements.txt
    ```

### 3. Verificação da Instalação

Para garantir que todas as bibliotecas foram instaladas corretamente, você pode listar todas as bibliotecas instaladas no ambiente virtual com o comando:

```sh
pip freeze
```

Este comando exibirá todas as bibliotecas instaladas no ambiente virtual juntamente com suas versões.



### 4. Como utilizar o programa

Basta garantir que todos os passos anteriores foram realizados e utilizar o seguinte comando no terminal:

```sh
python apply_gaussian.py --hw 10 --input_folder ./gaussian_data --output_folder ./output
```

Para entender cada flag, utilize o seguinte comando no terminal:

```sh
python apply_gaussian.py --help
```
### 5. Desativação do Ambiente Virtual

Ao terminar de trabalhar no seu projeto, você pode desativar o ambiente virtual com o comando:

```sh
deactivate
```
## Conclusão

Seguindo esses passos, você terá um ambiente virtual configurado e todas as bibliotecas necessárias instaladas para o seu projeto. Manter suas dependências gerenciadas pela `requirements.txt` e utilizando um ambiente virtual garantirá que seu projeto seja mais facilmente replicável e isolado de outras configurações de sistema.