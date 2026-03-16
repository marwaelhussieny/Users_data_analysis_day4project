def fetch_api_data():
    import requests
    import pandas as pd

    limit = 30
    total = 0
    skip = 0
    listpd = []
    page = 0

    while True:
        url = f"https://dummyjson.com/users?limit={limit}&skip={skip}"
        response = requests.get(url)
        data = response.json()['users']
        listpd.append(pd.DataFrame(data))
        total = response.json()['total']
        skip += limit

        if skip >= total:
            break

        print(f"page {page+1} loaded!")
        page += 1
    print("data fetched successfully")

    users = pd.concat(listpd)
    users.to_csv("user.csv", index=False)

    print("data saved successfully")