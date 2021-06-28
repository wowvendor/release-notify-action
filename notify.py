import os
import re
from slack_sdk import WebClient
from jira import JIRA, JIRAError

JIRA_TASK_REGEX = re.compile(r'[A-Z]+-\d+')


def notify():
    jira_login = os.getenv('INPUT_JIRA_LOGIN')
    jira_api_key = os.getenv('INPUT_JIRA_API_KEY')
    jira_org = os.getenv('INPUT_JIRA_ORG')
    github_commit_message = os.getenv('INPUT_COMMIT_MESSAGE')
    slack_token = os.getenv('INPUT_SLACK_TOKEN')
    slack_channel = os.getenv('INPUT_SLACK_CHANNEL')

    github_server_url = os.getenv('GITHUB_SERVER_URL')
    github_repository = os.getenv('GITHUB_REPOSITORY')
    github_sha = os.getenv('GITHUB_SHA')
    github_workflow = os.getenv('GITHUB_WORKFLOW')

    jira_found_task = True

    payload = {
        "channel": slack_channel,
        "attachments": [
            {
                "mrkdwn_in": ["text"],
                "color": "good",
                "pretext": "Release",
                # "author_name": issue.fields.assignee.displayName,
                # "author_icon": getattr(issue.fields.assignee.avatarUrls, '32x32'),
                "fields": [
                    {
                        "title": "Actions URL",
                        "value":
                            f"<{github_server_url}/{github_repository}/commit/{github_sha}/checks|{github_workflow}>",
                        "short": True,
                    },
                    {
                        "title": "Commit",
                        "value": f"<{github_server_url}/{github_repository}/commit/{github_sha}|{github_sha[:6]}>",
                        "short": True,
                    },
                ],
                "footer": "from Wowvendor Team with 🫀"
            }
        ]
    }

    slack = WebClient(token=slack_token)

    print(f'commit message:\n{github_commit_message}')
    try:
        jira_task = JIRA_TASK_REGEX.findall(github_commit_message)
        print(f'jira_task: {jira_task}')
        if not jira_task:
            raise JIRAError
        else:
            jira_task = jira_task[0]

        jira = JIRA(f'https://{jira_org}.atlassian.net', basic_auth=(jira_login, jira_api_key))
        issue = jira.issue(jira_task, fields='summary,assignee')

        payload['attachments'][0]['author_name'] = issue.fields.assignee.displayName
        payload['attachments'][0]['author_icon'] = getattr(issue.fields.assignee.avatarUrls, '32x32')
        payload['attachments'][0]['fields'].append({
            "title": issue.fields.summary,
            "value": f'https://wowvendor.atlassian.net/browse/{jira_task}',
            "short": False
        })
    except JIRAError:
        payload['attachments'][0]['fields'].append({
            "title": "Message",
            "value": github_commit_message,
            "short": False
        })

    slack.chat_postMessage(**payload)


if __name__ == '__main__':
    notify()
