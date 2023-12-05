FROM python:3.8

RUN pip install numpy pandas scikit-learn

WORKDIR /pyapp/
COPY apps/* apps/
COPY . .
CMD ["python3", "apps/main.py", "1 1 1 1"]
# Строка идет внутри 1 параметра