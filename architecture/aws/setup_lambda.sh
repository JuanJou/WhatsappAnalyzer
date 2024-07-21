zip lambda.zip ./parse_s3.py

awslocal lambda create-function \
    --function-name parse_chats \
    --zip-file fileb://lambda.zip \
    --handler parse_s3.handler \

aws lambda add-permission --function-name parse_chats \
  --principal s3.amazonaws.com \
  --statement-id 1 \
  --action "lambda:InvokeFunction" \
  --source-arn arn:aws:s3:::chats-bucket \
