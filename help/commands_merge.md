# 🚀 Windows CMD & Mac Terminal 완벽 명령어 모음 (기초부터 실무까지)

**마지막 업데이트: 2026-02-04**

> 💡 **이 가이드는**: Windows CMD와 Mac Terminal(Bash/Zsh) 명령어를 함께 제공합니다.
> Windows 사용자는 왼쪽, Mac 사용자는 오른쪽 명령어를 참고하세요!

---

## ⚠️ 주의사항 (Critical Warning)

### 1. **삭제 명령어 주의**

- **Windows**: `del`, `rmdir` 명령어로 삭제한 파일은 휴지통으로 가지 않고 **즉시 영구 삭제**됩니다.
- **Mac**: `rm`, `rm -rf` 명령어도 마찬가지로 **즉시 영구 삭제**됩니다. (휴지통 안 감)

### 2. **경로의 공백 처리**

폴더명에 공백이 있으면 반드시 쌍따옴표로 감싸야 합니다.

```bash
# Windows
cd "Program Files"  # 올바른 방법
cd Program Files    # 오류 발생

# Mac
cd "My Documents"   # 올바른 방법
cd My\ Documents    # 또는 백슬래시로 이스케이프
```

### 3. **경로 구분자**

- **Windows**: `\` (백슬래시)가 표준이지만, Python/Git 등은 `/`도 인식
- **Mac/Linux**: `/` (슬래시)가 표준

### 4. **관리자 권한 필요**

- **Windows**: CMD를 **관리자 권한**으로 실행
- **Mac**: 명령어 앞에 `sudo`를 붙여 실행 (예: `sudo brew install`)

### 5. **대소문자 구분**

- **Windows**: CMD는 대소문자를 구분하지 않음
- **Mac/Linux**: Terminal은 **대소문자를 엄격히 구분** (File.txt ≠ file.txt)

---

## 🎯 실무에서 가장 많이 쓰는 Top 20 (Quick Start)

### 탐색/관리

| 작업               | Windows CMD               | Mac Terminal          |
| ------------------ | ------------------------- | --------------------- |
| 폴더 이동          | `cd [경로]`             | `cd [경로]`         |
| 파일 목록          | `dir /o-d`              | `ls -lt`            |
| 탐색기/Finder 열기 | `start .`               | `open .`            |
| 폴더 생성          | `mkdir data\raw`        | `mkdir -p data/raw` |
| 경로 복사          | `echo %cd%                | clip`                 |
| 현재 위치          | `cd` 또는 `echo %cd%` | `pwd`               |

### 가상환경/Python

| 작업                 | Windows CMD                         | Mac Terminal                         |
| -------------------- | ----------------------------------- | ------------------------------------ |
| 가상환경 생성        | `python -m venv .venv`            | `python3 -m venv .venv`            |
| 가상환경 활성화      | `.venv\Scripts\activate`          | `source .venv/bin/activate`        |
| 가상환경 비활성화    | `deactivate`                      | `deactivate`                       |
| 패키지 설치          | `pip install -r requirements.txt` | `pip3 install -r requirements.txt` |
| 패키지 목록 저장     | `pip freeze > requirements.txt`   | `pip3 freeze > requirements.txt`   |
| Python 프로세스 종료 | `taskkill /f /im python.exe`      | `pkill -9 python`                  |

### 개발 도구

| 작업              | Windows CMD              | Mac Terminal             |
| ----------------- | ------------------------ | ------------------------ |
| Jupyter 실행      | `jupyter notebook`     | `jupyter notebook`     |
| Git 상태 확인     | `git status`           | `git status`           |
| Git 변경사항 추가 | `git add .`            | `git add .`            |
| Git 커밋          | `git commit -m "msg"`  | `git commit -m "msg"`  |
| Git 푸시          | `git push origin main` | `git push origin main` |

### 데이터/로그

| 작업            | Windows CMD                    | Mac Terminal                |
| --------------- | ------------------------------ | --------------------------- |
| 로그 검색       | `findstr /i "error" app.log` | `grep -i "error" app.log` |
| 파일 줄 수 확인 | `find /c /v "" < data.csv`   | `wc -l data.csv`          |
| 파일 내용 보기  | `more +1 data.csv`           | `head -n 20 data.csv`     |
| 화면 청소       | `cls`                        | `clear` (또는 `Ctrl+L`) |

---

## 🧭 경로 탐색의 기초 (Relative Paths)

### 상대 경로 기호

| 기호   | 의미          | Windows | Mac/Linux |
| ------ | ------------- | ------- | --------- |
| `.`  | 현재 폴더     | ✅      | ✅        |
| `..` | 상위 폴더     | ✅      | ✅        |
| `~`  | 홈 디렉토리   | ❌      | ✅        |
| `/`  | 루트 디렉토리 | ❌      | ✅        |

### 기본 탐색 명령어

**Windows CMD:**

```cmd
cd .                 # 변화 없음 (현재 위치)
cd ..                # 한 단계 위로 이동
cd ..\..             # 두 단계 위로 이동
cd ..\data           # 뒤로 갔다가 data 폴더로 들어가기
dir .\src            # 현재 폴더 내 src 폴더 내용 보기
cd C:\               # C 드라이브 루트로 이동
```

**Mac Terminal:**

```bash
cd .                 # 변화 없음 (현재 위치)
cd ..                # 한 단계 위로 이동
cd ../..             # 두 단계 위로 이동
cd ../data           # 뒤로 갔다가 data 폴더로 들어가기
ls ./src             # 현재 폴더 내 src 폴더 내용 보기
cd ~                 # 홈 디렉토리로 이동
cd /                 # 루트 디렉토리로 이동
cd -                 # 이전 디렉토리로 돌아가기
```

---

## 📁 파일 및 폴더 관리 (File Management)

### 목록 및 찾기

**Windows CMD:**

```cmd
dir /a               # 숨김 파일 포함 목록 보기
dir /s /b *.csv      # 하위 폴더 포함 모든 CSV 파일 경로만 표시
tree /f              # 폴더 구조를 트리 형태로 보기
where python         # 실행 파일 경로 찾기
```

**Mac Terminal:**

```bash
ls -la               # 숨김 파일 포함 상세 목록 보기
find . -name "*.csv" # 하위 폴더 포함 모든 CSV 파일 찾기
tree                 # 폴더 구조를 트리 형태로 보기 (brew install tree 필요)
which python3        # 실행 파일 경로 찾기
```

### 복사/이동/삭제

**Windows CMD:**

```cmd
copy a.txt b.txt               # 파일 복사
xcopy data backup /e /i /y     # 폴더 전체 복사 (하위 포함, 덮어쓰기)
move old.txt new.txt           # 이름 변경 또는 이동
del *.log                      # 모든 로그 파일 삭제
rmdir /s /q temp               # 폴더와 내부 파일 강제 삭제 (주의!)
```

**Mac Terminal:**

```bash
cp a.txt b.txt                 # 파일 복사
cp -R data backup              # 폴더 전체 복사 (하위 포함)
mv old.txt new.txt             # 이름 변경 또는 이동
rm *.log                       # 모든 로그 파일 삭제
rm -rf temp                    # 폴더와 내부 파일 강제 삭제 (주의!)
```

### 파일 내용 확인

**Windows CMD:**

```cmd
type readme.md                      # 파일 전체 내용 출력
findstr /s /n "TODO" *.py          # 모든 Python 파일에서 TODO가 있는 줄 번호 표시
more filename.txt                   # 파일 내용을 페이지 단위로 보기
```

**Mac Terminal:**

```bash
cat readme.md                       # 파일 전체 내용 출력
grep -rn "TODO" *.py               # 모든 Python 파일에서 TODO가 있는 줄 번호 표시
less filename.txt                   # 파일 내용을 페이지 단위로 보기
head -n 10 data.csv                # 파일 앞 10줄만 보기
tail -n 20 app.log                 # 파일 뒤 20줄만 보기
tail -f app.log                    # 실시간 로그 모니터링
```

---

## 🛠️ 개발 및 협업 도구 (Git / Jupyter / Pip)

### Git 실전 명령어

**공통 (Windows & Mac):**

```bash
git pull                           # 최신 코드 가져오기
git checkout -b [브랜치명]         # 새 브랜치 생성 및 이동
git log --oneline -5               # 최근 커밋 5개만 간단히 보기
git reset --soft HEAD~1            # 마지막 커밋 취소 (수정사항은 유지)
git diff                           # 현재 수정된 내용 비교
git stash                          # 현재 변경사항 임시 저장
git stash pop                      # 임시 저장한 변경사항 복원
```

### Jupyter/IPython

**Windows CMD:**

```cmd
# 가상환경을 주피터 커널로 등록
python -m ipykernel install --user --name .venv --display-name "Project-Venv"
jupyter kernelspec list            # 등록된 커널 목록 보기
jupyter notebook --port=8889       # 다른 포트로 주피터 실행
```

**Mac Terminal:**

```bash
# 가상환경을 주피터 커널로 등록
python3 -m ipykernel install --user --name .venv --display-name "Project-Venv"
jupyter kernelspec list            # 등록된 커널 목록 보기
jupyter notebook --port=8889       # 다른 포트로 주피터 실행
```

### PIP 관리

**Windows CMD:**

```cmd
python -m pip install --upgrade pip    # PIP 업그레이드
pip list --outdated                    # 업데이트 가능한 패키지 목록
pip show [패키지명]                    # 특정 패키지 정보 보기
```

**Mac Terminal:**

```bash
python3 -m pip install --upgrade pip   # PIP 업그레이드
pip3 list --outdated                   # 업데이트 가능한 패키지 목록
pip3 show [패키지명]                   # 특정 패키지 정보 보기
```

### Homebrew (Mac 전용 패키지 관리자)

```bash
brew install [패키지명]                # 패키지 설치
brew update                           # Homebrew 업데이트
brew upgrade                          # 모든 패키지 업그레이드
brew list                             # 설치된 패키지 목록
brew search [키워드]                  # 패키지 검색
brew uninstall [패키지명]             # 패키지 삭제
```

---

## 💻 시스템 및 네트워크 관리 (System & Network)

### 프로세스/포트 관리

**Windows CMD:**

```cmd
netstat -ano | findstr :8888      # 8888번 포트를 사용하는 PID 찾기
taskkill /f /pid [PID]            # 특정 PID 강제 종료
tasklist | findstr python         # 실행 중인 Python 프로세스만 확인
wmic process where name="python.exe" delete  # 모든 Python 프로세스 종료
```

**Mac Terminal:**

```bash
lsof -i :8888                     # 8888번 포트를 사용하는 프로세스 찾기
kill -9 [PID]                     # 특정 PID 강제 종료
ps aux | grep python              # 실행 중인 Python 프로세스만 확인
pkill -9 python                   # 모든 Python 프로세스 종료
top                               # 실시간 프로세스 모니터링
htop                              # 더 보기 좋은 프로세스 모니터링 (brew install htop)
```

### 네트워크 진단

**Windows CMD:**

```cmd
ipconfig                          # 내 IP 주소 확인
ipconfig /all                     # 네트워크 상세 정보
ping google.com                   # 인터넷 연결 확인
nslookup google.com              # DNS 조회
```

**Mac Terminal:**

```bash
ifconfig                          # 네트워크 인터페이스 정보
ifconfig | grep inet              # IP 주소만 간단히 보기
ping google.com                   # 인터넷 연결 확인
nslookup google.com              # DNS 조회
curl ifconfig.me                  # 외부 IP 주소 확인
traceroute google.com             # 네트워크 경로 추적
```

### 시스템 정보

**Windows CMD:**

```cmd
systeminfo                       # 시스템 전체 정보
echo %PATH%                      # 환경 변수 경로 확인
set                              # 모든 환경 변수 보기
whoami                           # 현재 사용자 정보
ver                              # Windows 버전 확인
```

**Mac Terminal:**

```bash
uname -a                         # 시스템 전체 정보
echo $PATH                       # 환경 변수 경로 확인
env                              # 모든 환경 변수 보기
whoami                           # 현재 사용자 정보
sw_vers                          # macOS 버전 확인

