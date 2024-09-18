import openai
from openai.error import RateLimitError, APIError

# Set your API key
openai.api_key = 'sk-6svO17K7-PNBZFAn3VgO87QAsgjmG9eIuSFLvbC8nsT3BlbkFJ39RFH3JuerMi2maL5k2wapFx6_NDZ2XK60al4mo_sA'

try:
    # Make a chat completion request
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": "Write an email to my boss for sick leave, my boss name: John, my name: Mike"}
        ]
    )

    # Extract the message content from the response
    message = response.choices[0].message['content']
    print(message)

except RateLimitError:
    print("You have exceeded your current quota. Please check your plan and billing details.")
except APIError as e:
    print(f"An API error occurred: {e}")
