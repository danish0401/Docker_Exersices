#!/bin/sh
aws configure set aws_access_key_id $ACCESS_KEY_ID;aws configure set aws_secret_access_key $SECRET_ACCESS_KEY;aws configure set default.region $DEFAULT_REGION;aws s3 ls;