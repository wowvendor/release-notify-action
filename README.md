Release notify action
===
[![Test](https://github.com/wowvendor/release-notify-action/actions/workflows/test.yml/badge.svg)](https://github.com/wowvendor/url-checker-action/actions/workflows/test.yml)

This action check urls.

## Inputs

### `jira_login`
**Required**

### `jira_api_key`
**Required**

### `jira_org`
**Required** Jira organization - `https://{{ jira_org }}.atlassian.net`

### `jira_task`
**Required** Jira task code

### `slack_token`
**Required**

### `slack_channel`
**Required**

### `debug`
**Default** False

## Example usage

```
uses: wowvendor/release-notify-action@v1
with:
  jira_login: user
  jira_api_key: key
  jira_org: org
  jira_task: jira-task-id
  slack_token: slack-token
  slack_channel: channel-id
```
