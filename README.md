# 1시간 간격 스트레칭 알림

## 프로젝트 개요
이 스크립트는 매시간 데스크탑 알림을 띄워 “wake up stretching” 메시지를 띄움.   
단순히 Python + `schedule` 모듈과 `plyer` 라이브러리만으로 구현되어, Windows는 물론 macOS/Linux(호환성 확인 필요)에서도 동작함

## 요구사항
- Python 3.7 이상
- `schedule` 패키지
- `plyer` 패키지

## 설치

```bash
# 저장소 클론 또는 파일 다운로드
git clone https://github.com/yourname/stretch-reminder.git
cd stretch-reminder

# 의존성 설치
pip install --upgrade pip
pip install schedule plyer
```

## 시스템 시작 시 자동 실행
작업스케줄러 등록

stretch_reminder.py 바로가기 파일을 여기에 복사

PC 켜면 자동 실행