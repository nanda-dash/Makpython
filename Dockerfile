FROM python:3.10

RUN pip install jupyter numpy scipy matplotlib pandas pypdf openpyxl

CMD ["jupyter", "notebook", "--ip=0.0.0.0", "--allow-root"]
