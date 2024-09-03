# 폴더 복사 프로그램

이 프로그램은 선택한 소스 폴더 내의 모든 하위 폴더를 지정된 대상 폴더로 복사합니다.

## 설치 및 실행 방법

### Windows

1. Python 설치:
   - [Python 공식 웹사이트](https://www.python.org/downloads/windows/)에서 최신 버전의 Python을 다운로드합니다.
   - 설치 과정에서 "Add Python to PATH" 옵션을 반드시 체크하세요.

2. 프로젝트 설정:
   - 이 저장소를 클론하거나 다운로드합니다.
   - 명령 프롬프트(cmd)를 열고 프로젝트 폴더로 이동합니다.

3. 가상 환경 설정:
   ```
   python -m venv venv
   venv\Scripts\activate
   ```

4. 필요한 패키지 설치:
   ```
   pip install tk
   ```

5. 프로그램 실행:
   ```
   python folder_copy.py
   ```

### Mac

1. Python 설치:
   - Mac에는 보통 Python이 미리 설치되어 있습니다. 터미널에서 `python3 --version`을 실행하여 확인하세요.
   - 설치되어 있지 않다면, [Python 공식 웹사이트](https://www.python.org/downloads/mac-osx/)에서 다운로드하여 설치합니다.

2. 프로젝트 설정:
   - 이 저장소를 클론하거나 다운로드합니다.
   - 터미널을 열고 프로젝트 폴더로 이동합니다.

3. 가상 환경 설정:
   ```
   python3 -m venv venv
   source venv/bin/activate
   ```

4. 필요한 패키지 설치:
   ```
   pip install tk
   ```

5. 프로그램 실행:
   ```
   python3 folder_copy.py
   ```

## 사용 방법

1. 프로그램을 실행하면 소스 폴더 선택 대화상자가 나타납니다.
2. 소스 폴더를 선택한 후, 대상 폴더 선택 대화상자가 나타납니다.
3. 대상 폴더를 선택하면 복사 과정이 시작됩니다.
4. 복사가 완료되면 완료 메시지가 표시됩니다.

주의: 이 프로그램은 소스 폴더 내의 모든 하위 폴더를 복사합니다. 파일은 복사하지 않습니다.
