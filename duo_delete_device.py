import duo_client
import json
import sys
import duo_admin_config


if (args_count := len(sys.argv)) > 2:
    print(f"One argument expected, got {args_count - 1}")
    raise SystemExit(2)
elif args_count < 2:
    print("You must specify the Phone ID!")
    raise SystemExit(2)

phone_id =  sys.argv[1]
print(f'Phone ID : {phone_id}')

admin_api = duo_client.Admin(ikey=duo_admin_config.ikey, skey=duo_admin_config.skey, host=duo_admin_config.api_hostname)


result = admin_api.get_phone_by_id(phone_id)
json_formatted_str = json.dumps(result, indent=2)
print(json_formatted_str)


params = {}
result = admin_api.json_api_call('DELETE','/admin/v1/phones/'+phone_id, params)
json_formatted_str = json.dumps(result, indent=2)
print(json_formatted_str)


