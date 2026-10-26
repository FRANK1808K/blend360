# Mock Exam 01 — 65 questions (English version)

> English version of [Simulacro 01](../mock-exam-01.md), using the terminology of the official AWS exam. The answer key and explanations are in the Spanish version. Questions and options keep the same numbers and letters.

---

## Domain 1 — Fundamentals of AI and ML

**1.** An online store wants to group its customers by purchasing behavior. It has no segment labels. Which approach is appropriate?

- A. Supervised classification
- B. Linear regression
- C. Clustering (unsupervised learning)
- D. Reinforcement learning

**2.** Which option BEST describes an **agentic AI** system?

- A. A system that uses an FM to plan, call tools, and take multi-step actions toward a goal.
- B. A diffusion model that generates images from text.
- C. An expert system based only on `if/else` rules.
- D. A regression model that predicts sales.

**3.** Which of the following is a **hyperparameter**?

- A. The weights of the neural network after training
- B. The model's predictions
- C. The features of the dataset
- D. The learning rate

**4.** A hospital trains a model to detect a serious disease. **Missing** a sick patient is far worse than running an extra test on a healthy patient. Which metric should the hospital prioritize?

- A. Accuracy
- B. Precision
- C. Recall
- D. R²

**5.** In a spam filter, sending an important **legitimate** email to the spam folder is the most expensive error. Which metric should be prioritized?

- A. Precision
- B. Recall
- C. RMSE
- D. MAE

**6.** A bank needs a model to approve or reject loans based on **tabular** data. The regulator requires the bank to **explain every individual decision**. Which approach is MOST appropriate?

- A. An LLM on Amazon Bedrock with a prompt that decides the approval
- B. A traditional ML model (for example, XGBoost) with explanations from Amazon SageMaker Clarify
- C. A diffusion model
- D. An Amazon Bedrock agent with access to the customer database

**7.** A demand forecasting model must penalize **large errors** in particular. Which metric is MOST appropriate?

- A. F1 score
- B. Precision
- C. RMSE
- D. AUC-ROC

**8.** A model reaches 99% accuracy on the training set and 65% on the validation set. Which action is appropriate?

- A. Increase the model complexity
- B. Train for more epochs
- C. Remove the validation set
- D. Apply regularization and collect more training data

**9.** A company needs to **label** 200,000 images with human help and reduce costs through automated labeling. Which service should the company use?

- A. Amazon SageMaker Ground Truth
- B. Amazon SageMaker Clarify
- C. Amazon SageMaker Model Monitor
- D. Amazon SageMaker Data Wrangler

**10.** A model receives **intermittent and unpredictable** traffic, with hours without requests. The team wants to minimize costs and can tolerate cold starts. Which SageMaker inference option should the team use?

- A. Real-time endpoint
- B. Serverless Inference
- C. Batch Transform
- D. Reserved Amazon EC2 instances

**11.** A model processes **500 MB** files that take about **20 minutes** each. Requests can be queued. Which inference option is appropriate?

- A. Real-time inference
- B. Serverless Inference
- C. Asynchronous Inference
- D. Amazon Bedrock On-Demand

**12.** A team wants to automate its ML workflow (data preparation, training, evaluation, and model registration) as a **CI/CD** pipeline. Which service should the team use?

- A. Amazon SageMaker Canvas
- B. Amazon SageMaker Ground Truth
- C. Amazon SageMaker JumpStart
- D. Amazon SageMaker Pipelines

**13.** A model performs very well on the test set but poorly in production. The team discovers that one feature was calculated with information from the target value itself. What is the problem?

- A. Underfitting
- B. Data leakage
- C. Class imbalance
- D. Concept drift

## Domain 2 — Fundamentals of Generative AI

**14.** A marketing team wants an LLM to generate **creative and varied** slogans. Which setting is appropriate?

- A. Temperature of 0
- B. Top K = 1
- C. High temperature (for example, 0.9)
- D. Reduce the maximum tokens to 10

**15.** A chatbot starts failing in long conversations with an "input too long" error. What is the BEST solution?

- A. Summarize or trim older conversation history so it stays within the context window
- B. Increase the temperature
- C. Switch to an image generation model
- D. Increase Top P

**16.** An application sends a complete 200-page manual in **every** request to the model, and costs are very high. Which change reduces cost the MOST without losing quality?

- A. Increase `maxTokens`
- B. Purchase Provisioned Throughput even though traffic is low
- C. Increase the temperature
- D. Use RAG to send only the relevant parts of the manual

