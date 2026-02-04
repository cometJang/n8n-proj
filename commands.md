# 🚀 Windows CMD 완벽 명령어 모음 (기초부터 실무까지)

**마지막 업데이트: 2026-02-04**

---

## ⚠️ 주의사항 (Critical Warning)

### 1. **삭제 명령어 주의**

CMD에서 `del`, `rmdir` 명령어로 삭제한 파일은 휴지통으로 가지 않고 **즉시 영구 삭제**됩니다.

### 2. **경로의 공백 처리**

폴더명에 공백이 있으면 반드시 쌍따옴표로 감싸야 합니다.

```cmd
cd "Program Files"  # 올바른 방법
cd Program Files    # 오류 발생
```

### 3. **경로 구분자**

Windows는 `\` (백슬래시)가 표준이지만, Python/Git 등은 `/`도 인식합니다.

### 4. **관리자 권한 필요**

시스템 설정 변경(환경변수 등)은 CMD를 **관리자 권한**으로 실행해야 합니다.

### 5. **대소문자 구분**

Windows CMD는 대소문자를 구분하지 않지만, Git이나 Python 코드는 **대소문자를 구분**합니다.

---

## 🎯 실무에서 가장 많이 쓰는 Top 20 (Quick Start)

### 탐색/관리

```cmd
cd [경로]             # 폴더 이동 (예: cd src, cd ..)
dir /o-d             # 파일 목록 보기 (최신순 정렬)
start .              # 현재 폴더를 Windows 탐색기로 열기
mkdir data\raw       # 폴더 생성 (하위 폴더 한 번에 생성 가능)
echo %cd% | clip     # 현재 절대 경로를 클립보드에 복사
```

### 가상환경/Python

```cmd
python -m venv .venv        # 가상환경 생성
.venv\Scripts\activate      # 가상환경 활성화
deactivate                  # 가상환경 비활성화
pip install -r requirements.txt    # 패키지 일괄 설치
pip freeze > requirements.txt      # 현재 설치된 패키지 목록 저장
taskkill /f /im python.exe         # 멈춘 Python 프로세스 강제 종료
```

### 개발 도구

```cmd
jupyter notebook     # 주피터 노트북 실행
git status           # 현재 Git 상태 확인
git add .            # 변경사항 전체 추가
git commit -m "msg"  # 커밋 실행
git push origin main # 원격 저장소에 업로드
```

### 데이터/로그

```cmd
findstr /i "error" app.log  # 로그에서 에러 단어 찾기
find /c /v "" < data.csv    # CSV 파일 전체 줄 수 확인
more +1 data.csv            # 대용량 파일 첫 화면만 보기
cls                         # 터미널 화면 청소
```

---

## 🧭 경로 탐색의 기초 (Relative Paths)

### 상대 경로 기호

- `.` : 현재 폴더 (Current Directory)
- `..` : 상위 폴더 (Parent Directory)
- `\` : 경로 구분자

### 기본 탐색 명령어

```cmd
cd .                 # 변화 없음 (현재 위치)
cd ..                # 한 단계 위로 이동
cd ..\..             # 두 단계 위로 이동
cd ..\data           # 뒤로 갔다가 data 폴더로 들어가기
dir .\src            # 현재 폴더 내 src 폴더 내용 보기
```

---

## 📁 파일 및 폴더 관리 (File Management)

### 목록 및 찾기

```cmd
dir /a               # 숨김 파일 포함 목록 보기
dir /s /b *.csv      # 하위 폴더 포함 모든 CSV 파일 경로만 표시
tree /f              # 폴더 구조를 트리 형태로 보기
where python         # 실행 파일 경로 찾기
```

### 복사/이동/삭제

```cmd
copy a.txt b.txt               # 파일 복사
xcopy data backup /e /i /y     # 폴더 전체 복사 (하위 포함, 덮어쓰기)
move old.txt new.txt           # 이름 변경 또는 이동
del *.log                      # 모든 로그 파일 삭제
rmdir /s /q temp               # 폴더와 내부 파일 강제 삭제 (주의!)
```

### 파일 내용 확인

```cmd
type readme.md                      # 파일 전체 내용 출력
findstr /s /n "TODO" *.py          # 모든 Python 파일에서 TODO가 있는 줄 번호 표시
more filename.txt                   # 파일 내용을 페이지 단위로 보기
```

---

## 🛠️ 개발 및 협업 도구 (Git / Jupyter / Pip)

### Git 실전 명령어

```cmd
git pull                           # 최신 코드 가져오기
git checkout -b [브랜치명]         # 새 브랜치 생성 및 이동
git log --oneline -5               # 최근 커밋 5개만 간단히 보기
git reset --soft HEAD~1            # 마지막 커밋 취소 (수정사항은 유지)
git diff                           # 현재 수정된 내용 비교
```

### Jupyter/IPython

```cmd
# 가상환경을 주피터 커널로 등록
python -m ipykernel install --user --name .venv --display-name "Project-Venv"
jupyter kernelspec list            # 등록된 커널 목록 보기
jupyter notebook --port=8889       # 다른 포트로 주피터 실행
```

### PIP 관리

```cmd
python -m pip install --upgrade pip    # PIP 업그레이드
pip list --outdated                    # 업데이트 가능한 패키지 목록
pip show [패키지명]                    # 특정 패키지 정보 보기
```

---

## 💻 시스템 및 네트워크 관리 (System & Network)

### 프로세스/포트 관리

```cmd
netstat -ano | findstr :8888      # 8888번 포트를 사용하는 PID 찾기
taskkill /f /pid [PID]            # 특정 PID 강제 종료
tasklist | findstr python         # 실행 중인 Python 프로세스만 확인
wmic process where name="python.exe" delete  # 모든 Python 프로세스 종료
```

### 네트워크 진단

```cmd
ipconfig                          # 내 IP 주소 확인
ipconfig /all                     # 네트워크 상세 정보
ping google.com                   # 인터넷 연결 확인
nslookup google.com              # DNS 조회
```

### 시스템 정보

```cmd
systeminfo                       # 시스템 전체 정보
echo %PATH%                      # 환경 변수 경로 확인
set                              # 모든 환경 변수 보기
whoami                           # 현재 사용자 정보
```

---

## ⚡ 실무 유용한 조합 명령어 (Patterns)

### 신규 프로젝트 세팅

```cmd
# 가상환경 생성 → 활성화 → 패키지 설치 (한 번에)
python -m venv .venv && .venv\Scripts\activate && pip install -r requirements.txt
```

### 날짜별 백업

```cmd
# 오늘 날짜로 백업 폴더 생성 및 데이터 복사
set today=%date:~0,4%%date:~5,2%%date:~8,2%
mkdir backup_%today% && xcopy data backup_%today% /e /i /y
```

### 코드 정리 및 저장

```cmd
# Python 프로세스 종료 → Git 커밋 → 푸시
taskkill /f /im python.exe & git add . & git commit -m "update" & git push
```

### 대용량 데이터 처리

```cmd
# 파일 개수 확인 → 용량 확인 → 샘플 데이터 보기
dir /s | find "File(s)" & dir /-c & head -n 10 data.csv
```

### 로그 분석

```cmd
# 에러 로그만 추출하여 새 파일로 저장
findstr /i /c:"error" /c:"exception" app.log > error_log.txt
```

---

## 📌 주요 단축키 & 팁 (Shortcuts)

### 필수 단축키

| 단축키          | 기능                       |
| --------------- | -------------------------- |
| `Tab`         | 파일/폴더명 자동 완성 ⭐   |
| `↑` / `↓` | 이전 명령어 히스토리 탐색  |
| `Ctrl + C`    | 실행 중인 명령어 강제 종료 |
| `F7`          | 명령어 히스토리 전체 팝업  |
| `Ctrl + L`    | 화면 청소 (cls와 동일)     |

### 생산성 팁

```cmd
doskey /history              # 명령어 히스토리 전체 보기
doskey ls=dir /w            # 별명(alias) 만들기
doskey h=doskey /history    # 단축 명령어 생성
```

### CMD 창 관리

```cmd
title "프로젝트 작업"        # CMD 창 제목 변경
color 0A                    # 배경색/글자색 변경 (검정바탕/초록글씨)
mode 120,30                 # 창 크기 조정 (가로120, 세로30)
exit                        # CMD 창 닫기
```

---

## 🚀 자동화 및 나만의 단축키 (BAT & DOSKEY)

배운 명령어들을 매번 치기 귀찮다면? 아래 두 가지 방법을 사용해 보세요.

### 1. `.bat` (배치 파일): 여러 명령어를 한 번에 실행하는 '자동 실행 단축키'

여러 단계를 거쳐야 하는 작업을 클릭 한 번으로 끝냅니다. 메모장에 작성 후 확장자를 `.bat`로 저장하세요.

**[예시] `start_project.bat` (가상환경 활성화 + 주피터 실행)**

```batch
@echo off
echo 가상환경을 활성화하고 주피터를 실행합니다...
call .venv\Scripts\activate
jupyter notebook
pause
```

---

### 2. `doskey`: 긴 명령어를 짧은 '별명'으로 줄이는 단축키

CMD 창이 열려 있는 동안 유효한 나만의 단축어를 만듭니다.

**[예시] 자주 쓰는 별칭 등록**

```cmd
doskey v=.venv\Scripts\activate    # 'v'만 치면 가상환경 활성화
doskey gs=git status               # 'gs'만 치면 깃 상태 확인
doskey gp=git push origin main     # 'gp'만 치면 바로 푸시
```

---

**💡 Pro Tip**: `.bat` 파일은 프로젝트 폴더에 넣어두면 팀원들과 공유하기 좋고, `doskey`는 내가 타이핑할 때의 손의 피로를 혁신적으로 줄여줍니다!