df -h                            # 디스크 사용량 확인
du -sh *                         # 현재 폴더의 각 항목별 용량
free -h                          # 메모리 사용량 확인 (Linux)
```

---

## ⚡ 실무 유용한 조합 명령어 (Patterns)

### 신규 프로젝트 세팅

**Windows CMD:**

```cmd
# 가상환경 생성 → 활성화 → 패키지 설치 (한 번에)
python -m venv .venv && .venv\Scripts\activate && pip install -r requirements.txt
```

**Mac Terminal:**

```bash
# 가상환경 생성 → 활성화 → 패키지 설치 (한 번에)
python3 -m venv .venv && source .venv/bin/activate && pip3 install -r requirements.txt
```

### 날짜별 백업

**Windows CMD:**

```cmd
# 오늘 날짜로 백업 폴더 생성 및 데이터 복사
set today=%date:~0,4%%date:~5,2%%date:~8,2%
mkdir backup_%today% && xcopy data backup_%today% /e /i /y
```

**Mac Terminal:**

```bash
# 오늘 날짜로 백업 폴더 생성 및 데이터 복사
today=$(date +%Y%m%d)
mkdir backup_$today && cp -R data backup_$today
```

### 코드 정리 및 저장

**Windows CMD:**

```cmd
# Python 프로세스 종료 → Git 커밋 → 푸시
taskkill /f /im python.exe & git add . & git commit -m "update" & git push
```

**Mac Terminal:**

```bash
# Python 프로세스 종료 → Git 커밋 → 푸시
pkill -9 python; git add .; git commit -m "update"; git push
```

### 대용량 데이터 처리

**Windows CMD:**

```cmd
# 파일 개수 확인 → 용량 확인 → 샘플 데이터 보기
dir /s | find "File(s)" & dir /-c & head -n 10 data.csv
```

**Mac Terminal:**

```bash
# 파일 개수 확인 → 용량 확인 → 샘플 데이터 보기
find . -type f | wc -l && du -sh . && head -n 10 data.csv
```

### 로그 분석

**Windows CMD:**

```cmd
# 에러 로그만 추출하여 새 파일로 저장
findstr /i /c:"error" /c:"exception" app.log > error_log.txt
```

**Mac Terminal:**

```bash
# 에러 로그만 추출하여 새 파일로 저장
grep -iE "error|exception" app.log > error_log.txt
```

### 배치/스크립트 실행

**Windows CMD:**

```cmd
# 배치 파일 생성 (.bat)
echo @echo off > setup.bat
echo python -m venv .venv >> setup.bat
echo .venv\Scripts\activate >> setup.bat
```

**Mac Terminal:**

```bash
# 쉘 스크립트 생성 (.sh)
cat > setup.sh << 'EOF'
#!/bin/bash
python3 -m venv .venv
source .venv/bin/activate
EOF
chmod +x setup.sh  # 실행 권한 부여
./setup.sh         # 스크립트 실행
```

---

## 📌 주요 단축키 & 팁 (Shortcuts)

### 필수 단축키

| 기능             | Windows CMD               | Mac Terminal                |
| ---------------- | ------------------------- | --------------------------- |
| 자동 완성        | `Tab` ⭐                | `Tab` ⭐                  |
| 명령어 히스토리  | `↑` / `↓`           | `↑` / `↓`             |
| 명령어 강제 종료 | `Ctrl + C`              | `Ctrl + C`                |
| 히스토리 팝업    | `F7`                    | `Ctrl + R` (검색)         |
| 화면 청소        | `Ctrl + L` 또는 `cls` | `Ctrl + L` 또는 `clear` |
| 줄 처음으로      | `Home`                  | `Ctrl + A`                |
| 줄 끝으로        | `End`                   | `Ctrl + E`                |
| 단어 단위 이동   | `Ctrl + ←/→`          | `Option + ←/→`          |
| 현재 줄 삭제     | `Esc`                   | `Ctrl + U`                |

### 생산성 팁

**Windows CMD:**

```cmd
doskey /history              # 명령어 히스토리 전체 보기
doskey ls=dir /w            # 별명(alias) 만들기
doskey h=doskey /history    # 단축 명령어 생성
doskey ga=git add .         # Git 명령어 별명
```

**Mac Terminal (.zshrc 또는 .bashrc 파일에 추가):**

```bash
alias ll='ls -la'           # 상세 목록 별명
alias ..='cd ..'            # 상위 폴더 이동 단축
alias ...='cd ../..'        # 두 단계 위로
alias ga='git add .'        # Git 명령어 별명
alias gc='git commit -m'    # Git 커밋 단축
alias gp='git push'         # Git 푸시 단축
alias gs='git status'       # Git 상태 단축
alias py='python3'          # Python 단축

