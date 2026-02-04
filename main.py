import sys
import os
import json
import pandas as pd

sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from src.data_engine.loader import smart_data_load
from src.data_engine.standardizer import standardize_real_estate, aggregate_telecom_data
from src.scoring.engine import calculate_neighborhood_scores
from src.reporting.formatter import build_reports
from src.reporting.visualizer import create_radar_chart
from src.reporting.explainer import extract_neighborhood_signals

def main(persona_key=None):
    output_dir = "outputs"
    
    try:
        # [MASTER POLICY LOAD] 시스템 마스터 정책 로드
        master_policy_path = os.path.join("policies", "score_policy_v1.json")
        master_policy = json.load(open(master_policy_path, 'r', encoding='utf-8'))
        sys_msgs = master_policy.get('system_messages', {})
        constants = master_policy.get('global_constants', {})
        
        # 페르소나 결정 (인자 -> 마스터 정책 기본값 순)
        if not persona_key:
            persona_key = master_policy.get('default_persona', 'career_slave')
            
        print(f"--- 🚀 AI Neighborhood Curator v3.2 (Persona: {persona_key}) ---")

        # [STAGE 1] 결정 레이어 로드 및 정제
        print(sys_msgs.get('stage_1_log', "1/4 결정 레이어 작동 중..."))
        
        # 페르소나 라이브러리 로드
        personas = json.load(open(os.path.join("policies", "personas.json"), 'r', encoding='utf-8'))
        selected_persona = personas['personas'].get(persona_key)
        
        raw_rent = smart_data_load(os.path.join("data", "raw", "seoul_real_estate_rent.csv"))
        raw_telecom = smart_data_load(os.path.join("data", "raw", "2025.11월_29개 통신정보.xlsx"))
        
        # 마스터 정책의 이자율 적용
        interest_rate = constants.get('annual_interest_rate', 0.055)
        std_rent = standardize_real_estate(raw_rent, interest_rate=interest_rate)
        agg_telecom = aggregate_telecom_data(raw_telecom)
        
        merged_df = pd.merge(std_rent, agg_telecom, on='행정동_명칭', how='left').fillna(0)
        
        print(f"적용 페르소나: {selected_persona['name']}")
        ranked_df = calculate_neighborhood_scores(merged_df, selected_persona)
        
        # [STAGE 2] 설명 레이어
        print(sys_msgs.get('stage_2_log', "2/4 설명 레이어 작동 중..."))
        raw_interest = smart_data_load(os.path.join("data", "raw", "2025.11월_10개 관심집단수.xlsx"))
        top3_df = ranked_df.head(constants.get('top_n_rank', 3))
        final_report_df = extract_neighborhood_signals(top3_df, raw_interest)
        
        # [STAGE 3] 결과 출력
        print(sys_msgs.get('stage_3_log', "3/4 최종 리포트 생성 중..."))
        build_reports(final_report_df, output_dir)
        create_radar_chart(final_report_df, os.path.join(output_dir, 'radar_final.html'))
        
        print(f"\n✅ {sys_msgs.get('completion_msg', '완료!')} [{selected_persona['name']}]")
        
    except Exception as e:
        print(f"❌ 오류 발생: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    import sys
    # 외부 인자 우선 순위
    target_persona = sys.argv[1] if len(sys.argv) > 1 else None
    main(persona_key=target_persona)
