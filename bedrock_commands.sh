#!/bin/bash


# This script demonstrates how to use the AWS CLI to interact with Amazon Bedrock.
# aws bedrock-runtime invoke-model \
# --model-id amazon.titan-text-express-v1 \
# --body '{"inputText": "Describe the purpose of a \"hello world\" program in one line.",
# "textGenerationConfig" : {"maxTokenCount": 512, "temperature": 0.5, "topP": 0.9}}' \
# --cli-binary-format raw-in-base64-out \
# invoke-model-output-text.json

# echo $(cat invoke-model-output-text.json)

# rm invoke-model-output-text.json

# AWS bedrock Converse command

aws bedrock-runtime converse \
--model-id amazon.titan-text-express-v1 \
--messages '[{"role": "user", "content": [{"text": "Describe the purpose of a \"hello world\" program in one line."}]}]' \
--inference-config '{"maxTokens": 512, "temperature": 0.5, "topP": 0.9}' \
--cli-binary-format raw-in-base64-out \
--color on \
--output yaml