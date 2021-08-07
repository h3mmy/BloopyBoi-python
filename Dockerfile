FROM gorialis/discord.py:alpine-full

ENV OCI_LINK=https://download.oracle.com/otn_software/linux/instantclient/1912000/instantclient-basic-linux.x64-19.12.0.0.0dbru.zip
ENV OCI_CKSUM=301017800

# Install Instantclient Basic Light Oracle and Dependencies
RUN apk --no-cache add libaio libnsl libc6-compat curl && \
cd /tmp && \
curl -o instantclient-basic.zip ${OCI_LINK} -SL && \
if [${$(cksum instantclient-basic.zip)::0:9} == ${OCI_CKSUM}] \
unzip instantclient-basic.zip && \
mv instantclient*/ /usr/lib/instantclient && \
rm instantclient-basic.zip && \
chmod +x symlink_oci.sh \
./symlink_oci.sh \
fi

WORKDIR /app

COPY requirements.txt ./
RUN pip3 install -r requirements.txt

COPY . .

# CMD ["python", "bot.py"]