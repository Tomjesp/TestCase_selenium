from selenium.webdriver.common.by import By
url="http://192.168.111.128/bsams/front/login.do?"
#ID
login_Id=By.ID,"taskId"
#用户名
login_username=By.ID,"loginName"
#密码
login_pwd=By.ID,"password"
#验证码
login_verity_code=By.ID,"vericode"
#登录按钮
login_btn=By.XPATH,"/html/body/div[1]/div[2]/form/div[2]/div[6]/input"
#brand_btn
brand_btn=By.ID,"leftmenu_asset_brand"
#Add_btn
add_btn=By.XPATH,"/html/body/div[2]/div/div[2]/div[2]/div[1]/div/input"
#brand_name
brand_name=By.ID,"title"
#brand_code
brand_code=By.ID,"code"
#brand_add_preservation
brand_add_preservation=By.LINK_TEXT,"保存"

