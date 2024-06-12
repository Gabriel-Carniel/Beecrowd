def max_char_count(s):
    # Dicionário para armazenar a contagem de cada caractere
    char_count = {}

    # Contar a frequência de cada caractere na string
    for char in s:
        if (65 <= ord(char) <= 90 or 97 <= ord(char) <= 122):
          if (65 <= ord(char) <= 90):
             aux = ord(char) + 32
             char = chr(aux)
          if char in char_count:
              char_count[char] += 1
          else:
              char_count[char] = 1

    # Encontrar a maior contagem de ocorrências
    max_count = max(char_count.values())

    # Encontrar todos os caracteres com a maior contagem
    max_chars = [char for char, count in char_count.items() if count == max_count]

    return max_chars, max_count

N = int(input())
for _ in range(N):
  frase = input()
  chars, count = max_char_count(frase)
  charsSort = sorted(chars)
  result_string = ''.join(charsSort)
  print(result_string)
