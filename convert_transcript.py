"""
Convert interview transcripts from various formats to JSON
Supports: Text files, Otter.ai format, plain Q&A format
"""

import sys
import json
import re
from datetime import datetime

def parse_text_transcript(text_content):
    """Parse a text transcript into structured Q&A pairs."""
    
    # Try different Q&A patterns
    patterns = [
        # Pattern 1: Q: ... A: ...
        r'Q:\s*(.*?)\s*A:\s*(.*?)(?=Q:|$)',
        # Pattern 2: Question: ... Answer: ...
        r'Question:\s*(.*?)\s*Answer:\s*(.*?)(?=Question:|$)',
        # Pattern 3: Interviewer: ... Candidate: ...
        r'Interviewer:\s*(.*?)\s*(?:Candidate|Applicant|Speaker \d):\s*(.*?)(?=Interviewer:|$)',
    ]
    
    qa_pairs = []
    
    for pattern in patterns:
        matches = re.findall(pattern, text_content, re.DOTALL | re.IGNORECASE)
        if matches:
            for question, answer in matches:
                qa_pairs.append({
                    'question': question.strip(),
                    'answer': answer.strip()
                })
            break
    
    # If no pattern matched, try line-by-line
    if not qa_pairs:
        lines = [line.strip() for line in text_content.split('\n') if line.strip()]
        for i in range(0, len(lines) - 1, 2):
            if i + 1 < len(lines):
                qa_pairs.append({
                    'question': lines[i],
                    'answer': lines[i + 1]
                })
    
    return qa_pairs

def convert_to_json(input_file, output_file=None, metadata=None):
    """Convert transcript to JSON format."""
    
    # Read input file
    try:
        with open(input_file, 'r', encoding='utf-8') as f:
            content = f.read()
    except FileNotFoundError:
        print(f"❌ Error: File '{input_file}' not found.")
        return False
    
    # Try to parse as JSON first
    try:
        data = json.loads(content)
        print("✅ File is already in JSON format!")
        if output_file:
            with open(output_file, 'w') as f:
                json.dump(data, f, indent=2)
            print(f"💾 Saved to: {output_file}")
        return True
    except json.JSONDecodeError:
        pass
    
    # Parse as text
    qa_pairs = parse_text_transcript(content)
    
    if not qa_pairs:
        print("❌ Could not parse transcript. Please check the format.")
        print("\nSupported formats:")
        print("1. Q: ... A: ...")
        print("2. Question: ... Answer: ...")
        print("3. Interviewer: ... Candidate: ...")
        return False
    
    # Create JSON structure
    json_data = {
        'interview_metadata': metadata or {
            'date': datetime.now().strftime('%Y-%m-%d'),
            'company': 'To be filled',
            'position': 'To be filled',
            'notes': f'Converted from {input_file}'
        },
        'interview_questions_and_answers': [
            {
                'question_number': i + 1,
                'question': qa['question'],
                'answer': qa['answer'],
            }
            for i, qa in enumerate(qa_pairs)
        ]
    }
    
    # Save to file
    if not output_file:
        output_file = input_file.rsplit('.', 1)[0] + '_converted.json'
    
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(json_data, f, indent=2, ensure_ascii=False)
    
    print(f"\n✅ Successfully converted!")
    print(f"📊 Found {len(qa_pairs)} Q&A pairs")
    print(f"💾 Saved to: {output_file}")
    print(f"\n💡 Next step: python analyze_transcript.py {output_file}")
    
    return True

def interactive_mode():
    """Interactive mode to add metadata."""
    print("\n" + "="*60)
    print("📝 Interview Transcript Converter")
    print("="*60)
    
    input_file = input("\nEnter input file path: ").strip()
    
    print("\n📋 Optional: Add interview metadata (press Enter to skip)")
    company = input("Company name: ").strip()
    position = input("Position: ").strip()
    date_str = input("Date (YYYY-MM-DD): ").strip()
    salary = input("Salary range: ").strip()
    location = input("Location: ").strip()
    
    metadata = {
        'date': date_str or datetime.now().strftime('%Y-%m-%d'),
        'company': company or 'Not specified',
        'position': position or 'Not specified',
    }
    
    if salary:
        metadata['salary_range'] = salary
    if location:
        metadata['location'] = location
    
    output_file = input("\nOutput file path (press Enter for auto): ").strip()
    if not output_file:
        output_file = None
    
    convert_to_json(input_file, output_file, metadata)

if __name__ == '__main__':
    if len(sys.argv) < 2:
        interactive_mode()
    else:
        input_file = sys.argv[1]
        output_file = sys.argv[2] if len(sys.argv) > 2 else None
        convert_to_json(input_file, output_file)
