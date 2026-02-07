"""
Generate progress report across multiple interviews
"""

import json
import os
import sys
from datetime import datetime
from interview_trainer import InterviewAnalyzer
import glob

def load_all_interviews(directory='./'):
    """Load all interview JSON files from directory."""
    
    # Find all JSON files
    json_files = glob.glob(os.path.join(directory, '*.json'))
    
    # Filter for interview files (exclude analysis files)
    interview_files = [f for f in json_files if 'analysis' not in f.lower()]
    
    interviews = []
    for filepath in interview_files:
        try:
            with open(filepath, 'r') as f:
                data = json.load(f)
                # Check if it's an interview file
                if 'interview_questions_and_answers' in data or 'individual_responses' in data:
                    interviews.append({
                        'filepath': filepath,
                        'data': data
                    })
        except:
            continue
    
    return interviews

def analyze_interview_data(interview_data):
    """Analyze interview data and return scores."""
    
    analyzer = InterviewAnalyzer()
    
    # Check if already analyzed
    if 'overall_scores' in interview_data:
        return interview_data
    
    # Extract Q&A pairs
    qa_pairs = []
    for qa in interview_data.get('interview_questions_and_answers', []):
        qa_pairs.append((qa.get('question', ''), qa.get('answer', '')))
    
    if not qa_pairs:
        return None
    
    results = analyzer.analyze_full_interview(qa_pairs)
    return results

