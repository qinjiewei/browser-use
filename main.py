from langchain_openai import ChatOpenAI
from langchain_ollama import ChatOllama
from browser_use import Agent, Browser, BrowserConfig
from pydantic import SecretStr
import asyncio
browser = Browser(
    config=BrowserConfig(
        # Specify the path to your Chrome executable
        chrome_instance_path='C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe',  # macOS path
        # For Windows, typically: 'C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe'
        # For Linux, typically: '/usr/bin/google-chrome'
    )
)



# Initialize the model
#llm=ChatOllama(base_url='http://10.21.11.238:11434',model="deepseek-r1:32b", num_ctx=32000)
llm=ChatOpenAI(base_url='https://api.deepseek.com/v1', model='deepseek-chat', api_key=SecretStr("sk-5aba90c4d4db41d288fe7975736958f2"))
# Create agent with the model
agent = Agent(
    task="查看今天的比特币价格",
    llm=llm,
    use_vision=False
)

async def main():
    await agent.run()

    input('Press Enter to close the browser...')
    await browser.close()

if __name__ == '__main__':
    asyncio.run(main())
