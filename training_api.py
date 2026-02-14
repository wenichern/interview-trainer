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
                
                <h4>Training Process Deep Dive:</h4>
                <ol>
                    <li><strong>Data Collection & Preparation:</strong> Gather historical data, clean, normalize, and split into train/validation/test sets</li>
                    <li><strong>Feature Engineering:</strong> Extract relevant features from raw data</li>
                    <li><strong>Model Selection:</strong> Choose architecture (neural network, tree-based, etc.)</li>
                    <li><strong>Training Loop:</strong> Feed data in batches, compute loss, backpropagate gradients, update weights</li>
                    <li><strong>Validation:</strong> Test on held-out data to prevent overfitting</li>
                    <li><strong>Hyperparameter Tuning:</strong> Adjust learning rate, batch size, regularization</li>
                    <li><strong>Model Evaluation:</strong> Measure accuracy, precision, recall on test set</li>
                    <li><strong>Model Export:</strong> Save trained weights for inference</li>
                </ol>
                
                <h4>Example Training Setup:</h4>
                <pre>
Training Pipeline:
Raw Data → Data Preprocessing → Feature Engineering
    ↓
Training Script (Python/PyTorch/TensorFlow)
    ↓
GPU Cluster (AWS EC2 p3 instances, SageMaker)
    ↓
Experiment Tracking (MLflow, Weights & Biases)
    ↓
Model Registry → Store best model artifacts
    ↓
CI/CD Pipeline → Deploy to production
                </pre>
                
                <h4>Inference (Production Use):</h4>
                <ul>
                    <li>🚀 Using trained model to make predictions on NEW data</li>
                    <li>🚀 Model parameters are FROZEN (no learning)</li>
                    <li>🚀 Optimized for low latency (milliseconds)</li>
                    <li>🚀 Handles real-time requests from users</li>
                    <li>🚀 Focus: speed, scalability, cost efficiency</li>
                </ul>
                
                <h4>Inference Example Flow:</h4>
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
                
                <h4>Real-World Example:</h4>
                <p><strong>Training:</strong> "I trained a recommendation model on 10 million user interactions using PyTorch on 4 GPUs. Training took 12 hours and we achieved 85% accuracy."</p>
                <p><strong>Inference:</strong> "We deployed the model using TorchServe on AWS ECS. It handles 1000 requests/second with p95 latency under 50ms. We use CPU instances since inference is less compute-intensive."</p>
                
                <h3 style="margin-top: 30px;">💰 Inference Cost Optimization: RAG with Rerankers</h3>
                
                <h4>The Challenge:</h4>
                <p>LLM inference is expensive - you pay per token (input + output). Large context windows = high costs.</p>
                
                <h4>The Solution: Retrieval Augmented Generation (RAG) with Reranking</h4>
                
                <p><strong>Without Reranker (Expensive):</strong></p>
                <pre>
Retrieve 50 documents → Send ALL 50 to LLM
50 docs × 500 tokens = 25,000 tokens
Cost: 💰💰💰 (High)
                </pre>
                
                <p><strong>With Reranker (Cost-Efficient):</strong></p>
                <pre>
Retrieve 50 documents (cast wide net)
    ↓
Amazon Bedrock Reranker (cheap 💰)
    ↓
Send ONLY top 3-5 to LLM
3 docs × 500 tokens = 1,500 tokens
Cost Reduction: ~94% 💰
                </pre>
                
                <h4>🏗️ AWS Production Pattern:</h4>
                <p><strong>Step 1: Hybrid Search (Retrieval Phase)</strong></p>
                <ul>
                    <li>Use <strong>Amazon OpenSearch Serverless</strong> (no cluster management)</li>
                    <li><strong>Vector embeddings</strong> for semantic search (finds similar meaning)</li>
                    <li><strong>Keyword matching</strong> for exact terms (lexical search)</li>
                    <li>Retrieve 50-100 documents for high recall</li>
                </ul>
                
                <p><strong>Step 2: Reranking (Precision Phase)</strong></p>
                <ul>
                    <li>Use <strong>Amazon Bedrock Reranker Models</strong> (fully managed)</li>
                    <li>Scores all retrieved docs by semantic relevance</li>
                    <li>Reorders results - best matches first</li>
                    <li>Select top 3-5 most relevant documents</li>
                    <li>Reranker cost << 1% of LLM inference cost</li>
                </ul>
                
                <p><strong>Step 3: LLM Inference (Generation Phase)</strong></p>
                <ul>
                    <li>Send only top-ranked docs to LLM (Amazon Bedrock)</li>
                    <li>Small, relevant context = low token count</li>
                    <li>Better answers + lower cost</li>
                </ul>
                
                <h4>Why This Pattern?</h4>
                <table style="width:100%; border-collapse: collapse; margin-top: 10px;">
                    <tr style="background: #f0f0f0;">
                        <th style="padding: 10px; text-align: left;">Component</th>
                        <th style="padding: 10px; text-align: left;">Benefit</th>
                    </tr>
                    <tr>
                        <td style="padding: 10px;"><strong>Hybrid Search</strong></td>
                        <td style="padding: 10px;">High recall - finds all relevant docs</td>
                    </tr>
                    <tr style="background: #f9f9f9;">
                        <td style="padding: 10px;"><strong>Reranker</strong></td>
                        <td style="padding: 10px;">High precision - filters to best matches</td>
                    </tr>
                    <tr>
                        <td style="padding: 10px;"><strong>OpenSearch Serverless</strong></td>
                        <td style="padding: 10px;">Zero ops overhead - no cluster management</td>
                    </tr>
                    <tr style="background: #f9f9f9;">
                        <td style="padding: 10px;"><strong>Bedrock Reranker</strong></td>
                        <td style="padding: 10px;">Fully managed - no model hosting</td>
                    </tr>
                </table>
                
                <h4>📊 Cost Comparison:</h4>
                <p>Example: 1 million queries/month</p>
                <ul>
                    <li><strong>Without Reranker:</strong> $5,000/month (25K tokens × $0.0002/token × 1M queries)</li>
                    <li><strong>With Reranker:</strong> $350/month ($300 LLM + $50 reranker)</li>
                    <li><strong>Savings:</strong> 93% = $4,650/month = $55,800/year</li>
                </ul>
                
                <h3 style="margin-top: 30px;">🏢 Alternative: Amazon Kendra Intelligent Ranking</h3>
                
                <h4>When to Use Kendra vs Bedrock Reranker?</h4>
                
                <table style="width:100%; border-collapse: collapse; margin-top: 10px;">
                    <tr style="background: #667eea; color: white;">
                        <th style="padding: 10px; text-align: left;">Feature</th>
                        <th style="padding: 10px; text-align: left;">Kendra Intelligent Ranking</th>
                        <th style="padding: 10px; text-align: left;">Bedrock Reranker</th>
                    </tr>
                    <tr>
                        <td style="padding: 10px;"><strong>Focus</strong></td>
                        <td style="padding: 10px;">Enterprise search, document retrieval</td>
                        <td style="padding: 10px;">General-purpose reranking for RAG</td>
                    </tr>
                    <tr style="background: #f9f9f9;">
                        <td style="padding: 10px;"><strong>Integration</strong></td>
                        <td style="padding: 10px;">Works with ANY search engine</td>
                        <td style="padding: 10px;">OpenSearch, custom systems</td>
                    </tr>
                    <tr>
                        <td style="padding: 10px;"><strong>Best For</strong></td>
                        <td style="padding: 10px;">Internal wikis, knowledge bases, helpdesk</td>
                        <td style="padding: 10px;">Chatbots, Q&A, general RAG</td>
                    </tr>
                    <tr style="background: #f9f9f9;">
                        <td style="padding: 10px;"><strong>Deployment</strong></td>
                        <td style="padding: 10px;">API service (bring your own search)</td>
                        <td style="padding: 10px;">Integrated with Knowledge Bases</td>
                    </tr>
                </table>
                
                <h4 style="margin-top: 20px;">🔄 Kendra + SageMaker JumpStart Pattern</h4>
                
                <p><strong>Use Case:</strong> Enterprise search with quick model deployment</p>
                
                <pre>
