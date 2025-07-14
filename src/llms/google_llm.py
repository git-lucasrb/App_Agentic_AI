from langchain_google_genai import ChatGoogleGenerativeAI
import os
from dotenv import load_dotenv

class GeminiLLM:
    def __init__(self):
        load_dotenv()

    def get_llm(self):
        try:
            os.environ["GEMINI_APY_KEY"]=self.gemini_api_key=os.getenv("GEMINI_API_KEY")
            llm=ChatGoogleGenerativeAI(gemini_api_key=self.gemini_api_key,model="gemini-2.5-flash")
            
        except Exception as e:
            raise ValueError(f"Error Ocurred with Exception: {e}")
        return llm