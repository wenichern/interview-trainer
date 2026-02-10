# Practice Interview Questions
## ML Infrastructure & Platform Engineering Roles

*Based on interview analysis - February 9, 2026*

---

## How to Use This Guide

**Practice Strategy:**
1. **Read the question** carefully
2. **Think** for 30 seconds before answering
3. **Answer out loud** (record yourself!)
4. **Time yourself** - aim for 2-3 minutes per answer
5. **Review** using the "Strong Answer Includes" checklist
6. **Repeat** until you can answer smoothly without notes

**Color Coding:**
- 🔴 **Critical** - Must master for ML infrastructure roles
- 🟡 **Important** - Common in platform engineering interviews
- 🟢 **Bonus** - Nice to have, shows depth

---

## Section 1: AWS Infrastructure & Architecture

### 🔴 Q1.1: Describe an AWS infrastructure you personally designed and owned end-to-end.

**What They're Really Asking:**
- Can you architect complete systems?
- Do you understand how components interact?
- Have you owned production infrastructure at scale?

**Strong Answer Includes:**
- [ ] Specific AWS services (EKS, RDS, S3, CloudFront, etc.)
- [ ] Architecture pattern (microservices, serverless, etc.)
- [ ] Scale metrics (users, requests/day, data volume)
- [ ] Your specific role and ownership
- [ ] Technical challenges solved
- [ ] Business impact/results
- [ ] Diagrams or visual description

**Follow-up Questions:**
- Why did you choose [service X] over [alternative Y]?
- How did you handle disaster recovery?
- What would you do differently now?
- How did you ensure high availability?

---

### 🟡 Q1.2: How do you design for high availability and disaster recovery in AWS?

**Strong Answer Includes:**
- [ ] Multi-AZ deployments
- [ ] Cross-region failover strategies
- [ ] RTO/RPO definitions for your use case
- [ ] Backup strategies (snapshots, cross-region replication)
- [ ] Load balancing and health checks
- [ ] Chaos engineering/testing
- [ ] Specific example from your experience

---

### 🟡 Q1.3: Walk me through how you would migrate a monolithic application to microservices on AWS.

**Strong Answer Includes:**
- [ ] Assessment phase (identify boundaries, dependencies)
- [ ] Strangler pattern or other migration strategy
- [ ] Service decomposition approach
- [ ] AWS services (ECS/EKS, API Gateway, EventBridge)
- [ ] Data migration strategy
- [ ] Phased rollout plan
- [ ] Monitoring and rollback strategy
- [ ] Example if you've done this

---

### 🟢 Q1.4: How do you optimize AWS costs for production infrastructure?

**Strong Answer Includes:**
- [ ] Reserved instances and Savings Plans
- [ ] Right-sizing based on CloudWatch metrics
- [ ] Auto-scaling policies
- [ ] S3 lifecycle policies
- [ ] Spot instances for appropriate workloads
- [ ] Cost allocation tags
- [ ] Regular cost review process
- [ ] Specific savings you achieved (percentage or dollars)

---

## Section 2: Machine Learning Infrastructure

### 🔴 Q2.1: Walk me through how a trained ML model produces predictions in production, from request to response.

**What They're Really Asking:**
- Do you understand the inference pipeline?
- Can you explain the technical flow?
- Have you actually built/operated this?

**Strong Answer Includes:**
- [ ] Entry point (API Gateway, Load Balancer)
- [ ] Request preprocessing/validation
- [ ] Model serving component (SageMaker, TorchServe, etc.)
- [ ] Model loading and inference execution
- [ ] Response formatting
- [ ] Monitoring/logging at each step
- [ ] Performance metrics (latency, throughput)
- [ ] Specific example with actual technologies

**Follow-up Questions:**
- How do you handle high-volume traffic?
- What happens if the model endpoint is down?
- How do you ensure low latency?
- How do you version models?

---

### 🔴 Q2.2: Which ML inference/serving tools have you used in production? Describe your experience.

**What They're Really Asking:**
- Have you actually deployed models?
- Do you know the ecosystem of tools?
- Can you compare trade-offs?

**Tools to Know:**
- SageMaker Endpoints
- TorchServe / TensorFlow Serving
- TensorRT
- Triton Inference Server
- KServe (formerly KFServing)
- Seldon Core
- Ray Serve

**Strong Answer Includes:**
- [ ] Specific tool(s) you've used
- [ ] Type of model deployed
- [ ] Infrastructure setup (instances, scaling)
- [ ] Performance achieved (latency, throughput)
- [ ] Why you chose this tool
- [ ] Challenges encountered and solutions
- [ ] Comparison with alternatives
- [ ] If no production experience: lab/learning experience with honesty

