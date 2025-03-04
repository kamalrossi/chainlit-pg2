## This is updated AI Agent by using
#the title of AI agent, along with
#basic AI sgent operations

import chainlit as cl


@cl.on_message
def main(message:str):
  you_typed=message.title()

  cl.send_message(aiagent_replied="Hey you typed:{you_typed}")    

cl.on_chat_start
def start():
 content="Welcome to AI Agent"
 cl.send_message(content)