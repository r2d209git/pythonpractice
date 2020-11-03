from jira import JIRA

jira = JIRA(basic_auth=('r2d209', 'api_token'), options={"server": 'jira.skbroadband.com'})

#create an issue
test_case_data = {
    "project": {"id" : "project_name"}
    "summary": "test_summary",
    "description": "test_description",
    "issuetype": {"name": "Test"}
}

jira.create_issue(fields=test_case_data)

#update an issue
test_case_updatedata = {
    "summary": "test_summary_update",
    "description": "test_description_update",
    "labels": ['label_1_update'],
    "name": "new_user_name"
}

issue = jira.issue("issue_key")
issue.update(fields=test_case_updatedata)

#delete an issue
issue2 = jira.issue("issue_key")
issue2.delete()
