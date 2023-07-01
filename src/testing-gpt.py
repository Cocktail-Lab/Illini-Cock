import openai

# Set up your OpenAI API key
api_key = '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'

# Set up the OpenAI API client
openai.api_key = api_key

# Provide a question as a prompt
question = "What is the capital of France?"

# Generate a response from the API
response = openai.Completion.create(
  engine='text-davinci-003',
  prompt=question,
  max_tokens=100,
  n=1,
  stop=None,
  temperature=0.7,
)

# Extract the generated answer from the response
answer = response.choices[0].text.strip()

# Print the generated answer
print(answer)