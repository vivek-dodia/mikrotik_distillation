import re
from dataclasses import dataclass
from typing import List, Optional
import os
from pathlib import Path
import logging

# Set up logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('pdf_doc_cleaner.log'),
        logging.StreamHandler()
    ]
)

def clean_code_block(text: str) -> str:
    """Clean up code blocks while preserving structure.

    This function takes a string containing code blocks and cleans it up by
    removing unnecessary whitespace while preserving the original structure
    of the code. It ensures that lines starting with specific prefixes are
    retained as they are, and it formats the output as a proper markdown
    code block if it is not already formatted.

    Args:
        text (str): The input string containing code blocks to be cleaned.

    Returns:
        str: The cleaned and properly formatted code block as a string.
    """
    if not text.strip():
        return ""
    
    # Clean up the code block content
    lines = text.split('\n')
    cleaned_lines = []
    for line in lines:
        # Preserve exact spacing for console outputs
        if '[admin@' in line or line.startswith('/'):
            cleaned_lines.append(line.rstrip())
        else:
            cleaned_lines.append(line.rstrip())
    
    # Ensure proper markdown code block formatting
    text = '\n'.join(cleaned_lines)
    if not text.startswith('```'):
        text = f'```\n{text}\n```'
    
    return text

def clean_property_table(text: str) -> str:
    """Format property description tables.

    This function takes a string containing property descriptions formatted
    in a specific way, and cleans it up by organizing the properties and
    their descriptions into a more readable format. It identifies new
    property definitions based on the presence of parentheses and the
    keyword 'Default:', and collects the associated descriptions. The
    cleaned output is returned as a single string with properties bolded and
    separated by new lines.

    Args:
        text (str): A string containing property descriptions, each potentially spanning
            multiple lines.

    Returns:
        str: A formatted string with cleaned property descriptions.
    """
    lines = text.split('\n')
    cleaned_lines = []
    current_property = []
    
    for line in lines:
        if '(' in line and ')' in line and 'Default:' in line:
            # New property definition
            if current_property:
                cleaned_lines.extend(current_property)
                cleaned_lines.append('')
                current_property = []
            current_property = [f"**{line.strip()}**"]
        elif line.strip() and current_property:
            # Property description
            current_property.append(line.strip())
        elif not line.strip() and current_property:
            # End of property description
            cleaned_lines.extend(current_property)
            cleaned_lines.append('')
            current_property = []
    
    # Add any remaining property
    if current_property:
        cleaned_lines.extend(current_property)
    
    return '\n'.join(cleaned_lines)

def clean_text(content: str) -> str:
    """Clean and format the documentation text.

    This function processes the input documentation text by extracting code
    blocks, cleaning up sections, and formatting property tables. It
    identifies code blocks enclosed in triple backticks and replaces them
    with placeholders. The function then splits the content into sections
    based on headers, cleans each section by removing unnecessary
    whitespace, and formats property tables if present. Finally, it restores
    the original code blocks in their respective locations.

    Args:
        content (str): The documentation text to be cleaned and formatted.

    Returns:
        str: The cleaned and formatted documentation text.
    """
    # Extract and save code blocks
    code_blocks = []
    def save_code_block(match):
        """Save a code block from a regex match.

        This function extracts a code block from a regex match object, strips
        any leading or trailing whitespace, and appends it to a list of code
        blocks. It returns a placeholder string that represents the index of the
        saved code block. If the extracted code block is empty, it returns an
        empty string.

        Args:
            match (re.Match): A regex match object containing the code block.

        Returns:
            str: A placeholder string for the saved code block or an empty string if no
                code was found.
        """

        code = match.group(1).strip()
        if code:
            code_blocks.append(code)
            return f"__CODE_BLOCK_{len(code_blocks)-1}__"
        return ""
    
    content = re.sub(r'```(.*?)```', save_code_block, content, flags=re.DOTALL)
    
    # Split into sections
    sections = re.split(r'(?=^# )', content, flags=re.MULTILINE)
    cleaned_sections = []
    
    for section in sections:
        if not section.strip():
            continue
        
        # Process section content
        lines = section.split('\n')
        cleaned_lines = []
        in_property_table = False
        property_lines = []
        
        for line in lines:
            # Handle property tables
            if ('Property Description' in line) or in_property_table:
                in_property_table = True
                if line.strip():
                    property_lines.append(line)
                continue
            elif in_property_table and not line.strip():
                in_property_table = False
                if property_lines:
                    cleaned_lines.append(clean_property_table('\n'.join(property_lines)))
                    property_lines = []
            
            # Clean normal lines
            if line.strip():
                # Handle headers
                if line.startswith('#'):
                    cleaned_lines.append('\n' + line)
                # Handle list items
                elif line.lstrip().startswith('*') or line.lstrip().startswith('-'):
                    cleaned_lines.append(line.strip())
                # Handle normal text
                else:
                    cleaned_lines.append(line.strip())
        
        # Add any remaining property lines
        if property_lines:
            cleaned_lines.append(clean_property_table('\n'.join(property_lines)))
        
        # Add section to cleaned content
        cleaned_sections.append('\n'.join(cleaned_lines))
    
    # Join sections
    content = '\n\n'.join(cleaned_sections)
    
    # Restore code blocks
    for i, block in enumerate(code_blocks):
        content = content.replace(f"__CODE_BLOCK_{i}__", clean_code_block(block))
    
    return content

