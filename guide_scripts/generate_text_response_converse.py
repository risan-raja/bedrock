import boto3
from botocore.exceptions import ClientError

# Create an Amazon Bedrock Runtime client.
brt = boto3.client("bedrock-runtime")

# Set the model ID, e.g., Amazon Titan Text G1 - Express.
model_id = "amazon.titan-text-express-v1"

inference_config = {
     'maxTokens': 512,
     'temperature': 0.5,
     'topP': 0.9
}
performanceConfig={
    'latency': 'standard'
}
# Start a conversation with the user message.
user_message = "Describe the purpose of a 'hello world' program in one line."
conversation = [
    {
        "role": "user",
        "content": [{"text": user_message}],
    },
    {
        "role": "assistant",
        "content": [{"text": "A 'hello world' program demonstrates the basic syntax of a programming language."}],
    },
    {
        "role": "user",
        "content": [{"text": "What is the purpose of a 'hello world' program in Python?"}],
    },
]

try:
    response = brt.converse(
        modelId=model_id,
        messages=conversation,
        inferenceConfig=inference_config,
        performanceConfig=performanceConfig,
    )
    response_text = response["output"]["message"]["content"][0]["text"]
    print(response_text)
except ClientError as e:
    print(f"An error occurred: {e}")
