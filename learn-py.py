fine_dust = {
    '서울': 72,
    '대전': 82,
    '구미': 29,
    '광주': 45,
}

bad_dust = {city: dust for city, dust in fine_dust.items() if dust > 70}

print(bad_dust)