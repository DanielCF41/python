def remove_non_alphanumeric(text):
    filtered_text = filter(str.isalnum, text)
    return ''.join(filtered_text)

print("..:: PALÍNDROMO ::..")
palavra_in = (input('Entre com uma palavra:'))
palavra_filtrada = remove_non_alphanumeric(palavra_in)

if palavra_filtrada == palavra_filtrada[::-1]:
    print("É palíndromo")
else:
    print("Não é palindromo")    
