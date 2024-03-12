# ⚙️ Importing Packages:
import base64
import streamlit as st
from streamlit_option_menu import option_menu
import streamlit .components .v1 as components #line:7
from PIL import Image
img = Image.open('fav.png')
# Import Selenium Packges
from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.keys import Keys
import selenium.webdriver.common.keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains
# Import Wwbdriver Packages
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
# Impot REGEX Packages
import re
# Impot Time Packages
import time
#from fake_useragent import UserAgent
import os
#import pandas as pd
#cwd = os.getcwd()










# Streamlit Codes:
########################### SSTREAMLIT - CSS ##################################


st.set_page_config(
    page_title="EmailDominator®",
    page_icon= img,
    layout = 'wide'

)


st.markdown("""
<style>
           .block-container.st-emotion-cache-z5fcl4.ea3mdgi4 {
                margin-top: -47px;
            }
            .st-emotion-cache-1v0mbdj.e115fcil1 {
                    width: 234px !important;
                    height: 80px !important;
                    margin-top: -44px;
                    margin-bottom: -44px;
                    
            }


            button.st-emotion-cache-1m4dglj.ef3psqc8 {
                border-radius: 50px;
            }

            button.st-emotion-cache-1m4dglj.ef3psqc13 {
                border-radius: 50px;
            }

            header {
                visibility: hidden;
            }

           

            footer {
                visibility: hidden;
            }

            ul.css-lrlib.e1akgbir9 {
                margin-top: -100px;
            }
            .eqr7zpz0 {font-size: 20px; }
            .css-12ttj6m.en8akda1 { margin-top: -15px;}
            hr { margin: 0 !important;}
            .css-16idsys p {
            word-break: break-word;
            margin-bottom: 0px;
            font-size: 15px;
            font-weight: bold;
            color: #626262;
             }

            .css-1v0mbdj.ebxwdo61 {
                width: 169px;
                margin-top: -66px;  }

            .mb-auto {
                margin-bottom: auto!important;
                font-family: monospace;
                font-size: 17px;
            }

            p {
                font-weight: bold;
            }

            a.nav-link{
                font-size: 15px !important;;
            }

    audio {
    visibility: hidden;
    }

    .css-1v0mbdj.ebxwdo61 {
            width: 227px;
            margin-top: -42px;
            margin-left: -3px;
            }




            .st-emotion-cache-10oheav {
                    padding: 2rem 1rem;
                }
            

            
            
                            

   .st-emotion-cache-12g66t4 a {
        color: rgb(46, 154, 255);
        display: inline-flex;
        -webkit-box-align: center;
        align-items: center;
        -webkit-box-pack: center;
        justify-content: center;
        font-weight: bold;
        padding: 0.25rem 0.75rem;
        border-radius: 50px;
        min-height: 38.4px;
        margin: 0px;
        text-decoration: none;
        line-height: 1.6;
        width: auto;
        user-select: none;
        background-color: rgb(252, 74, 26);
        color: rgb(255, 255, 255);
        border: 1px solid rgb(252, 74, 26);
}
            

    .css-x5ohxw {
    display: inline-flex;
    -webkit-box-align: center;
    align-items: center;
    -webkit-box-pack: center;
    justify-content: center;
    font-weight: 400;
    padding: 7px;
    border-radius: 50px;
    margin: 0px;
    line-height: 1.6;
    width: auto;
    user-select: none;
    background-color: rgb(252, 74, 26);
    color: rgb(255, 255, 255);
    border: 1px solid rgb(252, 74, 26);
}
            

            .css-12g66t4 a {
                color: white;
                background: #fc4a1b;
                text-decoration: none;
                padding: 10px;
                border-radius: 50px;
            }

.block-container.css-z5fcl4.e1g8pov64 {
    top: -67px;
}

</style>
""", unsafe_allow_html=True)





############### start st.sidebar ######################


image = Image.open('logo.png')