**17.** Which statement about **token-based pricing** for FMs on Amazon Bedrock On-Demand is correct?

- A. Only output tokens are billed.
- B. Input and output tokens are billed, and output tokens usually cost more per token.
- C. A fixed price is charged per request regardless of size.
- D. Billing is per instance-hour.

**18.** What is **context engineering**?

- A. Adjusting the model weights with labeled data
- B. Encrypting prompts with AWS KMS
- C. Deciding and structuring which information (instructions, retrieved data, tools, memory) goes into the model's context
- D. Choosing the GPU instance type for training

**19.** What is the **Model Context Protocol (MCP)**?

- A. An open protocol that standardizes how AI agents and applications connect to external tools and data sources
- B. A proprietary AWS billing protocol
- C. A model compression technique
- D. An evaluation metric for LLMs

**20.** A travel assistant has a coordinator agent that delegates to specialist agents for flights, hotels, and payments, and combines their results. Which pattern is this?

- A. RLHF
- B. Supervisor (orchestrator) multi-agent pattern
- C. Batch inference
- D. Few-shot prompting

**21.** An assistant must **remember user preferences across different sessions** (for example, an aisle seat). Which capability does it need?

- A. A lower temperature
- B. Stop sequences
- C. Long-term agent memory (for example, Amazon Bedrock AgentCore Memory)
- D. A higher Top K

**22.** A company wants an assistant that answers questions about its internal policies, which **change every week**, without retraining models. Which technique should the company use?

- A. RAG with a knowledge base
- B. Weekly fine-tuning
- C. Pre-training from scratch
- D. Including all policies as few-shot examples

**23.** What data is needed to perform instruction **fine-tuning** of an FM?

- A. An unlabeled corpus
- B. No data
- C. Only images
- D. Labeled prompt-response pairs

**24.** What is a **hallucination** in an LLM?

- A. A plausible response that is incorrect or not supported by the data
- B. The model refusing to answer
- C. A slow response
- D. An authentication error

**25.** To find documents that are **semantically similar** to a query, what must be generated for the query and the documents?

- A. Stop sequences
- B. Embeddings (vectors)
- C. Hyperparameters
- D. Model units

**26.** A team wants to automatically evaluate generated **summaries** by comparing them with reference summaries. Which metric should the team use?

- A. BLEU
- B. RMSE
- C. ROUGE
- D. F1 score

**27.** Which type of model generates images by **iteratively removing noise**?

- A. Diffusion model
- B. Encoder-only transformer
- C. Linear regression
- D. K-means

**28.** A developer wants the model to always return a specific JSON format **without training the model**. Which technique should the developer try first?

- A. Continued pre-training
- B. RLHF
- C. Fine-tuning
- D. Few-shot prompting with examples of the expected format

**29.** Which **TWO** are limitations of generative AI? (Select TWO.)

- A. Non-deterministic outputs
- B. Guaranteed factual accuracy
- C. Hallucinations
- D. Full explainability of every output
- E. Zero inference cost

## Domain 3 — Applications of Foundation Models

**30.** A startup wants to use FMs from several providers through an API, with the **LEAST operational overhead** and pay-per-use pricing. Which service should the startup choose?

- A. Amazon EC2 with GPUs
- B. Amazon SageMaker JumpStart
- C. Amazon Bedrock
- D. Amazon Comprehend

**31.** A data science team needs to deploy a specific open-source model, **choose the GPU instance type**, and modify the fine-tuning script. Which option is appropriate?

- A. Amazon SageMaker JumpStart
- B. Amazon Bedrock On-Demand
- C. Amazon Q Business
- D. Amazon Bedrock Guardrails

**32.** When you create an Amazon Bedrock knowledge base with the *Quick create* option, which vector store is provisioned by default?

- A. Amazon DynamoDB
- B. Amazon MemoryDB
- C. Amazon RDS for MySQL
- D. Amazon OpenSearch Serverless

**33.** A company already uses **Amazon Aurora PostgreSQL** and wants to store the embeddings of its knowledge base alongside its relational data. Which option is appropriate?

- A. Aurora PostgreSQL with the pgvector extension
- B. Amazon S3 Glacier
- C. Amazon ElastiCache
- D. Amazon Redshift without extensions

**34.** In Amazon Bedrock Agents, which component defines the **APIs that the agent can invoke**, usually run by AWS Lambda and described with an OpenAPI schema?

- A. Knowledge base
- B. Guardrail
- C. Action group
- D. Provisioned Throughput

