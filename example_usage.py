"""
Example usage of the Interview Training Tool
"""

from interview_trainer import InterviewAnalyzer

def practice_session():
    """Interactive practice session."""
    print("🎯 Interview Training Tool - Practice Session\n")
    print("This tool will help you improve your interview responses.\n")
    
    analyzer = InterviewAnalyzer()
    interview_data = []
    
    # Common interview questions
    questions = [
        "Tell me about yourself.",
        "Why do you want to work here?",
        "What's your greatest strength?",
        "What's your greatest weakness?",
        "Describe a challenging situation you faced.",
    ]
    
    print("Let's practice with common interview questions.")
    print("Type 'demo' to use sample answers, or 'custom' to input your own.\n")
    
    mode = input("Choose mode (demo/custom): ").strip().lower()
    
    if mode == 'demo':
        # Use sample answers
        interview_data = [
            (
                "Tell me about yourself.",
                "I'm a software developer with 5 years of experience in web development. I specialize in Python and JavaScript frameworks. In my current role at TechCorp, I led a team of 3 developers to build a customer portal that increased user engagement by 40%."
            ),
            (
                "Why do you want to work here?",
                "I'm impressed by your company's commitment to innovation and employee development. Specifically, your recent AI initiatives align perfectly with my background in machine learning. I believe I can contribute to your team while growing professionally."
            ),
            (
                "What's your greatest strength?",
                "My greatest strength is problem-solving. For example, when our production system had performance issues, I analyzed the bottleneck, implemented caching, and improved response time by 60%. This skill would help me tackle complex challenges in this role."
            ),
        ]
    else:
        # Custom input
        num_questions = int(input("How many questions do you want to practice? "))
        for i in range(num_questions):
            print(f"\n--- Question {i+1} ---")
            if i < len(questions):
                question = questions[i]
                print(f"Q: {question}")
            else:
                question = input("Enter your question: ")
            answer = input("Your answer: ")
            interview_data.append((question, answer))
    
    # Analyze
    print("\n🔄 Analyzing your responses...\n")
    results = analyzer.analyze_full_interview(interview_data)
    
    # Display results
    print("=" * 60)
    print("YOUR INTERVIEW ANALYSIS")
    print("=" * 60)
    
    print("\n📊 OVERALL PERFORMANCE:")
    for criterion, score in results['overall_scores'].items():
        bar = "█" * int(score) + "░" * (10 - int(score))
        print(f"  {criterion.capitalize():15} [{bar}] {score}/10")
    
    overall_avg = sum(results['overall_scores'].values()) / len(results['overall_scores'])
    print(f"\n  Overall Score: {overall_avg:.1f}/10")
    
    print("\n💬 KEY FEEDBACK:")
    for item in results['overall_feedback']:
        print(f"  {item}")
    
    print("\n" + "=" * 60)
    print("DETAILED RESPONSE ANALYSIS")
    print("=" * 60)
    
    for i, response in enumerate(results['individual_responses'], 1):
        print(f"\n❓ Question {i}:")
        print(f"   {response['question']}")
        print(f"\n📝 Your Answer:")
        print(f"   {response['answer'][:150]}{'...' if len(response['answer']) > 150 else ''}")
        
        print("\n💡 Specific Feedback:")
        if response['feedback']:
            for feedback in response['feedback']:
                print(f"   {feedback}")
        else:
            print("   ✅ No issues detected!")
        
        print("\n" + "-" * 60)
    
    # Save report
    filename = analyzer.save_report(results)
    print(f"\n💾 Detailed report saved to: {filename}")
    print("\n🎯 Keep practicing to improve your scores!")
    
    return results


if __name__ == "__main__":
    practice_session()