---

### 🔴 Q2.3: Describe your experience with GPU-backed inference workloads in production.

**Strong Answer Includes:**
- [ ] GPU instance types used (P3, P4, G4, Inf1)
- [ ] Specific model/workload requiring GPU
- [ ] Performance comparison (GPU vs CPU)
- [ ] Cost analysis
- [ ] Optimization techniques (batching, quantization)
- [ ] Monitoring GPU utilization
- [ ] Scaling considerations
- [ ] If no GPU experience: be honest, discuss related experience

**Follow-up Questions:**
- When would you choose GPU over CPU for inference?
- How do you optimize GPU utilization?
- What about cost vs performance trade-offs?

---

### 🟡 Q2.4: How do you monitor ML models in production?

**Strong Answer Includes:**
- [ ] Data drift detection (input distribution changes)
- [ ] Model performance metrics (accuracy, precision, recall)
- [ ] Infrastructure metrics (latency, errors, throughput)
- [ ] Prediction distribution monitoring
- [ ] Alerting thresholds and escalation
- [ ] Tools used (SageMaker Model Monitor, custom solutions)
- [ ] Retraining triggers
- [ ] Example of catching production issues

---

### 🟡 Q2.5: Explain how you would implement A/B testing for ML models.

**Strong Answer Includes:**
- [ ] Traffic splitting strategy
- [ ] Variant configuration (model versions)
- [ ] Metrics to track for comparison
- [ ] Statistical significance testing
- [ ] Gradual rollout approach (canary deployment)
- [ ] Rollback strategy
- [ ] Tools/services (SageMaker variants, custom routing)
- [ ] Example if available

---

### 🟢 Q2.6: How do you handle model versioning and rollback in production?

**Strong Answer Includes:**
- [ ] Model registry/artifact storage
- [ ] Versioning scheme (semantic versioning, date-based)
- [ ] Metadata tracking (training data, hyperparameters, metrics)
- [ ] Deployment history
- [ ] Automated rollback triggers
- [ ] Manual rollback process
- [ ] Blue-green or canary deployment patterns
- [ ] Testing before rollback

---

## Section 3: Infrastructure as Code (IaC)

### 🔴 Q3.1: Describe your experience with Terraform (or CloudFormation). What have you built with it?

**Strong Answer Includes:**
- [ ] Specific infrastructure managed
- [ ] Module structure and organization
- [ ] State management approach
- [ ] Environment strategy (workspaces, separate states)
- [ ] CI/CD integration
- [ ] Team workflows (PR reviews, plan/apply process)
- [ ] Number of resources managed
- [ ] Challenges solved (drift, dependencies, etc.)
- [ ] Terraform vs CloudFormation choice and rationale

---

### 🟡 Q3.2: How do you handle secrets and sensitive data in IaC?

**Strong Answer Includes:**
- [ ] Never in code or version control
- [ ] AWS Secrets Manager or Parameter Store
- [ ] Terraform data sources for secret retrieval
- [ ] Encryption at rest and in transit
- [ ] IAM policies for secret access
- [ ] Rotation strategy
- [ ] Audit logging
- [ ] Example from your experience

---

### 🟡 Q3.3: How do you test infrastructure code before deploying to production?

**Strong Answer Includes:**
- [ ] Terraform plan review process
- [ ] Dev/staging environment testing
- [ ] Terraform validate and fmt
- [ ] Policy as code (Sentinel, OPA)
- [ ] Cost estimation (Infracost)
- [ ] Security scanning (Checkov, tfsec)
- [ ] Integration tests
- [ ] Peer review process

---

### 🟢 Q3.4: Describe your experience with Terraform modules. How do you design reusable infrastructure?

**Strong Answer Includes:**
- [ ] Module design principles
- [ ] Input variables and outputs
- [ ] Module versioning
- [ ] Module registry or storage
- [ ] Examples of modules you've created
- [ ] Benefits achieved (consistency, speed)
- [ ] How team uses modules
- [ ] Documentation approach

---

## Section 4: CI/CD & DevOps

### 🟡 Q4.1: Describe a CI/CD pipeline you've built. Walk me through the stages.

