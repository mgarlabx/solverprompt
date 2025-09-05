import lambda_function as lbf

path = "analyze"
# path = "submit"
    
event = {
    "requestContext": {"http": {"method": "POST","path": f"/{path}"}},
    "body": {
        "language": "pt",
        "prompt_input": "Quem descobriu o Brasil?",
    }
}

resp = lbf.lambda_handler(event, None)
print(resp)


