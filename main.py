import pyautogui
import pyperclip
import time
from openai import OpenAI

client = OpenAI(
    api_key="Put your api key here "
)

def is_last_message_from_sender(chat_log, sender_name="sender's name"):
    messages = chat_log.strip().split("/2025")[-1]
    if sender_name in messages:
        return True
    return False

    
    # Step 1: Click on the icon
pyautogui.click(1268 ,1048)
time.sleep(1)


while True:



    # Step 2: Drag to select text
    pyautogui.moveTo(686,200)
    pyautogui.dragTo(891 , 934 , duration=1.0, button='left')  # optional duration to simulate natural dragging


    # Step 3: Copy the selected text
    pyautogui.hotkey('ctrl', 'c')
    time.sleep(2)  # wait for clipboard to update
    pyautogui.click(695,236)

    # Step 4: Get clipboard content
    chat_history = pyperclip.paste()

    # Optional: print the text
    print(chat_history)

    if is_last_message_from_sender(chat_history):


        completion = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role" : "system", "content":"you are a person named Tanish Kanchan , "
                "who speaks hindi as well as english. You are from india and you are a coder. "
                "you analyze chat history and respond like Tanish Kanchan. "
                "Output should be the next chat response (text message only no date time or  name to include in the text)"},
                {"role": "user", "content": chat_history }
            ]
        )

        response =completion.choices[0].message.content
        pyperclip.copy(response)

        pyautogui.click(882,975)
        time.sleep(1)

        pyautogui.hotkey('ctrl', 'v')
        time.sleep(1)

        pyautogui.press('enter')
