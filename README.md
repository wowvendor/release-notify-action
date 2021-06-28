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

### `commit_message`
**Required** Commit message

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
  commit_message: ${{ github.event.head_commit.message }}
  slack_token: slack-token
  slack_channel: channel-id
```
