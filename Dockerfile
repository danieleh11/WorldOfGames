FROM python
RUN pip install forex_python flask
RUN python -m pip install --upgrade pip setuptools wheel


Copy CurrencyRouletteGame.py /CurrencyRouletteGame.py
Copy e2e.py /e2e.py
Copy GuessGame.py /GuessGame.py
Copy index.html /index.html
Copy Live.py /Live.py
Copy MainGame.py /MainGame.py
Copy MainScores.py /MainScores.py
Copy MemoryGame.py /MemoryGame.py
Copy Score.py /Score.py
Copy Scores.txt /Scores.txt
Copy Utils.py /Utils.py


CMD python  MainGame.py
