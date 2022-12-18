
FROM public.ecr.aws/lambda/python:3.8


# Install chrome dependecies
RUN yum install unzip atk at-spi2-atk gtk3 cups-libs pango libdrm \ 
    libXcomposite libXcursor libXdamage libXext libXtst libXt \
    libXrandr libXScrnSaver alsa-lib -y
RUN yum install wget -y
RUN yum install tar -y

# Copy install scripts
COPY requirements.txt /tmp/
COPY install-chrome.sh /tmp/
COPY install-ffmpeg.sh /tmp/
COPY ffmpeg/ffmpeg ffmpeg/ffprobe /usr/local/bin/



# Install chromium, chrome-driver
RUN /usr/bin/bash /tmp/install-chrome.sh

# Install Python dependencies for function
RUN pip install --upgrade pip -q

# Remove unused packages
RUN yum remove unzip -y
RUN pip install --target "${LAMBDA_TASK_ROOT}" awslambdaric


COPY . ${LAMBDA_TASK_ROOT}
RUN  pip3 install -r requirements.txt --target "${LAMBDA_TASK_ROOT}"

ENTRYPOINT [ "python3", "-m", "awslambdaric" ]
CMD [ "app.handler" ]