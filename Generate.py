import random
import string


def gerar_senha(comprimento=12, incluir_maiusculas=True, incluir_numeros=True, 
                incluir_simbolos=True):
    grupos_de_caracteres = {
        string.ascii_letters: incluir_maiusculas,
        string.digits: incluir_numeros,
        string.punctuation: incluir_simbolos,
    }

    caracteres = ''.join(caracteres for caracteres, value in
                         grupos_de_caracteres.items() if value)
    
    if not caracteres:
        raise ValueError("Não pode ser tudo False")

    senha = ''.join(random.choice(caracteres) for _ in range(comprimento))
    return senha


if __name__ == "__main__":
    senha_segura = gerar_senha(comprimento=14, incluir_maiusculas=True, 
                               incluir_numeros=True, incluir_simbolos=True)
    print(senha_segura)
