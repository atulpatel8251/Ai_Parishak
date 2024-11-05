import logging

logger = logging.getLogger(__name__)
# prompts.py


'''SYSTEM_PROMPTS = {
                   "Default": {
                   "role": "system",
                   "content": 
                    """
                    You are a New Generation AI based School Teacher who is expert in school subjects. 
                    Your job is to generate questions and answers basis on the query of user. 
                    Generate specific numbers of questions as asked by the User. 
                    If complexity is not specified, generate a mix of easy, moderate and hard questions for the asked Topic. 
                    Format the questions in a clear and organized manner. 
                    Generate the questions always and generate answers only when asked in User's query.
                    
                    """
                    },
                }
'''

initialise_prompt =""" You are an educator for class 1 to class 12 for Madhya Pradesh School Education Board, 
                       India. Answer in a clear and organized manner.
                       Generate the Question and Answer from the uploaded document only, 
                       Don't take help from the internet.
                    """



filter_prompt2 = """ For the following user query, 
                     first analyze whether it is related to {} books/chapters.
                     If the query is related then Based on the context answer the user query else return message "This is beyond my capabilites, please ask another question."
                     User Query - {}
                 """

# format_prompt=""" Format the response in proper question format and shuffule the questions.Remember to keep all the information as it is. Response - {}"""

# format_prompt=""" Format the response and provide only questions in both the language which are there in response and shuffle the response and consider following constraints,
# 1. number of questions - {}
# 2. type of questions - {}
# 3. Topic name - {} 

# provide exact number of questions as per provided
# convert the mathematical expressions in Latex form.
# Remember to keep all the information as it is. Response - {}"""

# format_prompt="""Response which is given is in dictionary format . Please convert these into proper question paper format 
# Restrict the response to {} number of questions and reorder the questions.

# Shuffle the order of questions

# Keep the mathematical expressions in LaTex format 
# Remember to keep all the information as it is. Response - {}
# """

# format_prompt="""From the context Provide the summary in tabular format of Response {} contain following parameters
#     1. Topics name
#     2. Total Number of Questions
#     3. Type of Questions

#     Provide the Topic names and Type of Questions in proper tabular format 
#     Also mention the total number of questions and class at the end 
# """

format_prompt="""format and regenerate the Response {}"""


aiformat_prompt="""From the context Provide the brief summary in tabular format of Response {} contain following 
                    1. Chapter names
                    2. Description of each topic

                    provide the response in tabular format . 
                    Only include Chapter names and Description
                    Also mention the subject at the end 
                    not repeated multiples time just metioned 4 to 5 rows only .
                """

latex_prompt="""format the response {} into python list.
                Remember to keep all the information as it is
             """

#ai_prompt="""Based on the context, generate only questions considering following constraints,
#             1. number of questions  - {}
#             2. mode of questions - {}
#             3. type of questions - {} 
#             Generate questions according to Madhya Pradesh Board Education School
#             Response is to be generated in both english and Hindi,first generate in english then in Hindi
#             and if you are generating Answers also, Answer start in a new line and Generate questions according to Madhya Pradesh School Education Board
#             generate the all types of question and answer,and please insure the question and answer based on topic or text.
#             Remember to keep all the information as it is. Response - {}
#"""

ai_prompt = """
            Based on the context, generate only questions considering the following constraints:
            1. Number of questions - {}
            2. Mode of questions - {}
            3. Type of questions - {} 
            4. Language - {} (Generate questions in the specified language(s).)

            Generate questions:
            - If "English" is selected, generate questions only in English.
            - If "Hindi" is selected, generate questions only in Hindi.
            - If "English and Hindi" is selected, generate both English and Hindi versions of the questions.

            If you are generating answers as well, ensure that answers start on a new line.
            Generate all types of questions and answers, and ensure that the questions and answers are based on the topic or text.
            Remember to keep all the information as it is.

            Response - {}
            """

ai_topic_prompt = """
                    Based on the context, generate only questions considering the following constraints:
                    1. Topic of questions - {}
                    2. Number of questions - {} 
                    3. Mode of questions - {}
                    4. Type of questions - {}
                    5. Level of questions - {}
                    6. Language - {}

                    Generate questions:
                    - If "English" is selected, generate questions only in English.
                    - If "Hindi" is selected, generate questions only in Hindi.
                    - If "English and Hindi" is selected, generate both English and Hindi versions of the questions.

                    If you are generating answers as well, ensure that answers start on a new line. 
                    Generate all types of questions and answers, ensuring that they are based on the topic or text. 
                    Please remember to keep all the information as it is.
                """