**Strong Answer Includes:**
- [ ] Source control system (GitLab, GitHub)
- [ ] Build stage (compilation, Docker image building)
- [ ] Test stages (unit, integration, security)
- [ ] Quality gates (coverage, vulnerability thresholds)
- [ ] Deployment stages (dev → staging → production)
- [ ] Approval processes
- [ ] Rollback capabilities
- [ ] Specific tools (Jenkins, GitLab CI, GitHub Actions)
- [ ] Metrics (deployment frequency, lead time)

---

### 🟡 Q4.2: How do you implement security scanning in CI/CD pipelines?

**Strong Answer Includes:**
- [ ] SAST (Static Application Security Testing)
- [ ] DAST (Dynamic Application Security Testing)
- [ ] Dependency scanning
- [ ] Container image scanning
- [ ] IaC security scanning
- [ ] Secret detection
- [ ] Specific tools (SonarQube, Snyk, Trivy, etc.)
- [ ] Failure thresholds and policies
- [ ] How you handle findings

---

### 🟢 Q4.3: What's your approach to deployment strategies? (Blue-Green, Canary, Rolling)

**Strong Answer Includes:**
- [ ] Explanation of each strategy
- [ ] When to use which approach
- [ ] Example of implementation
- [ ] Tools used (AWS CodeDeploy, Kubernetes, etc.)
- [ ] Monitoring during deployment
- [ ] Rollback triggers
- [ ] Trade-offs of each approach

---

## Section 5: Kubernetes & Container Orchestration

### 🟡 Q5.1: Describe your experience running production workloads on Kubernetes.

**Strong Answer Includes:**
- [ ] Cluster setup (EKS, self-managed, etc.)
- [ ] Workload types (microservices, batch jobs, ML)
- [ ] Scale (number of nodes, pods, clusters)
- [ ] Namespace and RBAC strategy
- [ ] Networking (ingress, service mesh)
- [ ] Storage (PVs, EBS, EFS)
- [ ] Monitoring (Prometheus, Grafana)
- [ ] Challenges overcome
- [ ] HA and DR approach

---

### 🟡 Q5.2: How do you handle auto-scaling in Kubernetes?

**Strong Answer Includes:**
- [ ] Horizontal Pod Autoscaler (HPA)
- [ ] Vertical Pod Autoscaler (VPA)
- [ ] Cluster Autoscaler
- [ ] Metrics used (CPU, memory, custom)
- [ ] Configuration examples
- [ ] Scaling limits and considerations
- [ ] Specific use case example
- [ ] ML inference scaling considerations

---

### 🟢 Q5.3: Explain how you would deploy ML models on Kubernetes.

**Strong Answer Includes:**
- [ ] Containerization approach (Docker image)
- [ ] Serving framework (TorchServe, TF Serving, KServe)
- [ ] Deployment manifests
- [ ] Resource requests/limits (CPU, GPU, memory)
- [ ] Service exposure (LoadBalancer, Ingress)
- [ ] Auto-scaling setup
- [ ] Model loading strategy
- [ ] Monitoring and logging

---

## Section 6: Data Infrastructure

### 🟡 Q6.1: Describe your experience with data pipelines for ML workloads.

**Strong Answer Includes:**
- [ ] Data sources and ingestion
- [ ] ETL/ELT tools (Glue, Airflow, custom)
- [ ] Data transformation and feature engineering
- [ ] Storage layers (data lake, warehouse)
- [ ] Data quality and validation
- [ ] Orchestration approach
- [ ] Scale and performance
- [ ] Specific example project

---

### 🟢 Q6.2: What's your experience with feature stores?

**Strong Answer Includes:**
- [ ] Purpose and benefits of feature stores
- [ ] Tools used (SageMaker Feature Store, Feast, Tecton)
- [ ] Online vs offline features
- [ ] Feature computation and storage
- [ ] Serving latency requirements
- [ ] Version control for features
- [ ] Example use case
- [ ] If no experience: understanding of concept

---

## Section 7: Monitoring & Observability

### 🟡 Q7.1: How do you implement monitoring and observability for distributed systems?

**Strong Answer Includes:**
- [ ] Three pillars: logs, metrics, traces
- [ ] Tools used (CloudWatch, Prometheus, Grafana, Datadog, etc.)
- [ ] Key metrics tracked
- [ ] Distributed tracing approach
- [ ] Log aggregation and analysis
- [ ] Dashboard design
- [ ] Alerting strategy
- [ ] On-call and incident response

---

### 🟡 Q7.2: Describe a production issue you debugged. How did you troubleshoot it?

