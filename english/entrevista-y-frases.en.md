# Interview and useful phrases (A2 → B1 level)

> The model answers use **short, simple sentences on purpose**. In a technical interview, saying something simple and clear is much better than a long sentence with mistakes. **Adapt them, memorize them and practice out loud.**

---

## 1. Your self-introduction (60–90 seconds)

Fill in the template with your details, learn it by heart and record yourself saying it **10 times** before the exam.

> *"Hi, my name is **[your name]**. I'm from **[city]**, Colombia.*
> *I studied / I'm studying **[degree, e.g. Systems Engineering]** at **[university]**.*
> *I'm very interested in **data and cloud technologies**. I work with **SQL** and **Python** to analyze data, and I'm learning **AWS**: I'm preparing for the **AWS Certified AI Practitioner** certification.*
> *Recently, I **[built / worked on]** a project where I **[describe it in one line: e.g. analyzed sales data with SQL and created a dashboard]**.*
> *I want to join the **All Star program** because I want to grow as a data professional, work on real projects for international clients, and learn from experts.*
> *In my free time I like **[hobby]**. Thank you!"*

## 2. Phrases for the technical interview

### Asking them to repeat or clarify (there is nothing wrong with it!)

| Phrase | When |
|---|---|
| *Sorry, could you repeat the question, please?* | You did not understand |
| *Could you speak a little more slowly, please?* | They speak too fast |
| *Just to make sure I understand: you want me to… , right?* | Confirm the statement ⭐ |
| *What does "___" mean in this context?* | A specific word |
| *Can I assume that the input is always valid?* | Ask about assumptions ⭐ |
| *Should I consider null values / empty lists?* | Edge cases ⭐ |
| *Is it OK if I write the solution in Python / SQL?* | Language |

### Buying time to think

- *Let me think about it for a moment.*
- *That's a good question. Let me see…*
- *Give me a second to organize my ideas.*
- *I'm going to write down the main steps first.*

### Explaining your solution ⭐

- *My approach is to…*
- *First, I… Then, I… Finally, I…*
- *I'm going to use a dictionary / a hash map to count the elements.*
- *I use a LEFT JOIN because I want to keep all the customers.*
- *Here I group by department and calculate the average salary.*
- *This loop goes through the list once, so the time complexity is O(n).*
- *The space complexity is O(1) because I only use two variables.*
- *A simple solution is brute force, but it's O(n²). I can improve it with a set.*
- *Let me test it with an example: if the input is… the output is…*
- *An edge case is an empty list. In that case, I return zero.*
- *If I had more time, I would optimize this part.*

### When you do not know something (be honest, but show how you think)

- *I'm not 100% sure, but I think…*
- *I haven't used that service yet, but I know it's similar to…*
- *I don't remember the exact syntax, but the idea is…*
- *I would check the documentation, but my approach would be…*

## 3. Typical questions with model answers

### "Tell me about yourself."

→ Use your self-introduction (section 1).

### "Why do you want to work at Blend360?" / "Why the All Star program?"

> *"Blend360 is a leading data science and AI company, and it is an **AWS Premier Tier Partner**. I'm very interested in data and AWS, so it's a great place for me. I also like that Blend works with **international clients**, and it is **growing a lot in Colombia**. The All Star program is perfect for me because it combines **training and real projects**. I want to learn from experienced people and grow my career in data."*

### "What is your greatest strength?"

> *"I'm a fast learner and I'm very persistent. For example, I'm preparing for an AWS certification on my own. When I have a problem, I don't give up: I look for information, I test different solutions and I ask for help when I need it."*

### "What is your weakness?"

> *"My English is not perfect yet, but I'm working on it every day. I practice with technical videos and flashcards, and I'm improving quickly. I can read technical documentation without problems."*

💡 This answer turns your A2 level into a **strength** (active improvement). It is honest and it shows discipline.

### "Tell me about a challenge you faced." (the **STAR** method)

| STAR | What you say | Example |
|---|---|---|
| **S**ituation | The context | *"In a university project, we had to analyze a big dataset with many errors."* |
| **T**ask | Your responsibility | *"My task was to clean the data and prepare it for the analysis."* |
| **A**ction | What **you** did | *"I used Python and pandas to remove duplicates, fill missing values and fix the date formats. I also wrote SQL queries to check the results."* |
| **R**esult | The result (with numbers if you can!) | *"We finished on time, and the analysis was 30% faster because the data was clean. We got the highest grade."* |

