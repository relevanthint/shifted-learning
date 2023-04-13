from fastapi import APIRouter
from schemas import basewording
from models.base_wording_model import base_wording_model, shifted_wording_model
import openai
import os
from config.db import conn

wording_router = APIRouter()

# Set the model to use (in this case, GPT-3)
model_engine = "text-davinci-003"
model_chat_engine = "gpt-4"

# Set your OpenAI API key
openai.api_key = os.environ.get("OPENAI_API_KEY")

def get_prompt(base):
    base_wording = base.baseWording
    theme = base.theme
    tone = base.tone
    length = base.length
    learning_objective = base.learningObjective

    prompt = f'''Identify the core mathematical concept of the following exercise and use it to create a new exercise within the {theme} domain using a competency-based learning approach and bringing real-world relevance to a student that appreciates {theme}. Provide only the wording of the adapted exercise, without any additional information or context."
    Exercise: {base_wording}'''

    return prompt


def get_shifted_wording_chat(prompt):
    completion = openai.ChatCompletion.create(
    model = model_chat_engine,
    max_tokens = 500,
    temperature = 0.75,
    messages=[
        {"role": "user", "content": prompt}
    ]
    )

    shift_wording = completion.choices[0].message.content
    return shift_wording


def get_shifted_wording(prompt):
    gpt3 = openai.Completion.create(
    engine = model_engine,
    prompt = prompt,
    max_tokens = 500,
    temperature = 0.75,
    )

    # Get the response
    shift_wording = gpt3.choices[0].text

    # Clean the response
    # Split the text using "Exercise:"
    shift_wording = shift_wording.split("Exercise:")

    # Get the second part (index 1) and remove leading/trailing whitespace
    shift_wording = shift_wording[1].strip()

    return shift_wording


def save_base_wording(base: basewording.BaseWording):

    new_base_wording = {"base_wording": base.baseWording, 
                        "theme": base.theme, 
                        "tone": base.tone,
                        "length": base.length,
                        "learning_objective": base.learningObjective,
                        }
    result = conn.execute(base_wording_model.insert().values(new_base_wording))
    conn.commit()
    # result = conn.execute(base_wording_model.select().where(base_wording_model.c.id == result.lastrowid)).fetchone(dict)
    
    return "saved"

def save_shifted_wording(shifted_wording, base_wording_id):
    new_shifted_wording = {"base_wording_id": base_wording_id, 
                        "shifted_wording": shifted_wording, 
                        }
    # result = conn.execute(base_wording_model.insert().values(new_shifted_wording))
    # conn.commit()

    return ("success")


@wording_router.post('/shiftwording')
def shift_wording(base: basewording.BaseWording):
    #we save the base-wording in the database
    base_wording_id = save_base_wording(base)
    
    prompt = get_prompt(base)

    if base.use_gpt4:
        shifted_wording = get_shifted_wording_chat(prompt)
    else:
        shifted_wording = get_shifted_wording(prompt)


    save_shifted_wording(shifted_wording, base_wording_id)

    return shifted_wording


@wording_router.get('/allbasewordings')
def get_all_base_wordings():
    select_query = base_wording_model.select().order_by(base_wording_model.c.base_wording.desc()).limit(10)
    result = conn.execute(select_query)
    

    # # Display the results in a HTML table format
    # for row in result.fetchall():
    #     print(row)


    return result.fetchall()
