from openai_client import generate_response

if __name__ == "__main__":
    print("Sending request to OpenAI...")
    
    # Small, cheap test prompt
    answer = generate_response(
        prompt="In one sentence, what is the primary difference between a generative LLM and a vector database?",
        system_message="You are a highly technical GenAI instructor."
    )
    
    print("\nResponse:")
    print(answer)