User Query: "How do I reduce ML inference costs?"
    ↓
[1] Initial Search (Elasticsearch/OpenSearch/Custom)
    → Retrieves 50 docs (keyword + vector search)
    ↓
[2] Amazon Kendra Intelligent Ranking
    → Reranks by semantic relevance
    → Understands natural language intent
    → Returns top 5-10 docs
    ↓
[3] SageMaker JumpStart Foundation Model
    → Pre-trained LLM (no training needed!)
    → Generate answer from top-ranked docs
    ↓
Final Answer
                </pre>
                
                <h4>Why Kendra + JumpStart?</h4>
                <ul>
                    <li>✅ <strong>Works with existing search:</strong> Don't rebuild infrastructure</li>
                    <li>✅ <strong>JumpStart = Fast deployment:</strong> Pre-trained models, no ML expertise</li>
                    <li>✅ <strong>Enterprise-grade:</strong> Handles complex documents</li>
                    <li>✅ <strong>Semantic understanding:</strong> Beyond keyword matching</li>
                </ul>
                
                <h4>Real Example - Enterprise Knowledge Base:</h4>
                <p><em>"We had 50,000 internal documents in OpenSearch. Instead of rebuilding, I added Amazon Kendra Intelligent Ranking API to reorder results by relevance. Then deployed a Flan-T5 model from SageMaker JumpStart to generate answers from top-ranked docs. Time-to-relevant-answer decreased 60%, user satisfaction improved 40%. Total setup time: 2 weeks vs 3 months for custom solution."</em></p>
                
                <h3 style="margin-top: 30px;">📝 Amazon Bedrock Prompt Management</h3>
                
                <h4>What is Prompt Management?</h4>
                <p>Centralized storage, versioning, and optimization of prompts for LLM inference. Instead of hardcoding prompts in your application, manage them as reusable assets.</p>
                
                <h4>Key Features:</h4>
                
                <table style="width:100%; border-collapse: collapse; margin-top: 10px;">
                    <tr style="background: #667eea; color: white;">
                        <th style="padding: 10px; text-align: left;">Feature</th>
                        <th style="padding: 10px; text-align: left;">Purpose</th>
                        <th style="padding: 10px; text-align: left;">Benefit</th>
                    </tr>
                    <tr>
                        <td style="padding: 10px;"><strong>Prompt Templates</strong></td>
                        <td style="padding: 10px;">Reusable prompt patterns with variables</td>
                        <td style="padding: 10px;">Consistency across team</td>
                    </tr>
                    <tr style="background: #f9f9f9;">
                        <td style="padding: 10px;"><strong>Versioning</strong></td>
                        <td style="padding: 10px;">Track changes, rollback if needed</td>
                        <td style="padding: 10px;">Safe experimentation</td>
                    </tr>
                    <tr>
                        <td style="padding: 10px;"><strong>Variants</strong></td>
                        <td style="padding: 10px;">Multiple versions for different models</td>
                        <td style="padding: 10px;">Optimize per FM family</td>
                    </tr>
                    <tr style="background: #f9f9f9;">
                        <td style="padding: 10px;"><strong>A/B Testing</strong></td>
                        <td style="padding: 10px;">Compare prompt performance</td>
                        <td style="padding: 10px;">Data-driven optimization</td>
                    </tr>
                </table>
                
                <h4 style="margin-top: 20px;">Creating a Managed Prompt:</h4>
                <pre>
import boto3
import json

client = boto3.client('bedrock-agent')

# Create prompt with multiple variants
response = client.create_prompt(
    name="rag-query-prompt",
    description="Optimized RAG query prompt",
    variants=[
        {
            "name": "claude-variant",
            "modelId": "anthropic.claude-3-sonnet-v1",
            "templateConfiguration": {
                "text": {
                    "text": "You are a helpful assistant.\\n\\nContext: {{context}}\\n\\nQuestion: {{question}}\\n\\nPlease provide a detailed answer based on the context."
                }
            }
        },
        {
            "name": "titan-variant",
            "modelId": "amazon.titan-text-express-v1",
            "templateConfiguration": {
                "text": {
                    "text": "Context: {{context}}\\nQ: {{question}}\\nA:"
                }
            }
        }
    ]
)

