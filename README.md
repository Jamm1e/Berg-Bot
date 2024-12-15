# Berg-Bot: College Application Assistant
Berg-Bot is an interactive bot designed to assist prospective college students throughout the application process. Built using Python, the bot provides real-time help by recognizing keywords in user queries and returning relevant responses. Inspired by the ELIZA chatbot structure, Berg-Bot ensures that users can quickly find the information they need by simply typing "help" in any field where they encounter difficulties.

## Key Features
- **Keyword Recognition**: Identifies keywords from user input and delivers tailored responses based on a pre-defined database.
- **On-Demand Help**: Users can type "help" to receive targeted assistance for the specific application field they are working on.
- **Dynamic Inputs**: Validates user input for fields such as email, birth date, and GPA to ensure proper formatting.
- **Interactive Corrections**: Allows users to review, edit, and confirm their application details before submission.

## Technology Used
- **Python**: A core programming language for logic implementation.
- **Pandas**: Used for reading and managing keyword-response data from a CSV file.
- **CSV File**: Serves as the database for keywords and corresponding responses.
- **ELIZA Chatbot Structure**: Implements a keyword-response pattern to simulate a conversational flow.

## How It Works
1. **Keyword Database**: A CSV file stores keywords and their corresponding responses for each application field (e.g., first name, email, address).
2. **User Interaction**:
    - The bot asks users to fill out each field in the application.
    - If the user types "help," Berg-Bot searches for relevant keywords in the user’s question and retrieves an appropriate response.
3. **Validation**:
    - Special fields like email, birth date, and GPA are validated for correct formatting and values.
4. **Review and Edit**:
    - Users review their application details, make edits if necessary, and confirm before submission.

## Usage Instructions
1. Ensure that the `sample_responses.csv` file (containing keywords and responses) is in the same directory as the Python script.
2. Run the Python script.
3. Follow the prompts to fill out the application form.
4. Type "help" whenever assistance is needed for a particular field.
5. Review and edit the application details as needed before final submission.


## Future Enhancements
- Add natural language processing (NLP) for better contextual understanding.
- Include a wider range of keywords and responses for additional application fields.
- Develop a graphical user interface (GUI) for improved usability.

## Credits
Developed by Jammie-Ann Matthias, Anthony Jarama, Yuri Jeudy and Aidan Menendez.


