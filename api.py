import urllib.request, json
from jsonserial import jsonobj

if __name__ == '__main__':
    url = "http://xxxx/xxxx" 
    method = "POST"
    headers = {"Content-Type" : "application/json"}

    obj = jsonobj.JsonObj()
    obj.name = "Onur"
    obj.age = 35
    obj.dog = jsonobj.JsonObj()
    obj.dog.name = "Apollo"

    print(obj.toJSON())
    json_data = json.dumps(obj.toJSON()).encode("utf-8")
    print(json_data)
    # httpリクエストを準備してPOST
    request = urllib.request.Request(url, data=json_data, method=method, headers=headers)
    with urllib.request.urlopen(request) as response:
        response_body = response.read().decode("utf-8")