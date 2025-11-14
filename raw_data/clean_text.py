#!/usr/bin/env python3
"""
Ultra Clean File Content Extractor
Removes ALL HTML tags, unescapes content, and provides pure clean text
"""
import json
import os
import re
import html
from typing import Dict, List

def install_requirements():
    """Install required packages if not available"""
    try:
        from bs4 import BeautifulSoup
    except ImportError:
        print("📦 Installing BeautifulSoup...")
        os.system("pip3 install beautifulsoup4 lxml")

def ultra_clean_content(content: str, filename: str) -> List[str]:
    """
    Ultra clean content by removing ALL HTML tags, unescaping, and cleaning formatting
    
    Args:
        content (str): Raw file content
        filename (str): Name of the file being processed
        
    Returns:
        List[str]: Ultra clean lines of content
    """
    try:
        from bs4 import BeautifulSoup
        
        # Remove code block markers first
        lines = content.split('\n')
        filtered_lines = []
        skip_mode = False
        
        for line in lines:
            # Skip code block markers
            if line.strip().startswith('```'):
                skip_mode = not skip_mode
                continue
            if skip_mode:
                continue
            filtered_lines.append(line)
        
        content = '\n'.join(filtered_lines)
        
        # For Vue files, extract content from template, script, and style sections
        if filename.endswith('.vue'):
            soup = BeautifulSoup(content, 'html.parser')
            clean_lines = []
            
            # Extract and clean template content
            template = soup.find('template')
            if template:
                template_text = template.get_text(separator='\n', strip=True)
                if template_text.strip():
                    clean_lines.extend(['=== TEMPLATE SECTION ==='])
                    clean_lines.extend([line.strip() for line in template_text.split('\n') if line.strip()])
                    clean_lines.append('')
            
            # Extract and clean script content
            script = soup.find('script')
            if script:
                script_text = script.get_text(separator='\n', strip=True)
                if script_text.strip():
                    clean_lines.extend(['=== SCRIPT SECTION ==='])
                    clean_lines.extend([line.strip() for line in script_text.split('\n') if line.strip()])
                    clean_lines.append('')
            
            # Extract and clean style content
            style = soup.find('style')
            if style:
                style_text = style.get_text(separator='\n', strip=True)
                if style_text.strip():
                    clean_lines.extend(['=== STYLE SECTION ==='])
                    clean_lines.extend([line.strip() for line in style_text.split('\n') if line.strip()])
            
            return clean_lines
        
        # For JS files or other files, clean differently
        else:
            # Remove HTML tags if any
            soup = BeautifulSoup(content, 'html.parser')
            clean_text = soup.get_text()
            
            # Unescape HTML entities
            clean_text = html.unescape(clean_text)
            
            # Split into lines and clean each line
            lines = clean_text.split('\n')
            clean_lines = []
            
            for line in lines:
                # Remove extra whitespace but preserve indentation structure
                cleaned_line = line.rstrip()
                
                # Skip completely empty lines but keep lines with just spaces (for indentation)
                if cleaned_line or (line and line.isspace()):
                    clean_lines.append(cleaned_line)
            
            # Remove empty lines at start and end
            while clean_lines and not clean_lines[0].strip():
                clean_lines.pop(0)
            while clean_lines and not clean_lines[-1].strip():
                clean_lines.pop()
            
            return clean_lines
            
    except Exception as e:
        print(f"⚠️  Ultra cleaning failed for {filename}, using fallback: {e}")
        return fallback_ultra_clean(content)

def fallback_ultra_clean(content: str) -> List[str]:
    """
    Fallback ultra cleaning method
    """
    # Remove HTML tags using regex
    content = re.sub(r'<[^>]+>', '', content)
    
    # Unescape HTML entities
    content = html.unescape(content)
    
    # Remove code block markers
    lines = content.split('\n')
    clean_lines = []
    skip_mode = False
    
    for line in lines:
        if line.strip().startswith('```'):
            skip_mode = not skip_mode
            continue
        if skip_mode:
            continue
        
        # Clean the line
        cleaned_line = line.strip()
        if cleaned_line:  # Only add non-empty lines
            clean_lines.append(cleaned_line)
    
    return clean_lines

def load_text_file(file_path: str) -> str:
    """Load text content from a file"""
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()
        return content
    except Exception as e:
        print(f"❌ Error loading text file {file_path}: {e}")
        raise

def save_json(data: Dict[str, List[str]], file_path: str, indent: int = 2) -> None:
    """Save data to a JSON file"""
    try:
        dir_path = os.path.dirname(file_path)
        if dir_path:
            os.makedirs(dir_path, exist_ok=True)
        
        with open(file_path, 'w', encoding='utf-8') as file:
            json.dump(data, file, indent=indent, ensure_ascii=False)
        print(f"✅ Successfully saved ultra clean JSON to: {file_path}")
    except Exception as e:
        print(f"❌ Error saving JSON: {e}")
        raise



########################################################################################################################################
# Main execution
if __name__ == "__main__":
    print("🧽 Starting ULTRA clean file extraction...")
    print("🎯 Removing ALL HTML tags, unescaping content, cleaning formatting")
    
    # Install requirements if needed
    install_requirements()
    
    # Dictionary to store all ultra clean file contents
    ultra_clean_files_data = {}
    
    # List of files to process
    file_list = [
        "introduction.js",
        "CrunchTime.vue", 
        "Introduction.vue",
        "ProcrastinationHack.vue",
        "StudySkills.vue",
        "TimeManagement.vue"
    ]
    
    # Load each file and store ultra clean content
    for filename in file_list:
        if os.path.exists(filename):
            try:
                raw_content = load_text_file(filename)
                
                print(f"🧽 Ultra cleaning: {filename}")
                ultra_clean_lines = ultra_clean_content(raw_content, filename)
                
                ultra_clean_files_data[filename] = ultra_clean_lines
                print(f"✅ Ultra cleaned {filename} - {len(ultra_clean_lines)} pure lines")
                
            except Exception as e:
                print(f"❌ Failed to ultra clean {filename}: {e}")
        else:
            print(f"⚠️  File not found: {filename}")
    
    # Save the ultra clean data as JSON
    if ultra_clean_files_data:
        output_filename = "ultra_clean_files.json"
        save_json(ultra_clean_files_data, output_filename, indent=2)
        print(f"📁 Successfully saved ultra clean content from {len(ultra_clean_files_data)} files to {output_filename}")
        print("🎉 ULTRA clean extraction complete!")
        
        # Display summary
        print("\n📊 Ultra Clean Content Summary:")
        total_lines = 0
        for filename, lines in ultra_clean_files_data.items():
            line_count = len(lines)
            total_lines += line_count
            print(f"  - {filename}: {line_count} pure lines")
        print(f"\n📝 Total ultra clean lines: {total_lines}")
        
        # Show sample of first file
        if ultra_clean_files_data:
            first_file = list(ultra_clean_files_data.keys())[0]
            first_content = ultra_clean_files_data[first_file]
            print(f"\n📋 Ultra Clean Sample from {first_file} (first 15 lines):")
            for i, line in enumerate(first_content[:15]):
                print(f"  {i+1:2d}: {line}")
            if len(first_content) > 15:
                print(f"  ... and {len(first_content) - 15} more lines")
    else:
        print("❌ No files were processed successfully")
