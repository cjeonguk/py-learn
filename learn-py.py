company = ['Google', 'Facebook', 'Amazon', 'Microsoft', 'Apple']
print(company)

company.append('IBM')
company.remove('Amazon')
company.pop(2)

company.insert(2, 'Amazon')

company.sort()

# company.clear()


for i in company:
    print(i)