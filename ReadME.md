# Java 소스 파일 복사 프로그램

이 프로그램은 선택한 소스 폴더와 그 하위 폴더에서 모든 Java 소스 파일(.java)을 찾아 지정된 대상 폴더로 복사합니다.

## 주요 기능

- 소스 폴더와 하위 폴더에서 Java 파일 검색
- 선택한 대상 폴더로 Java 파일 복사
- 중복 파일명 처리 (숫자 추가)
- 복사된 파일 수 보고

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
   python java_source_copy.py
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
   python3 java_source_copy.py
   ```

## 사용 방법

1. 프로그램을 실행하면 소스 폴더 선택 대화상자가 나타납니다.
2. 소스 폴더를 선택한 후, 대상 폴더 선택 대화상자가 나타납니다.
3. 파일 확장자 선택 대화상자에서 .java를 선택합니다. (현재 버전에서는 .java만 지원)
4. 선택이 완료되면 복사 과정이 시작됩니다.
5. 복사가 완료되면 복사된 파일 수를 보여주는 완료 메시지가 표시됩니다.

주의: 이 프로그램은 현재 Java 소스 파일(.java)만 복사합니다. 다른 유형의 파일은 복사되지 않습니다.