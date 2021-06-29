import os
import logging
from slack_sdk import WebClient
from jira import JIRA

logger = logging.getLogger(__name__)


def notify():
    jira_login = os.getenv('INPUT_JIRA_LOGIN')
    jira_api_key = os.getenv('INPUT_JIRA_API_KEY')
    jira_org = os.getenv('INPUT_JIRA_ORG')
    jira_task = os.getenv('INPUT_JIRA_TASK')
    slack_token = os.getenv('INPUT_SLACK_TOKEN')
    slack_channel = os.getenv('INPUT_SLACK_CHANNEL')
    debug = os.getenv('INPUT_DEBUG')

    if debug:
        print(f"jira_login: {jira_login}\njira_api_key: {jira_api_key}\njira_org: {jira_org}\njira_task: {jira_task}\nslack_token: {slack_token}\nslack_channel: {slack_channel}")

    slack = WebClient(token=slack_token)

    options = {
        'server': f'https://{jira_org}.atlassian.net'
    }

    jira = JIRA(options, basic_auth=(jira_login, jira_api_key))
    issue = jira.issue(jira_task, fields='summary,assignee')
    jira.transition_issue(issue, 'Deploy')

    payload = {
        "channel": slack_channel,
        "attachments": [
            {
                "mrkdwn_in": ["text"],
                "color": "#b79654",
                "pretext": "Release",
                "author_name": issue.fields.assignee.displayName,
                "author_icon": getattr(issue.fields.assignee.avatarUrls, '32x32'),
                "fields": [
                    {
                        "title": issue.fields.summary,
                        "value": f'https://wowvendor.atlassian.net/browse/{jira_task}',
                        "short": False
                    }
                ],
                "footer": "from Wowvendor Team with 🫀"
            }
        ]
    }
    slack.chat_postMessage(**payload)


if __name__ == '__main__':
    notify()
