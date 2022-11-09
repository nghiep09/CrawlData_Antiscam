import json
import re

import requests

url = "https://api.antiscam.vn/api/Post/GetPosts"

i = 0

type_post = {
    "4": "SDT",
    "13": "Momo",
    "14": "Facebook",
    "8": "Website",
    "6": "Bank_acc_name",
    "7": "Bank_acc",
    "10": "Email"
}


while True:
    i += 1
    payload = json.dumps({
        "searchModel": {
            "currentPage": i,
            "searchText": "",
            "typeId": 0,
            "sortType": 1,
            "kindOfValue": 2,
            "pageSize": 10,
            "total": 0,
            "totalPage": 0,
            "isMine": False
        }
    })
    headers = {
        'content-type': 'application/json'
    }

    response = requests.request("POST", url, headers=headers, data=payload)

    print(response.text)

    articles = []
    file = open("file.json", "a+")

    if response.status_code == 200:

        for record in response.json().get("data").get("data"):
            # description = record.get('description')
            # typePosts = record.get('typePosts')
            # for typePost in typePosts:
            #     typePost_sdt = typePost.get('object').strip()
            #
            #     # sdt = re.findall("^84|0(3[2-9]|5[6|8|9]|7[0|6-9]|8[0-6|8|9]|9[0-4|6-9])[0-9]{7}$/", typePos_sdt)
            #     typePost_sdtt ="".join(re.findall("^(02[0-9]|84|0[3|5|7|8|9])([0-9]{8})", typePost_sdt)[0])
            #         # sdt = "".join(typePost_sdtt[0])
            #
            #     name = re.findall("^([a-z]+)((\s{1}[a-z]+){1,})$", typePost_sdt)
            #     mail = re.findall("^[A-Za-z0-9]+[A-Za-z0-9]*@[A-Za-z0-9]+(\\.[A-Za-z0-9]+)$", typePost_sdt)

                articles.append({
                    'title': record.get('title'),
                    'sdt': sdt,
                    'name': name,
                    'mail': mail,
                    'createdDate': record.get('createdDate'),
                })

        for ar in articles:
            file.write(json.dumps(ar) + '\n')

        if not articles:
            break

    file.close()


