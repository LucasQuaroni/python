capitales = {
    'EE.UU': 'Washington',
    'Francia': 'París',
    'Reino Unido': 'Londres',
    'España': 'Madrid',
    'Argentina': 'Buenos Aires'
}

capitales.update({'México': 'Ciudad de México'})

capitales.pop('Francia')

for x,y in capitales.items():
    print(x + ' -> ' + y)