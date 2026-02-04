# AI 동네 큐레이터 구현 계획 (Implementation Plan)

## 1. 개요
본 문서는 AI 동네 큐레이터 프로젝트의 기술적 구현 단계와 현재 상태를 추적합니다.

## 2. 주요 아키텍처 (v3.2)
- **Decision Layer**: 객관적 수치 기반 순위 산정
- **Explanation Layer**: 관심사 기반 정성적 해설 추가
- **Constitutional Firewall**: 레이어 간 데이터 침범 방지

## 3. 진행 상황 (Status)

### Phase 1: MVP & Architecture
- [x] 데이터 헌법 제정 및 아키텍처 수립
- [x] 스마트 로딩(.pkl 캐싱) 엔진 구축
- [x] 5대 페르소나 가중치 시스템 구현
- [x] 글로벌 스탠다드 네이밍(English Vars) 리팩토링

### Phase 2: Automation & AI (Next)
- [ ] n8n 워크플로우를 통한 실시간 수집 자동화
- [ ] LangChain 에이전트를 통한 대화형 상담 서비스
- [ ] 이메일/카카오톡 가공 리포트 발송

## 4. 핵심 파일 구조
- `main.py`: 파이프라인 지휘자
- `src/data_engine/`: 로드 및 표준화
- `src/scoring/`: 순위 결정 엔진
- `src/reporting/`: 리포트 발행 및 시각화
- `docs/`: 기획 및 헌법 문서

---
**"Done is better than perfect. But clean is better than messy."**
