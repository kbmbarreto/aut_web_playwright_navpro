# aut_web_playwright_navpro

<p>Automação do portal NAV Pro, da empresa DASA, para fins acadêmicos e aprendizado do Playwright</p>

## Ferramentas utilizadas

- Python 3.12
- Playwright 1.47.0
- Pytest 8.3.3
- Pytest Html 4.1.1

## Execução
Para executar, execute o comando do Pytest na raiz do projeto:

<br>`pytest`: Este comando irá executar todos os testes do projeto.
<br>`pytest -v`: Este comando irá executar os testes exibindo mais detalhes no console.
<br>`pytest --html=report.html`: Com este comando podemos rodar os testes e gerar um relatório.


### O projeto ainda está em constantes melhorias, sendo atualizado a cada alteração.


## Documentação do projeto.
````
aut_web_playwright_navpro/
├── .venv/
├── page_objects/
│   ├── actions/
│   │   └── home_page.py
│   ├── elements/
│   │   └── home_locators.py
├── support/
│   └── utils.py
├── tests/
│   └── test_navpro.py
├── .gitignore
├── conftest.py
├── README.md
└── requirements.txt
````

- [Documentação oficial](https://playwright.dev/python/)