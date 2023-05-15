from github import Github
import jdatetime
import os

ACCESS_TOKEN = os.environ['ACCESS_TOKEN']
REPO_NAME = os.environ['REPO_NAME']
README_FILE_NAME = os.environ['README_FILE_NAME']

g = Github(ACCESS_TOKEN)
repo = g.get_user().get_repo(REPO_NAME)

def commit_to_github():
    jtoday = jdatetime.date.today()
    jstr_today = jtoday.strftime('%Y/%m/%d')

    today = jtoday.togregorian().strftime('%Y-%m-%d')
    file_content = f"Today's date in Jalali calendar: {jstr_today} Today's date in Gregorian calendar: {today}"

    try:
        contents = repo.get_contents(README_FILE_NAME)
        if file_content in contents.decoded_content.decode('utf-8'):
            print(f"File has already been updated on {today}")
            return

        repo.update_file(contents.path, f"Update {README_FILE_NAME}", file_content, contents.sha)
        print(f"New date {jstr_today} has been added to the {README_FILE_NAME} in {REPO_NAME} repo.")
    except:
        repo.create_file(README_FILE_NAME, f"Add {README_FILE_NAME}", file_content)
        print(f"New file {README_FILE_NAME} with date {jstr_today} has been added to the {REPO_NAME} repo.")

commit_to_github()