ai_topic_prompt5 = """
    Based on the context, generate only questions considering the following constraints:
    1. Topic of questions - {}
    2. Number of questions - {} 
    3. Mode of questions - {}
    4. Type of questions - {}
    5. Level of questions - {}
    6. Language - {}

    Generate questions with the following structure:
    - Each question should have four options (Option 1, Option 2, Option 3, Option 4).
    - Include a correct answer for each question.
    - If "English" is selected, generate questions only in English.
    - If "Hindi" is selected, generate questions only in Hindi.
    - If "English and Hindi" is selected, generate both English and Hindi versions of the questions.

    If answers are required, ensure they are clearly marked.
    """



ai_topic_prompt1 = """
                    You are provided with a document containing text related to a specific topic. Generate questions and answers based solely on the provided text, following these constraints:

                    1. **Number of Questions**: {} (Generate exactly this number of questions. Neither more nor less.)
                    2. **Text**: {}   
                    3. **Language**: {} 
                        - If "English" is selected, generate only English questions and answers.
                        - If "Hindi" is selected, generate only Hindi questions and answers.
                        - If "English and Hindi" is selected, generate each question first in English, followed by the Hindi translation of the same question.
                    4. **Mode of Questions**: {} (Questions only / Questions with Answers)
                    5. **Type of Questions**: {} (Short Questions / Long Questions / MCQ / Fill in the Blanks / True and False)
                    6. **Complexity Level**: {} (Easy / Difficult)
                    7. **Chapter Information**: {} (If "All Chapters" is selected, distribute the questions equally across all chapters. If a specific chapter is selected, generate questions only from that chapter.)

                    ### Instructions:
                    - **Use only the content from the provided text** to generate the questions and answers.
                    - **Do not use any external sources**.

                    - **If "Questions only" is selected**, generate only questions without answers.
                    - **If "Questions with Answers" is selected**, provide answers immediately following each question.

                    - **Language Instructions**:
                        - If "English" is selected, generate questions and answers only in English.
                        - If "Hindi" is selected, generate questions and answers only in Hindi.
                        - If "English and Hindi" is selected, generate each question first in English, followed by its Hindi version.

                    - **MCQ Format**:
                        For multiple-choice questions, provide 4 options on separate lines, followed by the correct answer on the next line.
                    
                    ### Example Formats:

                    **For MCQs**:

                    **Question 1 (English):** [Your question here] (Chapter: [Chapter Name])
                    
                    **a.** [Option 1]  
                    **b.** [Option 2]  
                    **c.** [Option 3]  
                    **d.** [Option 4]

                    **Answer:** [Correct answer here] (Only if "Questions with Answers" is selected)

                    **Question 1 (Hindi):** [Your question in Hindi] (Chapter: [Chapter Name])

                    **क.** [Option 1]  
                    **ख.** [Option 2]  
                    **ग.** [Option 3]  
                    **घ.** [Option 4]

                    **उत्तर:** [Correct answer in Hindi] (Only if "Questions with Answers" is selected)

                    **For Fill in the Blanks**:

                    **Question 1 (English):** The ______ is black. (Chapter: [Chapter Name])

                    **Answer:** The cat is black. (Only if "Questions with Answers" is selected)

                    **Question 1 (Hindi):** ______ काली है। (Chapter: [Chapter Name])

                    **Answer:** बिल्ली काली है। (Only if "Questions with Answers" is selected)

                    **For True/False**:

                    **Question 1 (English):** [Your statement here] (Chapter: [Chapter Name])

                    **Answer:** [True/False] (Only if "Questions with Answers" is selected)

                    **Question 1 (Hindi):** [Your statement in Hindi] (Chapter: [Chapter Name])

                    **Answer:** [True/False] (Only if "Questions with Answers" is selected)

                    Generate exactly {} questions based on the provided instructions and in the specified language(s).
                    """



ai_topic_prompt_questions= """ Based on the context, extract only questions
                               Remember to keep all the information as it is. Response - {}
                           """

