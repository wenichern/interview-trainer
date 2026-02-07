"""
Interview Training Tool - POC
Helps applicants improve their interview performance by analyzing transcripts
and providing actionable feedback.
"""

import json
from datetime import datetime
from typing import Dict, List, Tuple

class InterviewAnalyzer:
    """Analyzes interview transcripts and provides feedback."""
    
    def __init__(self):
        self.evaluation_criteria = {
            'clarity': 'How clear and structured is the response?',
            'relevance': 'Does the answer address the question directly?',
            'confidence': 'Does the candidate sound confident?',
            'specificity': 'Are examples specific and detailed?',
            'professionalism': 'Is the tone professional?'
        }
    
    def analyze_response(self, question: str, answer: str) -> Dict:
        """Analyze a single Q&A pair."""
        analysis = {
            'question': question,
            'answer': answer,
            'scores': self._calculate_scores(answer),
            'feedback': self._generate_feedback(question, answer),
            'timestamp': datetime.now().isoformat()
        }
        return analysis
    
    def _calculate_scores(self, answer: str) -> Dict[str, int]:
        """Calculate scores for different criteria (1-10)."""
        scores = {}
        
        # Simple heuristic scoring (can be enhanced with AI/ML)
        word_count = len(answer.split())
        
        # Clarity - based on sentence structure
        sentences = answer.split('.')
        avg_sentence_length = word_count / max(len(sentences), 1)
        scores['clarity'] = min(10, int(10 - abs(15 - avg_sentence_length) / 2))
        
        # Relevance - placeholder (would need context analysis)
        scores['relevance'] = 7
        
        # Confidence - check for filler words
        filler_words = ['um', 'uh', 'like', 'you know', 'kind of', 'sort of']
        filler_count = sum(answer.lower().count(word) for word in filler_words)
        scores['confidence'] = max(1, 10 - filler_count * 2)
        
        # Specificity - look for concrete examples
        specificity_indicators = ['for example', 'specifically', 'in my role', 'at', 'project']
        specificity_score = sum(2 for indicator in specificity_indicators if indicator in answer.lower())
        scores['specificity'] = min(10, specificity_score)
        
        # Professionalism
        casual_words = ['yeah', 'gonna', 'wanna', 'kinda']
        casual_count = sum(answer.lower().count(word) for word in casual_words)
        scores['professionalism'] = max(1, 10 - casual_count * 2)
        
        return scores
    
    def _generate_feedback(self, question: str, answer: str) -> List[str]:
        """Generate actionable feedback."""
        feedback = []
        word_count = len(answer.split())
        
        # Length feedback
        if word_count < 30:
            feedback.append("⚠️ Response is too brief. Aim for 50-100 words to provide sufficient detail.")
        elif word_count > 150:
            feedback.append("⚠️ Response is lengthy. Try to be more concise while maintaining key points.")
        
        # Filler words
        filler_words = ['um', 'uh', 'like', 'you know']
        if any(word in answer.lower() for word in filler_words):
            feedback.append("💡 Reduce filler words (um, uh, like). Practice pausing instead.")
        
        # Structure
        if not any(phrase in answer.lower() for phrase in ['first', 'second', 'finally', 'additionally']):
            feedback.append("💡 Use structure words (First, Additionally, Finally) to organize your response.")
        
        # Examples
        if not any(phrase in answer.lower() for phrase in ['example', 'experience', 'project', 'role']):
            feedback.append("💡 Include specific examples from your experience to strengthen your answer.")
        
        # Positive reinforcement
        if word_count >= 50 and word_count <= 100:
            feedback.append("✅ Good response length!")
        
        return feedback
    
    def analyze_full_interview(self, interview_data: List[Tuple[str, str]]) -> Dict:
        """Analyze complete interview transcript."""
        analyses = []
        total_scores = {criterion: 0 for criterion in self.evaluation_criteria}
        
        for question, answer in interview_data:
            analysis = self.analyze_response(question, answer)
            analyses.append(analysis)
            
            for criterion, score in analysis['scores'].items():
                total_scores[criterion] += score
        
        num_questions = len(interview_data)
        avg_scores = {k: round(v / num_questions, 1) for k, v in total_scores.items()}
        
        return {
            'individual_responses': analyses,
            'overall_scores': avg_scores,
            'overall_feedback': self._generate_overall_feedback(avg_scores),
            'interview_date': datetime.now().isoformat()
        }
    
    def _generate_overall_feedback(self, avg_scores: Dict[str, float]) -> List[str]:
        """Generate overall interview feedback."""
        feedback = []
        
        # Identify strengths and weaknesses
        strengths = [k for k, v in avg_scores.items() if v >= 8]
        weaknesses = [k for k, v in avg_scores.items() if v < 6]
        
        if strengths:
            feedback.append(f"🌟 Strengths: {', '.join(strengths)}")
        
        if weaknesses:
            feedback.append(f"📈 Areas to improve: {', '.join(weaknesses)}")
        
        # Overall score
        overall_avg = sum(avg_scores.values()) / len(avg_scores)
        if overall_avg >= 8:
            feedback.append("🎉 Excellent performance! You're well-prepared.")
        elif overall_avg >= 6:
            feedback.append("👍 Good performance with room for improvement.")
        else:
            feedback.append("💪 Keep practicing! Focus on the areas mentioned above.")
        
        return feedback
    
    def save_report(self, analysis: Dict, filename: str = None):
        """Save analysis report to JSON file."""
        if filename is None:
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            filename = f"interview_report_{timestamp}.json"
        
        with open(filename, 'w') as f:
            json.dump(analysis, f, indent=2)
        
        return filename