### "Tell me about a time you worked in a team / had a disagreement."

> *"In a project, a teammate and I had different ideas about the database design. We listened to each other, we compared the advantages of each option, and we chose the best one together. I learned that good communication is very important."*

### "Where do you see yourself in five years?"

> *"I see myself as a data professional, maybe a data engineer or data scientist, working on important projects with AWS and AI. I also want to help and mentor new people."*

### "Do you have any questions for us?" ⭐ (always say yes)

- *What does a typical day look like for an All Star?*
- *What technologies will I use in the first months?*
- *How is the training organized in the program?*
- *What are the next steps in the process?*

## 4. Frequent technical questions and how to start the answer

| Question | Start of the answer |
|---|---|
| *What is the difference between WHERE and HAVING?* | *WHERE filters **rows** before grouping. HAVING filters **groups** after the GROUP BY, so it can use aggregate functions.* |
| *What is the difference between INNER JOIN and LEFT JOIN?* | *INNER JOIN returns only matching rows. LEFT JOIN returns all the rows from the left table, and NULL when there is no match.* |
| *What is a primary key?* | *It's a column that uniquely identifies each row. It can't be null or duplicated.* |
| *What is a window function?* | *It's a function that calculates a value over a group of rows, but it doesn't collapse the rows like GROUP BY. For example, ROW_NUMBER or a running total.* |
| *List vs. tuple in Python?* | *A list is mutable, so you can change it. A tuple is immutable.* |
| *What is Big O notation?* | *It describes how the time or memory of an algorithm grows when the input grows.* |
| *What is AWS?* | *AWS is Amazon's cloud platform. It offers services like computing, storage and databases on demand, and you pay only for what you use.* |
| *What is a data lake?* | *It's a central storage for all types of data (structured and unstructured) at any scale. In AWS, it's usually built on Amazon S3.* |
| *Athena vs. Redshift?* | *Athena is serverless SQL directly on S3, good for ad hoc queries. Redshift is a data warehouse, better for complex and frequent BI queries.* |
| *What is ETL?* | *Extract, Transform, Load: you take data from sources, clean and transform it, and load it into a destination like a data warehouse.* |

## 5. Pronunciation of technical words 🔊

The hints are written the way a Spanish speaker would read them.

| Word | Sounds roughly like | Common mistake |
|---|---|---|
| SQL | "és-kiu-él" or "síkuel" (both are valid) | |
| query | "kuíri" | ❌ "kuéri" |
| data | "déira" (US) or "déita" | ❌ "dáta" |
| Python | "páizon" | ❌ "pitón" |
| tuple | "túpol" or "tiúpol" | |
| queue | "kiú" (same as the letter Q) | ❌ "kuéue" |
| cache | "kash" (like *cash*) | ❌ "cáche" |
| char | "char" (like *charcoal*) or "kar" | |
| schema | "skíma" | ❌ "chema" |
| width / height | "uíz" / "jáit" | ❌ "jeigt" |
| algorithm | "álgo-ri-zem" | |
| analysis / analytics | "anális-is" / "ana-lí-tiks" | |
| AWS | "éi-dábliu-és" | |
| S3 | "és-zrí" | |
| EC2 | "í-sí-tú" | |
| Lambda | "lámda" (the *b* is silent) | |
| Azure | "ázher" | |
| GitHub | "guít-jab" | ❌ "jit-jub" |
| null | "nal" | ❌ "nul" |
| integer | "ín-ti-yer" | |
| array | "aréi" | |
| method | "mézod" | |
| pseudocode | "súdo-coud" (the *p* is silent) | |
| suite | "suít" (like *sweet*) | ❌ "suíte" |

## 6. Numbers out loud

| Written | Said |
|---|---|
| 2024 | *twenty twenty-four* |
| 1,500 | *one thousand five hundred* / *fifteen hundred* |
| 3.75 | *three point seven five* |
| 25% | *twenty-five percent* |
| O(n²) | *O of n squared* |
| O(n log n) | *O of n log n* |
| 10^6 | *ten to the sixth* / *one million* |
| 1st, 2nd, 3rd, 4th | *first, second, third, fourth* |

---

**Practice:** record yourself answering **3 questions a day** from section 3 during weeks 5 and 6.
