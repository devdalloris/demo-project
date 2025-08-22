GOOGLE_API_KEY = None
with open('.env', 'rt') as f:
    for line in f:
        splitted = line.split('=')
        if len(splitted)==2:
            key, value = splitted
            if key.strip() == 'GOOGLE_API_KEY':
                GOOGLE_API_KEY = value.strip()

print(GOOGLE_API_KEY)