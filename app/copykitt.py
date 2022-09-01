from cmd import PROMPT
import os
from urllib import response
import openai
import argparse


def main():
    print("Running Copy Kitt!")

    parser = argparse.ArgumentParser()
    # 1. name of variable that will get the user's argument
    # 2. the parameter
    # 3. value type of the argument
    # 4. whether the argument is required or not
    parser.add_argument("--input", "-i", type=str, required=True)
    args = parser.parse_args()
    user_input = args.input

    print(f"User Input:: {user_input}")
    pass


# # Load API Key into environment variable
# openai.api_key = os.getenv(
#     "OPENAI_API_KEY")

# subject = "coffee"
# prompt = f"Generate upbeat branding snippet for {subject}"

# response = openai.Completion.create(
#     engine="text-davinci-002", prompt=prompt, max_tokens=36)

# print(response)

if __name__ == "__main__":
    main()
