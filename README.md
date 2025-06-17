# AUTO-REPLY AI CHATBOT 


## DESCRIPTION:

This project automates the process of interacting with a chat application, specifically 
designed to analyze chat history and generate humorous responses using OpenAI's 
GPT-3.5-turbo model. The virtual assistant, named Naruto, is a character that roasts 
people in a funny way, based on the chat history. 

## FEATURES:
1. Automated Chat Interaction.
2. Uses pyautogui to perform mouse and keyboard operations, interacting with the 
chat application without manual intervention.
3. Chat History Analysis.
4. Copies chat history from the chat application and analyzes it to determine if the last 
message was sent by a specific user (e.g., "Himanshu Meshram").
5. Humorous Response Generation.
6. Integrates with OpenAI's GPT-3.5-turbo model to generate funny, roast-style 
responses based on the analyzed chat history.
7. Clipboard Operations.
8. Utilizes pyperclip to copy and paste text, facilitating the retrieval and insertion of 
chat messages.

## WORKFLOW:


• Initialization and Setup.

• Click on the Chrome icon to open the chat application. 

• Wait for a brief period to ensure the application is open and ready for interaction. 

• Chat History Retrieval.

• Periodically select and copy chat history by dragging the mouse over the chat 
area and using the copy shortcut.

• Retrieve the copied text from the clipboard.

• Message Analysis 

• Analyze the copied chat history to check if the last message is from a specific 
user (e.g., "Himanshu Meshram").

• If the last message is from the target user, send the chat history to OpenAI's 
GPT-3.5-turbo to generate a humorous response.

• Copy the generated response to the clipboard.

• Send Response 


## LIBRARIES USED:


1. pyautogui: For automating mouse and keyboard interactions. 
2. time: For adding delays between operations. 
3. pyperclip: For clipboard operations. 
4. openai: For interacting with OpenAI's GPT-3.5-turbo model.