**35.** A team built agents with an open-source framework (LangGraph) and wants to run them in production with a **managed serverless runtime, memory, identity, and observability**. Which service should the team use?

- A. Amazon Lex
- B. Amazon Bedrock AgentCore
- C. Amazon SageMaker Canvas
- D. Amazon Kendra

**36.** What is **Strands Agents**?

- A. An agentic IDE from AWS
- B. A mainframe modernization service
- C. An open-source AWS SDK for building model-driven agents with little code
- D. A managed vector store

**37.** A development team wants an IDE that converts a request into **requirements, a design, and a task list** before generating code (spec-driven development). Which tool fits?

- A. Kiro
- B. Amazon Q Business
- C. AWS CodeCommit
- D. Amazon SageMaker Canvas

**38.** An insurance company wants to modernize **mainframe COBOL** applications and migrate Windows **.NET** applications to Linux with help from AI agents. Which service should the company use?

- A. Amazon Textract
- B. Amazon Translate
- C. AWS Glue
- D. AWS Transform

**39.** A public chatbot built with Amazon Bedrock must not show **credit card numbers** in its responses. Which solution is the SIMPLEST?

- A. Fine-tuning with masking examples
- B. An Amazon Bedrock Guardrails sensitive information (PII) filter with the MASK action
- C. Amazon Macie on the responses
- D. An IAM policy that denies `bedrock:InvokeModel`

**40.** The team needs to **version** production prompts, compare them across models, and **roll back** to a previous version if quality drops. What should the team use?

- A. AWS CloudTrail
- B. Amazon S3 Lifecycle
- C. Amazon Bedrock Prompt Management
- D. Amazon CloudWatch Logs Insights

**41.** A company needs to extract amounts, dates, and tables from **scanned invoices**. Which service should the company use?

- A. Amazon Textract
- B. Amazon Rekognition
- C. Amazon Comprehend
- D. Amazon Polly

**42.** A company wants to analyze the **sentiment of recorded calls** from its contact center. Which combination of services is appropriate?

- A. Amazon Polly → Amazon Comprehend
- B. Amazon Rekognition → Amazon Lex
- C. Amazon Translate → Amazon Polly
- D. Amazon Transcribe → Amazon Comprehend

**43.** Employees want to ask questions about HR documents stored in SharePoint. Each employee must only see what they already have permission to see, and the company wants a **ready-to-use** solution. Which service should the company use?

- A. Amazon Q Developer
- B. Amazon Q Business
- C. Amazon Lex
- D. Amazon Personalize

**44.** Business analysts want to ask **natural language questions** about their dashboards, produce research with cited sources, and create **no-code automations**. Which service fits BEST?

- A. Amazon EMR
- B. AWS Glue DataBrew
- C. Amazon Quick (Quick Sight, Quick Research, Quick Flows)
- D. Amazon Athena

**45.** A company wants to compare three FMs on whether their responses follow the **brand's tone**, as judged by its own team. What should the company use?

- A. Amazon Bedrock Model Evaluation with human workers
- B. Amazon CloudWatch
- C. SageMaker Clarify (pre-training bias)
- D. AWS Trusted Advisor

**46.** A team needs to evaluate the **correctness and completeness** of thousands of FM responses at scale, without human reviewers and with explanations. Which method is appropriate?

- A. The BLEU metric only
- B. RMSE
- C. Manual review of every response
- D. LLM-as-a-judge in Amazon Bedrock Model Evaluation

**47.** Which metric BEST shows whether a support assistant delivers **business value**?

- A. Perplexity
- B. Rate of tasks completed without escalation to a human
- C. Number of model parameters
- D. Embedding dimension

## Domain 4 — Guidelines for Responsible AI

**48.** Before training a hiring model, a team wants to check whether the dataset is **imbalanced by gender**. Which service should the team use?

- A. Amazon SageMaker Model Monitor
- B. AWS CloudTrail
- C. Amazon SageMaker Clarify
- D. Amazon Bedrock Guardrails

**49.** A production model starts receiving data with a different distribution from the training data. Which service detects this **drift** and sends alerts?

- A. Amazon SageMaker Model Monitor
- B. Amazon SageMaker Ground Truth
- C. AWS Artifact
- D. Amazon Macie

**50.** Which tool documents a model's **intended use, risk rating, and metrics** in a standardized way?

- A. AWS Config
- B. Amazon SageMaker Feature Store
- C. AWS Artifact
- D. Amazon SageMaker Model Cards

