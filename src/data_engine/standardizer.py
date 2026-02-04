import pandas as pd
import numpy as np

def standardize_real_estate(df: pd.DataFrame, interest_rate: float = 0.055) -> pd.DataFrame:
    """부동산 원본 데이터를 시스템 표준 규격으로 변환합니다."""
    df = df.copy()
    
    # 컬럼 매핑 규칙
    map_rules = {
        '자치구명': '자치구', '법정동명': '법정동',
        '보증금(만원)': '보증금_만원', '임대료(만원)': '임대료_만원', 
        '건물명': '건물_명칭', '전월세구분': '전월세_구분'
    }
    for old, new in map_rules.items():
        if old in df.columns:
            df = df.rename(columns={old: new})
            
    df['보증금_만원'] = pd.to_numeric(df['보증금_만원'], errors='coerce').fillna(0)
    df['임대료_만원'] = pd.to_numeric(df['임대료_만원'], errors='coerce').fillna(0)
    df['환산_월세'] = (df['보증금_만원'] * interest_rate / 12) + df['임대료_만원']
    df['행정동_명칭'] = df['자치구'].astype(str) + " " + df['법정동'].astype(str)
    
    return df

def aggregate_telecom_data(df: pd.DataFrame) -> pd.DataFrame:
    """통신 데이터를 행정동 단위로 집계하고 특수값(*)을 처리합니다."""
    if df.empty: return df
    df = df.copy()
    
    # 특수값 (*) 처리 - 보수적 접근
    df = df.replace('*', 1.0)
    
    # 수치 변환 대상 컬럼
    target_cols = ['총인구수', '1인가구수', '배달 서비스 사용일수', '평균 출근 소요시간 평균', '야간상주지 변경횟수 평균']
    for col in target_cols:
        if col in df.columns:
            df[col] = pd.to_numeric(df[col], errors='coerce').fillna(0)
            
    df['행정동_명칭'] = df['자치구'].astype(str) + " " + df['행정동'].astype(str)
    
    # 집계 규칙 정의
    agg_dict = {
        '총인구수': 'sum', '1인가구수': 'sum',
        '배달 서비스 사용일수': 'mean', '평균 출근 소요시간 평균': 'mean', '야간상주지 변경횟수 평균': 'mean'
    }
    final_agg = {k: v for k, v in agg_dict.items() if k in df.columns}
    
    agg_df = df.groupby('행정동_명칭').agg(final_agg).reset_index()
    
    # 한글_언더바 표준 컬럼명으로 변경
    agg_df = agg_df.rename(columns={
        '1인가구수': '1인가구_수',
        '배달 서비스 사용일수': '배달_사용지수',
        '평균 출근 소요시간 평균': '출퇴근_소요시간',
        '야간상주지 변경횟수 평균': '안전_변동지수'
    })
    
    return agg_df
