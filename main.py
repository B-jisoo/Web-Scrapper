from alba import extract_alba_jobs
from save import save_to_file

alba_brand = extract_alba_jobs()

save_to_file(alba_brand)