# Use the prompt
prompt_arn = response['arn']
                </pre>
                
                <h4>Cross-Model Usage:</h4>
                
                <p><strong>✅ Can You Use Same Prompt Across Different FM Families?</strong></p>
                <p><strong>Yes!</strong> But with considerations:</p>
                
                <ul>
                    <li>✅ <strong>Same template CAN work</strong> across Claude, Titan, Cohere, etc.</li>
                    <li>⚠️ <strong>Performance varies</strong> - each model has optimal prompt format</li>
                    <li>✅ <strong>Best practice:</strong> Create variants optimized per model family</li>
                    <li>✅ <strong>Prompt Flows:</strong> Can chain different models together</li>
                </ul>
                
                <table style="width:100%; border-collapse: collapse; margin-top: 10px;">
                    <tr style="background: #f0f0f0;">
                        <th style="padding: 10px; text-align: left;">Model Family</th>
                        <th style="padding: 10px; text-align: left;">Prompt Style Preference</th>
                    </tr>
                    <tr>
                        <td style="padding: 10px;"><strong>Claude (Anthropic)</strong></td>
                        <td style="padding: 10px;">Detailed instructions, conversational</td>
                    </tr>
                    <tr style="background: #f9f9f9;">
                        <td style="padding: 10px;"><strong>Titan (Amazon)</strong></td>
                        <td style="padding: 10px;">Concise, direct formatting</td>
                    </tr>
                    <tr>
                        <td style="padding: 10px;"><strong>Cohere</strong></td>
                        <td style="padding: 10px;">Clear structure with separators</td>
                    </tr>
                    <tr style="background: #f9f9f9;">
                        <td style="padding: 10px;"><strong>Meta Llama</strong></td>
                        <td style="padding: 10px;">System/user message format</td>
                    </tr>
                </table>
                
                <h4 style="margin-top: 20px;">🔄 Prompt Flows (Advanced)</h4>
                <p>Visual builder to chain multiple prompts and models:</p>
                
                <pre>
User Input
    ↓
[Step 1] Claude: Understand intent & extract entities
    ↓
[Step 2] Vector Search: Find relevant docs
    ↓
[Step 3] Titan: Summarize documents
    ↓
[Step 4] Claude: Generate final answer
    ↓
