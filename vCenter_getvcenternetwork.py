#!/usr/bin/env python3
import json
import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

vcenter = "vcsa7.dis-cloud.jp"
username = "administrator@vsphere.local"
password = "Peg-6272"

if __name__ == "__main__":
    # セッション作成リクエスト
    url = "https://" + vcenter + "/rest/com/vmware/cis/session"
    headers = {"Accept":"application/json"}
    r = requests.post(url,
                      headers=headers,
                      auth=(username, password),
                      verify=False)

    # 取得した資格情報をヘッダに反映
    token = json.loads(r.text)["value"]
    headers.update({"vmware-api-session-id":token})

    print(headers)

    # Network情報を取得するリクエスト
    url = "https://" + vcenter + "/rest/vcenter/network"
    r = requests.get(url,
                     headers=headers,
                     verify=False)



    # 結果を表示
    print("vCenterNetwork情報")
    print(json.dumps(json.loads(r.text), indent=2))
    print()       
    
    # 資格削除リクエスト
    url = "https://" + vcenter + "/rest/com/vmware/cis/session"
    r = requests.delete(url,
                        headers=headers,
                        verify=False)

    

    print("資格削除結果")
    print(r.status_code)