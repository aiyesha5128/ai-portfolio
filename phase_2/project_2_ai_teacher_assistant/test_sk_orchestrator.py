from sk_orchestrator import run_prompt

if __name__ == "__main__":
    context = "Algebra uses variables and symbols to represent numbers and relationships."
    question = "Explain algebra in simple terms for a student."

    answer = run_prompt(question, context)
    print("\n--- ANSWER ---\n")
    print(answer)