Response
                </pre>
                
                <p><strong>Benefits:</strong></p>
                <ul>
                    <li>✅ Mix different models (not locked to one family)</li>
                    <li>✅ Add conditional logic</li>
                    <li>✅ Visual workflow management</li>
                    <li>✅ Built-in error handling</li>
                </ul>
                
                <h4>💰 Cost & Quality Benefits:</h4>
                <ul>
                    <li><strong>Token Optimization:</strong> Test prompts to find shortest effective version</li>
                    <li><strong>Model Selection:</strong> Use cheaper models for simple tasks, expensive for complex</li>
                    <li><strong>Version Control:</strong> Roll back if new prompt degrades quality</li>
                    <li><strong>Team Consistency:</strong> Everyone uses tested, approved prompts</li>
                </ul>
                
                <h4>🎯 Interview Talking Point:</h4>
                <p>"I use Amazon Bedrock Prompt Management to centralize our RAG prompts. We have variants optimized for Claude and Titan - Claude gets detailed instructions, Titan gets concise format. This improved response quality by 25% and reduced tokens by 15%. Prompt versioning lets us A/B test changes safely, and the whole data science team shares the same tested prompts instead of everyone maintaining their own."</p>
                
                <h4>🎯 Interview Talking Points:</h4>
                <p><strong>For RAG Chatbots:</strong> "I use Bedrock Reranker with Knowledge Bases for a fully managed, serverless RAG pipeline with tight LLM integration."</p>
                <p><strong>For Enterprise Search:</strong> "I use Amazon Kendra Intelligent Ranking with our existing search infrastructure and SageMaker JumpStart models for quick deployment without training."</p>
                """,
                "practice_prompts": [
                    "Explain inference to a non-technical person",
                    "Describe the request-response flow for a prediction",
                    "Walk through your experience with training a model from start to finish",
                    "How would you optimize LLM inference costs in a RAG system?",
                    "When would you choose Kendra vs Bedrock for reranking?",
                    "How do you manage prompts across different Bedrock foundation models?"
                ]
            },
            {
                "id": 2,
                "title": "Training Frameworks vs Inference Runtimes",
                "content": """
                <h3>⚠️ Key Distinction: Training ≠ Inference Tools</h3>
                
                <h4>Training Frameworks (Feature-Rich, Heavy)</h4>
                <p>Used for model development and training:</p>
                
                <table style="width:100%; border-collapse: collapse; margin-top: 10px;">
                    <tr style="background: #f0f0f0;">
                        <th style="padding: 10px; text-align: left;">Framework</th>
                        <th style="padding: 10px; text-align: left;">Purpose</th>
                    </tr>
                    <tr>
                        <td style="padding: 10px;"><strong>TensorFlow</strong></td>
                        <td style="padding: 10px;">Define models, training loops, backprop, optimization</td>
                    </tr>
                    <tr style="background: #f9f9f9;">
                        <td style="padding: 10px;"><strong>PyTorch</strong></td>
                        <td style="padding: 10px;">Research-friendly, dynamic computation graphs</td>
                    </tr>
                    <tr>
                        <td style="padding: 10px;"><strong>SageMaker Training</strong></td>
                        <td style="padding: 10px;">Managed training: GPU clusters, distributed training</td>
                    </tr>
                </table>
                
                <h4 style="margin-top: 20px;">❌ Why NOT Use Training Frameworks for Inference?</h4>
                <ul>
                    <li>❌ Large dependencies (GBs of libraries)</li>
                    <li>❌ Slow startup time</li>
                    <li>❌ High memory footprint</li>
                    <li>❌ Python overhead</li>
                    <li>❌ Not optimized for low latency</li>
                </ul>
                
                <h3 style="margin-top: 30px;">✅ Inference Runtimes (Optimized, Fast)</h3>
                
                <table style="width:100%; border-collapse: collapse; margin-top: 10px;">
                    <tr style="background: #667eea; color: white;">
                        <th style="padding: 10px; text-align: left;">Training Framework</th>
                        <th style="padding: 10px; text-align: left;">→</th>
                        <th style="padding: 10px; text-align: left;">Inference Runtime</th>
                        <th style="padding: 10px; text-align: left;">Speed Gain</th>
                    </tr>
                    <tr>
                        <td style="padding: 10px;">TensorFlow</td>
                        <td style="padding: 10px;">→</td>
                        <td style="padding: 10px;"><strong>TensorFlow Serving</strong></td>
                        <td style="padding: 10px;">2-3x faster</td>
                    </tr>
                    <tr style="background: #f9f9f9;">
                        <td style="padding: 10px;">TensorFlow</td>
                        <td style="padding: 10px;">→</td>
                        <td style="padding: 10px;"><strong>TensorFlow Lite</strong></td>
                        <td style="padding: 10px;">Mobile/Edge</td>
                    </tr>
                    <tr>
                        <td style="padding: 10px;">PyTorch</td>
                        <td style="padding: 10px;">→</td>
                        <td style="padding: 10px;"><strong>TorchServe</strong></td>
                        <td style="padding: 10px;">2-3x faster</td>
                    </tr>
                    <tr style="background: #f9f9f9;">
                        <td style="padding: 10px;">PyTorch</td>
                        <td style="padding: 10px;">→</td>
                        <td style="padding: 10px;"><strong>TorchScript</strong></td>
                        <td style="padding: 10px;">No Python overhead</td>
                    </tr>
                    <tr>
                        <td style="padding: 10px;">Any</td>
                        <td style="padding: 10px;">→</td>
                        <td style="padding: 10px;"><strong>ONNX Runtime</strong></td>
                        <td style="padding: 10px;">Cross-platform, 2-5x</td>
                    </tr>
                    <tr style="background: #f9f9f9;">
                        <td style="padding: 10px;">Any</td>
                        <td style="padding: 10px;">→</td>
                        <td style="padding: 10px;"><strong>NVIDIA TensorRT</strong></td>
                        <td style="padding: 10px;">GPU optimized, 5-10x</td>
                    </tr>
                    <tr>
                        <td style="padding: 10px;">Any</td>
                        <td style="padding: 10px;">→</td>
                        <td style="padding: 10px;"><strong>AWS Neuron</strong></td>
                        <td style="padding: 10px;">Inferentia chips, 70% cost reduction</td>
                    </tr>
                </table>
                
                <h3 style="margin-top: 30px;">🏗️ Popular Production Serving Tools</h3>
                
                <h4>🔹 TensorFlow Serving</h4>
                <p>Google's production-grade serving system</p>
                <ul>
                    <li>REST and gRPC APIs</li>
                    <li>Model versioning and hot-swapping</li>
                    <li>Request batching for throughput</li>
                </ul>
                
                <h4>🔹 TorchServe</h4>
                <p>PyTorch's official serving framework</p>
                <ul>
                    <li>Multi-model serving</li>
                    <li>A/B testing support</li>
                    <li>Built-in metrics and logging</li>
                </ul>
                
                <h4>🔹 AWS SageMaker Inference</h4>
                <p>Fully managed, multiple options:</p>
                <ul>
                    <li><strong>Real-time Endpoints:</strong> ml.c5 (CPU), ml.inf1 (Inferentia), ml.g5 (GPU)</li>
                    <li><strong>Serverless:</strong> Pay per invocation, auto-scales</li>
                    <li><strong>Async:</strong> Batch processing for non-real-time</li>
                    <li>Auto-scaling, monitoring, A/B testing built-in</li>
                </ul>
                
                <h4>🔹 NVIDIA Triton Inference Server</h4>
                <p>Multi-framework, GPU-optimized</p>
                <ul>
                    <li>Supports TensorFlow, PyTorch, ONNX, TensorRT</li>
                    <li>Dynamic batching</li>
                    <li>GPU memory optimization</li>
                    <li>Model ensembles</li>
                </ul>
                
                <h4>🎯 Interview Talking Point:</h4>
                <p>"For production inference, I don't use TensorFlow or PyTorch directly - they're designed for training. Instead, I export models to optimized runtimes like TensorFlow Serving or ONNX Runtime, which are 2-5x faster and have lower latency. For AWS deployments, I use SageMaker real-time endpoints with Inferentia instances for 70% cost savings compared to GPU instances."</p>
                """,
                "practice_prompts": [
                    "Why shouldn't you use PyTorch directly for production inference?",
                    "Which serving tool would you choose for a high-traffic API?",
                    "How would you handle model versioning in production?"
                ]
            },
            {
                "id": 3,
                "title": "Model Optimization & Production Challenges",
                "content": """
                <h3>🚀 Model Optimization Techniques</h3>
                
                <h4>1️⃣ Quantization (Reduce Precision)</h4>
                <p><strong>What:</strong> Convert model weights from 32-bit floats to 8-bit integers</p>
                <p><strong>Benefits:</strong></p>
                <ul>
                    <li>4x smaller model size (1GB → 250MB)</li>
                    <li>4x faster inference</li>
                    <li>Lower memory usage</li>
                    <li>Minimal accuracy loss (typically <1%)</li>
                </ul>
                
                <p><strong>Example (PyTorch):</strong></p>
                <pre>
import torch
model = MyModel()  # 1GB, 32-bit

# Quantize to 8-bit
quantized_model = torch.quantization.quantize_dynamic(
    model, {torch.nn.Linear}, dtype=torch.qint8
)  # 250MB, 4x faster
                </pre>
                
                <h4 style="margin-top: 20px;">2️⃣ Pruning (Remove Weights)</h4>
                <p><strong>What:</strong> Remove unnecessary connections/weights from the model</p>
                <p><strong>Benefits:</strong></p>
                <ul>
                    <li>30-50% smaller model</li>
                    <li>Faster inference</li>
                    <li>Can prune 80-90% of weights with minimal accuracy loss</li>
                </ul>
                
                <h4 style="margin-top: 20px;">3️⃣ Knowledge Distillation</h4>
                <p><strong>What:</strong> Train a small model to mimic a large model</p>
                <p><strong>Benefits:</strong></p>
                <ul>
                    <li>10-100x smaller model</li>
                    <li>10-100x faster inference</li>
                    <li>Example: BERT (340M params) → DistilBERT (66M params), 97% accuracy retained</li>
                </ul>
                
                <h4 style="margin-top: 20px;">4️⃣ Model Export to Optimized Formats</h4>
                
                <p><strong>ONNX (Open Neural Network Exchange):</strong></p>
                <pre>