**Strong Answer Includes:**
- [ ] Initial symptoms and alert
- [ ] Investigation approach
- [ ] Tools and data sources used
- [ ] Root cause identified
- [ ] Immediate fix applied
- [ ] Long-term solution
- [ ] Lessons learned
- [ ] Preventive measures implemented

---

## Section 8: Security & Compliance

### 🟡 Q8.1: Describe your experience with SOC 2 or other compliance frameworks.

**Strong Answer Includes:**
- [ ] Compliance requirements understood
- [ ] Infrastructure controls implemented
- [ ] Audit logging and retention
- [ ] Access control mechanisms
- [ ] Encryption (at rest, in transit)
- [ ] Vulnerability management
- [ ] Evidence collection for audits
- [ ] Automation of compliance checks
- [ ] Specific example

---

### 🟡 Q8.2: How do you implement least privilege access in AWS?

**Strong Answer Includes:**
- [ ] IAM roles and policies
- [ ] Service-specific policies
- [ ] Conditions and constraints
- [ ] Regular access reviews
- [ ] Temporary credentials (STS)
- [ ] Cross-account access
- [ ] Monitoring and alerts (CloudTrail)
- [ ] Tools for policy validation

---

## Section 9: Problem-Solving & System Design

### 🔴 Q9.1: Design a real-time ML inference system that handles 100K requests per second.

**What They're Really Asking:**
- Can you design at scale?
- Do you consider all components?
- How do you handle trade-offs?

**Strong Answer Includes:**
- [ ] Load balancing strategy
- [ ] Caching layer
- [ ] Model serving infrastructure
- [ ] Auto-scaling approach
- [ ] Database/storage for features
- [ ] Monitoring and alerting
- [ ] Cost estimation
- [ ] Availability and DR
- [ ] Latency requirements
- [ ] Alternative approaches and trade-offs

**Follow-up Questions:**
- How would you handle traffic spikes?
- What if latency increases beyond SLA?
- How do you deploy new models without downtime?
- What's the failure mode and recovery?

---

### 🟡 Q9.2: How would you design a multi-region ML serving architecture?

**Strong Answer Includes:**
- [ ] Region selection criteria
- [ ] Data replication strategy
- [ ] Traffic routing (latency-based, geo-based)
- [ ] Model synchronization
- [ ] Failover approach
- [ ] Cost considerations
- [ ] Compliance and data residency
- [ ] Testing strategy

---

### 🟡 Q9.3: Design a system to retrain ML models automatically based on performance degradation.

**Strong Answer Includes:**
- [ ] Performance monitoring setup
- [ ] Degradation detection logic
- [ ] Training data collection
- [ ] Automated training pipeline
- [ ] Model validation before deployment
- [ ] A/B testing or shadow deployment
- [ ] Rollback mechanisms
- [ ] Human oversight and approval
- [ ] Notification system

---

## Section 10: ML-Specific Technical Questions

### 🔴 Q10.1: What's the difference between online inference and batch inference? When would you use each?

**Strong Answer Includes:**
- [ ] Online: Real-time, low latency, single/small batch predictions
- [ ] Batch: Scheduled, high throughput, process large datasets
- [ ] Use case examples for each
- [ ] Infrastructure differences
- [ ] Cost considerations
- [ ] Tools for each (SageMaker Endpoints vs Batch Transform)

---

### 🟡 Q10.2: How do you optimize inference latency?

**Strong Answer Includes:**
- [ ] Model optimization (quantization, pruning)
- [ ] Caching strategies
- [ ] Request batching
- [ ] GPU acceleration
- [ ] Model compilation (TensorRT, ONNX)
- [ ] Network optimization
- [ ] Profiling and benchmarking
- [ ] Specific improvements achieved

---

### 🟡 Q10.3: Explain model drift and how you would detect it.

**Strong Answer Includes:**
- [ ] Definition (data drift vs concept drift)
- [ ] Why it matters
- [ ] Detection methods (statistical tests, monitoring)
- [ ] Tools (SageMaker Model Monitor, custom)
- [ ] Metrics to track
- [ ] Alerting thresholds
- [ ] Response actions (retrain, rollback)
- [ ] Example if available

---

### 🟢 Q10.4: What's your understanding of MLOps? How is it different from DevOps?

**Strong Answer Includes:**
- [ ] MLOps definition (ML + DevOps + DataOps)
- [ ] Unique ML challenges (data versioning, model versioning, experiment tracking)
- [ ] MLOps lifecycle (data → train → deploy → monitor → retrain)
- [ ] Differences from traditional DevOps
- [ ] Tools and practices
- [ ] Your experience with MLOps

---

