# 🚀 FLUX : Fast Local Unified eXecution

<img src="pic/flux_ai_removed.png" width="50%">

## 💡 Description
Flux는 개발자가 패키지 의존성 문제나 환경 설정 오류로 인해 겪는 흐름의 단절을 방지하기 위해 설계된 **AI 기반 로컬 환경 최적화 에이전트**입니다.

- Fast: 지연 없는 즉각적인 진단과 조치.
- Local: 사용자 시스템의 현재 상태(Python 버전, OS, 설치된 패키지)를 완벽히 이해합니다.
- Unified: Gemini와 Claude의 통합된 지능을 활용하여 최적의 솔루션을 도출합니다.
- eXecution: 단순 가이드를 넘어, 실제 해결 가능한 명령어를 실행 환경에 바로 제안합니다.

## 🛠 Features
- Smart pip Install: 단순 설치를 넘어, 현재 환경과의 충돌 가능성을 사전에 분석합니다.
- Self-Healing: 설치 중 오류 발생 시 에이전트가 즉시 개입하여 해결책을 제시합니다.
- Hybrid Intelligence: Google의 Gemini와 Anthropic의 Claude를 교차 활용하여 신뢰도를 높였습니다.

## 📋 Requirements
- python : 3.11 or higher version
- google-genai 
- anthropic
- python-dotenv
- rich

## 🤓 Let's Get Started
1. **가상환경 설정**
- 가장 먼저 개발, 연구, 실험에 사용할 가상환경을 생성하고 활성화하십시오.

```bash
# Windows
python -m venv venv
.\venv\Scripts\activate
```

```bash
# Mac/Linux
python3 -m venv venv
source venv/bin/activate
```

2. **저장소 및 클론 설치**
```bash
git clone https://github.com/JJUNHYEOK/Flux_Project.git
cd Flux_Project
pip install -r requirements.txt
```

3. **API KEY 설정**
- 프로젝트 루트 폴더에 .env를 생성하고 아래 내용을 입력하십시오.
```bash
GOOGLE_API_KEY=your_key_here
ANTHROPIC_API_KEY=your_key_here
```

4. **라이브러리 설치**
- FLUX와 함께 안전하게 라이브러리를 설치하십시오. 만약 문제가 발생하면 FLUX가 다 해결할 것이고, 문제가 없다면 평소처럼 무탈한 하루일거에요 !
```bash
python main.py pip install <라이브러리명>
```

## 😎 With FLUX
- FLUX와 함께라면 걱정은 쓸모없는 것입니다. 더 좋은 개발자, 연구자가 되기 위한 준비 완료!

