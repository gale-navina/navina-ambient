#!/bin/bash

set -e
set -x

echo "Starting setup script..."

# Install jq if it's not already installed
if ! command -v jq &> /dev/null
then
    echo "jq could not be found, installing..."
    apt-get update && apt-get install -y jq
fi

ROLE_NAME="kinesis-access-role"
POLICY_NAME="KinesisPutRecordPolicy"
STREAM_NAME="your-kinesis-stream-name"
SESSION_NAME="test-session"
USER_NAME="test-user"

# Use localstack as the hostname
LOCALSTACK_HOST="http://localstack:4566"

# Function to wait for LocalStack to be ready
wait_for_localstack() {
  echo "Waiting for LocalStack to be ready..."
  until curl -s ${LOCALSTACK_HOST}/_localstack/health | grep '"iam": "available"' | grep '"kinesis": "available"' | grep '"sts": "available"'; do
    echo "LocalStack is not yet available - retrying in 5 seconds..."
    sleep 5
  done
  echo "LocalStack is ready!"
}

wait_for_localstack

# Create Kinesis Stream
echo "Creating Kinesis Stream..."
awslocal --endpoint-url=${LOCALSTACK_HOST} kinesis create-stream --stream-name $STREAM_NAME --shard-count 1
echo "Kinesis Stream '$STREAM_NAME' created successfully."

# Create IAM Policy
echo "Creating IAM Policy..."
POLICY_ARN=$(awslocal --endpoint-url=${LOCALSTACK_HOST} iam create-policy \
    --policy-name $POLICY_NAME \
    --policy-document '{
        "Version": "2012-10-17",
        "Statement": [
            {
                "Effect": "Allow",
                "Action": [
                    "kinesis:PutRecord",
                    "kinesis:GetRecords",
                    "kinesis:GetShardIterator",
                    "kinesis:DescribeStream",
                    "kinesis:ListStreams",
                    "kinesis:ListShards"
                ],
                "Resource": "arn:aws:kinesis:us-east-1:000000000000:stream/'$STREAM_NAME'"
            }
        ]
    }' | jq -r '.Policy.Arn')
echo "Policy created with ARN: $POLICY_ARN"

# Create IAM Role
echo "Creating IAM Role..."
ROLE_ARN=$(awslocal --endpoint-url=${LOCALSTACK_HOST} iam create-role \
    --role-name $ROLE_NAME \
    --assume-role-policy-document '{
        "Version": "2012-10-17",
        "Statement": [
            {
                "Effect": "Allow",
                "Principal": {
                    "Service": "ec2.amazonaws.com"
                },
                "Action": "sts:AssumeRole"
            }
        ]
    }' | jq -r '.Role.Arn')
awslocal --endpoint-url=${LOCALSTACK_HOST} iam attach-role-policy \
    --role-name $ROLE_NAME \
    --policy-arn $POLICY_ARN
echo "IAM Role '$ROLE_NAME' created and policy attached."

# Create IAM User
echo "Creating IAM User..."
USER_ARN=$(awslocal --endpoint-url=${LOCALSTACK_HOST} iam create-user --user-name $USER_NAME | jq -r '.User.Arn')
echo "User '$USER_NAME' created with ARN: $USER_ARN"

# Create AssumeRole Policy for the User
echo "Creating AssumeRole Policy for the User..."
ASSUME_ROLE_POLICY_ARN=$(awslocal --endpoint-url=${LOCALSTACK_HOST} iam create-policy \
    --policy-name "AllowAssumeRole_$ROLE_NAME" \
    --policy-document '{
        "Version": "2012-10-17",
        "Statement": [
            {
                "Effect": "Allow",
                "Action": "sts:AssumeRole",
                "Resource": "'"$ROLE_ARN"'"
            }
        ]
    }' | jq -r '.Policy.Arn')
echo "AssumeRole policy created with ARN: $ASSUME_ROLE_POLICY_ARN"

# Attach the AssumeRole Policy to the User
echo "Attaching AssumeRole Policy to the User..."
awslocal --endpoint-url=${LOCALSTACK_HOST} iam attach-user-policy --user-name $USER_NAME --policy-arn $ASSUME_ROLE_POLICY_ARN
echo "AssumeRole policy attached to user '$USER_NAME'."

# Assume IAM Role to get temporary credentials
echo "Assuming IAM Role to get temporary credentials..."
CREDS=$(awslocal --endpoint-url=${LOCALSTACK_HOST} sts assume-role \
    --role-arn $ROLE_ARN \
    --role-session-name $SESSION_NAME | jq -r '.Credentials')

ACCESS_KEY=$(echo $CREDS | jq -r '.AccessKeyId')
SECRET_KEY=$(echo $CREDS | jq -r '.SecretAccessKey')
SESSION_TOKEN=$(echo $CREDS | jq -r '.SessionToken')
EXPIRATION=$(echo $CREDS | jq -r '.Expiration')

echo "Temporary credentials obtained:"
echo "Access Key: $ACCESS_KEY"
echo "Secret Access Key: $SECRET_KEY"
echo "Session Token: $SESSION_TOKEN"
echo "Expiration: $EXPIRATION"

# Create access key for the user
echo "Creating access key for user '$USER_NAME'..."
ACCESS_KEY_INFO=$(awslocal --endpoint-url=${LOCALSTACK_HOST} iam create-access-key --user-name $USER_NAME)

# Extract and output the credentials
echo "AWS_ACCESS_KEY_ID=$(echo $ACCESS_KEY_INFO | jq -r '.AccessKey.AccessKeyId')" > /tmp/aws_credentials
echo "AWS_SECRET_ACCESS_KEY=$(echo $ACCESS_KEY_INFO | jq -r '.AccessKey.SecretAccessKey')" >> /tmp/aws_credentials

echo "Access key created and credentials saved to /tmp/aws_credentials"
echo "Setup script completed."