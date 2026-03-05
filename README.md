# 🏃 Running Analysis AI

Aplicação de **Visão Computacional com Inteligência Artificial** que analisa vídeos de corrida ou caminhada e extrai métricas biomecânicas automaticamente.

O sistema utiliza **MediaPipe Pose** para identificar os pontos do corpo e calcular informações relevantes sobre o movimento, como ângulo do joelho e cadência da corrida.

A interface foi construída com **Streamlit**, permitindo que qualquer pessoa envie um vídeo e receba uma análise básica da corrida.

---

# 🚀 Demo

O usuário pode:

1. Enviar um vídeo de corrida ou caminhada
2. O sistema analisa os frames
3. A IA detecta a pose corporal
4. Métricas biomecânicas são calculadas automaticamente
5. O resultado é exibido na interface web

---

# 🧠 Tecnologias Utilizadas

- **Python**
- **MediaPipe (Pose Estimation)**
- **OpenCV**
- **Streamlit**
- **NumPy**

---

# 📊 Métricas Analisadas

Atualmente o sistema analisa:

- 📐 Ângulo médio do joelho durante a corrida
- ⚡ Estimativa de cadência de passos
- 🏃 Detecção de movimento corporal

Essas métricas podem ajudar na **avaliação de biomecânica de corrida**.

---

# 🖥️ Interface

A aplicação possui uma interface simples onde o usuário pode:

- Fazer upload de um vídeo
- Executar a análise automaticamente
- Visualizar as métricas calculadas

---

# 📂 Estrutura do Projeto
running-analysis-ai
│
├── app.py # Interface Streamlit
├── analyzer.py # Lógica de análise de vídeo
├── requirements.txt # Dependências do projeto
└── README.md


---

# ⚙️ Instalação

Clone o repositório:

```bash
git clone https://github.com/seuusuario/running-analysis-ai.git
cd running-analysis-ai

python -m venv venv

pip install -r requirements.txt

streamlit run app.py

🔮 Melhorias Futuras

Algumas melhorias planejadas para o projeto:

🎯 Desenhar o esqueleto da pose diretamente no vídeo

📈 Gerar gráficos da biomecânica da corrida

🧠 Criar um score de qualidade da corrida com Machine Learning

📹 Exportar vídeo com a análise aplicada

📊 Detectar assimetria de movimento

💡 Aplicações

Este tipo de sistema pode ser utilizado em:

Análise de performance esportiva

Prevenção de lesões

Treinamento esportivo

Avaliação fisioterapêutica

Aplicações de saúde digital

👨‍💻 Autor

Desenvolvido por Paulo Régis

Profissional em transição para Inteligência Artificial, Machine Learning e Visão Computacional, desenvolvendo projetos práticos em Python.

🔗 LinkedIn
🔗 GitHub
