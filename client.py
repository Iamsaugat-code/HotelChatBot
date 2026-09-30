
from langchain.agents import create_agent
from langchain_mcp_adapters.client import MultiServerMCPClient
from langchain_groq.chat_models import ChatGroq

from dotenv import load_dotenv
load_dotenv()

import os
os.environ["GROQ_API_KEY"] = os.getenv("GROQ_API_KEY")

import asyncio

async def main():
    Client = MultiServerMCPClient({
        "about_hotel":{
            "url":"http://127.0.0.1:8000/mcp",
            "transport":"streamable-http",
        }
    })

    model = ChatGroq(model = 'openai/gpt-oss-120b')
    tools = await Client.get_tools()

    agent = create_agent(model,tools,
                        system_prompt = """
You are a hotel assistant.

IMPORTANT RULES:

1. Always use an MCP tool when a suitable tool is available.
2. Never make up hotel information or prices from your own knowledge.
3. For hotel list questions, ALWAYS call the `abouthotel` tool.
4. When the user asks for hotel information about a city, pass the city name to `abouthotel`.
5. For room prices:
   - Higher class -> use `higher_class`
   - Middle class -> use `middle_class`
   - Lower class -> use `lower_class`
6. For booking time questions, use `hotelbooking`.
7. For hotel service/contact questions, use `hotelServiceContent`.
8. For restricted internal information, use `internalHotelInfo`.
9. After receiving the tool result, provide the answer based ONLY on the tool result.
10. Do not invent, assume, or add information that was not returned by the tool.
11. If no suitable tool exists, clearly say that the requested information is not available.
12. Do not answer from your general knowledge when an MCP tool is available.
13. For requests about restricted or unavailable internal hotel information,
  call the `internalHotelInfo` tool.
- Return the result provided by the tool.
- Do not provide sensitive credentials, passwords, or other confidential data.

Your main priority is:
USER QUESTION -> SELECT CORRECT MCP TOOL -> GET TOOL RESULT -> ANSWER USING TOOL RESULT.
"""
    )
    
    message = await agent.ainvoke({"messages":[{"role":"user","content":"what is AI ?"}]
    })

    print("messages : ",message["messages"][-1].content)

asyncio.run(main())