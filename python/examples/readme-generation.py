import yaml
import argparse
import os
from jinja2 import Environment, FileSystemLoader

# Set up command-line argument parsing
parser = argparse.ArgumentParser(description='Generate a README from a model YAML file.')
parser.add_argument('yaml_file', type=str, help='The path to the YAML file.')
parser.add_argument('output_dir', type=str, help='The directory to write the output README file.')
args = parser.parse_args()

# Load the YAML file
with open(args.yaml_file, 'r') as file:
    model = yaml.safe_load(file)

# Get the directory containing this script
script_dir = os.path.dirname(__file__)

# Construct the path to the template file
template_path = os.path.join(script_dir, '..', '..', 'templates', 'docs')

# Set up the Jinja environment and load the template
env = Environment(loader=FileSystemLoader(template_path))
template = env.get_template('readme.jinja')

# Render the template with the model as context
readme = template.render(model=model)

# Create the output directory if it doesn't exist
os.makedirs(args.output_dir, exist_ok=True)

# Write the rendered template to readme.md in the output directory
with open(os.path.join(args.output_dir, 'readme.md'), 'w') as file:
    file.write(readme)