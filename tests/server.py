from mcp.server.fastmcp import FastMCP

# MCP 서버 생성하기
mcp = FastMCP("server")

@mcp.tool()
def creat_folder(folder_name: str) -> str:
    """
    C:/dev/mcp-dev/tests 아래 폴더를 생성합니다.

    Parameters
    ----------
    folder_name : str
        생성할 폴더 이름

    Returns
    -------
        str
            생성 결과 메시지    
    """
    
    import os

    folder_path = os.path.join("C:/dev/mcp-dev/tests", folder_name)
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)
        return f"Folder '{folder_name}' created successfully at {folder_path}."
    else:
        return f"Folder '{folder_name}' already exists at {folder_path}."
    
@mcp.tool()
def delete_folder(folder_name: str) -> str:
    """
    C:/dev/mcp-dev/tests 아래 폴더를 삭제합니다.

    Parameters
    ----------
    folder_name : str
        삭제할 폴더 이름

    Returns
    -------
        str
            삭제 결과 메시지    
    """
    
    import os

    folder_path = os.path.join("C:/dev/mcp-dev/tests", folder_name)
    if os.path.exists(folder_path):
        os.rmdir(folder_path)
        return f"Folder '{folder_name}' deleted successfully from {folder_path}."
    else:
        return f"Folder '{folder_name}' does not exist at {folder_path}."
    
@mcp.tool()
def list_folders() -> list:
    """
    C:/dev/mcp-dev/tests 아래 폴더 목록을 반환합니다.

    Returns
    -------
        list
            폴더 목록    
    """
    
    import os

    folder_path = "C:/dev/mcp-dev/tests"
    folders = [f for f in os.listdir(folder_path) if os.path.isdir(os.path.join(folder_path, f))]
    return f"Folders in '{folder_path}': {', '.join(folders)}"

# 서버 실행하기
if __name__ == "__main__":
    mcp.run()