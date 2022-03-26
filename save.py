import csv


def save_to_file(jobs):
  file = open("jobs.csv", mode="w", encoding = "utf-8-sig", newline='')
  writer =csv.writer(file)
  writer.writerow(["location" , "company", "title","workingtime", "pay", "regdate", "link"])
  for job in jobs:
    writer.writerow(list(job.values()))
  return

