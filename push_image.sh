#!/bin/zsh
aws ecr get-login-password --region us-east-1 | docker login --username AWS --password-stdin 518240442847.dkr.ecr.us-east-1.amazonaws.com
docker push 518240442847.dkr.ecr.us-east-1.amazonaws.com/summarizer-translator:latest