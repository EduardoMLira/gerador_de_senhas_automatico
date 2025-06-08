from generator.generator import generate_password

def ask_boolean(msg):
    while True:
        resposta = input(f"{msg} (s/n): ").lower()
        if resposta in ['s', 'n']:
            return resposta == 's'
        print("Entrada inválida. Digite 's' para sim ou 'n' para não.")

def main():
    print("=== Gerador de Senhas Customizável ===")
    try:
        length = int(input("Tamanho da senha: "))
        use_upper = ask_boolean("Incluir letras maiúsculas?")
        use_lower = ask_boolean("Incluir letras minúsculas?")
        use_digits = ask_boolean("Incluir números?")
        use_symbols = ask_boolean("Incluir símbolos?")

        password = generate_password(length, use_upper, use_lower, use_digits, use_symbols)
        print(f"\nSenha gerada: {password}")
    except ValueError as e:
        print(f"Erro: {e}")

if __name__ == "__main__":
    main()