# Export PyTorch to ONNX
torch.onnx.export(model, dummy_input, "model.onnx")

# Deploy with ONNX Runtime (2-5x faster than PyTorch)
import onnxruntime
session = onnxruntime.InferenceSession("model.onnx")
outputs = session.run(None, {"input": data})
                </pre>
                
                <p><strong>TensorRT (NVIDIA GPU acceleration):</strong></p>
                <ul>
                    <li>5-10x faster than native frameworks</li>
                    <li>Optimizes for specific GPU architecture</li>
                    <li>Combines multiple operations (kernel fusion)</li>
                </ul>
                
                <h3 style="margin-top: 30px;">💰 AWS Compute Options for Inference</h3>
                
                <table style="width:100%; border-collapse: collapse; margin-top: 10px;">
                    <tr style="background: #f0f0f0;">
                        <th style="padding: 10px; text-align: left;">Instance Type</th>
                        <th style="padding: 10px; text-align: left;">Use Case</th>
                        <th style="padding: 10px; text-align: left;">Cost</th>
                    </tr>
                    <tr>
                        <td style="padding: 10px;"><strong>ml.c5.xlarge</strong></td>
                        <td style="padding: 10px;">CPU inference, small models</td>
                        <td style="padding: 10px;">💰 (Cheapest)</td>
                    </tr>
                    <tr style="background: #f9f9f9;">
                        <td style="padding: 10px;"><strong>ml.inf1</strong></td>
                        <td style="padding: 10px;">AWS Inferentia chips, optimized ML</td>
                        <td style="padding: 10px;">💰💰 (70% less than GPU)</td>
                    </tr>
                    <tr>
                        <td style="padding: 10px;"><strong>ml.g5</strong></td>
                        <td style="padding: 10px;">GPU inference, large models</td>
                        <td style="padding: 10px;">💰💰💰 (Expensive)</td>
                    </tr>
                    <tr style="background: #f9f9f9;">
                        <td style="padding: 10px;"><strong>Serverless</strong></td>
                        <td style="padding: 10px;">Variable traffic, pay-per-use</td>
                        <td style="padding: 10px;">💰 (Only when used)</td>
                    </tr>
                </table>
                
                <h3 style="margin-top: 30px;">⚡ Other Optimization Strategies</h3>
                
                <h4>🎯 Latency Optimization</h4>
                <ul>
                    <li><strong>Request Batching:</strong> Process multiple requests together (higher throughput)</li>
                    <li><strong>Model Caching:</strong> Keep model loaded in memory</li>
                    <li><strong>Response Caching:</strong> Cache frequent predictions (Redis)</li>
                    <li><strong>Warm Pools:</strong> Pre-warmed instances to avoid cold starts</li>
                </ul>
                
                <h4>🎯 Scalability</h4>
                <ul>
                    <li>Auto-scaling based on request volume</li>
                    <li>Load balancing across multiple instances</li>
                    <li>Multi-region deployment for global users</li>
                    <li>Edge deployment (CloudFront, Lambda@Edge)</li>
                </ul>
                
                <h3 style="margin-top: 30px;">🌍 High Availability: Amazon Bedrock Cross-Region Inference</h3>
                
                <p><strong>What It Is:</strong> Automatic routing of inference requests across AWS regions for high availability and throughput</p>
                
                <h4>When to Use:</h4>
                <ul>
                    <li>✅ High-traffic production systems (avoid throttling)</li>
                    <li>✅ Need 99.9%+ availability</li>
                    <li>✅ Using LLMs from Bedrock (Claude, Titan, etc.)</li>
                    <li>✅ Want automatic failover without custom code</li>
                </ul>
                
                <h4>Prerequisites:</h4>
                <ol>
                    <li><strong>Use Inference Profiles</strong> (not direct model IDs)</li>
                    <li><strong>Model must support cross-region</strong> (Claude, Titan, most foundation models)</li>
                    <li><strong>Latest Bedrock SDK</strong></li>
                    <li><strong>IAM permissions</strong> for bedrock:InvokeModel</li>
                </ol>
                
                <h4>How to Enable:</h4>
                
                <table style="width:100%; border-collapse: collapse; margin-top: 10px;">
                    <tr style="background: #f0f0f0;">
                        <th style="padding: 10px; text-align: left;">Type</th>
                        <th style="padding: 10px; text-align: left;">Model ID Format</th>
                        <th style="padding: 10px; text-align: left;">Cross-Region?</th>
                    </tr>
                    <tr>
                        <td style="padding: 10px;"><strong>Direct Model</strong></td>
                        <td style="padding: 10px;"><code>anthropic.claude-3-sonnet-v1</code></td>
                        <td style="padding: 10px;">❌ Single region only</td>
                    </tr>
                    <tr style="background: #f9f9f9;">
                        <td style="padding: 10px;"><strong>Inference Profile</strong></td>
                        <td style="padding: 10px;"><code>us.anthropic.claude-3-sonnet-v1</code></td>
                        <td style="padding: 10px;">✅ Auto cross-region</td>
                    </tr>
                </table>
                
                <p style="margin-top: 15px;"><strong>Python Example:</strong></p>
                <pre>
import boto3
import json

client = boto3.client('bedrock-runtime', region_name='us-east-1')

# ❌ Single-region (old way)
# model_id = "anthropic.claude-3-sonnet-v1"

# ✅ Cross-region inference profile (new way)
model_id = "us.anthropic.claude-3-sonnet-v1"
         # ↑ "us." prefix enables cross-region

response = client.invoke_model(
    modelId=model_id,
    body=json.dumps({
        "prompt": "What is ML inference optimization?",
        "max_tokens": 500
    })
)
                </pre>
                
                <h4>How It Works:</h4>
                <pre>
Your Application
    ↓
API call with profile: "us.anthropic.claude-v2"
    ↓
AWS Bedrock Service (automatic routing)
    ├─ Try us-east-1 ✅ Available
    ├─ If throttled → us-west-2 ✅
    └─ If throttled → us-east-2 ✅
    ↓
