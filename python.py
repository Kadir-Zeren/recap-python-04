text = 'Clarusway'
print(text, 'kelimesinin uzunlugu', len(text), 'harften olusur')

print(text)

print(*text)

print (3* 'upper',sep=' ----->')

a = 5
a = a + 1
a += 1

name = 'Yasin'
print('Merhaba, %s' % name)

name = 'Yasin'
age = 43
meslek = 'Content Creator'
print('Merhaba, ismin %s yasin %d meslegin ise % s' % (name, age, meslek))

name = 'Yasin'
age = 43.5
meslek = 'Content Creator'
print( 'Merhaba, ismin %s yasin %f meslegin ise % s' % (name, age, meslek))

name = 'Ali'
age = 43
meslek = 'Content Creator'
print(f'merhaba benim adim {name} yasim {age} meslegim {meslek}')

print('Merhaba, ismin {} , yasin {b} meslegin ise {c}' . format(name, c = meslek, b = age))

print(f'merhaba benim adim {name} yasim {age} meslegim {meslek}','Merhaba, ismin {} ,yasin {b} meslegin ise {c}' . format(name, b = age, c = meslek)  )
 
name = 'MARIAM'
print(F'My name is {name. capitalize()}')