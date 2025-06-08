from generator.generator import generate_password

def main():
    print("=== Gerador de Senhas Simples ===")
    try:
        length = int(input("Informe o tamanho da senha: "))
        password = generate_password(length)
        print(f"Senha gerada: {password}")
    except ValueError:
        print("Por favor, insira um número válido.")

if __name__ == "__main__":
    main()
