import json

pdFile = open('projectDescriptions.json',encoding="utf-8")
descriptions = json.load(pdFile)

projectMeta = open('zooniverse-for-metabase-20_projects.json', encoding="utf-8")
metaData = json.load(projectMeta)

projects = []
found = False
i = 0




for desc in descriptions:               #Toledo Zoo Wild Shots not included in Meta
    found = False
    for meta in metaData:
        if desc['ProjectName'] == meta['project_name']:
            project = {
                'project_name': desc['ProjectName'],
                'count_research_areas': meta['Number_of_Research_Areas'],
                'resarch_areas': meta['research_areas'],
                'about': desc['About'],
            }
            projects.append(project)
            found = True
            break

with open('mergedProjectDescription.json', 'w') as outfile:
    json.dump(projects, outfile)

