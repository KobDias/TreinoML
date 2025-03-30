# API Flask com Modelo de Aprendizagem

⚠️ **Status do Projeto**  
Este repositório está em fase de desenvolvimento inicial.

Se quiser contribuir ou testar, abra uma issue ou entre em contato!

## Visão Geral
Este projeto é uma API Flask que serve um modelo de aprendizagem, projetada para ser integrada a uma página web. A API permite uma interação fluida entre o front-end e o modelo de aprendizagem, possibilitando o processamento dinâmico de dados e previsões. É uma excelente oportunidade para estudar o backend conectado a modelos de aprendizagem.

## Funcionalidades
- **API Flask**: Uma API leve e eficiente construída com Flask.
- **Integração com Aprendizagem de Máquina**: Conecta-se a um modelo de aprendizagem pré-treinado para previsões.
- **Front-End Responsivo**: Utiliza HTML, CSS e Bootstrap para uma interface amigável.
- **Interação Dinâmica**: JavaScript para requisições assíncronas à API, melhorando a experiência do usuário.
- **Suporte a Entradas em CSV**: Permite o upload de arquivos CSV para processar múltiplas entradas de uma só vez.
- **Retorno de Predições em CSV**: Gera um arquivo CSV com as previsões, facilitando a análise dos resultados.

## Instalação
1. Clone o repositório:
   ```bash
   git clone https://github.com/KobDias/mlTraining
   ```
2. Navegue até o diretório do projeto:
   ```bash
   cd mlTraining
   ```
3. Configure um ambiente virtual:
   ```bash
   python -m venv venv
   ```
   - Ative o ambiente virtual:
     - No Windows:
       ```bash
       venv\Scripts\activate
       ```
     - No macOS/Linux:
       ```bash
       source venv/bin/activate
       ```
4. Instale os pacotes necessários:
   ```bash
   pip install -r requirements.txt
   ```

## Uso
1. Inicie o servidor Flask:
   ```bash
   python app.py
   ```
2. Acesse a API em [http://localhost:5000/api](http://localhost:5000/api).
3. Utilize a interface do front-end para interagir com o modelo de aprendizagem.
4. Para enviar entradas em CSV, utilize a funcionalidade de upload na interface.
5. As previsões serão retornadas em um arquivo CSV que você poderá baixar.

## Contribuições
Contribuições são bem-vindas! Por favor, envie um pull request ou abra uma issue para quaisquer melhorias ou correções de bugs.

## Licença
Este projeto está licenciado sob a Licença MIT. Consulte o arquivo LICENSE para mais detalhes.

## Contato
Para dúvidas ou sugestões, entre em contato com [seu-email@exemplo.com](mailto:seu-email@exemplo.com).