**51.** When Amazon Textract extracts data with **low confidence**, a person must review it before the process continues. Which service implements this workflow?

- A. Amazon Comprehend
- B. Amazon Augmented AI (Amazon A2I)
- C. Amazon Bedrock Model Evaluation
- D. AWS Step Functions without review

**52.** An insurance company must explain to each customer **which factors influenced** the price calculated by its model. Which technique is appropriate?

- A. SHAP values with SageMaker Clarify
- B. Increasing the temperature
- C. Encryption with AWS KMS
- D. Batch Transform

**53.** Which **TWO** AWS tools does the exam guide cite for the **explainability and transparency** of AI solutions? (Select TWO.)

- A. AWS Shield
- B. Amazon SageMaker Clarify
- C. Amazon Bedrock Model Evaluations
- D. Amazon Route 53
- E. AWS Snowball

**54.** A customer asks whether the prompts sent to Amazon Bedrock are used to **train the base models**. Which answer is correct?

- A. Yes, unless you turn it off in each request.
- B. Only for Amazon models.
- C. No. They are not used to train the base models and are not shared with the model providers.
- D. Only if you use Provisioned Throughput.

**55.** A speech recognition model performs poorly for older people because the dataset had very few recordings from that group. What is the problem, and how is it corrected?

- A. Overfitting; reduce the epochs
- B. Sampling bias; expand the dataset so it is representative
- C. Hallucination; lower the temperature
- D. Latency; use Provisioned Throughput

**56.** Which statement describes the **trade-off between interpretability and performance**?

- A. Simple models are always more accurate.
- B. Deep learning is fully interpretable.
- C. More complex models are usually more accurate but less interpretable.
- D. Interpretability does not matter in regulated industries.

## Domain 5 — Security, Compliance, and Governance for AI Solutions

**57.** When you use Amazon Bedrock, which of these tasks is the **customer's** responsibility?

- A. Patching the inference servers
- B. Configuring IAM permissions that control who can invoke each model
- C. Maintaining the physical security of the data centers
- D. Isolating the models from the model providers

**58.** An application in private subnets **without internet access** must invoke Amazon Bedrock. Which solution is appropriate?

- A. An interface VPC endpoint (AWS PrivateLink) for `bedrock-runtime`
- B. An internet gateway
- C. An Amazon S3 gateway endpoint
- D. AWS Direct Connect

**59.** The audit team needs to know **which identity** invoked an Amazon Bedrock model, when, and from which IP address. Which service records this?

- A. Amazon CloudWatch metrics
- B. AWS Config
- C. AWS CloudTrail
- D. Amazon Inspector

**60.** For regulatory compliance, the **text of the prompts and the responses** of the model must be retained. What should be enabled?

- A. AWS CloudTrail
- B. Amazon Bedrock model invocation logging
- C. AWS Trusted Advisor
- D. VPC Flow Logs

**61.** A company must classify **5 million historical documents** with an FM over the next month. There is no real-time requirement, and the goal is the **LOWEST cost**. Which option is appropriate?

- A. On-Demand
- B. Provisioned Throughput with a 6-month commitment
- C. Cross-Region inference
- D. Batch inference

**62.** A company needs **guaranteed throughput with no throttling** for a fine-tuned model on Amazon Bedrock with high, steady traffic. Which option should the company purchase?

- A. Provisioned Throughput
- B. On-Demand
- C. Batch inference
- D. Prompt caching

**63.** A customer service agent can issue refunds. The company must guarantee that the agent can **never** issue refunds over USD 500, **even if it suffers a prompt injection attack**. Which solution is appropriate?

- A. Add the rule to the agent's system prompt
- B. Increase the temperature
- C. Policy in Amazon Bedrock AgentCore with deterministic (Cedar) policies applied to tool calls in AgentCore Gateway
- D. An Amazon CloudWatch alarm

**64.** An agent must access the user's calendar and CRM **on the user's behalf** through OAuth, without storing secrets in the code. Which service manages these credentials?

- A. Amazon Bedrock AgentCore Identity
- B. Amazon Inspector
- C. An S3 bucket that holds the keys
- D. AWS Shield

**65.** Which **TWO** techniques help **detect hallucinations** in a RAG application? (Select TWO.)

- A. The contextual grounding check in Amazon Bedrock Guardrails
- B. Increasing the temperature
- C. Validating the output against a JSON schema and business rules
- D. Turning off logging
- E. Removing citations from the responses
