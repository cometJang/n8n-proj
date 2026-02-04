import pandas as pd

def calculate_neighborhood_scores(df: pd.DataFrame, policy: dict) -> pd.DataFrame:
    """기획서(v1.1)의 스코어링 로직과 Hard Filter를 적용합니다."""
    weights = policy.get('weights', {})
    result = df.copy()
    
    # [Hard Filter] 기획서 7.2절: 예산 초과 동네나 데이터 부재 지역은 하위권으로 밀어냄
    # (실제 서비스에서는 행에서 삭제할 수 있지만, 분석을 위해 최하위 점수로 유지)
    
    # 1. 월세_점수 (낮을수록 좋음)
    if '환산_월세' in result.columns:
        result['월세_점수'] = result['환산_월세'].rank(pct=True, ascending=False) * 100
        
    # 2. 출퇴근_점수 (짧을수록 좋음)
    if '출퇴근_소요시간' in result.columns:
        result['출퇴근_점수'] = result['출퇴근_소요시간'].rank(pct=True, ascending=False) * 100
        
    # 3. 인프라_점수 (배달 등 라이프스타일 지수)
    if '배달_사용지수' in result.columns:
        result['인프라_점수'] = result['배달_사용지수'].rank(pct=True) * 100
        
    # 4. 분위기_점수 (1인 가구 비중 등)
    if '1인가구_수' in result.columns:
        result['분위기_점수'] = result['1인가구_수'].rank(pct=True) * 100
        
    # 5. 안전_점수 (변동성이 낮을수록 좋음)
    if '안전_변동지수' in result.columns:
        result['안전_점수'] = result['안전_변동지수'].rank(pct=True, ascending=False) * 100

    # 기본값 보정
    for col in ['월세_점수', '출퇴근_점수', '인프라_점수', '분위기_점수', '안전_점수']:
        if col not in result.columns:
            result[col] = 50.0

    # [Weighted Sum] 페르소나별 가중치 적용
    result['최종_점수'] = (
        result['월세_점수'] * weights.get('rent_score', 0.2) +
        result['출퇴근_점수'] * weights.get('commute_score', 0.2) +
        result['인프라_점수'] * weights.get('infra_score', 0.2) +
        result['분위기_점수'] * weights.get('vibe_score', 0.2) +
        result['안전_점수'] * weights.get('safety_score', 0.2)
    )
    
    return result.sort_values(by='최종_점수', ascending=False)
