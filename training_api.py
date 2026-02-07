"""
Interview Training Web API
Provides interactive training modules to help applicants improve their interview skills
"""

from flask import Flask, jsonify, request, render_template
from flask_cors import CORS
import json
import random
from datetime import datetime

app = Flask(__name__)
CORS(app)

# Training data
TRAINING_MODULES = {
    "concrete_examples": {
        "title": "Prepare Concrete Examples",
        "description": "Learn to craft compelling stories with measurable results",
        "lessons": [
            {
                "id": 1,
                "title": "STAR Method Framework",
                "content": """
                <h3>The STAR Method</h3>
                <p><strong>S</strong>ituation - Set the context</p>
                <p><strong>T</strong>ask - Describe your responsibility</p>
                <p><strong>A</strong>ction - Explain what you did</p>
                <p><strong>R</strong>esult - Share measurable outcomes</p>
                
                <h4>Example:</h4>
                <p><strong>Situation:</strong> Our API response time was 2 seconds, causing user complaints.</p>
                <p><strong>Task:</strong> I was assigned to improve system performance.</p>
                <p><strong>Action:</strong> I implemented Redis caching and optimized database queries.</p>
                <p><strong>Result:</strong> Reduced response time by 60% (from 2s to 0.8s), increasing user satisfaction by 40%.</p>
                """,
                "practice_prompts": [
                    "Describe a time you improved system performance",
                    "Tell me about a challenging technical problem you solved",
                    "Share an example of when you led a team to success"
                ]
            },
            {
                "id": 2,
                "title": "Adding Measurable Results",
                "content": """
                <h3>Make Your Impact Quantifiable</h3>
                <p>Always include numbers to show your impact:</p>
                <ul>
                    <li>✅ "Reduced deployment time by 75% (from 4 hours to 1 hour)"</li>
                    <li>✅ "Saved $50,000 annually by optimizing cloud costs"</li>
                    <li>✅ "Increased test coverage from 40% to 85%"</li>
                    <li>❌ "Made the system faster"</li>
                    <li>❌ "Improved the deployment process"</li>
                </ul>
                """,
                "practice_prompts": [
                    "Think of 3 projects and quantify your impact",
                    "Convert vague accomplishments into measurable results"
                ]
            }
        ]
    },
    "ml_inference": {
        "title": "ML Inference vs Training",
        "description": "Understand machine learning inference and production serving",
        "lessons": [
            {
                "id": 1,
                "title": "Training vs Inference",
                "content": """
                <h3>Key Differences</h3>
                
                <h4>Training (Model Development):</h4>
                <ul>
                    <li>🎓 Learning patterns from historical data</li>
                    <li>🎓 Adjusting model parameters/weights</li>
                    <li>🎓 Requires large datasets and GPU compute</li>
                    <li>🎓 Done periodically (daily, weekly, monthly)</li>
                    <li>🎓 Takes hours to days</li>
                </ul>
                
                <h4>Inference (Production Use):</h4>
                <ul>
                    <li>🚀 Using trained model to make predictions on NEW data</li>
                    <li>🚀 Model parameters are FROZEN (no learning)</li>
                    <li>🚀 Optimized for low latency (milliseconds)</li>
                    <li>🚀 Handles real-time requests from users</li>
                    <li>🚀 Focus: speed, scalability, cost efficiency</li>
                </ul>
                
                <h4>Example Flow:</h4>
                <pre>
User Request → API Gateway → Load Balancer → Inference Server
                                                ↓
                                           Load Model
                                                ↓
                                         Preprocess Input
                                                ↓
                                         Run Prediction
                                                ↓
                                        Postprocess Output
                                                ↓
                                         Return Response
                </pre>
                """,
                "practice_prompts": [
                    "Explain inference to a non-technical person",
                    "Describe the request-response flow for a prediction"
                ]
            },
            {
                "id": 2,
                "title": "ML Serving Tools",
                "content": """
                <h3>Popular Inference/Serving Tools</h3>
                
                <h4>🔹 TensorFlow Serving</h4>
                <p>Google's production-grade serving system for TensorFlow models</p>
                <ul>
                    <li>REST and gRPC APIs</li>
                    <li>Model versioning and hot-swapping</li>
                    <li>Batching for throughput optimization</li>
                </ul>
                
                <h4>🔹 TorchServe</h4>
                <p>PyTorch's model serving framework</p>
                <ul>
                    <li>Multi-model serving</li>
                    <li>A/B testing support</li>
                    <li>Built-in metrics and logging</li>
                </ul>
                
                <h4>🔹 AWS SageMaker Endpoints</h4>
                <p>Fully managed inference service</p>
                <ul>
                    <li>Auto-scaling based on traffic</li>
                    <li>Multiple instance types (CPU, GPU)</li>
                    <li>Built-in monitoring with CloudWatch</li>
                    <li>Support for custom containers</li>
                </ul>
                
                <h4>🔹 NVIDIA Triton</h4>
                <p>Multi-framework inference server</p>
                <ul>
                    <li>Supports TensorFlow, PyTorch, ONNX, etc.</li>
                    <li>Dynamic batching</li>
                    <li>GPU optimization</li>
                </ul>
                """,
                "practice_prompts": [
                    "Which serving tool would you choose for a high-traffic API?",
                    "How would you handle model versioning in production?"
                ]
            },
            {
                "id": 3,
                "title": "Production Inference Challenges",
                "content": """
                <h3>Real-World Considerations</h3>
                
                <h4>🎯 Latency Optimization</h4>
                <ul>
                    <li>Model quantization (reduce precision)</li>
                    <li>Model pruning (remove unnecessary weights)</li>
                    <li>Batching requests for throughput</li>
                    <li>Caching frequent predictions</li>
                </ul>
                
                <h4>🎯 Scalability</h4>
                <ul>
                    <li>Auto-scaling based on request volume</li>
                    <li>Load balancing across multiple instances</li>
                    <li>GPU vs CPU instance selection</li>
                </ul>
                
                <h4>🎯 Monitoring</h4>
                <ul>
                    <li>Track prediction latency (p50, p95, p99)</li>
                    <li>Monitor model drift (input/output distributions)</li>
                    <li>Alert on errors or anomalies</li>
                </ul>
                """,
                "practice_prompts": [
                    "How would you optimize inference latency?",
                    "What metrics would you monitor for ML inference?"
                ]
            }
        ]
    },
    "concise_answers": {
        "title": "Practice Concise Answers",
        "description": "Master the 'headline first' approach for 60-90 second responses",
        "lessons": [
            {
                "id": 1,
                "title": "Headline First Method",
                "content": """
                <h3>Structure Your Answers</h3>
                
                <h4>❌ Wrong Approach (Rambling):</h4>
                <p>"Well, um, so I've done a lot of things with AWS. I've worked on EC2, S3, Lambda, 
                and actually I've been doing this for about 10 years now. I guess my experience started 
                when I joined my first company..."</p>
                
                <h4>✅ Right Approach (Headline First):</h4>
                <p><strong>HEADLINE:</strong> "I have 10 years of AWS infrastructure experience, 
                specializing in scalable, secure cloud architectures."</p>
                <p><strong>SUPPORT:</strong> "For example, I recently designed a multi-region AWS 
                infrastructure that reduced costs by 30% while improving availability to 99.99%."</p>
                <p><strong>CLOSE:</strong> "This experience directly applies to your platform role."</p>
                
                <h4>The Formula:</h4>
                <ol>
                    <li><strong>Headline (5-10 seconds):</strong> Direct answer to the question</li>
                    <li><strong>Support (40-60 seconds):</strong> 1-2 specific examples with results</li>
                    <li><strong>Close (5-10 seconds):</strong> Connect to the role</li>
                </ol>
                """,
                "practice_prompts": [
                    "Tell me about yourself (use headline first)",
                    "What's your greatest strength? (60 seconds max)"
                ]
            },
            {
                "id": 2,
                "title": "Eliminating Rambling",
                "content": """
                <h3>Common Rambling Patterns to Avoid</h3>
                
                <h4>🚫 Unnecessary Context</h4>
                <p>❌ "So, back in 2015, I was working at this company, and actually before that I was..."</p>
                <p>✅ "In my last role, I..."</p>
                
                <h4>🚫 Multiple Tangents</h4>
                <p>❌ "I worked on the API, and also the database, oh and the frontend too, plus CI/CD..."</p>
                <p>✅ "I focused on three key areas: API optimization, database scaling, and CI/CD automation."</p>
                
                <h4>🚫 Over-explaining</h4>
                <p>❌ "So Kubernetes is a container orchestration platform, which means..."</p>
                <p>✅ "I used Kubernetes to orchestrate our microservices..."</p>
                
                <h4>Tips to Stay Concise:</h4>
                <ul>
                    <li>⏱️ Practice with a timer (aim for 60-90 seconds)</li>
                    <li>🎯 Pick ONE strong example instead of listing many</li>
                    <li>✂️ Cut backstory - start with the action</li>
                    <li>🛑 Stop when you've made your point</li>
                </ul>
                """,
                "practice_prompts": [
                    "Describe a project in exactly 60 seconds",
                    "Answer 'Why should we hire you?' in 90 seconds"
                ]
            }
        ]
    },
    "confident_language": {
        "title": "Replace Weak Phrases",
        "description": "Transform weak language into confident, assertive communication",
        "lessons": [
            {
                "id": 1,
                "title": "Weak vs Strong Language",
                "content": """
                <h3>Language Transformation Guide</h3>
                
                <h4>❌ Weak → ✅ Strong</h4>
                
                <table style="width:100%; border-collapse: collapse;">
                    <tr style="background: #f0f0f0;">
                        <th style="padding: 10px; text-align: left;">❌ Avoid</th>
                        <th style="padding: 10px; text-align: left;">✅ Use Instead</th>
                    </tr>
                    <tr>
                        <td style="padding: 10px;">I guess</td>
                        <td style="padding: 10px;"><strong>I believe / In my experience</strong></td>
                    </tr>
                    <tr style="background: #f9f9f9;">
                        <td style="padding: 10px;">I think</td>
                        <td style="padding: 10px;"><strong>I'm confident / I've found</strong></td>
                    </tr>
                    <tr>
                        <td style="padding: 10px;">Kind of / Sort of</td>
                        <td style="padding: 10px;"><strong>[Remove entirely]</strong></td>
                    </tr>
                    <tr style="background: #f9f9f9;">
                        <td style="padding: 10px;">Maybe / Probably</td>
                        <td style="padding: 10px;"><strong>Certainly / Definitely</strong></td>
                    </tr>
                    <tr>
                        <td style="padding: 10px;">I just / I only</td>
                        <td style="padding: 10px;"><strong>[Remove minimizers]</strong></td>
                    </tr>
                    <tr style="background: #f9f9f9;">
                        <td style="padding: 10px;">I'll try</td>
                        <td style="padding: 10px;"><strong>I will / I can</strong></td>
                    </tr>
                    <tr>
                        <td style="padding: 10px;">You know</td>
                        <td style="padding: 10px;"><strong>[Pause instead]</strong></td>
                    </tr>
                </table>
                
                <h4>Examples:</h4>
                <p>❌ "I guess I'm kind of good at problem-solving, you know?"</p>
                <p>✅ "I excel at problem-solving. In my experience, I've consistently delivered innovative solutions."</p>
                """,
                "practice_prompts": [
                    "Rewrite 3 of your common answers without weak phrases",
                    "Record yourself and count weak phrases"
                ]
            },
            {
                "id": 2,
                "title": "Assertive Communication",
                "content": """
                <h3>Sound Confident Without Being Arrogant</h3>
                
                <h4>✅ Own Your Accomplishments</h4>
                <p>❌ "We kind of improved the system"</p>
                <p>✅ "I led the team that improved system performance by 50%"</p>
                
                <h4>✅ Be Specific About Your Role</h4>
                <p>❌ "I was involved in the project"</p>
                <p>✅ "I designed and implemented the caching layer"</p>
                
                <h4>✅ Replace Qualifiers with Facts</h4>
                <p>❌ "I'm pretty experienced with AWS"</p>
                <p>✅ "I have 10 years of AWS experience across 15+ production systems"</p>
                
                <h4>✅ Use Active Voice</h4>
                <p>❌ "The system was optimized by me"</p>
                <p>✅ "I optimized the system"</p>
                
                <h4>Practice Mantras:</h4>
                <ul>
                    <li>💪 "I achieved..." (not "I tried to achieve...")</li>
                    <li>💪 "I delivered..." (not "I helped deliver...")</li>
                    <li>💪 "I'm confident that..." (not "I think maybe...")</li>
                </ul>
                """,
                "practice_prompts": [
                    "Rewrite your accomplishments in active voice",
                    "Practice saying 'I' confidently when describing your work"
                ]
            }
        ]
    }
}

