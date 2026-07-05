
# Serverless Feedback System

This project is a complete Serverless Web Application built on AWS. It allows users to submit feedback through a simple web form, which is then processed by an AWS Lambda function and stored in a DynamoDB table.

## Architecture Overview
- **Frontend**: Hosted on Amazon S3.
- **API**: Managed by AWS API Gateway (with Lambda Proxy Integration).
- **Backend**: AWS Lambda (Python) processes the requests.
- **Database**: AWS DynamoDB stores the feedback data.

## Features
- Secure data submission using POST requests.
- CORS enabled for cross-origin communication.
- Real-time logging and debugging using Amazon CloudWatch.
- Unique ID generation for every feedback entry using Python's uuid library.

## How it works
1. The user fills out the feedback form on the S3-hosted website.
2. The browser sends a POST request to the API Gateway.
3. API Gateway triggers the Lambda function.
4. Lambda parses the JSON body and saves the data to DynamoDB.

## Troubleshooting & Learnings
- **CloudWatch Debugging**: Used CloudWatch Logs to identify and fix `KeyError` issues by analyzing runtime events.
- **Proxy Integration**: Enabled Lambda Proxy Integration in API Gateway to correctly handle JSON payloads.
- **CORS Configuration**: Configured OPTIONS method and CORS headers to allow communication between S3 and API Gateway.

## License
This project is open-source and available for educational purposes.