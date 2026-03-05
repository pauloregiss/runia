import streamlit as st
from analyzer import analisar_video
import tempfile

st.set_page_config(page_title="AI Running Analyzer", layout="centered")

st.title("🏃 AI Running Analyzer")
st.write("Envie um vídeo correndo ou caminhando para analisar sua biomecânica básica.")

video = st.file_uploader(
    "📤 Envie um vídeo", 
    type=["mp4", "mov", "avi"]
)

if video is not None:

    # salvar vídeo temporariamente
    temp = tempfile.NamedTemporaryFile(delete=False)
    temp.write(video.read())
    video_path = temp.name

    st.subheader("🎥 Vídeo enviado")
    st.video(video_path)

    st.write("⏳ Analisando vídeo...")

    # rodar análise
    resultado = analisar_video(video_path)

    st.subheader("📊 Resultado da análise")

    # verificar se retorno é válido
    if isinstance(resultado, dict):

        st.metric(
            "Ângulo médio do joelho",
            f"{resultado['angulo_joelho']:.2f}°"
        )

        st.metric(
            "Cadência estimada",
            f"{resultado['cadencia']} passos/min"
        )

        # feedback simples
        if resultado["angulo_joelho"] < 120:
            st.warning("⚠️ Seu joelho pode estar flexionando pouco durante a passada.")

        elif resultado["angulo_joelho"] > 160:
            st.warning("⚠️ Possível overstride (passada muito estendida).")

        else:
            st.success("✅ Movimento do joelho dentro de um padrão comum.")

    else:
        # se a função retornar erro
        st.error(resultado)