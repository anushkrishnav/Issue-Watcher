
# action will be run in python3 container
FROM python:3
# copying requirements.txt and install the action dependencies
COPY requirements.txt /requirements.txt
RUN pip install -r /requirements.txt
# main.py is the file that will contain the codes that we want to run for this action.
COPY src/main.py /src/main.py
# we will just run our main.py as our docker entrypoint by python main.py
CMD ["python", "/src/main.py"]