import pandas as pd
import numpy as np
import scipy as sp
import matplotlib.pyplot as plt
import scipy.stats as stats
import seaborn as sns
import warnings
import os # Adicionado para limpar o terminal

warnings.filterwarnings('ignore', category=UserWarning)

arquivo = 'dados_banco.csv'
target = 'Salario'
atributo = 'Idade'


try:
    df = pd.read_csv(arquivo)
except FileNotFoundError:
    print("Arquivo não encontrado")
    exit()



def item_a(x, y):
    media_x = np.mean(x)
    var_x = np.var(x)
    dp_x = np.std(x)
    mediana_x = np.median(x)

    media_y = np.mean(y)
    var_y = np.var(y)
    dp_y = np.std(y)
    mediana_y = np.median(y)

    print(f"--------- ITEM A ---------")

    print("Estatísticas para X:")
    print(f"Média: {media_x:.4f}")
    print(f"Variância: {var_x:.4f}")
    print(f"Desvio Padrão: {dp_x:.4f}")
    print(f"Mediana: {mediana_x:.4f}")

    print("\nEstatísticas para Y:")
    print(f"Média: {media_y:.4f}")
    print(f"Variância: {var_y:.4f}")
    print(f"Desvio Padrão: {dp_y:.4f}")
    print(f"Mediana: {mediana_y:.4f}")

    print("--------------------------\n")

def item_b(x, y):
    print(f"--------- ITEM B ---------")

    fig, axs = plt.subplots(1, 2, figsize=(15, 5))
    axs[0].hist(x, bins='auto', color='blue')
    axs[0].set_title(f'Histograma de {atributo}')
    axs[0].set_xlabel(atributo)
    axs[0].set_ylabel('Frequência')
    axs[0].grid(axis='y')
 
    axs[1].hist(y, bins='auto', color='green')
    axs[1].set_title(f'Histograma de {target}')
    axs[1].set_xlabel(target)
    axs[1].set_ylabel('Frequência')
    axs[1].grid(axis='y')

    plt.tight_layout()
    plt.show()

    print("--------------------------\n")

def item_c(x, y):
    print(f"--------- ITEM C ---------")
    sns.set(style="whitegrid")

    fig, axs = plt.subplots(1, 2, figsize=(15, 5)) # Criar subplots

    # Boxplot para Idade
    sns.boxplot(ax=axs[0], x=x) # Usar o primeiro subplot
    axs[0].set_title(f'Boxplot de {atributo}')
    axs[0].set_xlabel('Valores')

    # Boxplot para Salário
    sns.boxplot(ax=axs[1], x=y) # Usar o segundo subplot
    axs[1].set_title(f'Boxplot de {target}')
    axs[1].set_xlabel('Valores')

    plt.tight_layout() # Ajustar layout para evitar sobreposição
    plt.show()
    
    print("--------------------------\n")
    
def item_d(x, y):
    print(f"--------- ITEM D ---------")
    corr = np.corrcoef(x, y)[0, 1]
    print(f"Coeficiente de Correlação entre {atributo} e {target}: {corr:.4f}")
    print("--------------------------\n")

def item_e(x, y):
    print(f"--------- ITEM E ---------")
    alpha = 0.05
    significancia = 0.10
    
    print(f"\nTestes para {atributo}:")
    # Teste de Shapiro-Wilk
    stat, p = stats.shapiro(x)
    print('Statistics=%.3f, p=%.3f' % (stat, p))
    if p > alpha:
        print('Amostra Gaussiana (aceita H0)')
    else:
        print('Amostra não Gaussiana (rejeita H0)')
    
    # Teste de D'Agostino e Pearson
    stat_test, p_valor = stats.normaltest(x)
    print('\nEstatística do teste:', stat_test)
    print('Valor p:', p_valor)
    print("Rejeitamos a hipótese nula:", p_valor <= significancia)
    
    print(f"\nTestes para {target}:")
    # Teste de Shapiro-Wilk
    stat, p = stats.shapiro(y)
    print('Statistics=%.3f, p=%.3f' % (stat, p))
    if p > alpha:
        print('Amostra Gaussiana (aceita H0)')
    else:
        print('Amostra não Gaussiana (rejeita H0)')
    
    # Teste de D'Agostino e Pearson
    stat_test, p_valor = stats.normaltest(y)
    print('\nEstatística do teste:', stat_test)
    print('Valor p:', p_valor)
    print("Rejeitamos a hipótese nula:", p_valor <= significancia)
    
    print("--------------------------\n")

