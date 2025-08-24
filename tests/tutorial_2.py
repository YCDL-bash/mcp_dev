from mcp.server.fastmcp import FastMCP

# MCP 서버 생성하기
mcp = FastMCP("tutorial_2")

@mcp.tool()
def add(a: int, b: int) -> int:
    """
    두 숫자를 더하는 도구입니다.
    """
    return a + b

@mcp.resource("greeting://hello")
def get_greeting() -> str:
    """
    인사말을 제공하는 함수입니다..
    """
    return f"Hello, welcome to MCP tutorial 2!"

# 서버 실행하기
if __name__ == "__main__":
    mcp.run()
    