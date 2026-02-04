# 🚀 Windows CMD 완벽 가이드 (기본부터 실무 자동화까지)
**마지막 업데이트: 2026-02-04**

---

## ⚠️ 필수 주의사항 (Critical Warning)

### 1. **Ctrl + Z (^Z)는 '실행 취소'가 아닙니다!**
Windows CMD에서 **Ctrl + Z**는 **"입력의 끝(EOF)"**을 의미하는 시스템 신호입니다. 엑셀이나 메모장 같은 '되돌리기'가 아닙니다.
*   **터미널에서 '실행 취소(Undo)'가 필요할 때**:
    *   **입력 중인 내용을 싹 지우고 싶을 때**: `Esc` 키를 누르세요.
    *   **실행 중인 명령을 강제로 멈추고 싶을 때**: `Ctrl + C`를 누르세요.
    *   **이전 명령어를 다시 불러오고 싶을 때**: `↑` (위쪽 화살표)를 누르세요.

### 2. **삭제 명령어 주의**
*   CMD에서 `del`, `rmdir` 명령어로 삭제한 파일/폴더는 휴지통으로 가지 않고 **즉시 영구 삭제**됩니다. 

### 3. **경로의 공백 처리**
*   폴더명에 공백이 있으면 반드시 쌍따옴표로 감싸야 합니다.
    ```cmd
    cd "Program Files"  # 올바른 방법
    cd Program Files    # 오류 발생
    ```

---

## 🎯 실무 핵심 Top 15 (Quick Start)

| 작업 목적 | Windows CMD 명령어 | 활용 예시 |
| :--- | :--- | :--- |
| **폴더 이동** | `cd [경로]` | `cd src`, `cd ..` (상위) |
| **현재 위치 확인** | `cd` | 지금 어디 있는지 경로 출력 |
| **목록 보기** | `dir /o-d` | 최신 파일순으로 파일/폴더 보기 |
| **탐색기로 열기** | `start .` | 현재 폴더를 윈도우 창으로 열기 |
| **경로 복사** | `echo %cd% \| clip` | 현재 절대 경로를 클립보드에 복사 |
| **가상환경 활성화** | `.venv\Scripts\activate` | 파이썬 개발 시작 전 필수 |
| **가상환경 종료** | `deactivate` | 작업 종료 후 가상환경 끄기 |
| **패키지 일괄 설치**| `pip install -r requirements.txt`| 라이브러리 목록 한 번에 설치 |
| **패키지 목록 저장**| `pip freeze > requirements.txt` | 현재 설치된 패키지 환경 백업 |
| **파이썬 강제종료**| `taskkill /f /im python.exe`| 멈춰버린 파이썬 프로그램 종료 |
| **파일 내 단어 검색**| `findstr /i "err" app.log`| 로그 파일에서 에러 내용만 찾기 |
| **파일 줄 수 확인** | `find /c /v "" < data.csv` | CSV 데이터가 몇 줄인지 확인 |
| **포트 점유 확인** | `netstat -ano \| findstr :8000` | 서버가 어떤 PID에서 도는지 확인 |
| **화면 청소** | `cls` | 터미널 화면 깨끗하게 지우기 |
| **트리 구조 보기** | `tree /f` | 폴더 구조를 시각적으로 확인 |

---

## 🧭 경로 탐색의 기초 (Relative Paths)

- **`.`** : 현재 내가 있는 이 폴더 (Current Directory)
- **`..`** : 내 위쪽, 상위 폴더 (Parent Directory)
- **`\`** : 경로 구분자 (Windows 표준)

**이동 꿀팁:**
```cmd
cd ..          # 한 단계 뒤로 이동
cd ../data     # 뒤로 갔다가 data 폴더로 들어가기
cd ../../      # 두 단계 뒤로 이동
cd \           # C 드라이브 최상위(Root)로 이동
```

---

## 📁 파일 및 폴더 관리 상세 (File Management)

### 목록 및 찾기 (Search)
- `dir /a` : 숨김 파일(ex: .git)까지 포함해서 모두 보기
- `dir /s /b *.csv` : 하위 폴더까지 뒤져서 모든 CSV 파일 경로만 나열
- `where python` : 파이썬 실행 파일이 어느 경로에 있는지 확인

### 복사/이동/삭제 (Ops)
- `copy a.txt b.txt` : 파일 복사
- `xcopy data backup /e /i /y` : 폴더 전체 복사 (하위 폴더 포함, 덮어쓰기)
- `move old.txt new.txt` : 이름 변경 또는 폴더 이동
- `del *.log` : 현재 폴더의 모든 로그 파일 삭제
- `rmdir /s /q temp` : 폴더와 내부 파일을 묻지 않고 강제 삭제 (주의!)

---

## 🛠️ 개발 및 자동화 패턴 (Automation)

### 1. 신규 프로젝트 세팅 (원샷 명령어)
```cmd
# 가상환경 생성 + 활성화 + 패키지 설치를 한 번에
python -m venv .venv && .venv\Scripts\activate && pip install -r requirements.txt
```

### 2. 날짜별 폴더 백업
```cmd
# 오늘 날짜 폴더를 만들고 data 폴더를 복사
set today=%date:~0,4%%date:~5,2%%date:~8,2%
mkdir backup_%today% && xcopy data backup_%today% /e /i /y
```

### 3. 배치 파일 (.bat): 나만의 자동 버튼
메모장에 아래 내용을 적고 `start.bat`로 저장해 보세요.
```batch
@echo off
call .venv\Scripts\activate
jupyter notebook
pause
```

### 4. 단축 이름 등록 (doskey)
```cmd
doskey v=.venv\Scripts\activate    # 'v'만 치면 가상환경 켜짐
doskey gs=git status               # 'gs'만 치면 깃 상태 확인
```

---

**💡 Pro Tip**: 
Windows CMD는 알면 알수록 강력합니다. 이 가이드를 윈도우 작업 표시줄이나 즐겨찾기에 두고 필요할 때마다 참고하세요! 😇