def item_f(x, y):
    print(f"--------- ITEM F ---------")
    sns.set(style="whitegrid")

    fig, axs = plt.subplots(1, 2, figsize=(15, 6))

    # Histograma e Densidade para x (Idade)
    sns.histplot(x, kde=False, ax=axs[0], color='skyblue', stat="density", label='Histograma') # kde=False para não duplicar a densidade
    sns.kdeplot(x, ax=axs[0], color='blue', label='Densidade')
    axs[0].set_title(f'Histograma e Densidade de {atributo}')
    axs[0].set_xlabel('Valores')
    axs[0].set_ylabel('Densidade')
    axs[0].legend() # Adicionar legenda

    # Histograma e Densidade para y (Salário)
    sns.histplot(y, kde=False, ax=axs[1], color='lightcoral', stat="density", label='Histograma') # kde=False para não duplicar a densidade
    sns.kdeplot(y, ax=axs[1], color='red', label='Densidade')
    axs[1].set_title(f'Histograma e Densidade de {target}')
    axs[1].set_xlabel('Valores')
    axs[1].set_ylabel('Densidade')
    axs[1].legend() # Adicionar legenda

    plt.tight_layout()
    plt.show()
    
    print("--------------------------\n")

# Inserir função de menu interativo

def clear_screen():
    """Limpa o terminal."""
    os.system('cls' if os.name == 'nt' else 'clear')

def menu(x, y):
    while True:
        clear_screen() # Limpa a tela antes de mostrar o menu
        print(f"PROJETO DE PROBABILIDADE E ESTATÍSTICA\n\n")
        print(f"--------- ALUNOS ---------")
        print(f"Pedro Alexandre Custodio Silva - 22.123.049-3")
        print(f"Lucas Roberto Boccia dos Santos - 22.123.012-1")
        print(f"--------------------------\n\n")
        print("Menu de opções:")
        print("a - Estatísticas descritivas (Item A)")
        print("b - Histogramas (Item B)")
        print("c - Boxplots (Item C)")
        print("d - Coeficiente de Correlação (Item D)")
        print("e - Testes de Normalidade (Item E)")
        print("f - Histogramas e Densidade (Item F)")
        print("q - Sair")
        choice = input("Escolha uma opção: ").lower()
        print("--------------------------\\n")
        
        clear_screen() # Limpa a tela antes de mostrar o item selecionado

        if choice == 'a':
            item_a(x, y)
        elif choice == 'b':
            item_b(x, y)
        elif choice == 'c':
            item_c(x, y)
        elif choice == 'd':
            item_d(x, y)
        elif choice == 'e':
            item_e(x, y)
        elif choice == 'f':
            item_f(x, y)
        elif choice == 'q':
            print("Encerrando programa.")
            break
        else:
            print("Opção inválida. Tente novamente.\\n")
            input("Pressione Enter para continuar...") # Pausa para o usuário ler a mensagem
            continue # Volta para o início do loop sem pausar novamente

        if choice != 'q': # Não pausa se o usuário escolheu sair
            input("Pressione Enter para retornar ao menu...")


if __name__ == "__main__":
    x = df[atributo]
    y = df[target]
    print(f"PROJETO DE PROBABILIDADE E ESTATÍSTICA\n\n")
    print(f"--------- ALUNOS ---------")
    print(f"Pedro Alexandre Custodio Silva - 22.123.049-3")
    print(f"Lucas Roberto Boccia dos Santos - 22.123.012-1")
    print(f"--------------------------\n\n")

    menu(x, y)