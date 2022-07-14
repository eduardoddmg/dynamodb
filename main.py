import boto3
from tabulate import tabulate

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('crudBrawhalla')

def update(table):
    print('Digite o nome no qual voce deseja alterar algo')
    name = input()
    item = table.get_item(
        Key={
            'name': name
        }
    )
    item = item.get('Item')
    print(item)
    if item is None:
        print('esse nome nao existe na base de dados')
        return
    else:
        print('strength:')
        strength = input()
        print('dexterity:')
        dexterity = input()
        print('defence:')
        defence = input()
        print('speed:')
        speed = input()
        print('gender:')
        gender = input()
        print('price:')
        price = input()
        print('datereleased:')
        datereleased = input()

        response = table.put_item(
        Item={
            'name': name,
            'strength': strength,
            'dexterity': dexterity,
            'defence': defence,
            'speed': speed,
            'gender': gender,
            'price': price,
            'datereleased': datereleased,
        }
    )

def create(table):
    print('name:')
    name = input()
    print('strength:')
    strength = input()
    print('dexterity:')
    dexterity = input()
    print('defence:')
    defence = input()
    print('speed:')
    speed = input()
    print('gender:')
    gender = input()
    print('price:')
    price = input()
    print('datereleased:')
    datereleased = input()
    item = table.get_item(
        Key={
            'name': name
        }
    )
    item = item.get('Item')
    print(item)
    if item is not None:
        print('esse nome ja existe, tente outro')
    else:
        response = table.put_item(
        Item={
            'name': name,
            'strength': strength,
            'dexterity': dexterity,
            'defence': defence,
            'speed': speed,
            'gender': gender,
            'price': price,
            'datereleased': datereleased,
        }
    )


def remove(table):
    print('Digite o nome que voce deseja remover')
    n = input()
    table.delete_item(
        Key={
            'name': n
        }
    )

def geral(table):
    print('Digite uma opcao:\n[1]: create\n[2]: update\n[3]: remove\n[4]: printar\n[5]: sair')
    n = int(input())
    if n == 1:
        create(table)
    elif n == 2:
        update(table)
    elif n == 3:
        remove(table)
    elif n == 4:
        printar(table)
    elif n == 5:
        print('O programa será encerrado')
        exit()

def printar(table):
    array = []
    response = table.scan()
    response = response['Items']
    print('tabela dataset brawhalla')
    for i in range(0, len(response)):
        array.append([response[i]['name'], response[i]['strength'], response[i]['dexterity'], response[i]['defence'], response[i]['speed'], response[i]['gender'], response[i]['price'], response[i]['datereleased']])
    print(tabulate(array, headers=['name', 'strength', 'dexterity', 'defence', 'speed', 'gender', 'price', 'datereleased'], tablefmt='orgtbl'))

geral(table)