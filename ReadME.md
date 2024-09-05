
# Java Source File Copy Program

This program searches for all Java source files (.java) in the selected source folder and its subfolders, then copies them to a specified destination folder.

이 프로그램은 선택한 소스 폴더와 그 하위 폴더에서 모든 Java 소스 파일(.java)을 찾아 지정된 대상 폴더로 복사합니다.

## Key Features (주요 기능)

- Search for Java files in the source folder and subfolders  
  소스 폴더와 하위 폴더에서 Java 파일 검색
- Copy Java files to the selected destination folder  
  선택한 대상 폴더로 Java 파일 복사
- Handle duplicate filenames (add a number)  
  중복 파일명 처리 (숫자 추가)
- Report the number of copied files  
  복사된 파일 수 보고

## Installation and Execution (설치 및 실행 방법)

### Windows

1. **Install Python (Python 설치)**:
   - Download the latest version of Python from the [official Python website](https://www.python.org/downloads/windows/).  
     [Python 공식 웹사이트](https://www.python.org/downloads/windows/)에서 최신 버전의 Python을 다운로드합니다.
   - Be sure to check the "Add Python to PATH" option during the installation.  
     설치 과정에서 "Add Python to PATH" 옵션을 반드시 체크하세요.

2. **Set up the project (프로젝트 설정)**:
   - Clone or download this repository.  
     이 저장소를 클론하거나 다운로드합니다.
   - Open the Command Prompt (cmd) and navigate to the project folder.  
     명령 프롬프트(cmd)를 열고 프로젝트 폴더로 이동합니다.

3. **Set up a virtual environment (가상 환경 설정)**:
   ```bash
   python -m venv venv
   venv\Scripts\activate
   ```

4. **Install the required package (필요한 패키지 설치)**:
   ```bash
   pip install tk
   ```

5. **Run the program (프로그램 실행)**:
   ```bash
   python java_source_copy.py
   ```

### Mac

1. **Install Python (Python 설치)**:
   - Python usually comes pre-installed on Mac. Check by running `python3 --version` in the terminal.  
     Mac에는 보통 Python이 미리 설치되어 있습니다. 터미널에서 `python3 --version`을 실행하여 확인하세요.
   - If not installed, download and install it from the [official Python website](https://www.python.org/downloads/mac-osx/).  
     설치되어 있지 않다면, [Python 공식 웹사이트](https://www.python.org/downloads/mac-osx/)에서 다운로드하여 설치합니다.

2. **Set up the project (프로젝트 설정)**:
   - Clone or download this repository.  
     이 저장소를 클론하거나 다운로드합니다.
   - Open the terminal and navigate to the project folder.  
     터미널을 열고 프로젝트 폴더로 이동합니다.

3. **Set up a virtual environment (가상 환경 설정)**:
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

4. **Install the required package (필요한 패키지 설치)**:
   ```bash
   pip install tk
   ```

5. **Run the program (프로그램 실행)**:
   ```bash
   python3 java_source_copy.py
   ```

## How to Use (사용 방법)

1. When you run the program, a source folder selection dialog will appear.  
   프로그램을 실행하면 소스 폴더 선택 대화상자가 나타납니다.
2. After selecting the source folder, a destination folder selection dialog will appear.  
   소스 폴더를 선택한 후, 대상 폴더 선택 대화상자가 나타납니다.
3. In the file extension selection dialog, select .java. (Only .java is supported in the current version)  
   파일 확장자 선택 대화상자에서 .java를 선택합니다. (현재 버전에서는 .java만 지원)
4. Once the selection is complete, the copying process will begin.  
   선택이 완료되면 복사 과정이 시작됩니다.
