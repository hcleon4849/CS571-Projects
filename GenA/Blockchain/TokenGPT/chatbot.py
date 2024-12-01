
import gradio as gr
import os
import time
from brain import TokenGPT
import pandas as pd
import base64

# Initialize the TokenGPT instance
tk = TokenGPT()

def print_like_dislike(x: gr.LikeData):
    # This function will print the like/dislike information for each message
    print(x.index, x.value, x.liked)

def add_message(history, message):
    # This function handles the message input and adds it to the history
    for x in message["files"]:
        # If there are images, convert them to base64 and embed them
        with open(x, "rb") as img_file:
            b64_string = base64.b64encode(img_file.read()).decode()
            img_html = f"<img src='data:image/png;base64,{b64_string}' />"
            history.append((img_html, None))
    
    if message["text"] is not None:
        # Add the text message to the history
        history.append((message["text"], None))
    return history, gr.MultimodalTextbox(value=None, interactive=False)

def bot(history):
    # This function handles the bot's response
    response = tk.conversation(history[-1][0])  # Get response from TokenGPT

    if isinstance(response, tuple):  # If the response contains text and image paths
        message, image_paths = response
        print(message)
        for img_path in image_paths:
            # Convert images to base64
            with open(img_path, "rb") as img_file:
                b64_string = base64.b64encode(img_file.read()).decode()
                img_html = f"<img src='data:image/png;base64,{b64_string}' />"
                history.append((None, img_html))  # Add images to history
        history.append((None, message))  # Add message to history
    else:
        history[-1][1] = response  # If no images, just update the message
    return history

# Gradio interface setup
with gr.Blocks() as demo:
    # Chatbot component
    chatbot = gr.Chatbot([], elem_id="chatbot", bubble_full_width=False)

    # Multimodal input (text or image upload)
    chat_input = gr.MultimodalTextbox(interactive=True, file_types=["image"], placeholder="Enter message or upload file...", show_label=False)

    # Link input submission to add_message function
    chat_msg = chat_input.submit(add_message, [chatbot, chat_input], [chatbot, chat_input])

    # Call the bot function to process the message
    bot_msg = chat_msg.then(bot, chatbot, chatbot, api_name="bot_response")
    
    # Reset the input box after submitting a message
    bot_msg.then(lambda: gr.MultimodalTextbox(interactive=True), None, [chat_input])

    # Like functionality for each message
    chatbot.like(print_like_dislike, None, None)

# Run the interface
demo.queue()
demo.launch()
