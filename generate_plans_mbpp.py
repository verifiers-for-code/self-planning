import os
import json
import time
from vllm import LLM, SamplingParams

# Define variables
MODEL_NAME = "phi3_mini"
MODEL = "microsoft/Phi-3-mini-4k-instruct"
TEMPERATURE = 0.0
JSON_INPUT_FILENAME = "jsons/eval_prompts_mbpp.json"
JSON_OUTPUT_FILENAME = f"jsons/{MODEL_NAME}_self_plans_mbpp.json"
FEW_SHOT_ROOT = "./few_shot/mbpp/"

def read_text_file(file_path):
    with open(file_path, "r", encoding="utf-8") as file:
        return file.read()

def create_prompts(prompts, tokenizer):
    few_shot_messages = [
        message
        for i in range(1, 9)
        for message in [
            {"role": "user", "content": read_text_file(f"{FEW_SHOT_ROOT}example_{i}_input.txt")},
            {"role": "assistant", "content": read_text_file(f"{FEW_SHOT_ROOT}example_{i}_output.txt")}
        ]
    ]

    formatted_prompts = []
    for prompt in prompts:
        messages = few_shot_messages + [{"role": "user", "content": prompt}]
        x = tokenizer.apply_chat_template(messages, tokenize=False, add_generation_prompt=True)
        formatted_prompts.append(x)
    return formatted_prompts

def main():
    # Initialize vLLM and tokenizer
    llm = LLM(model=MODEL, tensor_parallel_size=1, gpu_memory_utilization=0.93)
    tokenizer = llm.get_tokenizer()
    sampling_params = SamplingParams(temperature=TEMPERATURE, max_tokens=2048)

    # Load prompts from JSON file
    with open(JSON_INPUT_FILENAME, 'r', encoding="utf-8") as f:
        eval_prompts = json.load(f)
    prompts = [item['prompt'] for item in eval_prompts]
    task_ids = [item['task_id'] for item in eval_prompts]

    formatted_prompts = create_prompts(prompts, tokenizer)

    # Print the first prompt exactly as it is sent to the model
    print("First prompt sent to the model:")
    print(json.dumps(formatted_prompts[0], indent=2, ensure_ascii=False))

    print(f"Processing {len(formatted_prompts)} prompts in a single batch...")
    outputs = llm.generate(formatted_prompts, sampling_params)

    results = [
        {
            'task_id': str(task_id),
            'prompt': prompt,
            'output': output.outputs[0].text
        }
        for task_id, prompt, output in zip(task_ids, prompts, outputs)
    ]

    # Save results to JSON file
    try:
        with open(JSON_OUTPUT_FILENAME, "w", encoding="utf-8") as f:
            json.dump(results, f, indent=2, ensure_ascii=False)
        print(f"Successfully saved results to {JSON_OUTPUT_FILENAME}")
    except Exception as e:
        print(f"Failed to save results to disk: {e}")

if __name__ == "__main__":
    main()