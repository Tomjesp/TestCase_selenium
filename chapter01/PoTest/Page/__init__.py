from selenium.webdriver.common.by import By
#testUrl
url="http://192.168.111.128/bsams/front/login.do?"
#ID
login_Id=By.ID,"taskId"
#username
login_username=By.ID,"loginName"
#password
login_pwd=By.ID,"password"
#vericode
login_vericode=By.ID,"vericode"
#login_botton
login_btn=By.XPATH,"/html/body/div[1]/div[2]/form/div[2]/div[6]/input"
#brand_btn
brand_btn=By.ID,"leftmenu_asset_brand"
#Add_btn
add_btn=By.CLASS_NAME,"add_submit"
#brand_name
brand_name=By.ID,"title"
#brand_code
brand_code=By.ID,"code"
#brand_add_preservation
brand_add_preservation=By.XPATH,"/html/body/div[6]/div[1]/div[2]/div[2]/div[1]/div/div[3]/a[2]"