# 설정 적용
source ~/.zshrc             # Zsh 사용 시
source ~/.bashrc            # Bash 사용 시
```

### CMD/Terminal 창 관리

**Windows CMD:**

```cmd
title "프로젝트 작업"        # CMD 창 제목 변경
color 0A                    # 배경색/글자색 변경 (검정바탕/초록글씨)
mode 120,30                 # 창 크기 조정 (가로120, 세로30)
exit                        # CMD 창 닫기
```

**Mac Terminal:**

```bash
echo -ne "\033]0;프로젝트 작업\007"  # 터미널 제목 변경
export PS1="\u@\h:\w$ "              # 프롬프트 커스터마이징
clear                                # 화면 청소
exit                                 # 터미널 창 닫기
```

### Mac 전용 유용한 팁

```bash
pbcopy < file.txt           # 파일 내용을 클립보드에 복사
pbpaste > file.txt          # 클립보드 내용을 파일로 저장
say "작업 완료"             # 음성으로 메시지 읽기
open -a "Visual Studio Code" .  # VSCode로 현재 폴더 열기
mdfind "검색어"             # Spotlight 검색 (매우 빠름)
caffeinate -t 3600          # 1시간 동안 Mac 절전 방지
```

---

## 🆚 Windows vs Mac 주요 차이점 요약

| 작업              | Windows CMD         | Mac Terminal        |
| ----------------- | ------------------- | ------------------- |
| 파일 목록         | `dir`             | `ls`              |
| 경로 구분자       | `\`               | `/`               |
| 홈 디렉토리       | `%USERPROFILE%`   | `~`               |
| 환경변수          | `%PATH%`          | `$PATH`           |
| 복사              | `copy`, `xcopy` | `cp`, `cp -R`   |
| 이동/이름변경     | `move`            | `mv`              |
| 삭제              | `del`, `rmdir`  | `rm`, `rm -rf`  |
| 파일 내용         | `type`            | `cat`             |
| 검색              | `findstr`         | `grep`            |
| 프로세스 확인     | `tasklist`        | `ps aux`          |
| 프로세스 종료     | `taskkill`        | `kill`, `pkill` |
| 네트워크 정보     | `ipconfig`        | `ifconfig`        |
| 파이썬            | `python`          | `python3`         |
| 패키지 관리       | (없음)              | `brew`            |
| 관리자 권한       | 관리자로 실행       | `sudo`            |
| 클립보드 복사     | `clip`            | `pbcopy`          |
| 클립보드 붙여넣기 | (불가)              | `pbpaste`         |

---

## 📚 추가 학습 자료

### Windows CMD

- [Microsoft 공식 CMD 문서](https://docs.microsoft.com/en-us/windows-server/administration/windows-commands/windows-commands)
- PowerShell로 업그레이드 고려 (더 강력한 기능)

### Mac Terminal

- [macOS Terminal 가이드](https://support.apple.com/guide/terminal/welcome/mac)
- Zsh 설정: [Oh My Zsh](https://ohmyz.sh/) 프레임워크 추천
- iTerm2: 기본 Terminal보다 강력한 대체 앱

---

**💡 Pro Tip**:

- **Windows**: 자주 쓰는 명령어를 `.bat` 파일로 저장하거나 `doskey`로 별명을 만드세요!
- **Mac**: `~/.zshrc` 또는 `~/.bashrc` 파일에 `alias`를 추가하여 영구적으로 단축 명령어를 사용하세요!
