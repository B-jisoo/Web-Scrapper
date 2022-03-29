import requests
from bs4 import BeautifulSoup

ALBA_URL = "http://www.alba.co.kr/"

def extract_dic(html, link):


    local = html.find("td", class_="local")
    brand_table_company = html.find("span", class_="company")
    brand_table_title = html.find("span", class_="title")
    brand_table_workingtime = html.find("td", class_="data")
    brand_table_pay = html.find("td", class_="pay")
    brand_table_regdate_last = html.find("td", class_="regDate last")
    brand_table_link =html.find("td", class_="title")
    

    if local is not None:
      return {
        'local':local.text.replace('\xa0',' '),
        'company':brand_table_company.text,
        'title':brand_table_title.text,
        'workingtime':brand_table_workingtime.text,
        'pay':brand_table_pay.text.replace(',',''),
        'regdate_last':brand_table_regdate_last.text,
        'link': str(link) + str(brand_table_link.find("a")["href"])
      }
    


def extract_array(html): 
  brand_jobs =[]

  alba_company_link = html.find("a")["href"]                      # a인 요소의 href(배열)를 찾아 alba_company_link에 넣음  a요소에 href 정보가 있기때문에 가능

  brand_info = requests.get(alba_company_link)
  brand_soup = BeautifulSoup(brand_info.text, "html.parser") 
  brand_table = brand_soup.find("tbody")
  brand_table_info = brand_table.find_all("tr")
 
  for td in brand_table_info:
    if extract_dic(td, alba_company_link) is not None:
      job = extract_dic(td, alba_company_link)
      brand_jobs.append(job)

  return brand_jobs
             

def extract_alba_jobs(): # 알바천국 링크와 브랜드 이름
  jobs = []
  alba_result = requests.get(ALBA_URL)                              #requests.get 으로 ALBA_URL에 있는 데이터 싹다 긁어옴
  alba_soup = BeautifulSoup(alba_result.text, "html.parser")        #BeautifulSoup으로 html를 가져온다
  superbrand = alba_soup.find("div", {"id":"MainSuperBrand"})       #superbrand에 div고 id가 MainSuperBrand인 요소를 넣음
  alba_brand = superbrand.find("ul", {"class":"goodsBox"})          #alba_brand에다가 superbrand에서 ul이고 class가 goodsBox인 요소를 넣음
  
  alba_company_info = alba_brand.find_all("li", class_="impact")                     #alba_company_info에다가 alba_brand에서 li요소를 "다(all)" 찾음

  for brand in alba_company_info:                              #brand는 변수고 alba_company_info는 걸러진 요소
    jobs.extend(extract_array(brand))
    

  return jobs
