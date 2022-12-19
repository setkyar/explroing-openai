import openai
import os
import sys

import argparse
from dotenv import load_dotenv

load_dotenv()

openai.api_key = os.getenv("OPENAI_API_KEY")

if len(sys.argv) < 3:
    print("Please choose optons: --ask or --grammar_check")
    sys.exit(1)

parser = argparse.ArgumentParser()

parser.add_argument("--ask", help="Ask a question")
parser.add_argument("--grammar_check", help="Check grammar")

args = parser.parse_args()

if args.ask:
    question = args.ask

if args.grammar_check:
    question = "check grammar, print out old and correct sentence and explain the mistakes..." + args.grammar_check

response = openai.Completion.create(
    engine="text-davinci-003",
    prompt=question,
    max_tokens=1024,
    temperature=0.5,
)
print(response["choices"][0]["text"])