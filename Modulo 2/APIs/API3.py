import requests

print('Boa tarde! veja nosso menu:') 
print('PRATOS🍽️')
print('🍕 Pizza Margherita (Pizza tradicional com molho de tomate, queijo mozzarella e manjericão) Valor: R$ 30,00')
print('🍔 Hambúrguer (Hambúrguer com queijo cheddar, alface, tomate e molho especial) Valor: R$ 25,00')
print('🍲 Feijoada (Feijoada com arroz, farofa, couve e laranja) Valor: R$ 40,00')
print('BEBIDAS🍹')
print('🥤 Coca-Cola (Refrigerante clássico, gelado e refrescante) valor: R$ 5,00')
print('🍊 Suco de Laranja (Suco natural de laranja, sem conservantes) valor: R$ 7,50')
print('💧 Água Mineral (Água pura e refrescante) valor: R$ 3,00')
print('MESA🪑')
print('Mesas Disponiveis: 1, 2, 3')
print('FAÇA SEU PEDIDO:')

prato=input("Digite seu prato:")
bebida=input("Digite sua bebida:")
mesa=input('Digite o numero de sua mesa:')
id=mesa 
print(prato)
print(bebida)
resposta=input('SEU PEDIDO ESTA CORRETO?')

lala={
    'Prato':prato,
    'Bebida':bebida,
    'Mesa':mesa,
}
 

if resposta== 'sim':
    print('OK, aguarde seu pedido')

    

else:
    
    prato=input("Digite seu prato:")
    bebida=input("Digite sua bebida:")
    mesa=input('Digite o numero de sua mesa:')
    
    lala={
        'Prato':prato,
        'Bebida':bebida,
        'Mesa':mesa,
    }

    
    requests.post(f"https://68ca9f8b430c4476c34a3cbf.mockapi.io/Restaurante/{id}",lala) 
    

add=input("Voce gostaria de adicionar mais algum item?")

if add=="nao":
    print("Ok entao :)")
    
else:
    print("DIGITE SEUS ITENS EM SEQUENCIA:")
    pratos=input('digite seu outro prato:')
    bebidas=input('digite sua outra bebida:')
    
tuf={
    'prato':prato,
    'bebida':bebida,
    'mesa':mesa
}
  
    



r=requests.put(f"https://68ca9f8b430c4476c34a3cbf.mockapi.io/Restaurante/{id}",tuf) 

deletes=input('pronto, deseja deletar seu pedido?')

if deletes=='nao':
 print('ok entao, como desejar! :)')
 
else: 
    requests.delete(f"https://68ca9f8b430c4476c34a3cbf.mockapi.io/Restaurante/{id}",lala) 
    
print('verifique sua mesa!')

requests.get(f"https://68ca9f8b430c4476c34a3cbf.mockapi.io/Restaurante/{id}",lala) 

print(r.json())


