import pandas as pd
import json
import os

def build_reports(ranked_df: pd.DataFrame, output_dir: str):
    """최종 리포트 파일(CSV, JSON)을 생성합니다."""
    os.makedirs(output_dir, exist_ok=True)
    
    # 1. 원본 데이터 복사 및 소수점 기본 반올림
    top3_df = ranked_df.head(3).copy()
    numeric_cols = top3_df.select_dtypes(include=['number']).columns
    top3_df[numeric_cols] = top3_df[numeric_cols].round(2)
    top3_df = top3_df.fillna(0)

    # [가독성 강화] 천 단위 콤마 포맷팅 필터
    def format_with_commas(val):
        if isinstance(val, (int, float)):
            if val == 0: return "0"
            # 소수점이 있는 경우와 없는 경우 구분
            if val == int(val):
                return "{:,}".format(int(val))
            return "{:,.2f}".format(val)
        return val

    # 리포트용 포맷팅 적용 (문자열 변환)
    display_df = top3_df.copy()
    for col in numeric_cols:
        display_df[col] = display_df[col].apply(format_with_commas)

    # 2. CSV 저장 (사용자 가시성 전용 컬럼)
    display_cols = [
        '행정동_명칭', '건물_명칭', '전월세_구분', 
        '보증금_만원', '임대료_만원', '환산_월세', '최종_점수'
    ]
    # 존재하는 컬럼만 필터링
    valid_cols = [c for c in display_cols if c in display_df.columns]
    formatted_csv = display_df[valid_cols]
    formatted_csv.to_csv(os.path.join(output_dir, 'top3_final.csv'), index=False, encoding='utf-8-sig')
    
    # 3. JSON 저장 (n8n 및 시스템 연동용)
    # JSON에는 숫자형과 포맷팅형을 함께 제공하거나, 리포트 성격에 맞게 포맷팅된 결과 제공
    result_dict = display_df.to_dict(orient='records')
    
    report_json = {
        "status": "ok",
        "top_recommendations": result_dict,
        "metadata": {
            "version": "3.2.0",
            "naming_rule": "korean_underscore",
            "description": "숫자 필드에 천 단위 콤마 및 소수점 2자리 포맷팅 적용됨"
        }
    }
    
    with open(os.path.join(output_dir, 'report.json'), 'w', encoding='utf-8') as f:
        json.dump(report_json, f, ensure_ascii=False, indent=2)
