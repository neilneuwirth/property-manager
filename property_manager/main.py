from openai import OpenAI
import instructor
import json
from property_manager.schema.task import TaskRequest

client = instructor.patch(OpenAI())

SYSTEM_PROMPT = """
You are virtual property manager that received a maintenance request from a tenant. 

Given the maintenance request context you will: 
1. Determine what is the most appropiate values to map. 
2. Truly analuze the context of what the tenant inputs for classification and conservatively assign values.
3. Always translate the information to English. 

Think step-by-step
"""


def convert_to_service_order(
    service_order_details,
    response_model=TaskRequest,
    system_prompt: str = SYSTEM_PROMPT,
    model: str = "gpt-4",
):
    response = client.chat.completions.create(
        model=model,
        response_model=response_model,
        temperature=0,
        messages=[
            {
                "role": "system",
                "content": system_prompt,
            },
            {
                "role": "user",
                "content": service_order_details,
            },
        ],
    )
    return json.loads(response.model_dump_json(by_alias=True))