## Section 11: Behavioral Questions

### 🟡 Q11.1: Tell me about a time you had to make a difficult technical decision with limited information.

**Use STAR Method:**
- **Situation:** Context and challenge
- **Task:** Your responsibility
- **Action:** What you did, why
- **Result:** Outcome and learnings

---

### 🟡 Q11.2: Describe a time when you disagreed with a team member's technical approach. How did you handle it?

**Strong Answer Includes:**
- [ ] Context of disagreement
- [ ] Your perspective and rationale
- [ ] How you communicated
- [ ] Resolution approach
- [ ] Outcome
- [ ] What you learned

---

### 🟡 Q11.3: Tell me about a production outage you were involved in. What happened and what did you learn?

**Strong Answer Includes:**
- [ ] Incident description
- [ ] Your role in response
- [ ] Troubleshooting process
- [ ] Resolution
- [ ] Root cause analysis
- [ ] Preventive measures
- [ ] Process improvements
- [ ] Lessons learned

---

### 🟡 Q11.4: Describe a time you had to learn a new technology quickly for a project.

**Strong Answer Includes:**
- [ ] Technology and why it was needed
- [ ] Learning approach
- [ ] Timeline
- [ ] Application to project
- [ ] Outcome
- [ ] Demonstrates learning ability

---

## Section 12: Scenario-Based Questions

### 🔴 Q12.1: Your ML inference endpoint is experiencing high latency. Walk me through how you would diagnose and fix it.

**Strong Answer Includes:**
- [ ] Check monitoring dashboards (latency metrics)
- [ ] Review CloudWatch logs and metrics
- [ ] Check model endpoint health
- [ ] Analyze request patterns (traffic spike?)
- [ ] Review auto-scaling configuration
- [ ] Check resource utilization (CPU, memory, GPU)
- [ ] Test model locally
- [ ] Possible solutions (scale up/out, optimize model, caching)
- [ ] Implement fix and validate
- [ ] Post-mortem and prevention

---

### 🟡 Q12.2: A data scientist wants to deploy a new model that requires GPUs. How would you support this?

**Strong Answer Includes:**
- [ ] Understand requirements (model size, latency, throughput)
- [ ] Select appropriate GPU instance type
- [ ] Estimate costs
- [ ] Set up infrastructure (Terraform/IaC)
- [ ] Configure auto-scaling
- [ ] Implement monitoring
- [ ] Test performance
- [ ] Document process for future models
- [ ] Optimize costs if needed

---

### 🟡 Q12.3: Your team wants to move from SageMaker to a custom inference solution on Kubernetes. What factors would you consider?

**Strong Answer Includes:**
- [ ] Current pain points with SageMaker
- [ ] Requirements for custom solution
- [ ] Cost comparison
- [ ] Complexity and maintenance burden
- [ ] Team expertise required
- [ ] Migration effort and risk
- [ ] Feature comparison (monitoring, scaling, etc.)
- [ ] Recommendation with rationale
- [ ] Phased migration approach if approved

---

## Section 13: Company/Role-Specific Questions

### 🟡 Q13.1: Why are you interested in ML infrastructure specifically?

**Strong Answer Includes:**
- [ ] Your background and journey
- [ ] What excites you about ML infrastructure
- [ ] Specific aspects you enjoy (scale, optimization, impact)
- [ ] How it aligns with career goals
- [ ] What you want to learn/accomplish

---

### 🟡 Q13.2: What's your experience working with data scientists or ML engineers?

**Strong Answer Includes:**
- [ ] Types of collaboration
- [ ] Your role in supporting them
- [ ] Infrastructure/tools you provided
- [ ] Challenges in collaboration
- [ ] How you bridged technical gaps
- [ ] Successful outcomes
- [ ] What you learned about their needs

---

### 🟡 Q13.3: Where do you see ML infrastructure heading in the next 2-3 years?

**Strong Answer Includes:**
- [ ] Current trends (LLMs, edge ML, MLOps maturity)
- [ ] Technology evolution (serverless, specialized hardware)
- [ ] Your perspective on what's important
- [ ] How you're staying current
- [ ] What excites you about the future

---

## Practice Schedule

### Week 1: Foundation Questions
- Monday: Q1.1, Q3.1 (AWS + IaC)
- Tuesday: Q2.1, Q2.2 (ML inference basics)
- Wednesday: Q4.1, Q7.1 (CI/CD + Monitoring)
- Thursday: Q5.1 (Kubernetes)
- Friday: Review all, record yourself