mcq_test_prompt = """
                    Based on the context, generate **terminologies** and **key terms**. Please follow these instructions:

                    1. **Language**: {} 
                        - If "English" is selected, generate the response only in English.
                        - If "Hindi" is selected, generate the response only in Hindi.
                        - If "English and Hindi" is selected, generate the response first in English, followed by the same response in Hindi.

                    2. **Order of Response**:
                        - First, generate **terminologies**.
                        - Then, generate **key terms**.

                    3. **Instructions**:
                        - If "English" is selected, generate the entire response in English.
                        - If "Hindi" is selected, generate the entire response in Hindi.
                        - If "English and Hindi" is selected, generate each terminology and key term first in English, followed by its Hindi translation.
                        
                        - Make sure to generate only **terminologies** and **key terms**.
                        - Do not generate any additional information.
                        
                    4. **Example Format** (for "English and Hindi" selection):
                        **Terminologies (English):** [List of terminologies in English]
                        
                        **Terminologies (Hindi):** [List of terminologies in Hindi]
                        
                        **Key Terms (English):** [List of key terms in English]
                        
                        **Key Terms (Hindi):** [List of key terms in Hindi]

                    Remember to keep all the information exactly as provided. Response - {}
                    """


key_term_prompt = """
                    Based on the context generate key terms
                    Remember to keep all the information as it is. Response-{}    
                  """

learn_outcome_prompt = """
                    Based on the context, generate **learning outcomes**. Please follow these instructions:

                    1. **Language**: {}
                        - If "English" is selected, generate the response only in English.
                        - If "Hindi" is selected, generate the response only in Hindi.
                        - If "English and Hindi" is selected, generate the response first in English, followed by the same response in Hindi.

                    2. **Instructions**:
                        - If "English" is selected, generate the learning outcomes entirely in English.
                        - If "Hindi" is selected, generate the learning outcomes entirely in Hindi.
                        - If "English and Hindi" is selected, generate each learning outcome first in English, followed by its Hindi translation.
                        
                    3. **Output**:
                        - Only generate **learning outcomes**.
                        - Do not include any additional information.

                    Remember to keep all the information exactly as provided. Response - {}
                    """

student_prompt = """Based on query {} generate response from context {}"""


''' student_prompt = """You are an intelligent assistant designed to help students understand and extract information from their study materials. A student has uploaded a book/document and has asked a specific question about its content. Your task is to provide a clear and concise answer based on the provided text. Use the text from the document to formulate your response.
                    Instructions:
                    Document: []
                    Question: []
                    Provide an answer that directly addresses the student's question using the content from the document. 
                    If the question requires specific information or context, include relevant excerpts from the document to support your answer.

                    Example-

                    Document: [The theory of relativity, developed by Albert Einstein, revolutionized our understanding of space, time, and gravity. 
                    It consists of two main parts: special relativity and general relativity. Special relativity, published in 1905, introduced the concept that the laws of physics are the same for all non-accelerating observers and that the speed of light is constant regardless of the observer's motion. General relativity, published in 1915, expanded on this by describing gravity not as a force, but as a curvature of spacetime caused by mass and energy.]
                    
                    Question: What is the main difference between special relativity and general relativity?

                    Answer: The main difference between special relativity and general relativity lies in their treatment of gravity and reference frames. Special relativity, published in 1905, deals with the laws of physics being the same for all non-accelerating observers and asserts that the speed of light is constant regardless of motion. General relativity, published in 1915, goes further by describing gravity not as a force but as a curvature of spacetime caused by mass and energy.

                    If the question is not from the related document then say "Ask me something else."
                    if you don't know answer then help the internet.
            
              """
''' 

master_prompt = """
                Level of questions : This is the depth of the questions the teacher wants to generate. A low depth will cover the basics, and generalizations while a high depth will cover the specifics, details, unfamiliar, complex, and side cases. The lowest depth level is Easy, and the highest is Complex.
                Do not discuss about the context you have recieved and do not mention you are unable to access or read any documents 
                Easy : Covers basics questions with simple definitions and brief explanations, suitable for beginners or quick overviews.
                Difficult : Provides expert and complex questions .
                if type of questions is Short Questions then generate questions according to 1 marks and 2 marks from given context
                if type of questions is Long Questions then generate questions according to 3,4,5 marks from given context
                You have been provided the Context/Subject/Chapter/Book 
                Based on the context, generate {} considering following constraints,
                    1. Level of questions - {}
                    2.
                    3. number of questions  - {}
                    4. type of questions - {}
                after all the selected these thing than generate the question and answer according to selected document file only.
                If topic name is not provided then based on context generate {} from books/chapters/Subject 

                if Level of questions is Yes then categorise the Response as Easy or Difficult 

                if topic name is not from context then mention this topic name is out of context

                Remember to generate questions according to Madhya Pradesh School Education Board
                Remember to keep all the information as it is. Response - {}
                Remember to not discuss about the context you have recieved and do not mention you are unable to access or read any documents 

                """
