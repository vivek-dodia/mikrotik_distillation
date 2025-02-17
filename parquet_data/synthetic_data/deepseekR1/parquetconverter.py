import pandas as pd
import yaml
import re
from pathlib import Path
import logging
from typing import Dict, List, Any
from tqdm import tqdm

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

class DeepseekProcessor:
    def __init__(self):
        self.metadata_fields = [
            'topic', 'category', 'version', 'scale', 'level',
            'subnet', 'scenario', 'environment', 'affected_users', 'duration'
        ]

    def process_md_file(self, file_path: Path) -> Dict[str, Any]:
        """Process a single deepseek markdown file"""
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()

            # Extract YAML metadata
            yaml_match = re.match(r'---\n(.*?)\n---\n', content, re.DOTALL)
            metadata = yaml.safe_load(yaml_match.group(1)) if yaml_match else {}
            
            # Split content into prompt and solution
            remaining_content = content.split('---\n', 2)[-1]
            sections = remaining_content.split('# Troubleshooting Guide', 1)
            
            prompt = sections[0].replace('# Analysis Process\n', '').strip()
            solution = sections[1].strip() if len(sections) > 1 else ''

            # Create record
            record = {
                # Key metadata fields
                'topic': metadata.get('topic', ''),
                'category': metadata.get('category', ''),
                'version': metadata.get('version', ''),
                'scale': metadata.get('scale', ''),
                'level': metadata.get('level', ''),
                
                # Network specific fields
                'subnet': metadata.get('subnet', ''),
                'scenario': metadata.get('scenario', ''),
                'environment': metadata.get('environment', ''),
                'affected_users': int(metadata.get('affected_users', 0)),
                'duration': metadata.get('duration', ''),
                
                # Content fields
                'prompt': prompt,
                'solution': solution,
                
                # Additional markers
                'has_mermaid': 'mermaid' in solution,
                'has_code_snippets': '```' in solution,
                'filename': file_path.name
            }
            
            return record
            
        except Exception as e:
            logger.error(f"Error processing file {file_path}: {str(e)}")
            return None

def process_directory(input_dir: str, output_file: str):
    """Process all markdown files in directory into parquet dataset"""
    processor = DeepseekProcessor()
    records = []
    input_path = Path(input_dir)
    
    logger.info(f"Processing markdown files from: {input_dir}")
    
    # Process each markdown file
    for md_file in tqdm(list(input_path.glob('*.md'))):
        record = processor.process_md_file(md_file)
        if record:
            records.append(record)
            
    if not records:
        logger.error("No records were processed successfully")
        return
        
    # Convert to DataFrame
    df = pd.DataFrame(records)
    
    # Save to parquet
    output_path = Path(output_file)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    df.to_parquet(output_file, index=False)
    
    # Print statistics
    logger.info(f"\nDataset Creation Summary:")
    logger.info(f"Total scenarios processed: {len(df)}")
    logger.info(f"\nCategories distribution:")
    print(df['category'].value_counts())
    logger.info(f"\nComplexity levels distribution:")
    print(df['level'].value_counts())
    logger.info(f"\nEnvironments distribution:")
    print(df['environment'].value_counts())
    
    logger.info(f"\nDataset saved to: {output_file}")

if __name__ == "__main__":
    input_dir = r"C:\Users\Vivek\Documents\MikroTik_dis\Scraped_Data\synthetic_data\deepseek"
    output_file = r"C:\Users\Vivek\Documents\MikroTik_dis\parquet_data\synthetic_data\deepseekR1\deepseek_dataset.parquet"
    
    try:
        process_directory(input_dir, output_file)
    except Exception as e:
        logger.error(f"Error during processing: {str(e)}", exc_info=True)