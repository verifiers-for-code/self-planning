import os
import json
import time
from vllm import LLM, SamplingParams

# os.environ["VLLM_ATTENTION_BACKEND"] = "FLASHINFER"

# Define variables
MODEL_NAME = "gemma2b"
MODEL = "google/gemma-2-2b-it"  # This will be used as the model_path for vLLM
TEMPERATURE = 0.0
JSON_INPUT_FILENAME = "jsons/eval_prompts.json"
JSON_OUTPUT_FILENAME = f"jsons/{MODEL_NAME}_self_plans.json"
FEW_SHOT_ROOT = "./few_shot/"

def read_text_file(file_path):
    with open(file_path, "r", encoding="utf-8") as file:
        return file.read()

def create_prompts(prompts, tokenizer):
    few_shot_messages = [
        {"role": "user", "content": read_text_file(f"{FEW_SHOT_ROOT}example_1_input.txt")},
        {"role": "assistant", "content": read_text_file(f"{FEW_SHOT_ROOT}example_1_output.txt")},
        {"role": "user", "content": read_text_file(f"{FEW_SHOT_ROOT}example_2_input.txt")},
        {"role": "assistant", "content": read_text_file(f"{FEW_SHOT_ROOT}example_2_output.txt")},
        {"role": "user", "content": read_text_file(f"{FEW_SHOT_ROOT}example_3_input.txt")},
        {"role": "assistant", "content": read_text_file(f"{FEW_SHOT_ROOT}example_3_output.txt")},
        {"role": "user", "content": read_text_file(f"{FEW_SHOT_ROOT}example_4_input.txt")},
        {"role": "assistant", "content": read_text_file(f"{FEW_SHOT_ROOT}example_4_output.txt")},
        {"role": "user", "content": read_text_file(f"{FEW_SHOT_ROOT}example_5_input.txt")},
        {"role": "assistant", "content": read_text_file(f"{FEW_SHOT_ROOT}example_5_output.txt")},
        {"role": "user", "content": read_text_file(f"{FEW_SHOT_ROOT}example_6_input.txt")},
        {"role": "assistant", "content": read_text_file(f"{FEW_SHOT_ROOT}example_6_output.txt")},
        {"role": "user", "content": read_text_file(f"{FEW_SHOT_ROOT}example_7_input.txt")},
        {"role": "assistant", "content": read_text_file(f"{FEW_SHOT_ROOT}example_7_output.txt")},
        {"role": "user", "content": read_text_file(f"{FEW_SHOT_ROOT}example_8_input.txt")},
        {"role": "assistant", "content": read_text_file(f"{FEW_SHOT_ROOT}example_8_output.txt")},
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

    formatted_prompts = create_prompts(prompts, tokenizer)

    # Print the first prompt exactly as it is sent to the model
    print("First prompt sent to the model:")
    print(json.dumps(formatted_prompts[0], indent=2, ensure_ascii=False))

    print(f"Processing {len(formatted_prompts)} prompts in a single batch...")
    outputs = llm.generate(formatted_prompts, sampling_params)

    results = [
        {'prompt': prompt, 'output': output.outputs[0].text}
        for prompt, output in zip(prompts, outputs)
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