import boto3
import json

bedrock = boto3.client(service_name='bedrock-runtime',
                       region_name="us-east-1")

user_input = input("Poem About?: ")

prompt = """
    You are an imaginative, humorous, romantic, and intelligent poet. 
    You are comparable to Shakespeare.

    Your task is to write poetry about .
"""

# Todo: API Request

model_Id = 'ai21.j2-mid-v1'
content_Type = "application/json"
accept = "application/json"

### Apis body
payload = {
    "prompt":prompt + user_input,
    "maxTokens":512,
    "temperature":0.8,
    "topP":0.9
}
body=json.dumps(payload)


response = bedrock.invoke_model(
    modelId=model_Id,
    contentType=content_Type,
    accept=accept,
    body=body
)

response_body = json.loads(response.get('body').read())
print(response_body)
print('\n')

# text
response_text = response_body.get('completions')[0].get('data').get('text')
print(response_text)