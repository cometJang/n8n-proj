import pandas as pd

def extract_neighborhood_signals(top_df: pd.DataFrame, interest_df: pd.DataFrame) -> pd.DataFrame:
    """
    [설명 레이어] 
    기획서의 맞춤 추천 철학을 기반으로 동네별 라이프스타일 시그널을 입힙니다.
    """
    result = top_df.copy()
    
    # 페르소나별/지역별 맞춤형 시그널 맵 (기획서 시나리오 반영)
    signal_map = {
        "관악구 신림동": "회사가 가깝고 배달 인프라가 완벽합니다. 1인 가구의 성지다운 편리함을 누리세요.",
        "마포구 서교동": "개성 있는 카페와 문화시설이 가득합니다. 트렌디한 라이프스타일을 원하신다면 최고의 선택입니다.",
        "관악구 봉천동": "합리적인 월세와 안정적인 주거 여건을 제공합니다. 가성비와 실속을 동시에 챙길 수 있습니다.",
        "광진구 화양동": "대학가의 활기와 편리한 대중교통을 동시에 누릴 수 있는 역동적인 동네입니다."
    }
    
    # 동네별 매핑
    result['동네_시그널'] = result['행정동_명칭'].map(lambda x: signal_map.get(x, "당신의 라이프스타일에 부합하는 풍부한 인프라를 갖춘 동네입니다."))
    
    return result
