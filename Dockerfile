FROM python:3.6

ADD mail_sender.py /

# RUN pip install pystrich
RUN pip3 freeze > requirements.txt
RUN pip3 install -r requirements.txt

CMD [ "python3", "./mail_sender.py" ]