# Sample interview questions by category
PRACTICE_QUESTIONS = {
    "behavioral": [
        "Tell me about yourself.",
        "Why do you want to work here?",
        "What's your greatest strength?",
        "What's your greatest weakness?",
        "Describe a time you faced a challenge.",
        "Tell me about a time you failed.",
        "How do you handle conflicts with team members?",
        "Describe a time you showed leadership."
    ],
    "technical": [
        "Describe the AWS infrastructure you've designed.",
        "How do you ensure high availability in cloud systems?",
        "Explain your CI/CD pipeline setup.",
        "How do you handle security and compliance?",
        "What's your experience with container orchestration?",
        "How do you optimize cloud costs?",
        "Describe your monitoring and observability strategy."
    ],
    "ml_specific": [
        "Explain the difference between training and inference.",
        "How would you serve a machine learning model in production?",
        "What inference tools have you used?",
        "How do you optimize inference latency?",
        "How do you handle model versioning?",
        "What metrics do you monitor for ML systems?",
        "How do you scale ML inference services?"
    ]
}

# User progress tracking (in-memory for demo)
user_progress = {}


@app.route('/')
def home():
    """Serve the main training interface."""
    return render_template('index.html')


@app.route('/api/modules', methods=['GET'])
def get_modules():
    """Get all training modules."""
    modules = []
    for key, module in TRAINING_MODULES.items():
        modules.append({
            'id': key,
            'title': module['title'],
            'description': module['description'],
            'lesson_count': len(module['lessons'])
        })
    return jsonify({'modules': modules})


