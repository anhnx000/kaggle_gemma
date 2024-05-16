FROM continuumio/anaconda3:4.4.0
COPY . /usr/app/
EXPOSE 5000
WORKDIR /usr/app/
RUN pip install --upgrade pip
RUN pip uninstall -y numpy
RUN pip install numpy
RUN pip install scikit-learn==0.22.1
RUN pip install --ignore-installed -r requirements_test.txt
CMD python flask_test.py
