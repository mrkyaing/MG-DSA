from fpdf import FPDF
pdf = PDF()
pdf.add_page()

pdf.chapter_title("AI-900 Microsoft Azure AI Fundamentals - Practice Questions")
pdf.chapter_body("25 Practice Questions with Answers and Explanations")

questions = [
    ("Which of the following is an example of a computer vision workload?",
     "A. Predicting house prices\nB. Translating text between languages\nC. Detecting faces in an image\nD. Analyzing customer sentiment from reviews",
     "C. Detecting faces in an image",
     "Computer Vision involves interpreting visual input like images and videos."),

    ("What is a primary goal of machine learning?",
     "A. To write rule-based logic\nB. To develop hard-coded algorithms\nC. To allow systems to learn from data and improve over time\nD. To translate programming languages",
     "C. To allow systems to learn from data and improve over time",
     "ML enables models to make predictions or decisions based on past data."),

    ("Which Azure service would you use to create a chatbot?",
     "A. Azure Cognitive Services\nB. Azure Bot Service\nC. Azure Logic Apps\nD. Azure Functions",
     "B. Azure Bot Service",
     "Azure Bot Service is designed specifically to build and deploy bots."),

    ("What is the purpose of Natural Language Processing (NLP)?",
     "A. Detecting objects in images\nB. Recognizing spoken language\nC. Understanding and processing human language\nD. Recommending products",
     "C. Understanding and processing human language",
     "NLP helps machines interpret human language in context."),

    ("Which scenario best represents a classification machine learning model?",
     "A. Predicting next week’s weather temperature\nB. Grouping customers by purchase behavior\nC. Identifying whether an email is spam or not\nD. Summarizing a document",
     "C. Identifying whether an email is spam or not",
     "Classification assigns items into categories, like spam or not spam."),

    ("What type of machine learning is used when the model is trained with labeled data?",
     "A. Unsupervised learning\nB. Reinforcement learning\nC. Supervised learning\nD. Deep learning",
     "C. Supervised learning",
     "Supervised learning uses labeled data to train the model to predict outcomes."),

    ("You want to group customers based on purchasing behavior without labeled data. What type of ML is best?",
     "A. Regression\nB. Classification\nC. Supervised learning\nD. Unsupervised learning",
     "D. Unsupervised learning",
     "Unsupervised learning is used to find hidden patterns in data without labels (e.g., clustering)."),

    ("Which Azure service provides a drag-and-drop interface to build ML models without coding?",
     "A. Azure ML Designer\nB. Azure Cognitive Services\nC. Azure Functions\nD. Azure Bot Service",
     "A. Azure ML Designer",
     "Azure ML Designer allows you to build and deploy models visually with pre-built components."),

    ("What is the main advantage of Automated ML (AutoML) in Azure?",
     "A. You must write custom code for all models\nB. It predicts customer behavior without any model\nC. It automates model selection and tuning\nD. It builds web apps for ML",
     "C. It automates model selection and tuning",
     "AutoML helps identify the best model and parameters for your dataset automatically."),

    ("In machine learning, what is 'overfitting'?",
     "A. The model is too simple and can't learn\nB. The model performs well on training data but poorly on new data\nC. The model performs equally well on all data\nD. The model cannot be trained",
     "B. The model performs well on training data but poorly on new data",
     "Overfitting occurs when a model memorizes training data instead of generalizing patterns."),

    ("Which Azure service is used to extract text from images and documents?",
     "A. Azure Speech\nB. Form Recognizer\nC. QnA Maker\nD. Azure Bot Service",
     "B. Form Recognizer",
     "Form Recognizer extracts structured text and key-value pairs from forms and documents."),

    ("What is the purpose of the Custom Vision service?",
     "A. Translate text to different languages\nB. Extract sentiment from text\nC. Build a custom image classifier\nD. Identify intent from user queries",
     "C. Build a custom image classifier",
     "Custom Vision lets you train a model with your own images for object detection or classification."),

    ("What type of problem is object detection solving?",
     "A. Classifying entire images into categories\nB. Finding and labeling objects within an image\nC. Extracting data from forms\nD. Converting speech to text",
     "B. Finding and labeling objects within an image",
     "Object detection identifies both the location and category of objects in an image."),

    ("You want to verify someone's identity using facial features. Which service do you use?",
     "A. Text Analytics\nB. Face API\nC. Translator\nD. Azure ML Studio",
     "B. Face API",
     "Face API can detect and compare facial features for identification and verification."),

    ("What is a common use case of OCR (Optical Character Recognition)?",
     "A. Predicting product sales\nB. Translating spoken words\nC. Converting scanned documents to text\nD. Sentiment analysis on text",
     "C. Converting scanned documents to text",
     "OCR technology is used to extract machine-readable text from scanned images or documents."),

    ("Which Azure service helps extract key phrases, entities, and sentiment from text?",
     "A. Azure Bot Service\nB. Text Analytics API\nC. Translator\nD. Form Recognizer",
     "B. Text Analytics API",
     "It provides insights like sentiment, key phrases, named entities, and language detection from text."),

    ("You want to translate customer feedback from multiple languages into English. Which service should you use?",
     "A. Translator\nB. Face API\nC. Azure Machine Learning\nD. Azure Bot Service",
     "A. Translator",
     "Translator service automatically translates text between languages."),

    ("What is the purpose of Language Understanding (LUIS)?",
     "A. To analyze images\nB. To identify user intents and extract entities from natural language queries\nC. To extract text from scanned documents\nD. To convert speech to text",
     "B. To identify user intents and extract entities from natural language queries",
     "LUIS helps build conversational AI that understands user input."),

    ("Which of the following is an example of sentiment analysis?",
     "A. Determining if a tweet is positive, negative, or neutral\nB. Translating text from Spanish to English\nC. Recognizing faces in a photo\nD. Classifying an email as spam or not spam",
     "A. Determining if a tweet is positive, negative, or neutral",
     "Sentiment analysis classifies the emotion or opinion in text."),

    ("Which Azure service provides a unified platform for NLP tasks such as translation, summarization, and entity recognition?",
     "A. Azure AI Language\nB. Azure Bot Service\nC. Azure Functions\nD. Azure Cognitive Search",
     "A. Azure AI Language",
     "Azure AI Language integrates multiple NLP capabilities in one service."),

    ("What Azure service is primarily used to build and deploy chatbots?",
     "A. Azure Cognitive Services\nB. Azure Bot Service\nC. Azure Functions\nD. Azure Logic Apps",
     "B. Azure Bot Service",
     "Azure Bot Service provides an integrated environment to develop, test, and deploy chatbots."),

    ("What is the role of QnA Maker in conversational AI?",
     "A. To recognize speech and convert it to text\nB. To create a question-and-answer knowledge base from FAQs\nC. To translate conversations in real-time\nD. To perform sentiment analysis on chats",
     "B. To create a question-and-answer knowledge base from FAQs",
     "QnA Maker lets you build a simple FAQ bot using existing content."),

    ("Which of the following is a key feature of the Bot Framework?",
     "A. Drag-and-drop ML model building\nB. SDK and tools for developing conversational AI bots\nC. Automated text translation\nD. Facial recognition for authentication",
     "B. SDK and tools for developing conversational AI bots",
     "Bot Framework provides a rich SDK and tools for building complex bots."),

    ("How can you integrate an Azure chatbot into Microsoft Teams?",
     "A. By exporting it as a PowerPoint file\nB. By registering the bot and adding it as a Teams app\nC. By sending an email to Microsoft support\nD. By enabling Face API on the chatbot",
     "B. By registering the bot and adding it as a Teams app",
     "Bots must be registered and configured for Teams integration."),

    ("Which service helps your chatbot understand user intent and extract important information from conversations?",
     "A. Azure Functions\nB. Language Understanding (LUIS)\nC. Azure Machine Learning\nD. Form Recognizer",
     "B. Language Understanding (LUIS)",
     "LUIS processes natural language queries to understand intent and entities.")
]

for i, (q, opts, ans, expl) in enumerate(questions, start=1):
    pdf.chapter_title(f"Q{i}. {q}")
    pdf.chapter_body(f"{opts}\n\nAnswer: {ans}\nExplanation: {expl}")

pdf_path = "D:\\works\\MG-DSA\\AI-900_Practice_Questions.pdf"
pdf.output(pdf_path)
pdf_path
