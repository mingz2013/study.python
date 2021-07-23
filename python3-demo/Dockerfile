FROM python
RUN adduser app
WORKDIR /home/app
COPY r.txt r.txt
RUN python -m venv venv
RUN venv/bin/pip install -r r.txt
COPY app app
COPY boot.sh main.py ./
RUN chmod +x boot.sh
RUN chown -R app:app ./
USER app
RUN mkdir logs
ENTRYPOINT ["./boot.sh"]
