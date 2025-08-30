from mcp.server.fastmcp import FastMCP
import os

# MCP 서버 생성하기
mcp = FastMCP("server")

# 기본 작업 디렉토리 설정
BASE_PATH = "C:/dev/mcp-dev"

def get_full_path(path: str) -> str:
    """상대 경로를 절대 경로로 변환하고 BASE_PATH 내부인지 확인"""
    if os.path.isabs(path):
        # 절대 경로인 경우, BASE_PATH로 시작하는지 확인
        if not path.startswith(BASE_PATH):
            path = os.path.join(BASE_PATH, os.path.basename(path))
    else:
        # 상대 경로인 경우 BASE_PATH와 결합
        path = os.path.join(BASE_PATH, path)
    
    # 정규화하여 .. 등의 경로 조작 처리
    path = os.path.normpath(path)
    
    # 보안 체크: BASE_PATH 외부로 벗어나는 것을 방지
    if not path.startswith(BASE_PATH):
        path = os.path.join(BASE_PATH, os.path.basename(path))
    
    return path

@mcp.tool()
def creat_folder(folder_path: str) -> str:
    """
    C:/dev/mcp-dev 아래 폴더를 생성합니다.

    Parameters
    ----------
    folder_path : str
        생성할 폴더 경로 (예: 'servers/github', 'tests/new_folder')

    Returns
    -------
        str
            생성 결과 메시지    
    """
    
    full_path = get_full_path(folder_path)
    try:
        if not os.path.exists(full_path):
            os.makedirs(full_path)
            return f"Folder created successfully at {full_path}."
        else:
            return f"Folder already exists at {full_path}."
    except Exception as e:
        return f"Failed to create folder at {full_path}. Error: {str(e)}"

@mcp.tool()
def delete_folder(folder_path: str) -> str:
    """
    C:/dev/mcp-dev 아래 폴더를 삭제합니다.

    Parameters
    ----------
    folder_path : str
        삭제할 폴더 경로

    Returns
    -------
        str
            삭제 결과 메시지    
    """
    
    full_path = get_full_path(folder_path)
    try:
        if os.path.exists(full_path):
            if os.path.isdir(full_path):
                # 빈 폴더만 삭제 (안전을 위해)
                os.rmdir(full_path)
                return f"Folder deleted successfully from {full_path}."
            else:
                return f"Path {full_path} is not a directory."
        else:
            return f"Folder does not exist at {full_path}."
    except OSError as e:
        return f"Failed to delete folder at {full_path}. Error: {str(e)} (폴더가 비어있지 않을 수 있습니다)"

@mcp.tool()
def list_folders(directory_path: str = "") -> str:
    """
    C:/dev/mcp-dev 아래 폴더 및 파일 목록을 반환합니다.

    Parameters
    ----------
    directory_path : str, optional
        조회할 디렉토리 경로 (비어있으면 루트 디렉토리)

    Returns
    -------
        str
            폴더 및 파일 목록    
    """
    
    if directory_path:
        full_path = get_full_path(directory_path)
    else:
        full_path = BASE_PATH
    
    try:
        if not os.path.exists(full_path):
            return f"Directory does not exist at {full_path}."
        
        items = os.listdir(full_path)
        folders = [f for f in items if os.path.isdir(os.path.join(full_path, f))]
        files = [f for f in items if os.path.isfile(os.path.join(full_path, f))]
        
        result = f"Contents of '{full_path}':\n"
        if folders:
            result += f"Folders: {', '.join(folders)}\n"
        if files:
            result += f"Files: {', '.join(files)}"
        
        return result if folders or files else f"Directory '{full_path}' is empty."
    except Exception as e:
        return f"Failed to list contents of {full_path}. Error: {str(e)}"

@mcp.tool()
def write_file(file_path: str, content: str) -> str:
    """
    C:/dev/mcp-dev 아래 파일을 생성하고 내용을 작성합니다.

    Parameters
    ----------
    file_path : str
        생성할 파일 경로 (예: 'servers/config.json', 'tests/note.txt')
    content : str
        파일에 작성할 내용

    Returns
    -------
        str
            파일 작성 결과 메시지    
    """
    
    full_path = get_full_path(file_path)
    
    # 디렉토리가 없으면 생성
    directory = os.path.dirname(full_path)
    if not os.path.exists(directory):
        try:
            os.makedirs(directory)
        except Exception as e:
            return f"Failed to create directory {directory}. Error: {str(e)}"
    
    try:
        with open(full_path, 'w', encoding="utf-8") as f:
            f.write(content)
        return f"File created successfully at {full_path}."
    except Exception as e:
        return f"Failed to create file at {full_path}. Error: {str(e)}"

@mcp.tool()
def read_file(file_path: str) -> str:
    """
    C:/dev/mcp-dev 아래 파일을 읽고 내용을 반환합니다.
    
    Parameters
    ----------
    file_path : str
        읽을 파일 경로 (예: 'servers/config.json', 'tests/note.txt')

    Returns
    -------
        str
            파일 내용 또는 에러 메시지    
    """
    
    full_path = get_full_path(file_path)
    
    if not os.path.exists(full_path):
        return f"File does not exist at {full_path}."
    
    if not os.path.isfile(full_path):
        return f"Path {full_path} is not a file."
    
    try:
        with open(full_path, 'r', encoding="utf-8") as f:
            content = f.read()
        return content
    except Exception as e:
        return f"Failed to read file at {full_path}. Error: {str(e)}"

@mcp.tool()
def append_to_file(file_path: str, content: str) -> str:
    """
    C:/dev/mcp-dev 아래 파일에 내용을 추가합니다.

    Parameters
    ----------
    file_path : str
        내용을 추가할 파일 경로 (예: 'servers/log.txt', 'tests/note.txt')
    content : str
        파일에 추가할 내용

    Returns
    -------
        str
            파일 내용 추가 결과 메시지    
    """
    
    full_path = get_full_path(file_path)
    
    if not os.path.exists(full_path):
        return f"File does not exist at {full_path}."
    
    try:
        with open(full_path, 'a', encoding="utf-8") as f:
            f.write(content)
        return f"Content appended to file successfully at {full_path}."
    except Exception as e:
        return f"Failed to append content to file at {full_path}. Error: {str(e)}"

# 서버 실행하기 
if __name__ == "__main__":
    mcp.run()