import os
from pathlib import Path
from collections import defaultdict
import logging
import json
from typing import Dict, List, Set, Tuple
import re

# Set up logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('repo_analysis.log'),
        logging.StreamHandler()
    ]
)

class RepoAnalyzer:
    def __init__(self, base_dir: str):
        self.base_dir = Path(base_dir)
        self.file_types = defaultdict(int)
        self.doc_files = defaultdict(int)
        self.code_files = defaultdict(int)
        self.config_files = defaultdict(int)
        self.repo_stats = defaultdict(dict)
        self.total_size = 0
        self.total_files = 0
        
        # Common file patterns
        self.doc_patterns = {'.md', '.rst', '.txt', '.doc', '.docx', '.pdf'}
        self.code_patterns = {'.py', '.js', '.java', '.cpp', '.c', '.h', '.go', '.rs', '.rb', '.php', '.sh'}
        self.config_patterns = {'.yml', '.yaml', '.json', '.toml', '.ini', '.cfg', '.conf'}
        
    def is_git_repo(self, path: Path) -> bool:
        """Check if a directory is a Git repository.

        This function determines whether the specified directory contains a
        `.git` folder, which is indicative of a Git repository. It constructs
        the path to the `.git` directory and checks for its existence.

        Args:
            path (Path): The path to the directory to check.

        Returns:
            bool: True if the directory is a Git repository, False otherwise.
        """
        return (path / '.git').exists()
    
    def get_file_category(self, file_path: Path) -> str:
        """Determine the category of a file based on its extension and name.

        This function analyzes the provided file path to determine its category.
        It first checks for special file names such as 'README.md', 'LICENSE',
        and 'CHANGELOG'. If none of these match, it then checks the file
        extension against predefined patterns for documentation, code, test, and
        configuration files. If the file does not match any known categories, it
        defaults to 'other'.

        Args:
            file_path (Path): The path of the file to categorize.

        Returns:
            str: The category of the file, which can be one of
                'readme', 'license', 'changelog', 'documentation',
                'code', 'test', 'config', or 'other'.
        """
        extension = file_path.suffix.lower()
        path_str = str(file_path).lower()
        
        # Check special files first
        if file_path.name.lower() == 'readme.md':
            return 'readme'
        elif 'license' in file_path.name.lower():
            return 'license'
        elif 'changelog' in file_path.name.lower():
            return 'changelog'
        
        # Check by extension
        if extension in self.doc_patterns:
            return 'documentation'
        elif extension in self.code_patterns:
            if 'test' in path_str:
                return 'test'
            else:
                return 'code'
        elif extension in self.config_patterns:
            return 'config'
        
        return 'other'
    
    def analyze_repo(self, repo_path: Path) -> dict:
        """Analyze a single repository.

        This function inspects the specified repository to gather various
        statistics, including the total number of files, total size of files,
        types of files, categories of files, and whether the repository contains
        documentation files, tests, and CI/CD configurations. It traverses the
        repository directory, skipping any contents within the `.git` directory,
        and aggregates the relevant information into a dictionary.

        Args:
            repo_path (Path): The path to the repository to be analyzed.

        Returns:
            dict: A dictionary containing statistics about the repository, including:
                - total_files (int): The total number of files in the repository.
                - total_size (int): The total size of all files in bytes.
                - file_types (defaultdict): A dictionary mapping file extensions to
                their counts.
                - categories (defaultdict): A dictionary mapping file categories to
                their counts.
                - doc_files (list): A list of documentation file paths relative to the
                repository.
                - main_language (str or None): The primary programming language used in
                the repository.
                - has_tests (bool): Indicates if the repository contains test files.
                - has_ci (bool): Indicates if the repository has CI/CD configuration
                files.
        """
        repo_stats = {
            'total_files': 0,
            'total_size': 0,
            'file_types': defaultdict(int),
            'categories': defaultdict(int),
            'doc_files': [],
            'main_language': None,
            'has_tests': False,
            'has_ci': False
        }
        
        # Check for CI/CD configuration
        ci_paths = [
            repo_path / '.github' / 'workflows',
            repo_path / '.gitlab-ci.yml',
            repo_path / 'Jenkinsfile'
        ]
        repo_stats['has_ci'] = any(p.exists() for p in ci_paths)
        
        try:
            for file_path in repo_path.rglob('*'):
                if file_path.is_file():
                    # Skip .git directory contents
                    if '.git' in str(file_path):
                        continue
                    
                    # Update statistics
                    extension = file_path.suffix.lower()
                    size = file_path.stat().st_size
                    category = self.get_file_category(file_path)
                    
                    repo_stats['total_files'] += 1
                    repo_stats['total_size'] += size
                    repo_stats['file_types'][extension] += 1
                    repo_stats['categories'][category] += 1
                    
                    # Track documentation files
                    if category == 'documentation':
                        repo_stats['doc_files'].append(str(file_path.relative_to(repo_path)))
                    
                    # Check for tests
                    if category == 'test':
                        repo_stats['has_tests'] = True
            
            # Determine main language
            code_files = {ext: count for ext, count in repo_stats['file_types'].items() 
                         if ext.lstrip('.') in [p.lstrip('.') for p in self.code_patterns]}
            if code_files:
                repo_stats['main_language'] = max(code_files.items(), key=lambda x: x[1])[0].lstrip('.')
            
        except Exception as e:
            logging.error(f"Error analyzing repo {repo_path}: {str(e)}")
            return None
        
        return repo_stats
    
    def analyze_all_repos(self):
        """Analyze all repositories in the base directory.

        This function traverses the base directory to identify and analyze all
        Git repositories. It counts the total number of repositories, as well as
        the number of successfully processed and failed repositories. For each
        repository found, it logs the analysis process and attempts to gather
        statistics. If the analysis fails for any repository, an error is
        logged, and the failure count is incremented. Finally, a summary of the
        analysis results is generated.
        """
        total_repos = 0
        processed_repos = 0
        failed_repos = 0
        
        # Find all git repositories
        for path in self.base_dir.rglob('*'):
            if path.is_dir() and self.is_git_repo(path):
                total_repos += 1
                repo_name = path.relative_to(self.base_dir)
                logging.info(f"Analyzing repo: {repo_name}")
                
                try:
                    stats = self.analyze_repo(path)
                    if stats:
                        self.repo_stats[str(repo_name)] = stats
                        processed_repos += 1
                    else:
                        failed_repos += 1
                except Exception as e:
                    logging.error(f"Failed to analyze repo {repo_name}: {str(e)}")
                    failed_repos += 1
        
        # Generate summary
        self.generate_summary(total_repos, processed_repos, failed_repos)
    
    def generate_summary(self, total_repos: int, processed_repos: int, failed_repos: int):
        """Generate an analysis summary of repository statistics.

        This method compiles a summary of the repository analysis, including the
        total number of repositories, the number of processed and failed
        repositories, and various aggregate statistics such as total files,
        total size, and the distribution of programming languages used across
        the repositories. The summary is then saved to a JSON file and logged
        for review.

        Args:
            total_repos (int): The total number of repositories found.
            processed_repos (int): The number of repositories successfully analyzed.
            failed_repos (int): The number of repositories that failed to analyze.
        """
        summary = {
            'total_repos': total_repos,
            'processed_repos': processed_repos,
            'failed_repos': failed_repos,
            'repo_statistics': self.repo_stats,
            'aggregate_stats': {
                'total_files': sum(repo['total_files'] for repo in self.repo_stats.values()),
                'total_size': sum(repo['total_size'] for repo in self.repo_stats.values()),
                'repositories_with_docs': sum(1 for repo in self.repo_stats.values() if repo['categories']['documentation'] > 0),
                'repositories_with_tests': sum(1 for repo in self.repo_stats.values() if repo['has_tests']),
                'repositories_with_ci': sum(1 for repo in self.repo_stats.values() if repo['has_ci']),
                'language_distribution': defaultdict(int),
                'file_categories': defaultdict(int)
            }
        }
        
        # Aggregate statistics
        for repo_stats in self.repo_stats.values():
            if repo_stats['main_language']:
                summary['aggregate_stats']['language_distribution'][repo_stats['main_language']] += 1
            for category, count in repo_stats['categories'].items():
                summary['aggregate_stats']['file_categories'][category] += count
        
        # Save summary to file
        with open('repo_analysis_summary.json', 'w') as f:
            json.dump(summary, f, indent=2)
        
        # Log summary info
        logging.info("\nRepository Analysis Summary:")
        logging.info(f"Total repositories found: {total_repos}")
        logging.info(f"Successfully analyzed: {processed_repos}")
        logging.info(f"Failed to analyze: {failed_repos}")
        logging.info(f"\nTop languages:")
        for lang, count in sorted(summary['aggregate_stats']['language_distribution'].items(), 
                                key=lambda x: x[1], reverse=True)[:5]:
            logging.info(f"  {lang}: {count} repos")
        logging.info(f"\nFile categories:")
        for category, count in sorted(summary['aggregate_stats']['file_categories'].items(), 
                                    key=lambda x: x[1], reverse=True):
            logging.info(f"  {category}: {count} files")

if __name__ == "__main__":
    # Analyze GitHub repositories
    github_directory = r"C:\Users\Vivek\Documents\MikroTik_dis\Scraped_Data\github_repos"
    logging.info("\nAnalyzing GitHub repositories...")
    github_analyzer = RepoAnalyzer(github_directory)
    github_analyzer.analyze_all_repos()
    
    # Analyze GitLab repositories
    gitlab_directory = r"C:\Users\Vivek\Documents\MikroTik_dis\Scraped_Data\gitlab_repos"
    logging.info("\nAnalyzing GitLab repositories...")
    gitlab_analyzer = RepoAnalyzer(gitlab_directory)
    gitlab_analyzer.analyze_all_repos()