def demo_interview():
    """Demo with sample interview questions."""
    sample_interview = [
        (
            "Tell me about yourself.",
            "Um, well, I'm a software developer with like 5 years of experience. I've worked on various projects, you know, mostly web applications. I'm really passionate about coding and I think I'd be a good fit for this role."
        ),
        (
            "What's your greatest strength?",
            "My greatest strength is problem-solving. For example, in my last role at TechCorp, I identified a critical performance bottleneck in our API that was causing 30% slower response times. I analyzed the code, implemented caching strategies, and reduced response time by 50%. This directly improved user satisfaction scores."
        ),
        (
            "Describe a challenging situation you faced.",
            "I faced a challenging situation when our production database went down during peak hours. I remained calm, quickly assessed the situation, coordinated with the team to implement our backup plan, and restored service within 2 hours. Additionally, I documented the incident and proposed preventive measures that we implemented."
        )
    ]
    
    analyzer = InterviewAnalyzer()
    results = analyzer.analyze_full_interview(sample_interview)
    
    # Print results
    print("=" * 60)
    print("INTERVIEW TRAINING TOOL - ANALYSIS REPORT")
    print("=" * 60)
    
    print("\n📊 OVERALL SCORES:")
    for criterion, score in results['overall_scores'].items():
        bar = "█" * int(score) + "░" * (10 - int(score))
        print(f"  {criterion.capitalize():15} [{bar}] {score}/10")
    
    print("\n💬 OVERALL FEEDBACK:")
    for item in results['overall_feedback']:
        print(f"  {item}")
    
    print("\n" + "=" * 60)
    print("INDIVIDUAL RESPONSES:")
    print("=" * 60)
    
    for i, response in enumerate(results['individual_responses'], 1):
        print(f"\n❓ Question {i}: {response['question']}")
        print(f"\n💭 Your Answer: {response['answer'][:100]}...")
        print("\n📊 Scores:")
        for criterion, score in response['scores'].items():
            print(f"  {criterion.capitalize():15} {score}/10")
        print("\n💡 Feedback:")
        for feedback in response['feedback']:
            print(f"  {feedback}")
        print("\n" + "-" * 60)
    
    # Save report
    filename = analyzer.save_report(results)
    print(f"\n💾 Report saved to: {filename}")
    
    return results


if __name__ == "__main__":
    print("\n🎯 Welcome to Interview Training Tool - POC\n")
    demo_interview()
