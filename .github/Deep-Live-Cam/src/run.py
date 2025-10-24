import argparse
import os
import sys
from utils.helpers import load_model, preprocess_input, postprocess_output

def main(execution_provider):
    # Load the model
    model = load_model(execution_provider)

    # Preprocess input data
    input_data = preprocess_input()

    # Run the model
    output_data = model(input_data)

    # Postprocess the output
    results = postprocess_output(output_data)

    # Display results
    print("Results:", results)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Run the deep learning model.")
    parser.add_argument('--execution-provider', type=str, default='none', help='Execution provider to use (e.g., cuda, coreml, directml, openvino)')
    args = parser.parse_args()

    main(args.execution_provider)