#   구현 못 한 것
#   브랜드 안에 데이터를 1페이지가 아닌 뒷페이지까지 읽어와야함 

# 예외처리를 사용해서 코드 작성해보기

from alba import extract_alba_jobs
from save import save_to_file

alba_brand = extract_alba_jobs()

save_to_file(alba_brand)

