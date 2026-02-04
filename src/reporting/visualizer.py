import plotly.graph_objects as go
import pandas as pd

def create_radar_chart(df: pd.DataFrame, output_path: str):
    """상위 동네들을 비교하는 프리미엄 레이더 차트를 생성합니다."""
    metrics = ['월세_점수', '출퇴근_점수', '인프라_점수', '분위기_점수', '안전_점수']
    labels = ['Rent', 'Commute', 'Infra', 'Vibe', 'Safety']
    
    fig = go.Figure()
    colors = ['rgba(99, 110, 250, 0.5)', 'rgba(239, 85, 59, 0.5)', 'rgba(0, 204, 150, 0.5)']
    line_colors = ['#636EFA', '#EF553B', '#00CC96']
    
    for i, (_, row) in enumerate(df.head(3).iterrows()):
        r_values = [row.get(c, 0) for c in metrics]
        r_values.append(r_values[0]) # 도형 닫기
        
        fig.add_trace(go.Scatterpolar(
            r=r_values,
            theta=labels + [labels[0]],
            fill='toself',
            fillcolor=colors[i % 3],
            name=row.get('행정동_명칭', f'지역 {i+1}'),
            line=dict(color=line_colors[i % 3], width=2)
        ))

    fig.update_layout(
        polar=dict(
            radialaxis=dict(visible=True, range=[0, 100], gridcolor="#EEE"),
            bgcolor="#FDFDFD"
        ),
        title=dict(text="<b>동네별 핵심 역량 DNA 비교</b>", x=0.5, font=dict(size=20)),
        paper_bgcolor='white',
        margin=dict(l=50, r=50, t=100, b=50)
    )
    fig.write_html(output_path)
