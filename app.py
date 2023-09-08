from github import Github
import jdatetime
import os
import schedule
import time

ACCESS_TOKEN = os.environ['ACCESS_TOKEN']
REPO_NAME = os.environ['REPO_NAME']
FILE_NAME = os.environ['FILE_NAME']
SCHEDULE = os.environ['SCHEDULE']

print(f"ACCESS_TOKEN, {ACCESS_TOKEN}!")
print(f"REPO_NAME, {REPO_NAME}!")
print(f"FILE_NAME, {FILE_NAME}!")
print(f"SCHEDULE, {SCHEDULE}!")

g = Github(ACCESS_TOKEN)
repo = g.get_user().get_repo(REPO_NAME)

def commit_to_github():
    jtoday = jdatetime.date.today()
    jstr_today = jtoday.strftime('%Y/%m/%d')

    today = jtoday.togregorian().strftime('%Y-%m-%d')
    file_content = f"Today's date in Jalali calendar: {jstr_today} Today's date in Gregorian calendar: {today}\n # Auto commit\nThis project updates its GitHub repository README.md on a daily basis using Docker and Python.\n\n## Usage\n\nDefine the following environment variable to configure project.\n\nVariable | Description | Optional\n-------- | ----------- | --------\nFILE_NAME | The file you want to edit  | no\nACCESS_TOKEN | Your github access token | no\nREPO_NAME | Repository name | no\nSCHEDULE | Execution time | 07:00  \n\n## Note\n\nFor the ACCESS_TOKEN, make sure to set the options for **Codespaces** and **Contents** to **Read and write**.\n\n## Docker hub\n\nMy Docker at Docker Hub: [jepbura/auto-commit](https://hub.docker.com/r/jepbura/auto-commit/)\n"

    try:
        contents = repo.get_contents(FILE_NAME)
        if file_content in contents.decoded_content.decode('utf-8'):
            print(f"File has already been updated on {today}")
            return

        repo.update_file(contents.path, f"Update {FILE_NAME}", file_content, contents.sha)
        print(f"New date {jstr_today} has been added to the {FILE_NAME} in {REPO_NAME} repo.")
    except:
        repo.create_file(FILE_NAME, f"Add {FILE_NAME}", file_content)
        print(f"New file {FILE_NAME} with date {jstr_today} has been added to the {REPO_NAME} repo.")


def job():
    commit_to_github()

schedule.every().day.at(SCHEDULE).do(job)

while True:
    schedule.run_pending()
    time.sleep(1)