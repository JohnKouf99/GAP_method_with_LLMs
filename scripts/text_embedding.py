from openai import BadRequestError, OpenAI, RateLimitError
import os
import time


#function to create text embeddings

os.environ['OPENAI_API_KEY'] = ''
client = OpenAI()

def create_text_embeddings(df, positions ,cols):
    
    for (pos,col) in zip(positions, cols):

        for i in range(len(df)):
            print(i)
            response = client.embeddings.create(
            input= df.iloc[i,pos] ,
            model="text-embedding-3-small")

            df.at[i,col] = response.data[0].embedding

def single_text_embedding(text):
    
    try:
        response = client.embeddings.create(
        input= text,
        model="text-embedding-3-small")

        return response.data[0].embedding
    except BadRequestError as e:
        print(e)
        print('On text:', text)
        return None
    except RateLimitError as e:
        time.sleep(60)  # Wait for 60 seconds
        return single_text_embedding(text)
        