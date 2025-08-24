from mcp.server.fastmcp import FastMCP, Context

# MCP 서버 생성하기
mcp = FastMCP("tutorial_5")

@mcp.tool()
async def greeting(name: str, ctx: Context) -> str:
    """
    Get a greeting using the greeting resource
    """
    try:
        result = await ctx.read_resource("greeting://{name}")
        content = result[0] if isinstance(result, tuple) else result
        return f"Tool response: {content}"
    except Exception as e:
        return f"Error occurred: {str(e)}"
    
@mcp.resource("greeting://{name}")
def get_greeting(name: str) -> str:
    """
    Get a personalized greeting
    """
    return f"Hello, {name}! Welcome to MCP tutorial 5!"

# 서버 실행하기
if __name__ == "__main__":
    mcp.run()
