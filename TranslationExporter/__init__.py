# importing the requests library
import requests




def getAccessToken():
    url = "https://pame8xi-dev1.build.ifs.cloud/auth/realms/pame8xidev1/protocol/openid-connect/token"

    headers = {
        "Accept": "*/*",
        "Cache-Control": "no-cache",
        "Host": "pame8xi-dev1.build.ifs.cloud",
        "Accept-Encoding": "gzip, deflate, br",
        "Content-Type": "application/x-www-form-urlencoded",
        
        }
    
    body = {
        "grant_type":"password",
        "username":"ifsapp",
        "password":"f5d1ekfpvf0m8lp080fJ7NMSGe8QCJ",
        "scope":"openid microprofile-jwt",
        "client_id":"TRMOB_Client",
        "client_secret":"kLEt4WHkoEhbdWOYP11gSMG3OvGhBwzZ", 
        }

    # sending post request and saving response as response object
    r = requests.post(url = url, headers=headers, data=body)
    if (r.status_code == 200):
        r= r.json()

        # extracting response text
        access_token = r["access_token"]
        #print("The access_token is:%s"%access_token)
        return access_token
    
    return ""

accessToken = getAccessToken()
#print("The access_token is:%s"%accessToken)





url= "https://pame8xi-dev1.build.ifs.cloud/main/ifsapplications/projection/v1/TextTranslationsHandling.svc/TextTranslations?$filter=(LangCode eq 'tr')&$select=ContextId,AttributeId,Path,Module,ProgText,FieldTrans&$count=true&$skip=0&$top=1"
r= requests.get(url, headers={"Authorization": f"Bearer {accessToken}"})
if (r.status_code == 200):
    nCount = r.json()["@odata.count"]
    print("Number of records: %i"%nCount)

    nPtr=0
    while(nPtr<nCount):
        url= f"https://pame8xi-dev1.build.ifs.cloud/main/ifsapplications/projection/v1/TextTranslationsHandling.svc/TextTranslations?$filter=(LangCode eq 'tr')&$select=ContextId,AttributeId,Path,Module,ProgText,FieldTrans&$skip={nPtr}&$top=100"
        r= requests.get(url, headers={"Authorization": f"Bearer {accessToken}"})
        if (r.status_code == 200):
            print(f"Pointer => {nPtr}")
            data = r.json()["value"]
            nPtr += 100
        else:
            break
            
print("The access_token is:%s"%accessToken)