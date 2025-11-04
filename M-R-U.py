def menu_inicial():
    print('\n----------------------------------------')
    print('   Programa de Simulação de M.R.U')
    print('----------------------------------------')
    print('1. Simulação de M.R.U')
    print('2. Como é calculado')
    print('3. Sair do programa')
    print('----------------------------------------')

def MRU():
    try:
        S0 = float(input("Digite a Posição Inicial em metros (S0): "))
        V = float(input("Digite a Velocidade em m/s (V): "))
        T_final = float(input("Digite o Tempo FINAL em segundos (T): "))
        
        if T_final < 0:
            print("\nErro: O tempo deve ser um valor positivo.")
            input("Pressione Enter para voltar ao menu...")
            return
        
        T_int = int(T_final)
        
        # --- INÍCIO DA REPETIÇÃO (Intervalo de 0 até T_final) ---
        print("\n--- Resultados do M.R.U. no Intervalo de Tempo ---")
        print(f"Posição Inicial (S0): {S0:.2f} m | Velocidade (V): {V:.2f} m/s")
        print("----------------------------")
        print("| Tempo (s) | Posição (m) |")
        print("----------------------------")
        
        for t in range(T_int + 1):
            S = S0 + V * t
            print(f"| {t:9d} | {S:11.2f} |")

        if T_final > T_int:
             S = S0 + V * T_final
             print(f"| {T_final:9.2f} | {S:11.2f} |")
             
        print("----------------------------\n")
        # --- FIM DA REPETIÇÃO ---

        # -----------------------------------------------------------
        # NOVO DESTAQUE: Cálculo e impressão do resultado final (S)
        # -----------------------------------------------------------
        S_final = S0 + V * T_final
        print(f"Cálculo Final (S = S0 + V * T):")
        print(f"S({T_final:.2f}s) = {S0:.2f} + {V:.2f} * {T_final:.2f}")
        print(f"Resultado -> Posição final S(t): {S_final:.2f} m\n")

    except ValueError:
        print("Erro: por favor, digite números válidos.")
        
    input("Pressione Enter para voltar ao menu...")

def mostrar_regra():
    print("\nComo é calculado o M.R.U.:")
    print("Fórmula: S(t) = S0 + V * T")
    print("- S0: posição inicial (m)")
    print("- V: velocidade constante (m/s)")
    print("- T: tempo decorrido (s)\n")
    input("Pressione Enter para voltar ao menu...")

if __name__ == '__main__':
    while True:
        menu_inicial()
        escolha = input("Escolha uma opção (1-3): ").strip()
        if escolha == '1':
            MRU()
        elif escolha == '2':
            mostrar_regra()
        elif escolha == '3':
            print("Encerrando o programa.")
            break
        else:
            print("Opção inválida. Por favor, escolha 1, 2 ou 3.")
