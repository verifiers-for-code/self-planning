import json
import argparse
import os

def insert_output_into_docstring(prompt, output):
    # Find the end of the docstring
    docstring_start = prompt.find('"""')
    docstring_end = prompt.find('"""', docstring_start + 3)
    
    # If there's no docstring or it's malformed, return the original prompt
    if docstring_end == -1:
        return prompt
    
    # Append the output text as is
    output_text = "\n\n" + output
    
    return prompt[:docstring_end] + output_text + prompt[docstring_end:]

def process_item(item):
    new_prompt = insert_output_into_docstring(item['prompt'], item['output'])
    item['cleaned-output'] = new_prompt  # Add the new 'cleaned-output' field
    return item

def main(input_file_path):
    # Load input JSON file
    with open(input_file_path, 'r') as f:
        data = json.load(f)
    
    # Process each item in the dataset
    processed_data = [process_item(item) for item in data]
    
    # Create the output file path
    dir_name = os.path.dirname(input_file_path)
    base_name = os.path.basename(input_file_path)
    output_file_path = os.path.join(dir_name, "cleaned-" + base_name)
    
    # Save processed data to new JSON file as a list
    with open(output_file_path, 'w') as f:
        json.dump(processed_data, f, indent=2)
    
    print(f"Processed data saved to {output_file_path}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Process JSON file and append output to prompts.")
    parser.add_argument('--input_file', type=str, required=True, help="Path to the input JSON file")
    args = parser.parse_args()
    
    main(args.input_file)