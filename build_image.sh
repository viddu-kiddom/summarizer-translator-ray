#!/bin/zsh
docker build -t summarizer-translator .
docker tag summarizer-translator:latest 518240442847.dkr.ecr.us-east-1.amazonaws.com/summarizer-translator:latest