def generate_progress_report(directory='./'):
    """Generate comprehensive progress report."""
    
    print("\n" + "="*70)
    print("📊 INTERVIEW PROGRESS REPORT")
    print("="*70)
    
    # Load all interviews
    interviews = load_all_interviews(directory)
    
    if not interviews:
        print("\n❌ No interview files found in directory:", directory)
        print("\nMake sure you have JSON files with interview data.")
        return
    
    print(f"\n📁 Found {len(interviews)} interview(s)")
    
    # Analyze each interview
    analyzed = []
    for interview in interviews:
        metadata = interview['data'].get('interview_metadata', {})
        date_str = metadata.get('date', 'Unknown')
        
        results = analyze_interview_data(interview['data'])
        if results:
            analyzed.append({
                'date': date_str,
                'company': metadata.get('company', 'Unknown'),
                'position': metadata.get('position', 'Unknown'),
                'filepath': interview['filepath'],
                'results': results
            })
    
    if not analyzed:
        print("\n❌ Could not analyze interviews. Please check file format.")
        return
    
    # Sort by date
    analyzed.sort(key=lambda x: x['date'])
    
    # Display timeline
    print("\n" + "="*70)
    print("📅 INTERVIEW TIMELINE")
    print("="*70)
    
    for i, interview in enumerate(analyzed, 1):
        scores = interview['results']['overall_scores']
        avg_score = sum(scores.values()) / len(scores)
        
        print(f"\n{i}. {interview['date']}")
        print(f"   Company: {interview['company']}")
        print(f"   Position: {interview['position']}")
        print(f"   Overall Score: {avg_score:.1f}/10")
        
        # Show bar
        bar = "█" * int(avg_score) + "░" * (10 - int(avg_score))
        print(f"   [{bar}]")
    
    # Score progression
    print("\n" + "="*70)
    print("📈 SCORE PROGRESSION")
    print("="*70)
    
    criteria = list(analyzed[0]['results']['overall_scores'].keys())
    
    print(f"\n{'Criterion':<20}", end='')
    for i in range(len(analyzed)):
        print(f"Int {i+1:>2}  ", end='')
    print("Trend")
    print("-"*70)
    
    for criterion in criteria:
        print(f"{criterion.capitalize():<20}", end='')
        
        scores = []
        for interview in analyzed:
            score = interview['results']['overall_scores'][criterion]
            scores.append(score)
            print(f"{score:>5.1f}  ", end='')
        
        # Calculate trend
        if len(scores) > 1:
            trend = scores[-1] - scores[0]
            if trend > 0:
                print(f"📈 +{trend:.1f}")
            elif trend < 0:
                print(f"📉 {trend:.1f}")
            else:
                print("➡️  0.0")
        else:
            print()
    
    # Overall trend
    print("-"*70)
    print(f"{'OVERALL':<20}", end='')
    
    overall_scores = []
    for interview in analyzed:
        avg = sum(interview['results']['overall_scores'].values()) / len(interview['results']['overall_scores'])
        overall_scores.append(avg)
        print(f"{avg:>5.1f}  ", end='')
    
    if len(overall_scores) > 1:
        overall_trend = overall_scores[-1] - overall_scores[0]
        if overall_trend > 0:
            print(f"📈 +{overall_trend:.1f}")
        elif overall_trend < 0:
            print(f"📉 {overall_trend:.1f}")
        else:
            print("➡️  0.0")
    else:
        print()
    
    # Key insights
    print("\n" + "="*70)
    print("💡 KEY INSIGHTS")
    print("="*70)
    
    if len(analyzed) > 1:
        # Most improved areas
        improvements = {}
        for criterion in criteria:
            first_score = analyzed[0]['results']['overall_scores'][criterion]
            last_score = analyzed[-1]['results']['overall_scores'][criterion]
            improvements[criterion] = last_score - first_score
        
        most_improved = sorted(improvements.items(), key=lambda x: x[1], reverse=True)
        
        print("\n✅ Most Improved Areas:")
        for criterion, change in most_improved[:3]:
            if change > 0:
                print(f"  • {criterion.capitalize()}: +{change:.1f} points")
        
        print("\n⚠️ Areas Needing Work:")
        for criterion, change in most_improved[-3:]:
            if change <= 0:
                score = analyzed[-1]['results']['overall_scores'][criterion]
                print(f"  • {criterion.capitalize()}: {score:.1f}/10 ({change:+.1f})")
        
        # Overall progress
        print(f"\n🎯 Overall Progress: {overall_trend:+.1f} points")
        
        if overall_trend >= 1.5:
            print("   🎉 Excellent improvement! Keep it up!")
        elif overall_trend >= 0.5:
            print("   👍 Good progress! You're on the right track.")
        elif overall_trend > 0:
            print("   📈 Slight improvement. Keep practicing!")
        elif overall_trend == 0:
            print("   ➡️ Maintaining current level. Try new strategies.")
        else:
            print("   📉 Focus on training modules to improve.")
    
    # Current status
    latest = analyzed[-1]
    latest_scores = latest['results']['overall_scores']
    latest_avg = sum(latest_scores.values()) / len(latest_scores)
    
    print("\n" + "="*70)
    print("🎯 CURRENT STATUS")
    print("="*70)
    
    print(f"\nYour latest interview score: {latest_avg:.1f}/10")
    
    if latest_avg >= 8.5:
        print("🎉 Excellent! You're interview-ready!")
    elif latest_avg >= 7.5:
        print("👍 Good! A bit more practice and you'll be great!")
    elif latest_avg >= 6.5:
        print("📈 Decent. Focus on weak areas to improve.")
    else:
        print("💪 Keep practicing! Use the training modules.")
    
    # Recommendations
    weak_areas = [(k, v) for k, v in latest_scores.items() if v < 7]
    
    if weak_areas:
        print("\n📋 Focus Areas for Next Interview:")
        for criterion, score in sorted(weak_areas, key=lambda x: x[1]):
            print(f"  • {criterion.capitalize()} ({score:.1f}/10)")
    
    print("\n" + "="*70)
    print("💾 Report generated:", datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
    print("="*70 + "\n")

if __name__ == '__main__':
    directory = sys.argv[1] if len(sys.argv) > 1 else './'
    
    print("\n🔍 Searching for interview files in:", directory)
    generate_progress_report(directory)
