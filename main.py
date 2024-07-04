import os
from dotenv import load_dotenv

# 加載 .env 文件中的環境變數
load_dotenv()

# 獲取環境變數
google_api_key = os.getenv('GOOGLE_API_KEY')
langchain_api_key = os.getenv('LANGCHAIN_API_KEY')

# 檢查是否成功加載環境變數
if google_api_key:
    print("Google API Key:", google_api_key)
else:
    print("Google API Key is not set in .env file")

# 使用 Google API Key 配置 genai
if google_api_key:
    import google.generativeai as genai
    genai.configure(api_key=google_api_key)
    try:
        model = genai.GenerativeModel('gemini-pro')
        
        # 假設 invoke 是你要調用的方法
        result = model.invoke("Hello, world!")
        print(result)
    except Exception as e:
        print("There seems to be something wrong with your Gemini API. Please follow our demonstration in the slide to get a correct one.")
        print(f"Error: {e}")
else:
    print("Google API key is not set. Please set the GOOGLE_API_KEY environment variable.")
