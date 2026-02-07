"""
Analyze interview transcript from JSON file
"""

import json
from interview_trainer import InterviewAnalyzer

def analyze_json_transcript(json_file_path):
    """Load and analyze interview transcript from JSON file."""
    
    # Load the JSON file
    with open(json_file_path, 'r') as f:
        interview_data = json.load(f)
    
    print("=" * 70)
    print("INTERVIEW TRANSCRIPT ANALYSIS")
    print("=" * 70)
    
    # Display metadata
    metadata = interview_data.get('interview_metadata', {})
    print("\n📋 INTERVIEW INFORMATION:")
    print(f"  Date: {metadata.get('date', 'N/A')}")
    print(f"  Position: {metadata.get('position', 'N/A')}")
    print(f"  Company: {metadata.get('company', 'N/A')}")
    print(f"  Salary Range: {metadata.get('salary_range', 'N/A')}")
    print(f"  Location: {metadata.get('location', 'N/A')}")
    
    # Prepare Q&A pairs for analysis
    qa_pairs = []
    questions_and_answers = interview_data.get('interview_questions_and_answers', [])
    
    for qa in questions_and_answers:
        question = qa.get('question', '')
        answer = qa.get('answer', '')
        qa_pairs.append((question, answer))
    
    print(f"\n  Total Questions: {len(qa_pairs)}")
    
    # Analyze with our tool
    print("\n🔄 Analyzing responses with Interview Training Tool...\n")
    
    analyzer = InterviewAnalyzer()
    results = analyzer.analyze_full_interview(qa_pairs)
    
    # Display overall scores
    print("=" * 70)
    print("📊 OVERALL PERFORMANCE SCORES")
    print("=" * 70)
    
    for criterion, score in results['overall_scores'].items():
        bar = "█" * int(score) + "░" * (10 - int(score))
        print(f"  {criterion.capitalize():15} [{bar}] {score}/10")
    
    overall_avg = sum(results['overall_scores'].values()) / len(results['overall_scores'])
    print(f"\n  Overall Score: {overall_avg:.1f}/10")
    
    # Display overall feedback
    print("\n💬 OVERALL FEEDBACK:")
    for item in results['overall_feedback']:
        print(f"  {item}")
    
    # Display original interview summary if available
    if 'interview_summary' in interview_data:
        summary = interview_data['interview_summary']
        print("\n" + "=" * 70)
        print("📝 INTERVIEWER'S OBSERVATIONS")
        print("=" * 70)
        
        if 'candidate_strengths' in summary:
            print("\n✅ Candidate Strengths:")
            for strength in summary['candidate_strengths']:
                print(f"  • {strength}")
        
        if 'candidate_weaknesses' in summary:
            print("\n⚠️ Areas for Improvement:")
            for weakness in summary['candidate_weaknesses']:
                print(f"  • {weakness}")
    
    # Detailed response analysis
    print("\n" + "=" * 70)
    print("DETAILED RESPONSE ANALYSIS")
    print("=" * 70)
    
    for i, response in enumerate(results['individual_responses'], 1):
        print(f"\n{'─' * 70}")
        print(f"❓ QUESTION {i}")
        print(f"{'─' * 70}")
        print(f"{response['question']}")
        
        print(f"\n💭 ANSWER PREVIEW:")
        answer_preview = response['answer'][:200] + "..." if len(response['answer']) > 200 else response['answer']
        print(f"{answer_preview}")
        
        print(f"\n📊 SCORES:")
        for criterion, score in response['scores'].items():
            bar = "█" * int(score) + "░" * (10 - int(score))
            print(f"  {criterion.capitalize():15} [{bar}] {score}/10")
        
        print(f"\n💡 FEEDBACK:")
        if response['feedback']:
            for feedback in response['feedback']:
                print(f"  {feedback}")
        else:
            print("  ✅ No issues detected!")
    
    # Save detailed analysis report
    output_filename = json_file_path.replace('.json', '_analysis.json')
    analyzer.save_report(results, output_filename)
    
    print("\n" + "=" * 70)
    print(f"💾 Detailed analysis saved to: {output_filename}")
    print("=" * 70)
    
    # Generate improvement recommendations
    print("\n" + "=" * 70)
    print("🎯 PERSONALIZED IMPROVEMENT RECOMMENDATIONS")
    print("=" * 70)
    
    recommendations = generate_recommendations(results, interview_data)
    for i, rec in enumerate(recommendations, 1):
        print(f"\n{i}. {rec}")
    
    return results


