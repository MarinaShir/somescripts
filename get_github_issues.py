from github import Github
import datetime

# here you need to use your token for authorisation 
TOKEN = ''
g = Github(TOKEN)

repo_name = ''
repo = g.get_repo(repo_name)

# counting how many labels we have in our repo
#labels = repo.get_labels()
#print(labels.totalCount)

# get the number of open issues with specific label, if you need to use several lalels use a list: labels = ['label1', 'label2']
#open_issues = repo.get_issues(state = 'open', labels = ['my_label'])
#print(open_issues.totalCount)

# get number of open issues since some day - variable first_day
# format for datetime is (year, month, day)
#first_day = datetime.datetime(2022, 5, 16)
#open_issues = repo.get_issues(state = 'open', labels = ['my_label'], since = first_day)
#print(open_issues.totalCount)

#here I'm calculating some stats aka historical number of open issues etc. important attributes of issus are: created_at, closed_at, updated_at - all datetime type
#all_mondays = [[1,3], [1, 10], [1, 17], [1, 24], [1, 31]]
#for each_week in all_mondays:
#    count = 0
#    last_day = datetime.datetime(2022, each_week[0], each_week[1])
#    issues = repo.get_issues(state='all', labels = ['my_label'])
#    for issue in issues:
#        if issue.state == 'open' and issue.created_at < last_day:
#            count = count + 1
#        if issue.state == 'close' and issue.created_at < last_dat and issue_closed_at > last_day:
#            count = count + 1
#    print (count)

all_issues = repo.get_issues(state='all')
print(all_issues.totalCount)