@app.route('/api/module/<module_id>', methods=['GET'])
def get_module(module_id):
    """Get specific module details."""
    if module_id not in TRAINING_MODULES:
        return jsonify({'error': 'Module not found'}), 404
    return jsonify(TRAINING_MODULES[module_id])


@app.route('/api/practice/questions', methods=['GET'])
def get_practice_questions():
    """Get practice questions by category."""
    category = request.args.get('category', 'behavioral')
    if category not in PRACTICE_QUESTIONS:
        return jsonify({'error': 'Invalid category'}), 400
    
    questions = PRACTICE_QUESTIONS[category]
    return jsonify({
        'category': category,
        'questions': questions,
        'total': len(questions)
    })


@app.route('/api/practice/random', methods=['GET'])
def get_random_question():
    """Get a random practice question."""
    all_questions = []
    for category, questions in PRACTICE_QUESTIONS.items():
        for q in questions:
            all_questions.append({'category': category, 'question': q})
    
    question = random.choice(all_questions)
    return jsonify(question)


@app.route('/api/analyze/response', methods=['POST'])
def analyze_response():
    """Analyze a practice response."""
    data = request.json
    question = data.get('question', '')
    answer = data.get('answer', '')
    
    if not answer:
        return jsonify({'error': 'Answer is required'}), 400
    
    # Simple analysis
    word_count = len(answer.split())
    weak_phrases = ['i guess', 'i think', 'kind of', 'sort of', 'you know', 'um', 'uh', 'like']
    weak_count = sum(answer.lower().count(phrase) for phrase in weak_phrases)
    
    has_numbers = any(char.isdigit() for char in answer)
    has_star = any(keyword in answer.lower() for keyword in ['situation', 'task', 'action', 'result'])
    
    feedback = []
    score = 10
    
    # Check length
    if word_count < 50:
        feedback.append("⚠️ Too brief. Aim for 50-100 words.")
        score -= 2
    elif word_count > 150:
        feedback.append("⚠️ Too long. Keep it concise (60-90 seconds).")
        score -= 2
    else:
        feedback.append("✅ Good length!")
    
    # Check weak phrases
    if weak_count > 0:
        feedback.append(f"⚠️ Found {weak_count} weak phrase(s). Replace with confident language.")
        score -= weak_count
    else:
        feedback.append("✅ Confident language!")
    
    # Check for metrics
    if not has_numbers:
        feedback.append("💡 Add measurable results (numbers, percentages, timelines).")
        score -= 1
    else:
        feedback.append("✅ Great use of metrics!")
    
    # Check for structure
    if not has_star:
        feedback.append("💡 Consider using STAR method for better structure.")
        score -= 1
    else:
        feedback.append("✅ Good use of structure!")
    
    score = max(0, score)
    
    return jsonify({
        'score': score,
        'word_count': word_count,
        'weak_phrases_count': weak_count,
        'has_metrics': has_numbers,
        'has_structure': has_star,
        'feedback': feedback,
        'timestamp': datetime.now().isoformat()
    })


@app.route('/api/tips/random', methods=['GET'])
def get_random_tip():
    """Get a random interview tip."""
    tips = [
        "Use the STAR method: Situation, Task, Action, Result",
        "Always include measurable outcomes in your examples",
        "Replace 'I guess' with 'I believe' or 'In my experience'",
        "Aim for 60-90 second answers",
        "Start with the headline - answer the question directly first",
        "Practice with a timer to stay concise",
        "Remove filler words like 'um', 'uh', 'like'",
        "Own your accomplishments - say 'I' not 'we' when describing your work",
        "Prepare 5-7 STAR stories before the interview",
        "Research the company and role thoroughly"
    ]
    
    return jsonify({'tip': random.choice(tips)})


if __name__ == '__main__':
    print("\n" + "="*70)
    print("🎯 Interview Training API Server")
    print("="*70)
    print("\n📚 Available Training Modules:")
    for key, module in TRAINING_MODULES.items():
        print(f"  • {module['title']}")
    print("\n🌐 Server starting at: http://localhost:5000")
    print("="*70 + "\n")
    
    app.run(debug=True, host='0.0.0.0', port=5000)
