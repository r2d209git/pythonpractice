"""
reference : https://jira.readthedocs.io/en/master/examples.html
"""

from jira import JIRA
from collections import Counter

try:
    assignee = "yk1.bae"
    jira = JIRA(auth=(assignee, 'kimsujin1!'), options={"server": 'https://jira.skbroadband.com'})

    issues = jira.search_issues(f"assignee={assignee}")
    top_ten = Counter([issue.fields.project.key for issue in issues]).most_common(
        10)  # assignee에 assign된 이슈에 대해 동일 project key 값인 issue들의 counter 묶음 표시를 tuple 형태로 제공

    print("{0} assigned these issues.".format(assignee))
    print("%s assigned these issues." % assignee)
    print(top_ten)
    while top_ten:
        item = top_ten.pop()
        prj_name = item[0]
        issue_count = item[1]
        print("Project name : {name}, Assigned Count : {count}".format(name=prj_name, count=issue_count))

        #project 상세 정보 표출
        if prj_name == "BTVD":
            prj = jira.project(prj_name)
            print("=" * 30)
            print("Project name : %s" %prj.name)
            print("Project leader name : %s" %prj.lead.displayName)
            components = jira.project_components(prj)
            print("Components : " + str([c.name for c in components]))
            print("Roles : " + str(jira.project_roles(prj)))
            versions = jira.project_versions(prj)
            print("Versions : " + str([v.name for v in reversed(versions)]))
            print("=" * 30)
        else:
            continue

    break_loop = False
    for issue in issues:
        print("Issue summary : " + issue.fields.summary)
        watcher = jira.watchers(issue)
        if watcher.watchCount > 1:
            print("Issue has {} watchers(s)".format(watcher.watchCount))
            for watcher in watcher.watchers:
                print(watcher)
                print(watcher.emailAddress)
                break_loop = True
        elif break_loop:
            break
        else:
            pass


except Exception as e:
    print(e)
