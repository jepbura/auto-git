Today's date in Jalali calendar: 1403/07/04 Today's date in Gregorian calendar: 2024-09-25
 # Auto commit
This project updates its GitHub repository README.md on a daily basis using Docker and Python.

## Usage

Define the following environment variable to configure project.

Variable | Description | Optional
-------- | ----------- | --------
FILE_NAME | The file you want to edit  | no
ACCESS_TOKEN | Your github access token | no
REPO_NAME | Repository name | no
SCHEDULE | Execution time | 07:00  

## Note

For the ACCESS_TOKEN, make sure to set the options for **Codespaces** and **Contents** to **Read and write**.

## Docker hub

My Docker at Docker Hub: [jepbura/auto-commit](https://hub.docker.com/r/jepbura/auto-commit/)
