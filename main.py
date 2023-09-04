import os
from textbase import bot, Message
# from textbase.models import OpenAI
from typing import List
import requests

from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain.llms import OpenAI

# Load your OpenAI API key
# OpenAI.api_key = ""
# or from environment variable:

# OpenAI.api_key =""



# Prompt for GPT-3.5 Turbo
# SYSTEM_PROMPT = """You are chatting with an AI. There are no specific prefixes for responses, so you can ask or talk about anything you like.
# You will respond in a natural, conversational manner. Feel free to start the conversation with any question or topic, and let's have a pleasant chat!
# """

# SYSTEM_PROMPT = """
#     You are an AI designed to help software developers learn new technologies. 
#     You will provide all the steps needed to learn the said technology. 
#     Only give the name of the things to learn separated by commas.    
# """

# SYSTEM_PROMPT = """
#     Generate a concise list of steps for learning a new technology, without providing explanations.
#     Assume that the user has no prior knowledge of the technology and is looking for a straightforward list of actions to get started.
# """

@bot()
def on_message(message_history: List[Message], state: dict = None):



    steps_template = PromptTemplate(
        input_variables = ['topic'],
        template='Generate a concise list of topics to be learnt for mastering {topic}, without providing explanations. Assume that the user has no prior knowledge of the technology. Do not give more than 10 steps'
    )

    prerequisites_template = PromptTemplate(
        input_variables=['steps'],
        template='For each of the steps given, give the prerequisite knowledge, such as the programming languages, tools, frameworks, concepts etc required to learn it. Return prerequisite as "step name: prerequisite"   STEPS: {steps}'
    )

    resources_template = PromptTemplate(
        input_variables=['steps'],
        template='For each of the steps given, give exactly 1 link of a documentation website where they can be learnt. STEPS: {steps}'
    )


    prompt = message_history[-1]["content"][0]['value']

    # Generate GPT-3.5 Turbo response
    # bot_response = OpenAI.generate(
    #     system_prompt=SYSTEM_PROMPT,
    #     message_history=message_history, # Assuming history is the list of user messages
    #     model="gpt-3.5-turbo",
    # )

    print("Prompt is " + prompt)

    llm = OpenAI(openai_api_key= os.environ.get('OPENAI_API_KEY'), temperature=0.7)
    steps_chain = LLMChain(llm=llm, prompt=steps_template, verbose=True, output_key='steps')
    prerequisites_chain = LLMChain(llm=llm, prompt=prerequisites_template, verbose=True, output_key='prerequisites')
    resources_chain = LLMChain(llm=llm, prompt=resources_template, verbose=True, output_key='resources')

    if prompt:
        steps = steps_chain.run(prompt)
        resources = resources_chain.run(steps = steps)
        prerequisites = prerequisites_chain.run(steps = steps)
        

        # print(steps)
        print(prerequisites)
        print(resources)

        data = {
            'topic': prompt,
            'steps': steps,
            'prerequisites': prerequisites,
            'resources': resources
        }

        

        BASE_URL = "https://roadmap-chatbot-server.onrender.com"
        # BASE_URL = "http://localhost:5000"
        res = requests.post(BASE_URL+'/roadmap', json=data)
        print("res is :")
        print(res.json())

        roadmapId = res.json()['id']
        roadmapURL = BASE_URL + '/roadmap/' + roadmapId

        bot_response = 'I wish you the best of luck on your journey of learning ' + prompt + '. Your roadmap can be found at the following URL: ' + roadmapURL
 

    # print(bot_response)

        response = {
            "data": {
                "messages": [
                    {
                        "data_type": "STRING",
                        "value": bot_response
                    }
                ],
                "state": state
            },
            "errors": [
                {
                    "message": ""
                }
            ]
        }

        return {
            "status_code": 200,
            "response": response
        }
