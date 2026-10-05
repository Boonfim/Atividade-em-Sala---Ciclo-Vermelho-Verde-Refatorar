"""
PLANO DE TDD E REFATORAÇÃO (Atividade Assíncrona - Ciclo Vermelho-Verde-Refatorar)

1. Problema Escolhido: 
   Cálculo do preço final de um produto (Equação matemática: Preço Base + Imposto - Desconto). 
   A estrutura da equação é fixa, mas as regras de imposto e desconto variam por categoria.

2. Padrão de Projeto Escolhido: 
   Template Method.
   - Por que escolhi este padrão? Conforme visto em aula, 
   o Template Method define o esqueleto de um algoritmo na superclasse 
   (a equação de preço final) e deixa as subclasses implementarem os 
   passos que variam (o cálculo de imposto e desconto específicos)
    Isso evita duplicação de código e impede que a ordem matemática das operações seja alterada por engano[cite: 47].

3. Casos que vou testar (3 variações de comportamento):
   - Teste 1: Cálculo para produto da categoria "Livro" (Isento de imposto (0%), 10% de desconto).
   - Teste 2: Cálculo para produto da categoria "Eletrônico" (20% de imposto, 5% de desconto).
   - Teste 3: Cálculo para produto da categoria "Alimento" (5% de imposto, sem desconto (0%)).

4. Tempo estimado para cada fase:
   - Plano: 10 minutos (concluído)
   - Fase Red (escrever os 3 testes falhando): 15 minutos
   - Fase Green (implementar a matemática direta, usando 'ifs', até os testes passarem): 25 minutos
   - Fase Refactor (aplicar o padrão Template Method, criando uma classe base 'Produto' e subclasses para cada categoria): 40 minutos
   - Autoavaliação e revisão: 10 minutos

5. Uso de IA: 
   Utilizei uma IA (Gemini) na fase de planejamento (Passo 1) para me ajudar a bolar uma ideia de problema matemático simples que se adequasse de forma didática aos padrões de projeto ensinados nos slides da disciplina e para formatar o rascunho deste plano.
"""

import calculadora 


# criando teste de cada categoria
def teste_calculo_livro():
    preco_base = 100.0
    categoria = "Livro"

    resultado = calcular_preco_final(preco_base, categoria)
    assert resultado == 90.0

def teste_calculo_eletronico():
    preco_base = 100.0
    categoria = "Eletrônico"

    resultado = calcular_preco_final(preco_base, categoria)
    assert resultado == 210.0

def teste_calculo_alimento():
    preco_base = 100.0
    categoria = "Alimento"

    resultado = calcular_preco_final(preco_base, categoria)
    assert resultado == 105.0