Response from available region
                </pre>
                
                <h4>Available Inference Profile Prefixes:</h4>
                <ul>
                    <li><strong>us.*</strong> - US regions (us-east-1, us-west-2, etc.)</li>
                    <li><strong>eu.*</strong> - European regions</li>
                    <li><strong>ap.*</strong> - Asia-Pacific regions</li>
                </ul>
                
                <h4>Benefits:</h4>
                <table style="width:100%; border-collapse: collapse; margin-top: 10px;">
                    <tr style="background: #f0f0f0;">
                        <th style="padding: 10px; text-align: left;">Feature</th>
                        <th style="padding: 10px; text-align: left;">Benefit</th>
                    </tr>
                    <tr>
                        <td style="padding: 10px;">High Availability</td>
                        <td style="padding: 10px;">99.9%+ uptime with automatic failover</td>
                    </tr>
                    <tr style="background: #f9f9f9;">
                        <td style="padding: 10px;">Better Throughput</td>
                        <td style="padding: 10px;">No throttling from single region capacity</td>
                    </tr>
                    <tr>
                        <td style="padding: 10px;">Zero Code Changes</td>
                        <td style="padding: 10px;">Just change model ID prefix</td>
                    </tr>
                    <tr style="background: #f9f9f9;">
                        <td style="padding: 10px;">Same Pricing</td>
                        <td style="padding: 10px;">No extra cost for cross-region routing</td>
                    </tr>
                    <tr>
                        <td style="padding: 10px;">Transparent</td>
                        <td style="padding: 10px;">AWS handles all routing logic</td>
                    </tr>
                </table>
                
                <h4>Considerations:</h4>
                <ul>
                    <li>Small latency variance (different regions = different RTT)</li>
                    <li>Typically adds 5-20ms depending on region distance</li>
                    <li>Check which region handled request via response metadata</li>
                </ul>
                
                <h4>🎯 Interview Talking Point:</h4>
                <p>"For our high-availability RAG system using Amazon Bedrock, I enabled cross-region inference by using inference profiles instead of direct model IDs. Simply prefixing the model with 'us.' (e.g., <code>us.anthropic.claude-v2</code>) enables automatic failover across US regions. This improved our system availability to 99.9% and eliminated throttling issues during peak traffic, all without writing custom routing logic or managing multiple endpoints."</p>
                
                <h4>🎯 Monitoring</h4>
                <ul>
                    <li>Track prediction latency (p50, p95, p99)</li>
                    <li>Monitor model drift (input/output distributions)</li>
                    <li>Alert on errors or anomalies</li>
                    <li>A/B test model versions</li>
                    <li>Track cost per prediction</li>
                </ul>
                
                <h4>🎯 Interview Answer Example:</h4>
                <p>"To optimize inference costs, I implemented several strategies: First, I quantized our PyTorch model from 32-bit to 8-bit, reducing size by 75% and latency by 4x. Then I deployed to SageMaker Inferentia instances instead of GPUs, cutting costs by 70%. I also implemented request batching and response caching for frequent queries. Combined, these optimizations reduced our inference costs from $10K/month to $1.5K/month while maintaining 99th percentile latency under 100ms."</p>
                """,
                "practice_prompts": [
                    "How would you optimize inference latency?",
                    "Explain quantization and its benefits",
                    "What metrics would you monitor for ML inference?",
                    "Compare CPU vs GPU vs Inferentia for inference",
                    "How do you enable Amazon Bedrock cross-region inference for high availability?"
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
    },
    "platform_management": {
        "title": "ML Platform Management",
        "description": "Organize and manage ML infrastructure at scale with developer portals",
        "lessons": [
            {
                "id": 1,
                "title": "Platform Engineering for ML",
                "content": """
                <h3>🏗️ What is ML Platform Management?</h3>
                
                <p>ML Platform Management = Providing <strong>self-service tools</strong> for data scientists and ML engineers to:</p>
                <ul>
                    <li>Discover and deploy models</li>
                    <li>Access documentation and APIs</li>
                    <li>Monitor performance and costs</li>
                    <li>Manage model lifecycle</li>
                    <li>Standardize workflows</li>
                </ul>
                
                <h4>⚠️ Key Distinction:</h4>
                <table style="width:100%; border-collapse: collapse; margin-top: 10px;">
                    <tr style="background: #f0f0f0;">
                        <th style="padding: 10px; text-align: left;">Layer</th>
                        <th style="padding: 10px; text-align: left;">Purpose</th>
                        <th style="padding: 10px; text-align: left;">Tools</th>
                    </tr>
                    <tr>
                        <td style="padding: 10px;"><strong>Platform Layer</strong></td>
                        <td style="padding: 10px;">Organize, manage, discover</td>
                        <td style="padding: 10px;">Backstage, Portals, Catalogs</td>
                    </tr>
                    <tr style="background: #f9f9f9;">
                        <td style="padding: 10px;"><strong>Execution Layer</strong></td>
                        <td style="padding: 10px;">Actually run models</td>
                        <td style="padding: 10px;">TorchServe, SageMaker, Triton</td>
                    </tr>
                </table>
                
                <h3 style="margin-top: 30px;">🎭 Backstage: Developer Portal for ML</h3>
                
                <h4>What is Backstage?</h4>
                <p><strong>Backstage</strong> (by Spotify) is an open-source <strong>developer portal platform</strong> for:</p>
                <ul>
                    <li>📚 Service catalogs - discover all models and services</li>
                    <li>📖 Centralized documentation</li>
                    <li>🚀 Self-service deployment templates</li>
                    <li>📊 Infrastructure visibility</li>
                </ul>
                
                <h4>❌ What Backstage Does NOT Do:</h4>
                <ul>
                    <li>❌ Does NOT serve ML models</li>
                    <li>❌ Does NOT run inference</li>
                    <li>❌ Does NOT replace TorchServe or SageMaker</li>
                    <li>❌ Does NOT execute predictions</li>
                </ul>
                
                <h4>✅ What Backstage DOES for ML:</h4>
                
                <p><strong>1. Model Catalog & Discovery</strong></p>
                <pre>
# catalog-info.yaml
apiVersion: backstage.io/v1alpha1
kind: Component
metadata:
  name: fraud-detection-model-v2
  description: XGBoost fraud detection
  tags: [ml, production, inference]
