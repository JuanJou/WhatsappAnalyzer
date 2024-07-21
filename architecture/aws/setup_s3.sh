#/bin/sh
echo "Setting up aws environment..."

awslocal s3api create-bucket --bucket chats-bucket
awslocal s3api create-bucket --bucket vectors-bucket

aws s3api put-bucket-notification-configuration --bucket chats-bucket --notification-configuration file://lambda_trigger.json

echo "Buckets created:"
awslocal s3api list-buckets
