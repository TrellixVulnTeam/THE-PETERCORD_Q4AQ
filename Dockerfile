FROM sandy1709/catuserbot:latest

RUN git clone https://github.com/IlhamMansiez/THE-PETERCORD /root/userbot
#working directory 
WORKDIR /root/userbot

# Install requirements
RUN pip3 install -U -r requirements.txt

ENV PATH="/home/userbot/bin:$PATH"

CMD ["python3","-m","userbot"]
