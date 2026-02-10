# Week 1 - Day 1 & 2: Conceptual Understanding
## ML Inference Basics

**Goal:** Understand what ML inference is and how it differs from training

---

## Day 1 Tasks (February 9, 2026)

### ✅ Task 1: Read AWS SageMaker Documentation (45 min)

**What to Read:**
1. Go to: https://docs.aws.amazon.com/sagemaker/latest/dg/deploy-model.html
2. Focus on these sections:
   - "Deploy a Model in Amazon SageMaker"
   - "Real-time inference"
   - "How SageMaker Hosting Services Works"
   - "Deploy Models for Inference"

**Key Concepts to Understand:**
- [ ] What is a model endpoint?
- [ ] What is real-time vs batch inference?
- [ ] How does auto-scaling work for inference?
- [ ] What are the components: model artifact, Docker image, endpoint config

**Take Notes Here:**

**Model Endpoint:**


**Real-time vs Batch Inference:**


**Auto-scaling:**


**Components:**


---

### ✅ Task 2: Watch Video - ML Model Serving (45 min)

**Videos to Watch (choose 1-2):**

1. Search YouTube: "Machine Learning Model Serving" + company name (Netflix/Uber/AWS)
2. AWS re:Invent talks on SageMaker
3. "Deploying Machine Learning Models in Production"

**Recommended:**
- "Machine Learning Inference at Scale" (any tech company talk)
- "AWS SageMaker Deployment Best Practices"

**Notes from Videos:**

**Key Takeaways:**


**New Terms Learned:**


**Questions I Still Have:**


---

### ✅ Task 3: Draw the Inference Flow (30 min)

**Exercise:** Draw out the request-to-response flow for ML inference

```
Client Request
     ↓
[ Your diagram here - add each component ]
     ↓
     ↓
     ↓
Response to Client
```

**Components to Include:**
1. API Gateway / Load Balancer
2. Preprocessing layer
3. Model serving endpoint
4. Model loading
5. Inference execution
6. Response formatting
7. Monitoring/logging points

**My Flow Diagram:**




---

### ✅ Task 4: Key Concepts Quiz (15 min)

**Test Yourself - Can you answer these?**

1. What happens when a request comes to an inference endpoint?



2. What's the difference between training and inference?



3. What metrics matter for inference systems?



4. What AWS services are involved in real-time inference?



5. What does "cold start" mean for model serving?



---

## Day 2 Tasks (February 10, 2026)

### ✅ Task 1: Deep Dive - Inference Patterns (45 min)

**Research these patterns:**

**1. Online/Real-time Inference:**
- Use case:
- Latency requirement:
- Example:


**2. Batch Inference:**
- Use case:
- Latency requirement:
- Example:


**3. Asynchronous Inference:**
- Use case:
- Latency requirement:
- Example:


**4. Edge Inference:**
- Use case:
- Latency requirement:
- Example:


---

### ✅ Task 2: Study Request/Response Flow in Detail (45 min)

**Break down each step:**

**Step 1: Request arrives**
- What validation happens?
- What format is expected?


**Step 2: Preprocessing**
- What transformations occur?
- Where does this happen?


**Step 3: Model invocation**
- How is the model loaded?
- Where does it run?


**Step 4: Inference execution**
- What happens inside the model?
- How long does it take?


**Step 5: Response formatting**
- What format is returned?
- What metadata is included?


**Step 6: Monitoring**
- What gets logged?
- What metrics are captured?


---

### ✅ Task 3: Compare Inference Tools (Research) (45 min)

**Create a comparison table:**

| Tool | Best For | Pros | Cons |
|------|----------|------|------|
| SageMaker Endpoints | | | |
| TorchServe | | | |
| TensorFlow Serving | | | |
| KServe | | | |

**Research each tool:**
- Read their documentation
- Look at GitHub repos
- Find example deployments


---

### ✅ Task 4: Write Your First Inference Story Draft (30 min)

**Practice Question:** "Walk me through ML inference flow from request to response"

**Your Draft Answer (2-3 minutes when spoken):**

[Write your answer here - include specific technologies even if you haven't used them yet]




**Record yourself reading this answer:**
- [ ] Recorded
- [ ] Timed (goal: 2-3 min)
- [ ] Reviewed

**What needs improvement:**


---

## End of Day 1-2 Checklist

- [ ] Understand what inference is vs training
- [ ] Know the major inference patterns (online, batch, async)
- [ ] Can draw inference flow diagram
- [ ] Familiar with SageMaker concepts
- [ ] Know the major serving tools
- [ ] Have draft answer to inference flow question
- [ ] Ready to start hands-on labs tomorrow!

---

## Questions for Further Research




## Resources Used
- [ ] AWS SageMaker docs
- [ ] YouTube videos
- [ ] Tool documentation
- [ ] 

---

**Time Spent Today:** ___ hours

**Confidence Level (1-10):** ___

**Ready for Labs?** Yes / No / Almost

**Notes for Tomorrow:**