spec:
  type: ml-model
  owner: ml-team
  lifecycle: production
  metadata:
    model_version: "2.1.0"
    framework: "xgboost"
    endpoint: "https://api.company.com/fraud/predict"
    sla: "p99 < 50ms"
    cost_per_month: "$500"
                </pre>
                
                <h4 style="margin-top: 20px;">⚠️ Important: Two Types of YAML Files</h4>
                
                <table style="width:100%; border-collapse: collapse; margin-top: 10px;">
                    <tr style="background: #667eea; color: white;">
                        <th style="padding: 10px; text-align: left;">YAML Type</th>
                        <th style="padding: 10px; text-align: left;">Purpose</th>
                        <th style="padding: 10px; text-align: left;">Where It Lives</th>
                    </tr>
                    <tr>
                        <td style="padding: 10px;"><strong>catalog-info.yaml</strong></td>
                        <td style="padding: 10px;">Describe models/services in Backstage catalog</td>
                        <td style="padding: 10px;">Your Git repos (with model code)</td>
                    </tr>
                    <tr style="background: #f9f9f9;">
                        <td style="padding: 10px;"><strong>Kubernetes YAML</strong></td>
                        <td style="padding: 10px;">Deploy Backstage platform itself</td>
                        <td style="padding: 10px;">Kubernetes cluster</td>
                    </tr>
                </table>
                
                <p style="margin-top: 15px;"><strong>Example: Deploying Backstage on Kubernetes</strong></p>
                <pre>
# Option 1: Helm Chart (Easiest)
helm repo add backstage https://backstage.github.io/charts
helm install backstage backstage/backstage

# Option 2: Kubernetes Manifests
kubectl apply -f backstage-deployment.yaml
kubectl apply -f backstage-service.yaml
                </pre>
                
                <p><strong>Complete Setup Flow:</strong></p>
                <pre>
┌─────────────────────────────────────────┐
│   Kubernetes Cluster                    │
│                                         │
│  ┌───────────────────────────────┐     │
│  │  Backstage Pod (Platform)     │     │
│  │  - Deployed via Helm/K8s      │     │
│  │  - Reads catalog-info.yaml    │     │
│  │  - Port 7007                   │     │
│  └───────────────────────────────┘     │
│         ↓ (reads)                       │
│  catalog-info.yaml files in Git repos  │
│         ↓                               │
│  ┌───────────────────────────────┐     │
│  │  Your ML Models               │     │
│  │  TorchServe / SageMaker       │     │
│  └───────────────────────────────┘     │
└─────────────────────────────────────────┘
                </pre>
                
                <p><strong>3-Step Setup Process:</strong></p>
                <ol>
                    <li><strong>Deploy Backstage:</strong> <code>helm install backstage backstage/backstage</code></li>
                    <li><strong>Add catalog-info.yaml to model repos:</strong> Describe each model</li>
                    <li><strong>Register with Backstage:</strong> Point to your Git repos with catalog files</li>
                </ol>
                
                <p><strong>2. Self-Service Deployment</strong></p>
                <ul>
                    <li>Click "Deploy Model" in UI</li>
                    <li>Fill in template (model name, version, resources)</li>
                    <li>Automatically creates CI/CD pipeline</li>
                    <li>Deploys to SageMaker/Kubernetes</li>
                </ul>
                
                <p><strong>3. Centralized Documentation</strong></p>
                <ul>
                    <li>Model cards (metadata, performance)</li>
                    <li>API documentation</li>
                    <li>Training data lineage</li>
                    <li>Version history</li>
                </ul>
                
                <p><strong>4. Monitoring Integration</strong></p>
                <ul>
                    <li>Links to Grafana/Datadog dashboards</li>
                    <li>Model metrics (latency, drift, accuracy)</li>
                    <li>Cost tracking</li>
                    <li>Alerts and incidents</li>
                </ul>
                
                <h4>🔄 Complete Architecture:</h4>
                <pre>
