import google.generativeai as genai
import warnings

warnings.filterwarnings("ignore")

# Ignore specific category of warnings
warnings.filterwarnings("ignore", category=DeprecationWarning)
warnings.filterwarnings("ignore", category=UserWarning)

from langchain import HuggingFaceHub

import os
os.environ['HUGGINGFACEHUB_API_TOKEN'] = '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'
llm_model = HuggingFaceHub(repo_id = 'google/flan-t5-large',model_kwargs = {'temperature':0})

print('the capital of india is :'+ str(llm_model.predict("what is the capital of india")))

# by using Templates and chains
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain

prompt = PromptTemplate(input_variables=['country'], template = 'tell me the most famous place to visit in {country}')
# input1 = input('enter your country:')
# output = LLMChain(llm = llm_model, prompt = prompt).run(input1)
# print(output)

# by using multiple chains
prompt2 = PromptTemplate(input_variables = ['country'], template = 'what is the capital of {country}')
chain2 = LLMChain(llm = llm_model, prompt = prompt2, output_key ='capital')
chain1 = LLMChain(llm = llm_model, prompt = prompt, output_key = 'place')
from langchain.chains import SequentialChain
chain = SequentialChain(chains = [chain1, chain2],input_variables = ['country'], output_variables = ['capital','place'] )
print(chain({'country':'usa'}))