### Week 2: Deep Technical Questions
- Monday: Q2.3, Q2.4, Q2.5 (ML monitoring and testing)
- Tuesday: Q9.1, Q9.2 (System design)
- Wednesday: Q10.1, Q10.2, Q10.3 (ML-specific)
- Thursday: Q6.1, Q8.1 (Data + Security)
- Friday: Mock interview with all questions

### Week 3: Behavioral + Scenarios
- Monday: Q11.1, Q11.2, Q11.3, Q11.4 (Behavioral)
- Tuesday: Q12.1, Q12.2, Q12.3 (Scenarios)
- Wednesday: Q13.1, Q13.2, Q13.3 (Company-specific)
- Thursday: Random question practice (simulate interview)
- Friday: Full mock interview

### Week 4: Polish + Advanced
- Review all weak areas
- Practice smooth transitions
- Time yourself for all answers
- Record and critique
- Mock interviews with peers

---

## Answer Quality Checklist

After each practice answer, score yourself:

### Structure (1-5):
- [ ] Clear beginning (context)
- [ ] Logical flow
- [ ] Concise ending

### Content (1-5):
- [ ] Specific technologies/tools
- [ ] Metrics and scale
- [ ] Your role clear
- [ ] Results/outcomes

### Delivery (1-5):
- [ ] Confident tone
- [ ] No filler words (um, uh, like)
- [ ] Good pace
- [ ] 2-3 minute length

**Goal: 12-15 total score for each answer**

---

## Common Mistakes to Avoid

❌ **DON'T:**
- Ramble without structure
- Use buzzwords without substance
- Say "we" without clarifying your role
- Provide only theoretical knowledge
- Forget metrics and outcomes
- Pause to check notes or think too long
- Misunderstand the question (ask for clarification!)
- Pretend to have experience you don't have

✅ **DO:**
- Use STAR method for behavioral questions
- Include specific numbers and metrics
- Clarify your personal contributions
- Provide real examples from experience
- Ask clarifying questions if needed
- Be honest about gaps while showing willingness to learn
- Practice out loud, not just in your head
- Time yourself

---

## Interview Day Preparation

### Day Before:
- [ ] Review your project summaries
- [ ] Practice 5 key questions out loud
- [ ] Prepare questions to ask interviewer
- [ ] Get good sleep

### Morning Of:
- [ ] Review key metrics from your projects
- [ ] Quick practice of 2-3 answers
- [ ] Test your setup (if virtual)
- [ ] Have your notes ready (architecture diagrams, etc.)

### During Interview:
- [ ] Listen carefully to full question
- [ ] Ask for clarification if needed
- [ ] Structure your answer before speaking
- [ ] Provide example when possible
- [ ] Watch for interviewer's cues
- [ ] Ask follow-up questions about the role/company

---

## Sample Mock Interview Script

**Try this 45-minute flow:**

1. Introductions (5 min)
2. Q1.1: AWS infrastructure end-to-end (5 min)
3. Q2.1: ML inference flow (5 min)
4. Q2.2: Inference tools experience (5 min)
5. Q3.1: Terraform/IaC experience (5 min)
6. Q9.1: System design at scale (10 min)
7. Q11.3: Production incident behavioral (5 min)
8. Your questions for them (5 min)

**Record this and review:**
- Where did you hesitate?
- What felt unclear?
- Where did you shine?
- What needs more practice?

---

## Resources

### Videos to Watch:
- AWS re:Invent talks on ML infrastructure
- "Machine Learning in Production" series
- Company engineering blogs (Netflix, Uber, Airbnb)

### Practice Platforms:
- Pramp (mock interviews)
- interviewing.io
- Practice with colleagues

### Additional Reading:
- AWS ML Infrastructure Best Practices
- Google's ML Engineering book
- MLOps community resources

---

## Track Your Progress

Create a spreadsheet:

| Question | First Try | Second Try | Final Score | Notes |
|----------|-----------|------------|-------------|-------|
| Q1.1 | 8/15 | 12/15 | 14/15 | Added more metrics |
| Q2.1 | 6/15 | 10/15 | 13/15 | Clarified flow |
| ... | | | | |

**Goal: 12+ for all critical questions**

---

**Remember: Great answers come from:**
1. **Real experience** (even from labs/projects)
2. **Specific details** (technologies, metrics, outcomes)
3. **Clear structure** (context → action → result)
4. **Confident delivery** (practice makes perfect)

**You've got this! 🚀**

---

*Practice Questions Guide - Last Updated: February 9, 2026*