with st.sidebar:
    
    st.image(image)
    
    selected = option_menu(
        menu_title=None,
        options=["Welcome","Email Scraper", "Contact Us" ],
        icons= ["house","person-bounding-box","buildings"],
        #menu_icon="cast",
        #default_index=0,
        menu_icon="cast", default_index=0,


        
        styles={
            "container": {"font-family":"monospace","border-radius":"inherit", "background-color": "#000"},
            "icon": {"color": "white"}, 
            "nav-link": {"font-weight":"bold","font-family":"monospace","border-radius": "50px", "--hover-color": "#262730" , "font-size": "17px"},
            "nav-link-selected": {"font-weight":"bold","border-radius": "50px", "font-size": "17px"},
            
           
 
        }
    
    )

    




if selected == "Welcome":
        st.info(f"▶ You Have Selected [ ⌂ {selected} ]")
        st.write("With [ Email Dominator ], you can effortlessly create and design visually stunning emails, personalize content for individual recipients.")
        st.divider()
        
       

        st.markdown("▶ By : [ <span style='color:gray'>Adil Benmohamed</span>" + " ]",
             unsafe_allow_html=True)

        


        



        



if selected == "Email Scraper":


    st.info(f"▶ You Have Selected [ {selected} ]")
    with st.form("E_Scraper"):




        st.write("⚙ EMAIL SCRAPER DATA ↴")
        st.divider()
        col1,col2          = st.columns(2)
        targeted_site      = col1.text_input('Targeted_site : ',value='linkedin.com')
        targeted_esp       = col2.text_input('Targeted_esp :',value='gmail.com')
        geo_target         = st.text_input('Target_Business :',value='usa')


        # Upload Emails List text File
        uploaded_keywords_list_file = st.file_uploader("Choose Your Keywords List Data File To Get Scraping Emails :")
        
        if uploaded_keywords_list_file is not None:
            # Store file content as binary in "raw_bytes_text" object/variable
            raw_bytes_text = uploaded_keywords_list_file.read() #binary
            
            # Decode binary to string
            encoding = 'utf-8'
            list_text = raw_bytes_text.decode(encoding) #string
            uploaded_keywords_list = list_text.split('\n')

            # Get a list from uploaded_keywords_list_file
            # Cleaning up the list
            Keywords_List = [element.strip() for element in uploaded_keywords_list if element.strip()]
            
            

        submit          = st.form_submit_button('✉ Start Scraping Campaign...', type="primary")
        if submit:
            
            # Remove Content From Text Files
            with open('Extracted_Emails_List.txt', 'w') as file:
                file.truncate(0)

            with open('Search_Results_Links.txt', 'w') as file:
                file.truncate(0)

           

            with st.spinner('✉ Scraping Emails Proccess...'):

            #######################################################
            ######## start Email Scraper Functions Section ########
            #######################################################

                # Launch driver process
                # Launch Chrome driver instance:
                service = Service()
                options = webdriver.ChromeOptions()
                options.add_argument("--headless=new")
                driver = webdriver.Chrome(service=service, options=options)
                driver.implicitly_wait(30)
                driver.maximize_window()


                # Search_Process function
                def Search_Process():

                    
                    # Navigate To [ bing.com ]
                    driver.get("https://www.bing.com/")  

                    # Search_Query
                    time.sleep(5)
                    Search_Query = "site: " + targeted_site + ' "@' + targeted_esp + '" ' + keyword + " " + geo_target 
                    
                    #Search_Query =  target_business + " in " + city
                    time.sleep(5)
                    ### Type Phrase In Search Input & Click To Search Button
                    Bing_Search_Input_Xpath = "//input[@id='sb_form_q']"

                    # Input Element - Bing_Search_Input_Xpath
                    Bing_Search_Input_Xpath = driver.find_element(By.XPATH, Bing_Search_Input_Xpath)
                    Bing_Search_Input_Xpath.clear()
                    Bing_Search_Input_Xpath.send_keys(Search_Query)
                    # Click Button To Search
                    Bing_Click_Search_Button_Xpath = "//label[@id='search_icon']//*[name()='svg']"

                    # Click Element - Bing_Click_Search_Button_Xpath
                    Bing_Click_Search_Button_Xpath = driver.find_element(By.XPATH, Bing_Click_Search_Button_Xpath)
                    Bing_Click_Search_Button_Xpath.click()










                # Save_Extracted_Links_To_Text_File function
                def Scrape_And_Save_Extracted_Links_To_Text_File():


                    #-Function-Content-#
                    Search_Results_Links_Xpath = "//main//li/h2/a"

                    # Scrape Element Attribute Values List - Search_Results_Links_Xpath
                    elements_list = driver.find_elements(By.XPATH, Search_Results_Links_Xpath)
                    Search_Results_Links_Xpath_element_attribute_values_list = []
                    for element in elements_list:
                        element_attribute_value = element.get_attribute('href')
                        Search_Results_Links_Xpath_element_attribute_values_list.append(element_attribute_value)

                    # Save Scraped Links in a file.txt
                    # Save Search_Results_Links_Xpath_element_attribute_values_list to text file
                    text_file = open("Search_Results_Links.txt", "a")
                    for element in Search_Results_Links_Xpath_element_attribute_values_list:
                        text_file.write(element + "\n")
                    text_file.close()

                    # remove duplicate lines from Search_Results_Links.txt
                    unique_lines_list = set(open("Search_Results_Links.txt").readlines())
                    file_data_txt = open("Search_Results_Links.txt", 'w')
                    file_data_txt.writelines(set(unique_lines_list))
                    file_data_txt.close()






                # Scrape_Page_Emails function
                def Scrape_And_Save_Extracted_Emails_To_Text_File():

                    # Email Regex Code
                    email_regex = """(?:[a-z0-9!#$%&'*+/=?^_`{|}~-]+(?:\.[a-z0-9!#$%&'*+/=?^_`{|}~-]+-a-z0-9!#$%&+com/a-z0-9!#$%&+com.a-z0-9!#$%&+/a-z0-9!#$%&/+//+/+/@)*|"(?:[\x01-\x08\x0b\x0c\x0e-\x1f\x21\x23-\x5b\x5d-\x7f]|\\[\x01-\x09\x0b\x0c\x0e-\x7f])*")@(?:(?:[a-z0-9](?:[a-z0-9-]*[a-z0-9])?\.)+[a-z0-9](?:[a-z0-9-]*[a-z0-9])?|\[(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?|[a-z0-9-]*[a-z0-9]:(?:[\x01-\x08\x0b\x0c\x0e-\x1f\x21-\x5a\x53-\x7f]|\\[\x01-\x09\x0b\x0c\x0e-\x7f])+)\])"""
                    #             """(?:[a-z0-9!#$%&'*+/=?^_`{|}~-]+(?:\.[a-z0-9!#$%&'*+/=?^_`{|}~-]+)*|"(?:[\x01-\x08\x0b\x0c\x0e-\x1f\x21\x23-\x5b\x5d-\x7f]|\\[\x01-\x09\x0b\x0c\x0e-\x7f])*")@(?:(?:[a-z0-9](?:[a-z0-9-]*[a-z0-9])?\.)+[a-z0-9](?:[a-z0-9-]*[a-z0-9])?|\[(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?|[a-z0-9-]*[a-z0-9]:(?:[\x01-\x08\x0b\x0c\x0e-\x1f\x21-\x5a\x53-\x7f]|\\[\x01-\x09\x0b\x0c\x0e-\x7f])+)\])"""
                    # Scrape page text
                    page_text = driver.find_element(by=By.TAG_NAME, value='body').text
                    page_text = page_text.lower()

                    # Scrape element list with regex
                    Extracted_Emails_List = re.findall(email_regex, page_text)
                    # Save Extracted_Emails_List to text file
                    text_file = open("Extracted_Emails_List.txt", "a")
                    for element in Extracted_Emails_List:
                        text_file.write(element + "\n")
                    text_file.close()

                    # remove duplicate lines from Extracted_Emails_List.txt
                    unique_lines_list = set(open("Extracted_Emails_List.txt").readlines())
                    file_data_txt = open("Extracted_Emails_List.txt", 'w')
                    file_data_txt.writelines(set(unique_lines_list))
                    file_data_txt.close()






                    # One_Keywords_Scraping_Emails_And_Links_Process function
                def One_Keywords_Scraping_Emails_And_Links_Process():
                    # While [true] Loop
                    while True:

                        time.sleep(3)
                        # Next Page Element Detector Script - 0/1
                        # Find next_page_button_list Elements List
                        next_page_button_list_xpath = "//a[@title='Next page']"
                        next_page_button_list = driver.find_elements(By.XPATH, next_page_button_list_xpath)

                        # If Next Page Button Exist / Then Click To Next Button
                        # if next_page_button_list == 1
                        if (len(next_page_button_list)) == 1:

                            # Scroll To Elament On Page
                            Next_Page_Button_Xpath = "//a[@title='Next page']"
                            Next_Page_Button = driver.find_element(By.XPATH, Next_Page_Button_Xpath)
                            actions = ActionChains(driver)
                            actions.move_to_element(Next_Page_Button).perform()

                            # Scrape And Save Extracted Links To Text File
                            Scrape_And_Save_Extracted_Links_To_Text_File()
                            # Scrape And Save Extracted Emails To Text File
                            Scrape_And_Save_Extracted_Emails_To_Text_File()

                            # Click Element - Next_Page_Button_Xpath
                            Next_Page_Button_Xpath = "//a[@title='Next page']"
                            Next_Page_Button = driver.find_element(By.XPATH, Next_Page_Button_Xpath)
                            Next_Page_Button.click()
                            
                            

                        else:
                            
                            break 
                            


                def autoplay_audio_scraper(file_path: str):
                        with open(file_path, "rb") as f:
                            data = f.read()
                            b64 = base64.b64encode(data).decode()
                            md = f"""
                                <audio controls autoplay="true">
                                <source src="data:audio/mp3;base64,{b64}" type="audio/mp3">
                                </audio>
                                """
                            st.markdown(
                                md,
                                unsafe_allow_html=True,
                            )







                #######################################################
                ######## End Email Scraper Functions Section ##########
                #######################################################

                # Loop from Keywords_List
                Extracted_Emails_List = []
                for element in Keywords_List:
                    keyword = element
                    #st.write(f"▶ The Curent keyword Is :   :green[{element}]")
                    st.markdown(f"▶ The Curent keyword Is : [ <span style='color:gray'>{element}</span>" + " ]",
                        unsafe_allow_html=True)
                    try:
                        Search_Process()
                        One_Keywords_Scraping_Emails_And_Links_Process()
                        
                    except:
                        st.error("Process Error...")
                        driver.quit()    



                # Emails Scraping ] Mission Is Complete...
                
                st.success("[ Emails Scraping ] Mission Is Complete...")
                
                driver.quit()



                def get_binary_file_downloader_html(bin_file, file_label='File'):
                    with open(bin_file, 'rb') as f:
                        data = f.read()
                        bin_str = base64.b64encode(data).decode()
                        href = f'<a href="data:file/txt;base64,{bin_str}" download="{bin_file}">{file_label}</a>'
                        return href

                # Provide download button for Extracted_Emails_List.txt
                st.write("▶ Download Extracted Emails List ↴")
                st.divider()
                st.markdown(get_binary_file_downloader_html("Extracted_Emails_List.txt", '▼ Download Extracted Emails Now ▼'), unsafe_allow_html=True)

                autoplay_audio_scraper("noti.mp3")

                





if selected == "Contact Us":

        st.info(f"▶ You Have Selected [ ✉ {selected} ]")
        st.error("This App Powred By [ Adil Harouiya ] ")


















































footer="""<style>

.footer {
position: fixed;
left: 0;
bottom: 0;
width: 100%;
background-color: #262730;
color: white;
text-align: center;
}
</style>
<div class="footer">
<p style="margin: auto;padding-left: 352px;font-weight: lighter;font-size: 15px;">Copyright © 2023-2024 EmailDominator®</p>
</div>
"""
st.markdown(footer,unsafe_allow_html=True)







































