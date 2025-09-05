import json
from functions.analyze import analyze
from functions.submit import submit

def lambda_handler(event, context):

    method = event["requestContext"]["http"]["method"]
    path = event["requestContext"]["http"]["path"]
    
    body = {}
    if 'body' in event and event['body'] is not None: body = event['body']
    if isinstance(body, str): body = json.loads(event['body']) # to convert to json when from JS or Postman

    ret = "No response"

    if (path == "/analyze") & (method == "POST"):
        ret = analyze(body)
    
    elif (path == "/submit") & (method == "POST"):
        ret = submit(body)
    
    else:
        return {
            'statusCode': 400,
            'body': 'Bad Request'
        }
            
    resp = ret
    
    return {
         'statusCode': 200,
         'body': resp
    }
     