import openai
import os
import sys
from dotenv import load_dotenv
from colored import fg, bg, attr

def main():
  # check if min length is 2
  if len(sys.argv) < 2:
    print("Usage: python main.py 'sentence'")
    return

  sentence = sys.argv[1]

  # Load the environment variables from the .env file
  load_dotenv()

  # Set up the OpenAI API client
  openai.api_key = os.environ.get('OPENAI_API_KEY')

  # Check the grammar of the given sentence
  check_grammar(sentence)

def check_grammar(sentence):
  # Use the OpenAI language model to check the grammar of the sentence
  response = openai.Completion.create(
      engine="text-davinci-002",
      prompt=f"Please correct the following sentence: {sentence}",
      temperature=0.1,
      max_tokens=1024,
      top_p=1,
      frequency_penalty=0,
      presence_penalty=0
  )

  # Extract the corrected sentence from the response
  corrected_sentence = response["choices"][0]["text"]

  print("Original:", fg('red'), sentence, attr('reset'))
  print("Corrected:", fg('green'), corrected_sentence, attr('reset'))

if __name__ == "__main__":
  main()
