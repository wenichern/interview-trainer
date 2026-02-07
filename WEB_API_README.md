# Interview Training Web API 🎯

An interactive web application to help job applicants improve their interview skills based on personalized feedback.

## 🚀 What's Included

### 📚 Training Modules

1. **Prepare Concrete Examples**
   - STAR Method Framework (Situation, Task, Action, Result)
   - Adding Measurable Results
   - Converting vague accomplishments into quantifiable achievements

2. **ML Inference vs Training**
   - Understanding the difference between training and inference
   - ML Serving Tools (TensorFlow Serving, TorchServe, SageMaker Endpoints, Triton)
   - Production inference challenges and optimization

3. **Practice Concise Answers**
   - Headline First Method
   - Eliminating rambling and staying within 60-90 seconds
   - Structuring responses effectively

4. **Replace Weak Phrases**
   - Transforming weak language into confident communication
   - Assertive communication without arrogance
   - Common phrase replacements (I guess → I believe)

### 💪 Interactive Features

- **Practice Mode**: Answer random interview questions and get instant feedback
- **Question Categories**: Behavioral, Technical, ML-specific
- **Real-time Analysis**: Get scores on clarity, confidence, specificity
- **Word Counter**: Track your response length and speaking time
- **Quick Tips**: Get random interview tips

## 🖥️ How to Use

### Starting the Server

```bash
# Option 1: Use the start script
./start_server.sh

# Option 2: Manual start
source venv/bin/activate
python training_api.py
```

### Accessing the Application

Once the server is running, open your browser and go to:

```
http://localhost:5000
```

## 📖 Using the Web Interface

### 1. Training Modules Tab
- Click on any module to view lessons
- Read through the content and examples
- Review practice prompts at the end of each lesson

### 2. Practice Tab
- Click "Get Random Question" or select a category
- Type your answer in the text area
- Watch the word count and estimated speaking time
- Click "Analyze My Answer" to get instant feedback
- Review your score (out of 10) and specific feedback items

### 3. Quick Tips Tab
- Click "Get Random Tip" for actionable interview advice
- Review the key reminders checklist

## 🎯 Scoring System

When you analyze your practice responses, you'll receive:

- **Overall Score**: 0-10 based on multiple factors
- **Word Count**: Aim for 50-100 words (60-90 seconds when spoken)
- **Weak Phrases Count**: Number of phrases like "I guess", "kind of", "you know"
- **Metrics Check**: Whether you included measurable results
- **Structure Check**: Whether you used framework words (STAR method)

### Scoring Breakdown:
- ✅ **Good length** (50-100 words)
- ✅ **No weak phrases**
- ✅ **Includes metrics/numbers**
- ✅ **Uses structure** (STAR or similar)

## 🔌 API Endpoints

The application also provides a REST API:

### Get All Modules
```
GET /api/modules
```

### Get Specific Module
```
GET /api/module/<module_id>
```

### Get Practice Questions
```
GET /api/practice/questions?category=behavioral
GET /api/practice/random
```

### Analyze Response
```
POST /api/analyze/response
Body: {
  "question": "Tell me about yourself",
  "answer": "Your answer here"
}
```

### Get Random Tip
```
GET /api/tips/random
```

## 📝 Example Usage

### Practice Workflow:

1. **Choose a Module** - Start with "Prepare Concrete Examples"
2. **Read the Lesson** - Learn the STAR method
3. **Go to Practice** - Get a random question
4. **Write Your Answer** - Apply what you learned
5. **Get Feedback** - Analyze and improve
6. **Iterate** - Practice multiple questions

### Improvement Focus Areas:

Based on your interview analysis, focus on:

1. ✅ **Prepare 5-7 STAR Stories** with measurable results
2. ✅ **Study ML Inference** concepts and tools
3. ✅ **Practice Concise Answers** (60-90 seconds)
4. ✅ **Replace Weak Phrases** with confident language

## 🛠️ Technical Stack

- **Backend**: Flask (Python)
- **Frontend**: Vanilla JavaScript, HTML5, CSS3
- **API**: RESTful endpoints
- **Analysis**: Custom scoring algorithm

## 📦 Files Structure

```
/Users/smarticle/2-7-2026/
├── training_api.py           # Flask API server
├── templates/
│   └── index.html           # Web interface
├── interview_trainer.py      # Core analysis engine
├── analyze_transcript.py     # Transcript analyzer
├── interview_transcript.json # Your interview data
├── start_server.sh          # Server startup script
└── venv/                    # Python virtual environment
```

## 🎓 Tips for Maximum Benefit

1. **Practice Daily**: Spend 15-20 minutes practicing answers
2. **Record Yourself**: Practice speaking your written answers
3. **Track Progress**: Save your scores and watch improvement
4. **Focus on Weakness**: Prioritize areas with lowest scores
5. **Use Real Examples**: Practice with your actual work experiences
6. **Time Yourself**: Use a timer when speaking your answers
7. **Mock Interviews**: Have friends ask you the questions

## 🔒 Privacy

All practice sessions are analyzed in real-time and not stored. Your responses are private and only visible to you.

## 🆘 Troubleshooting

### Port Already in Use
If port 5000 is busy:
```python
# Edit training_api.py, line 658
app.run(debug=True, host='0.0.0.0', port=5001)  # Change port
```

### Virtual Environment Issues
```bash
# Recreate virtual environment
rm -rf venv
python3 -m venv venv
source venv/bin/activate
pip install flask flask-cors
```

## 🚀 Next Steps

After using this tool, you should be able to:
- Answer interview questions with STAR method
- Include measurable results in all examples
- Keep answers concise (60-90 seconds)
- Use confident, assertive language
- Understand ML inference concepts for technical roles

## 📞 Support

For issues or questions, review the training modules and practice regularly. The more you practice, the more natural these techniques will become!

---

**Good luck with your interviews! 🎉**
