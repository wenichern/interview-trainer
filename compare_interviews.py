"""
Compare two interview transcripts to track progress
"""

import json
import sys
from interview_trainer import InterviewAnalyzer

def load_transcript(filepath):
    """Load interview transcript from JSON file."""
    with open(filepath, 'r') as f:
        return json.load(f)

def compare_interviews(file1, file2):
    """Compare two interview transcripts and show improvement."""
    
    print("\n" + "="*70)
    print("📊 INTERVIEW COMPARISON REPORT")
    print("="*70)
    
    # Load transcripts
    interview1 = load_transcript(file1)
    interview2 = load_transcript(file2)
    
    # Display metadata
    meta1 = interview1.get('interview_metadata', {})
    meta2 = interview2.get('interview_metadata', {})
    
    print("\n📋 INTERVIEW 1 (BASELINE):")
    print(f"  Date: {meta1.get('date', 'N/A')}")
    print(f"  Company: {meta1.get('company', 'N/A')}")
    print(f"  Position: {meta1.get('position', 'N/A')}")
    
    print("\n📋 INTERVIEW 2 (CURRENT):")
    print(f"  Date: {meta2.get('date', 'N/A')}")
    print(f"  Company: {meta2.get('company', 'N/A')}")
    print(f"  Position: {meta2.get('position', 'N/A')}")
    
    # Prepare Q&A pairs
    analyzer = InterviewAnalyzer()
    
    qa_pairs1 = []
    for qa in interview1.get('interview_questions_and_answers', []):
        qa_pairs1.append((qa.get('question', ''), qa.get('answer', '')))
    
    qa_pairs2 = []
    for qa in interview2.get('interview_questions_and_answers', []):
        qa_pairs2.append((qa.get('question', ''), qa.get('answer', '')))
    
    # Analyze both
    results1 = analyzer.analyze_full_interview(qa_pairs1)
    results2 = analyzer.analyze_full_interview(qa_pairs2)
    
    # Compare scores
    print("\n" + "="*70)
    print("📈 SCORE COMPARISON")
    print("="*70)
    
    scores1 = results1['overall_scores']
    scores2 = results2['overall_scores']
    
    print(f"\n{'Criterion':<20} {'Interview 1':<15} {'Interview 2':<15} {'Change':<10}")
    print("-"*70)
    
    improvements = []
    declines = []
    
    for criterion in scores1.keys():
        score1 = scores1[criterion]
        score2 = scores2[criterion]
        change = score2 - score1
        
        change_symbol = "📈" if change > 0 else "📉" if change < 0 else "➡️"
        change_str = f"{change:+.1f}"
        
        print(f"{criterion.capitalize():<20} {score1:<15.1f} {score2:<15.1f} {change_symbol} {change_str}")
        
        if change > 0:
            improvements.append(f"{criterion} (+{change:.1f})")
        elif change < 0:
            declines.append(f"{criterion} ({change:.1f})")
    
    # Overall averages
    avg1 = sum(scores1.values()) / len(scores1)
    avg2 = sum(scores2.values()) / len(scores2)
    overall_change = avg2 - avg1
    
    print("-"*70)
    print(f"{'OVERALL':<20} {avg1:<15.1f} {avg2:<15.1f} {overall_change:+.1f}")
    
    # Summary
    print("\n" + "="*70)
    print("📊 SUMMARY")
    print("="*70)
    
    if improvements:
        print("\n✅ IMPROVEMENTS:")
        for imp in improvements:
            print(f"  • {imp}")
    
    if declines:
        print("\n⚠️ AREAS THAT DECLINED:")
        for dec in declines:
            print(f"  • {dec}")
    
    if not improvements and not declines:
        print("\n➡️ No significant changes detected")
    
    # Overall assessment
    print(f"\n🎯 OVERALL PROGRESS: ", end="")
    if overall_change >= 1.0:
        print(f"🎉 Excellent improvement! (+{overall_change:.1f})")
    elif overall_change >= 0.5:
        print(f"👍 Good progress! (+{overall_change:.1f})")
    elif overall_change > 0:
        print(f"📈 Slight improvement (+{overall_change:.1f})")
    elif overall_change == 0:
        print("➡️ Maintained same level")
    else:
        print(f"📉 Needs work ({overall_change:.1f})")
    
    # Recommendations
    print("\n" + "="*70)
    print("💡 RECOMMENDATIONS FOR NEXT INTERVIEW")
    print("="*70)
    
    # Find weakest areas in latest interview
    weak_areas = [(k, v) for k, v in scores2.items() if v < 7]
    weak_areas.sort(key=lambda x: x[1])
    
    if weak_areas:
        print("\nFocus on improving:")
        for criterion, score in weak_areas[:3]:
            print(f"  • {criterion.capitalize()} (current: {score:.1f}/10)")
    else:
        print("\n✅ All areas are strong! Keep practicing to maintain excellence.")
    
    # Additional insights
    print("\n📈 Progress Tracking Tips:")
    print("  • Interview 1 had", len(qa_pairs1), "questions")
    print("  • Interview 2 had", len(qa_pairs2), "questions")
    
    if overall_change > 0:
        print("  • Keep doing what you're doing! 🎉")
    else:
        print("  • Review training modules at http://localhost:5000")
        print("  • Practice with STAR method for better structure")
        print("  • Add measurable results to every answer")
    
    print("\n" + "="*70)
    
    return {
        'interview1': results1,
        'interview2': results2,
        'improvements': improvements,
        'declines': declines,
        'overall_change': overall_change
    }

if __name__ == '__main__':
    if len(sys.argv) < 3:
        print("Usage: python compare_interviews.py <interview1.json> <interview2.json>")
        print("\nExample:")
        print("  python compare_interviews.py interview_transcript.json new_interview.json")
        sys.exit(1)
    
    file1 = sys.argv[1]
    file2 = sys.argv[2]
    
    try:
        compare_interviews(file1, file2)
    except FileNotFoundError as e:
        print(f"\n❌ Error: {e}")
        print("Please make sure both files exist.")
    except Exception as e:
        print(f"\n❌ Error comparing interviews: {e}")
