📋 Descrição
Sistema simples de carrinho de compras desenvolvido com o objetivo de aplicar os conceitos de testes unitários, seguindo o ciclo de desenvolvimento incremental com validação automática das regras de negócio.

📁 Estrutura do Projeto
sistemacdecompras/
├── carrinho.py        # Classe principal com as regras de negócio
├── test_carrinho.py   # Testes unitários com pytest
└── relatorio.html     # Relatório gerado pelo pytest-html


⚙️ Funcionalidades

✅ Adicionar itens ao carrinho
✅ Remover itens do carrinho
✅ Calcular total da compra
✅ Aplicar desconto (máximo de 20%)


📏 Regras de Negócio

Desconto máximo permitido: 20%
Carrinho vazio deve retornar total zero
Desconto acima de 20% ou negativo lança ValueError


🧪 Testes Implementados
TesteDescriçãotest_carrinho_vazio_retorna_zeroCarrinho sem itens retorna total 0test_adicionar_um_itemAdiciona um item e verifica o totaltest_soma_multiplos_itensSoma correta de vários itenstest_soma_com_quantidadeSoma com quantidade maior que 1test_remover_itemRemove item e recalcula o totaltest_remover_item_inexistente_nao_quebraRemoção de item inexistente não gera errotest_remover_unico_item_deixa_carrinho_vazioCarrinho fica vazio após remover único itemtest_desconto_validoAplica desconto válido corretamentetest_desconto_maximo_20_porcentoDesconto de 20% funciona corretamentetest_desconto_acima_20_levanta_erroDesconto acima de 20% lança ValueErrortest_desconto_negativo_levanta_erroDesconto negativo lança ValueErrortest_desconto_zero_retorna_total_cheioDesconto 0% retorna total sem alteração

🚀 Como Executar
Instalação das dependências
bashpip install pytest pytest-html
Rodar os testes
bashpython -m pytest test_carrinho.py -v
Gerar relatório HTML
bashpython -m pytest test_carrinho.py -v --html=relatorio.html

🛠️ Tecnologias Utilizadas

Python 3.12
pytest 9.0.3
pytest-html 4.2.0


👤 Autor
Atividade Individual — Desenvolvimento com Testes Unitários
Cenário 5: Sistema de Carrinho de Compras