def process_file(input_file: str, output_file: str):
    """Process a single documentation file.

    This function reads the content of the specified input file, cleans the
    text using a helper function, and writes the cleaned content to the
    specified output file. It handles file operations and ensures that any
    errors encountered during the process are logged.

    Args:
        input_file (str): The path to the input file that needs to be processed.
        output_file (str): The path to the output file where cleaned content will be written.

    Returns:
        bool: True if the file was processed successfully, False otherwise.
    """
    try:
        # Read input file
        with open(input_file, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Clean the content
        cleaned_content = clean_text(content)
        
        # Write output
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(cleaned_content)
        
        return True
    except Exception as e:
        logging.error(f"Error processing file {input_file}: {str(e)}")
        return False

def process_directory(input_dir: str, output_dir: str):
    """Process all markdown files in the directory.

    This function scans the specified input directory for all markdown files
    and processes each file by cleaning its content. The cleaned files are
    saved in the specified output directory with a prefix "cleaned_". It
    logs the processing summary, including the total number of files
    processed, the number of successfully cleaned files, and the number of
    files that failed to process.

    Args:
        input_dir (str): The path to the input directory containing markdown files.
        output_dir (str): The path to the output directory where cleaned files will be saved.

    Returns:
        tuple: A tuple containing two integers:
            - The number of successfully cleaned files.
            - The number of files that failed to process.
    """
    input_path = Path(input_dir)
    output_path = Path(output_dir)
    output_path.mkdir(parents=True, exist_ok=True)
    
    total_files = 0
    successful_files = 0
    failed_files = 0
    
    for md_file in input_path.glob('**/*.md'):
        total_files += 1
        try:
            output_file = output_path / f"cleaned_{md_file.name}"
            
            if process_file(str(md_file), str(output_file)):
                successful_files += 1
                if successful_files % 10 == 0:
                    logging.info(f"Processed {successful_files} files successfully...")
            else:
                failed_files += 1
        except Exception as e:
            failed_files += 1
            logging.error(f"Error processing {md_file.name}: {str(e)}")
    
    logging.info("\nProcessing Summary:")
    logging.info(f"Total files processed: {total_files}")
    logging.info(f"Successfully cleaned: {successful_files}")
    logging.info(f"Failed to process: {failed_files}")
    
    return successful_files, failed_files

if __name__ == "__main__":
    input_directory = r"C:\Users\Vivek\Documents\MikroTik_dis\Scraped_Data\processed_pdf"
    output_directory = r"C:\Users\Vivek\Documents\MikroTik_dis\cleaned_data\processed_pdf"
    
    logging.info("Starting PDF documentation cleaning process...")
    successful, failed = process_directory(input_directory, output_directory)
    logging.info("Cleaning process completed!")