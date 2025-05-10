characters = input('Ingrese caracteres: ')

def isBalanced(characters):
    pila = []
    pares = {')':'(', ']':'[', '}':'{'}
    
    for char in characters:
        if char in '([{':
            pila.append(char)
        elif char in ')]}':
            if not pila or pila[-1] != pares[char]:
                return False
            pila.pop()

    return not pila

print('Balanceado' if isBalanced(characters) else 'No balanceado')