def generate_recommendations(analysis_results, interview_data):
    """Generate personalized recommendations based on analysis."""
    recommendations = []
    
    scores = analysis_results['overall_scores']
    
    # Based on confidence score
    if scores.get('confidence', 0) < 7:
        recommendations.append(
            "🗣️ **Practice Reducing Filler Words**: Record yourself answering questions and "
            "count filler words like 'um', 'uh', 'like'. Try pausing silently instead."
        )
    
    # Based on clarity score
    if scores.get('clarity', 0) < 7:
        recommendations.append(
            "📝 **Use the STAR Method**: Structure your answers with Situation, Task, Action, Result. "
            "This makes your responses more organized and easier to follow."
        )
    
    # Based on specificity score
    if scores.get('specificity', 0) < 7:
        recommendations.append(
            "💼 **Prepare Concrete Examples**: Before interviews, prepare 5-7 specific examples from your "
            "experience with measurable results (e.g., 'reduced costs by 30%', 'improved performance by 50%')."
        )
    
    # Check for common issues in responses
    all_answers = " ".join([r['answer'] for r in analysis_results['individual_responses']]).lower()
    
    if 'i guess' in all_answers or 'i think' in all_answers:
        recommendations.append(
            "💪 **Sound More Confident**: Replace phrases like 'I guess' or 'I think' with 'I believe' "
            "or 'In my experience'. Be assertive about your accomplishments."
        )
    
    if 'you know' in all_answers:
        recommendations.append(
            "🎤 **Eliminate 'You Know'**: This phrase appears frequently. Practice answering questions "
            "without using it. Pause briefly instead when you need to think."
        )
    
    # Based on interview-specific feedback
    if 'interview_summary' in interview_data:
        summary = interview_data['interview_summary']
        if 'candidate_weaknesses' in summary:
            weaknesses_str = " ".join(summary['candidate_weaknesses']).lower()
            
            if 'inference' in weaknesses_str or 'ml' in weaknesses_str:
                recommendations.append(
                    "🤖 **Study ML Inference Concepts**: Review the difference between model training and "
                    "inference. Focus on tools like TensorFlow Serving, TorchServe, SageMaker Endpoints. "
                    "Prepare examples of how requests flow through an inference pipeline."
                )
            
            if 'communication' in weaknesses_str or 'unclear' in weaknesses_str:
                recommendations.append(
                    "🎯 **Practice Concise Answers**: Use the 'headline first' approach - state your main "
                    "point in the first sentence, then provide supporting details. Aim for 60-90 second responses."
                )
    
    # General recommendations
    recommendations.append(
        "📚 **Mock Interview Practice**: Do 2-3 mock interviews with friends or use online platforms. "
        "Focus on the areas identified above. Record yourself to track improvement."
    )
    
    recommendations.append(
        "📖 **Research the Role**: Based on this interview, review the specific technologies mentioned "
        "(GPU workloads, inference tools, ML serving). Prepare 1-2 concrete examples for each requirement."
    )
    
    return recommendations


if __name__ == "__main__":
    print("\n🎯 Interview Transcript Analyzer\n")
    
    # Analyze the JSON transcript
    json_file = "interview_transcript.json"
    
    try:
        results = analyze_json_transcript(json_file)
        print("\n✅ Analysis complete! Review the feedback above to improve for your next interview.\n")
    except FileNotFoundError:
        print(f"❌ Error: Could not find {json_file}")
        print("Please make sure the interview transcript JSON file exists in the current directory.")
    except Exception as e:
        print(f"❌ Error analyzing transcript: {e}")
