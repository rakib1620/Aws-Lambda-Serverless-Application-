import json
import boto3
import uuid


dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('UserData')

def lambda_handler(event, context):
    try:
        
        body = json.loads(event['body'])
        name = body.get('name')
        feedback = body.get('feedback')
        
        
        table.put_item(
            Item={
                'id': str(uuid.uuid4()),
                'name': name,
                'feedback': feedback
            }
        )
        
       
        return {
            'statusCode': 200,
            'headers': {
                'Access-Control-Allow-Origin': '*',
                'Access-Control-Allow-Headers': 'Content-Type',
                'Access-Control-Allow-Methods': 'OPTIONS,POST,GET'
            },
            'body': json.dumps({'message': 'Data inserted successfully!'})
        }
        
    except Exception as e:
        # কোনো সমস্যা হলে এরর মেসেজ পাঠানো
        return {
            'statusCode': 500,
            'headers': {
                'Access-Control-Allow-Origin': '*'
            },
            'body': json.dumps({'error': str(e)})
        }