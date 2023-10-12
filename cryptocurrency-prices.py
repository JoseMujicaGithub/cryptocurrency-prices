import requests

def validar_ingreso_int(): 
    contador=0
    while contador<1:
        try:
            variable=int(input(': '))
        except:
            print('ERROR ingrese un valor valido...')
            continue
        if type(variable)==int:
            contador+=1
    return variable

api_key_coin_market='93ba737e-38d8-41f4-acff-d89de9b8b78c'

print('Este programa te da el precio real de criptos en coinmarketcap.com')

print('Ingrese la cantidad de veces/monedas que quiere evaluar')
evaluaciones=validar_ingreso_int()

monedas_list=[]


headers = {  'Accepts': 'application/json',  'X-CMC_PRO_API_KEY':  api_key_coin_market}
data=requests.get("https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest",headers=headers).json()
for cripto in data["data"]:
    monedas_list.append(cripto["symbol"])
    monedas=tuple(monedas_list)

print(monedas)

i=0
while i<evaluaciones:
    cripto_name=input('Ingrese el nombre de una criptomoneda: ').upper()
    if cripto_name in monedas:
        response2=requests.get('https://api.binance.com/api/v3/ticker/price?symbol='+cripto_name+'USDT')
        if response2.ok:
            datos=response2.json() 
            price=str(round(float(datos['price']),2))
            print('El ',cripto_name,' se cotiza a ',price,' USDT')                     
            i+=1
    else:
        print('Error moneda invalida')
        continue