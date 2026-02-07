# FLUX : Fast Local Unified eXecution

## Description
- Flux는 '흐름'이라는 뜻을 가진 단어로, 본 에이전트를 활용하여 개발 흐름이 끊어지지 않도록 합니다.
- Fast Local Unified eXecution : 현재 로컬(Local)의 환경을 이해하고, 이를 통합(Unified)된 지능(Gemini + Claude)으로부터 도출된 솔루션을 빠르게(Fast) 실행(eXecution) 가능하도록 제공합니다. 

## How to use program?
1. create .env file at srcs folder
2. clone the source code.
3. ./srcs/get_err_log_from_pip.py
4. if error occur, select a option that GenAI recommed.

## Requirements
- python 3.11 or higher version
- google-genai
- Claude
- python-dotenv

## example of .env file
GEMINI_API_KEY=Your GEMINI_API_KEY
