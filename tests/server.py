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

@mcp.tool()
def write_file(file_name: str, content: str) -> str:
    """
    C:/dev/mcp-dev/tests 아래 파일을 생성하고 내용을 작성합니다.

    Parameters
    ----------
    file_name : str
        생성할 파일 이름 (including extension, e.g., test.txt) 
    content : str
        파일에 작성할 내용

    Returns
    -------
        str
            파일 작성 결과 메시지    
    """
    
    import os

    file_path = os.path.join("C:/dev/mcp-dev/tests", file_name)
    try:
        with open(file_path, 'w', encoding="utf-8") as f:
            f.write(content)
        return f"File '{file_name}' created successfully at {file_path} with content."
    except Exception as e:
        return f"Failed to create file '{file_name}' at {file_path}. Error: {str(e)}"

@mcp.tool()
def read_file(file_name: str) -> str:
    """
    C:/dev/mcp-dev/tests 아래 파일을 읽고 내용을 반환합니다.
    Parameters
    ----------
    file_name : str
        읽을 파일 이름 (including extension, e.g., test.txt) 

    Returns
    -------
        str
            파일 내용 또는 에러 메시지    
    """
    
    import os

    file_path = os.path.join("C:/dev/mcp-dev/tests", file_name)
    if not os.path.exists(file_path):
        return f"File '{file_name}' does not exist at {file_path}."
    try:
        with open(file_path, 'r', encoding="utf-8") as f:
            content = f.read()
        return content
    except Exception as e:
        return f"Failed to read file '{file_name}' at {file_path}. Error: {str(e)}"
    
@mcp.tool()
def append_to_file(file_name: str, content: str) -> str:
    """
    C:/dev/mcp-dev/tests 아래 파일에 내용을 추가합니다.

    Parameters
    ----------
    file_name : str
        내용을 추가할 파일 이름 (including extension, e.g., test.txt) 
    content : str
        파일에 추가할 내용

    Returns
    -------
        str
            파일 내용 추가 결과 메시지    
    """
    
    import os

    file_path = os.path.join("C:/dev/mcp-dev/tests", file_name)
    if not os.path.exists(file_path):
        return f"File '{file_name}' does not exist at {file_path}."
    try:
        with open(file_path, 'a', encoding="utf-8") as f:
            f.write(content)
        return f"Content appended to file '{file_name}' successfully at {file_path}."
    except Exception as e:
        return f"Failed to append content to file '{file_name}' at {file_path}. Error: {str(e)}"

# 서버 실행하기
if __name__ == "__main__":
    mcp.run()