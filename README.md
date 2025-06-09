# FASTAPI Template with MongoDB

이 프로젝트는 MongoDB를 이용한 FASTAPI 템플릿입니다. Docker를 사용하지 않고, 대신 venv를 사용합니다.

## 설치 방법 (Installation)

1. 가상 환경 생성 (Create a virtual environment):

   ```bash
   python -m venv venv
   ```

2. 가상 환경 활성화 (Activate the virtual environment):

   - Windows:
     ```bash
     .\venv\Scripts\activate
     ```
   - macOS/Linux:
     ```bash
     source venv/bin/activate
     ```

3. 필요한 패키지 설치 (Install the required packages):
   ```bash
   pip install -r requirements.txt
   ```

## 사용 방법 (Usage)

1. 서버 실행 (Run the server):

   ```bash
   uvicorn main:app --reload
   ```

2. API 문서 확인 (Check the API documentation):
   - Swagger UI: `http://127.0.0.1:8000/docs`
   - ReDoc: `http://127.0.0.1:8000/redoc`

## 프로젝트 구조 (Project Structure)

```
fastAPI_tem/
├── app/
│   ├── main.py
│   ├── models/
│   ├── routes/
│   └── ...
├── venv/
├── requirements.txt
└── README.md
```

## 기여 방법 (Contributing)

기여를 원하시면, 이슈를 등록하거나 풀 리퀘스트를 제출해 주세요.

---

This project is a FASTAPI template using MongoDB. It does not use Docker, but instead uses venv.

## Installation

1. Create a virtual environment:

   ```bash
   python -m venv venv
   ```

2. Activate the virtual environment:

   - Windows:
     ```bash
     .\venv\Scripts\activate
     ```
   - macOS/Linux:
     ```bash
     source venv/bin/activate
     ```

3. Install the required packages:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. Run the server:

   ```bash
   uvicorn main:app --reload
   ```

2. Check the API documentation:
   - Swagger UI: `http://127.0.0.1:8000/docs`
   - ReDoc: `http://127.0.0.1:8000/redoc`

## Project Structure

```
fastAPI_tem/
├── app/
│   ├── main.py
│   ├── models/
│   ├── routes/
│   └── ...
├── venv/
├── requirements.txt
└── README.md
```

## Contributing

If you want to contribute, please open an issue or submit a pull request.
