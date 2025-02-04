import os
from pathlib import Path
import re
import shutil
import hashlib
import logging
from typing import Set, Dict, List
import json

class MikroTikContentCleaner:
    def __init__(self, input_dir: str, output_dir: str):
        self.input_dir = Path(input_dir)
        self.output_dir = Path(output_dir)
        self.file_hashes = {}  # Track file hashes to detect duplicates
        
        # Setup logging
        logging.basicConfig(
            level=logging.INFO,
            format='%(asctime)s - %(levelname)s - %(message)s',
            handlers=[
                logging.FileHandler('mikrotik_content_cleaning.log'),
                logging.StreamHandler()
            ]
        )
        
        # Patterns to identify MikroTik-specific content
        self.mikrotik_patterns = {
            'config': ['.rsc', '.conf', '.backup'],
            'script': ['.py', '.sh', '.js', '.php'],
            'documentation': ['.md', '.txt'],
        }
        
        # Important file patterns
        self.important_patterns = [
            r'routeros',
            r'mikrotik',
            r'winbox',
            r'ros\b',
            r'\/ip\b',
            r'\/interface\b',
            r'\/system\b',
            r'\/tool\b'
        ]
        
        # Categories for organizing content
        self.categories = {
            'networking': [
                'interface', 'bridge', 'vlan', 'routing', 'firewall', 
                'nat', 'dhcp', 'dns', 'vpn', 'wireless'
            ],
            'security': [
                'firewall', 'certificate', 'ipsec', 'authentication',
                'encryption', 'radius'
            ],
            'automation': [
                'script', 'scheduler', 'backup', 'monitoring', 'api'
            ],
            'management': [
                'user', 'group', 'password', 'identity', 'logging'
            ]
        }

    def get_file_hash(self, file_path: Path) -> str:
        """Calculate the MD5 hash of the content of a file.

        This function opens a file in binary mode, reads its content, and
        computes the MD5 hash. The resulting hash can be used to identify
        duplicate files based on their content.

        Args:
            file_path (Path): The path to the file for which the hash is to be calculated.

        Returns:
            str: The MD5 hash of the file content as a hexadecimal string.
        """
        with open(file_path, 'rb') as f:
            return hashlib.md5(f.read()).hexdigest()

    def is_mikrotik_related(self, file_path: Path, content: str) -> bool:
        """Check if file content is MikroTik-related.

        This function determines whether the provided file content or its
        filename indicates a relation to MikroTik products. It checks for
        specific patterns in the filename and the content of the file. If any of
        the patterns are found, the function returns True; otherwise, it returns
        False.

        Args:
            file_path (Path): The path of the file to check.
            content (str): The content of the file as a string.

        Returns:
            bool: True if the file or its content is related to MikroTik,
                False otherwise.
        """
        # Check filename patterns
        if any(file_path.name.lower().find(pattern) != -1 
               for pattern in ['mikrotik', 'routeros', 'ros', 'winbox']):
            return True
            
        # Check content patterns
        return any(re.search(pattern, content, re.IGNORECASE) 
                  for pattern in self.important_patterns)

    def categorize_content(self, content: str) -> List[str]:
        """Determine categories for the given content based on predefined keywords.

        This function analyzes the input content and assigns it to one or more
        categories based on the presence of specific keywords. It checks each
        category's keywords against the content (case insensitive) and returns a
        list of matching categories. If no categories match, it defaults to
        returning 'uncategorized'.

        Args:
            content (str): The content to be categorized.

        Returns:
            List[str]: A list of categories that match the content, or ['uncategorized']
            if no matches are found.
        """
        categories = []
        for category, keywords in self.categories.items():
            if any(keyword in content.lower() for keyword in keywords):
                categories.append(category)
        return categories or ['uncategorized']

    def clean_and_organize_content(self):
        """Clean and organize MikroTik content from input directories.

        This function processes each repository in the input directory, cleaning
        and organizing MikroTik-related files into categorized output
        directories. It creates a directory structure based on predefined
        categories, reads the content of each file, checks for duplicates, and
        saves the files in their respective categories. A summary of the
        processing results, including the number of processed, duplicate, and
        organized files, is generated and saved as a JSON file.
        """
        processed_files = 0
        duplicate_files = 0
        organized_files = 0

        # Create output directory structure
        for category in self.categories.keys():
            (self.output_dir / category).mkdir(parents=True, exist_ok=True)

        # Process each repository
        for repo_dir in self.input_dir.iterdir():
            if not repo_dir.is_dir():
                continue

            logging.info(f"Processing repository: {repo_dir.name}")

            try:
                # Process files in repository
                for file_path in repo_dir.rglob('*'):
                    if not file_path.is_file():
                        continue

                    processed_files += 1
                    
                    try:
                        # Read file content
                        with open(file_path, 'r', encoding='utf-8') as f:
                            content = f.read()
                        
                        # Skip if not MikroTik related
                        if not self.is_mikrotik_related(file_path, content):
                            continue

                        # Check for duplicates
                        file_hash = self.get_file_hash(file_path)
                        if file_hash in self.file_hashes:
                            duplicate_files += 1
                            continue
                        self.file_hashes[file_hash] = file_path

                        # Determine categories
                        categories = self.categorize_content(content)
                        
                        # Save file in appropriate categories
                        for category in categories:
                            output_path = self.output_dir / category / f"{repo_dir.name}_{file_path.name}"
                            shutil.copy2(file_path, output_path)
                            organized_files += 1

                    except Exception as e:
                        logging.error(f"Error processing file {file_path}: {str(e)}")

            except Exception as e:
                logging.error(f"Error processing repository {repo_dir}: {str(e)}")

        # Generate summary
        summary = {
            'processed_files': processed_files,
            'duplicate_files': duplicate_files,
            'organized_files': organized_files,
            'categories': {cat: len(list((self.output_dir / cat).glob('*'))) 
                         for cat in self.categories.keys()}
        }

        # Save summary
        with open(self.output_dir / 'cleaning_summary.json', 'w') as f:
            json.dump(summary, f, indent=2)

        logging.info("\nCleaning Summary:")
        logging.info(f"Total files processed: {processed_files}")
        logging.info(f"Duplicate files skipped: {duplicate_files}")
        logging.info(f"Files organized: {organized_files}")
        for category, count in summary['categories'].items():
            logging.info(f"{category}: {count} files")

if __name__ == "__main__":
    input_directory = r"C:\Users\Vivek\Documents\MikroTik_dis\Scraped_Data\gitlab_repos"
    output_directory = r"C:\Users\Vivek\Documents\MikroTik_dis\cleaned_data\gitlab_repos"
    
    cleaner = MikroTikContentCleaner(input_directory, output_directory)
    cleaner.clean_and_organize_content()