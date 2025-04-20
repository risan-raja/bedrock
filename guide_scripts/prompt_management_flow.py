# Import Python SDK and create client
import boto3

client = boto3.client(service_name='bedrock-agent')

FLOWS_SERVICE_ROLE = "arn:aws:iam::123456789012:role/MyPromptFlowsRole" # Flows service role that you created. For more information, see https://docs.aws.amazon.com/bedrock/latest/userguide/flows-permissions.html
PROMPT_ARN = prompt_version_arn # ARN of the prompt that you created, retrieved programatically during creation.

# Define each node

# The input node validates that the content of the InvokeFlow request is a JSON object.
input_node = {
    "type": "Input",
    "name": "FlowInput",
    "outputs": [
        {
            "name": "document",
            "type": "Object"
        }
    ]
}

# This prompt node contains a prompt that you defined in Prompt management.
# It validates that the input is a JSON object that minimally contains the fields "genre" and "number", which it will map to the prompt variables.
# The output must be named "modelCompletion" and be of the type "String".
prompt_node = {
    "type": "Prompt",
    "name": "MakePlaylist",
    "configuration": {
        "prompt": {
            "sourceConfiguration": {
                "resource": {
                    "promptArn": ""
                }
            }
        }
    },
    "inputs": [
        {
            "name": "genre",
            "type": "String",
            "expression": "$.data.genre"
        },
        {
            "name": "number",
            "type": "Number",
            "expression": "$.data.number"
        }
    ],
    "outputs": [
        {
            "name": "modelCompletion",
            "type": "String"
        }
    ]
}

# The output node validates that the output from the last node is a string and returns it as is. The name must be "document".
output_node = {
    "type": "Output",
    "name": "FlowOutput",
    "inputs": [
        {
            "name": "document",
            "type": "String",
            "expression": "$.data"
        }
    ]
}

# Create connections between the nodes
connections = []

#   First, create connections between the output of the flow input node and each input of the prompt node
for input in prompt_node["inputs"]:
    connections.append(
        {
            "name": "_".join([input_node["name"], prompt_node["name"], input["name"]]),
            "source": input_node["name"],
            "target": prompt_node["name"],
            "type": "Data",
            "configuration": {
                "data": {
                    "sourceOutput": input_node["outputs"][0]["name"],
                    "targetInput": input["name"]
                }
            }
        }
    )

# Then, create a connection between the output of the prompt node and the input of the flow output node
connections.append(
    {
        "name": "_".join([prompt_node["name"], output_node["name"]]),
        "source": prompt_node["name"],
        "target": output_node["name"],
        "type": "Data",
        "configuration": {
            "data": {
                "sourceOutput": prompt_node["outputs"][0]["name"],
                "targetInput": output_node["inputs"][0]["name"]
            }
        }
    }
)

# Create the flow from the nodes and connections
client.create_flow(
    name="FlowCreatePlaylist",
    description="A flow that creates a playlist given a genre and number of songs to include in the playlist.",
    executionRoleArn=FLOWS_SERVICE_ROLE,
    definition={
        "nodes": [input_node, prompt_node, output_node],
        "connections": connections
    }
)
