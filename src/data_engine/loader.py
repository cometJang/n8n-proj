import pandas as pd
import os

def smart_data_load(file_path: str, use_cache: bool = True) -> pd.DataFrame:
    """캐시(.pkl)가 있으면 캐시를 읽고, 없으면 원본을 읽어 캐시를 생성합니다."""
    cache_path = file_path.replace('.xlsx', '.pkl').replace('.csv', '.pkl')
    
    if use_cache and os.path.exists(cache_path):
        print(f"DEBUG: 캐시 파일 로드 중... ({cache_path})")
        return pd.read_pickle(cache_path)
    
    print(f"DEBUG: 원본 파일 로드 중... ({file_path})")
    if file_path.endswith('.xlsx'):
        df = pd.read_excel(file_path)
    else:
        try:
            df = pd.read_csv(file_path, encoding='utf-8-sig')
        except:
            df = pd.read_csv(file_path, encoding='cp949')
            
    df.columns = [c.strip() for c in df.columns]
    
    if use_cache:
        df.to_pickle(cache_path)
    return df
