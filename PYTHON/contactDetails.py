import requests

auth_token="59550a0e2b1a864a31bef962363e029f" #YOUR_AUTH_TOKEN
org_id="652853630" #YOUR_ORGANISATION_ID

contact_id="215666000000175001" #Contact ID

params="include=accounts" #OPTIONS

headers={
    "Authorization":auth_token,
    "orgId":org_id,
    "contentType": "application/json; charset=utf-8"
}

request=requests.get('https://desk.zoho.com/api/v1/contacts/'+contact_id+'?'+params, headers=headers)

if contact_id:

    if request.status_code == 200:
        print "Request Successful,Response:"
        print request.content
    else:
        print "Request not successful,Response code ",request.status_code," \nResponse : ",request.content;

else:
    print "Contact ID is missing"
