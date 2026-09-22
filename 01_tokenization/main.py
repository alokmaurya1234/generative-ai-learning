import tiktoken


enc = tiktoken.encoding_for_model("gpt-4o")

text = "Hey There! My name is Alok Maurya"

tokens = enc.encode(text)

print("Tokens:", tokens)