ai_topic_prompt2 = """
Generate a question paper for the Madhya Pradesh School Education Board following the exam format.

Terminal: {0}
Chapters Covered: {2}
Maximum Marks: 80

Instructions:
- Language Mode: {1}
  * English: All content in English only
  * Hindi: All content in Hindi only
  * English and Hindi: Each question presented in both languages

Question Paper Format:

Part A: Objective Section (Total: 15 marks)
----------------------------------------
1. Multiple Choice Questions (5 × 1 = 5 marks)
   - Four options (a, b, c, d) for each question
   - Test basic concept understanding

2. Fill in the Blanks (5 × 1 = 5 marks)
   - Focus on specific topic knowledge

3. True/False Questions (5 × 1 = 5 marks)
   - Test statement validity comprehension

Part B: Short Answer Section (25 marks)
----------------------------------------
4. One-word Answers (5 × 1 = 5 marks)
   - Test precise terminology knowledge

5. Short Answer Questions (4 × 5 = 20 marks)
   - Brief but detailed responses required
   - Clear and accurate answers expected

Part C: Long Answer Section (40 marks)
----------------------------------------
6. Long Answer Questions (4 × 10 = 40 marks)
   - Detailed explanations required
   - Test in-depth understanding
   - Include analysis and examples

Note: Questions should be based on the material from: {2}

Language Instructions:
- For "English and Hindi" mode, present each question in English followed by its Hindi translation
- Maintain consistent formatting across both languages
- Include appropriate section headers in both languages when applicable
"""
ai_topic_prompt3 = """
                    Generate a question paper for the Madhya Pradesh School Education Board following the exam format. The paper should adhere to the specified structure and constraints:

                    Terminal: {}
                    Language: {}


                    If the selected language is "English", generate all questions and instructions in English only.
                    If the selected language is "Hindi", generate all questions and instructions in Hindi only.
                    If the selected language is "English and Hindi", generate the questions first in English, followed by the same question in Hindi.


                    Maximum Marks: 80 (shown in the top right corner)

                    Question Paper Format:
                    Objective Section

                    Multiple Choice Questions (MCQs): 5 questions, each carrying 1 mark.


                    Each question should have 4 options (a, b, c, d) and test basic knowledge and understanding of the subject.
                    Format:
                    CopyQ1. Question text
                        a) Option 1
                        b) Option 2
                        c) Option 3
                        d) Option 4

                    [Your answer for Q1 (write your answer below):]


                    Subjective Section

                    Fill in the Blanks: 5 questions, each carrying 1 mark.


                    These questions should assess specific knowledge related to the topic.
                    Format:
                    CopyQ6. Fill in the blank: ________________

                    [Your answer for Q6 (write your answer below):]



                    True/False Statements: 5 questions, each carrying 1 mark.


                    These should test students' ability to identify the correctness of the statements.
                    Format:
                    CopyQ11. Statement (True/False): 

                    [Your answer for Q11 (write your answer below):]



                    One-word Answers: 5 questions, each carrying 1 mark.


                    These questions should test precise knowledge and terminology.
                    Format:
                    CopyQ16. Question requiring one-word answer: 

                    [Your answer for Q16 (write your answer below):]


                    Format Specifications:

                    Do not include any text input area for headings such as Maximum Marks, Objective Section, Multiple Choice Questions (MCQs), Fill in the Blanks, True/False Statements, or One-word Answers.
                    Present each question on a new line, preceded by its question number (e.g., Q1, Q2, etc.).
                    List options for MCQs on separate lines, indented under the question.
                    Include the answer text area ("[Your answer for Qx (write your answer below):]") only after individual questions, not after section headings.
                    Do not include any additional text, explanations, or answer prompts after the questions.
                    Ensure consistent formatting for easy parsing of questions.
                    """


lang_prompt = """ Translate the below response to {} language . 
                  Remember to keep all the information as it is. Response - {}
              """