Data Scientist → Backstage Portal
                      ↓
            [Service Catalog]
            View 50+ ML models
            See APIs, metrics, docs
                      ↓
         Click "Deploy New Model"
                      ↓
         Triggers GitLab Actions
                      ↓
              Deploys to:
    ├─ TorchServe (runs inference)
    ├─ SageMaker (runs inference)
    └─ Triton/K8s (runs inference)
                      ↓
         Model serves predictions
                </pre>
                
                <h4>📊 Real-World Example:</h4>
                <p><em>"I built an ML platform with Backstage as the front door. Data scientists discover all 50+ deployed models, view APIs, see real-time metrics, and deploy new versions through self-service templates. Behind the scenes, models run on SageMaker endpoints and TorchServe, but Backstage provides the unified interface. This reduced deployment time from 2 weeks to 2 hours and improved model discoverability across 5 teams."</em></p>
                """,
                "practice_prompts": [
                    "Explain the difference between a platform layer and execution layer",
                    "How would you help data scientists discover and deploy models?",
                    "Describe your approach to ML infrastructure management",
                    "What's the difference between catalog-info.yaml and Kubernetes deployment YAML?",
                    "How would you deploy Backstage on Kubernetes?"
                ]
            },
            {
                "id": 2,
                "title": "Platform Tools Ecosystem",
                "content": """
                <h3>🧰 Common Platform Management Tools</h3>
                
                <table style="width:100%; border-collapse: collapse; margin-top: 10px;">
                    <tr style="background: #667eea; color: white;">
                        <th style="padding: 10px; text-align: left;">Tool</th>
                        <th style="padding: 10px; text-align: left;">Purpose</th>
                        <th style="padding: 10px; text-align: left;">Use Case</th>
                    </tr>
                    <tr>
                        <td style="padding: 10px;"><strong>Backstage</strong></td>
                        <td style="padding: 10px;">Developer portal, service catalog</td>
                        <td style="padding: 10px;">Centralized ML infrastructure management</td>
                    </tr>
                    <tr style="background: #f9f9f9;">
                        <td style="padding: 10px;"><strong>MLflow</strong></td>
                        <td style="padding: 10px;">Experiment tracking, model registry</td>
                        <td style="padding: 10px;">Track training runs, manage model versions</td>
                    </tr>
                    <tr>
                        <td style="padding: 10px;"><strong>Kubeflow</strong></td>
                        <td style="padding: 10px;">ML workflows on Kubernetes</td>
                        <td style="padding: 10px;">End-to-end ML pipelines</td>
                    </tr>
                    <tr style="background: #f9f9f9;">
                        <td style="padding: 10px;"><strong>Metaflow</strong></td>
                        <td style="padding: 10px;">ML workflow orchestration</td>
                        <td style="padding: 10px;">Data science pipelines (by Netflix)</td>
                    </tr>
                    <tr>
                        <td style="padding: 10px;"><strong>Weights & Biases</strong></td>
                        <td style="padding: 10px;">Experiment tracking, collaboration</td>
                        <td style="padding: 10px;">Team collaboration on ML experiments</td>
                    </tr>
                    <tr style="background: #f9f9f9;">
                        <td style="padding: 10px;"><strong>ArgoCD</strong></td>
                        <td style="padding: 10px;">GitOps continuous delivery</td>
                        <td style="padding: 10px;">Deploy models via Git</td>
                    </tr>
                </table>
                
                <h3 style="margin-top: 30px;">🎯 Platform Capabilities You Should Discuss</h3>
                
                <h4>1️⃣ Model Discovery</h4>
                <ul>
                    <li>Searchable catalog of all models</li>
                    <li>Metadata: owner, version, SLA, cost</li>
                    <li>API documentation and examples</li>
                    <li>Usage statistics</li>
                </ul>
                
                <h4>2️⃣ Self-Service Deployment</h4>
                <ul>
                    <li>Standardized templates for common patterns</li>
                    <li>One-click deployment to dev/staging/prod</li>
                    <li>Automated CI/CD pipelines</li>
                    <li>Rollback capabilities</li>
                </ul>
                
                <h4>3️⃣ Observability</h4>
                <ul>
                    <li>Centralized metrics across all models</li>
                    <li>Latency, throughput, error rates</li>
                    <li>Model drift detection</li>
                    <li>Cost per prediction tracking</li>
                </ul>
                
                <h4>4️⃣ Governance & Compliance</h4>
                <ul>
                    <li>Model approval workflows</li>
                    <li>Audit trails (who deployed what, when)</li>
                    <li>Access controls (RBAC)</li>
                    <li>Compliance documentation</li>
                </ul>
                
                <h4>5️⃣ Resource Management</h4>
                <ul>
                    <li>Auto-scaling policies</li>
                    <li>Cost allocation by team/project</li>
                    <li>Resource quotas</li>
                    <li>Multi-tenancy support</li>
                </ul>
                
                <h3 style="margin-top: 30px;">💼 Interview Talking Points</h3>
                
                <p><strong>For Platform/DevOps Roles:</strong></p>
                <p>"I built an ML platform using Backstage as the developer portal. Data scientists can discover all models in a central catalog, deploy new versions through self-service templates, and monitor performance through integrated dashboards. This reduced deployment friction and improved model lifecycle management across the organization."</p>
                
                <p><strong>For ML Engineering Roles:</strong></p>
                <p>"I've worked with platforms like MLflow for experiment tracking and model registry, integrated with Backstage for discoverability. This enables data scientists to track experiments, promote models to production, and maintain visibility across the ML lifecycle."</p>
                
                <p><strong>For Architecture Roles:</strong></p>
                <p>"I designed an ML platform with three layers: presentation (Backstage), orchestration (Kubeflow/ArgoCD), and execution (SageMaker/TorchServe). This separation allows teams to manage models at scale while maintaining flexibility in deployment targets."</p>
                """,
                "practice_prompts": [
                    "How would you design an ML platform for 10 teams?",
                    "Describe your experience with model lifecycle management",
                    "What tools would you use for ML platform observability?"
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
    ],
    "platform_management": [
        "How would you build an ML platform for multiple teams?",
        "Describe your experience with model lifecycle management.",
        "What tools have you used for ML infrastructure management?",
        "How do you enable self-service for data scientists?",
        "Explain how you'd organize and discover models at scale.",
        "How do you monitor and govern ML models in production?",
        "What's your approach to ML platform observability?"
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


@app.route('/api/interviews', methods=['GET'])
def get_interviews():
    """Get list of interview analysis files."""
    import os
    import glob
    
    # Look for JSON files that contain 'interview' and 'analysis' in the name
    interview_files = glob.glob('*interview*analysis*.json')
    interview_files += glob.glob('interview_report_*.json')
    
    interviews = []
    for filename in interview_files:
        if os.path.exists(filename):
            try:
                with open(filename, 'r') as f:
                    data = json.load(f)
                    
                # Extract metadata
                interviews.append({
                    'filename': filename,
                    'date': data.get('timestamp', data.get('individual_responses', [{}])[0].get('timestamp', 'Unknown')).split('T')[0] if data.get('timestamp') or (data.get('individual_responses') and data['individual_responses']) else 'Unknown',
                    'total_questions': len(data.get('individual_responses', [])),
                    'overall_scores': data.get('overall_scores', {})
                })
            except:
                pass
    
    # Sort by date, newest first
    interviews.sort(key=lambda x: x['date'], reverse=True)
    
    return jsonify({'interviews': interviews})


@app.route('/api/interview/<filename>', methods=['GET'])
def get_interview_detail(filename):
    """Get detailed interview analysis."""
    import os
    
    # Security: prevent directory traversal
    filename = os.path.basename(filename)
    
    if not os.path.exists(filename):
        return jsonify({'error': 'Interview not found'}), 404
    
    try:
        with open(filename, 'r') as f:
            data = json.load(f)
        
        # Try to find the original transcript for metadata
        transcript_filename = filename.replace('_analysis', '').replace('interview_report_', 'interview_transcript_')
        if os.path.exists(transcript_filename):
            try:
                with open(transcript_filename, 'r') as f:
                    transcript_data = json.load(f)
                    data['interview_metadata'] = transcript_data.get('interview_metadata', {})
            except:
                pass
        
        # Also try the standard interview_transcript.json
        if 'interview_metadata' not in data and os.path.exists('interview_transcript.json'):
            try:
                with open('interview_transcript.json', 'r') as f:
                    transcript_data = json.load(f)
                    data['interview_metadata'] = transcript_data.get('interview_metadata', {})
            except:
                pass
        
        return jsonify(data)
    except Exception as e:
        return jsonify({'error': str(e)}), 500


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
