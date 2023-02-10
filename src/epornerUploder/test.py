from epornerUploder.app import handler
import json

def main(data,index):
    try:        
        del data['_id']
        if index%10==0:
            handler(
                {'body':json.dumps(data),'create_account':True},
                {}
                )
        else:
            handler(
                {'body':json.dumps(data),'create_account':False},
                {}
                )
    except Exception as e:
        print(e)
