company = ('Google', 'Facebook', 'Amazon', 'Microsoft', 'Apple')

for x in company:
    print(x)

print(company.count('Google'))
print(company.index('Amazon'))

if 'Google' in company:
    print('Google is present in the company list')