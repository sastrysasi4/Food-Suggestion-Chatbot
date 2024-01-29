# required packages
from dotenv import load_dotenv
load_dotenv()
import google.generativeai as genai
import os
import streamlit as st
import time

# Configure Google API Key
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
genai.configure(api_key=GOOGLE_API_KEY)


# Set up the model
generation_config = {
    "temperature": 0.4,
    "top_p": 1,
    "top_k": 32,
    "max_output_tokens": 4096,
}
safety_settings = [
    {"category": "HARM_CATEGORY_HARASSMENT", "threshold": "BLOCK_MEDIUM_AND_ABOVE"},
    {"category": "HARM_CATEGORY_HATE_SPEECH", "threshold": "BLOCK_MEDIUM_AND_ABOVE"},
    {
        "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
        "threshold": "BLOCK_MEDIUM_AND_ABOVE",
    },
    {
        "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
        "threshold": "BLOCK_MEDIUM_AND_ABOVE",
    },
]
model = genai.GenerativeModel(
    model_name="gemini-pro",
    generation_config=generation_config,
    safety_settings=safety_settings,
)


# Prompt
input_prompt = """
Food Suggestion Assistance

You are a food suggestion assistant. Given a menu, you can help by finding the perfect dish for any occasion. If the requested dish is not on the menu, respond with "We don't have your type of food.

MENU:

VEG APPETIZERS:

PAKORAS ONION / SPINACH -
    Delicately spiced (Onion or Spinach or Both) fritters dipped in batter and fried.
VEGETABLE SAMOSA -
    Two crisp patties stuffed with potatoes and green peas.
CHILI PANEER - 
    Homemade cheese, chilies and onions sautéed and cooked with spicy curry.
GOBI MANCHURIAN -
    Cauliflower battered & cooked with manchurian sauce.
PANEER 555 -
    Fried homemade cheese cubes tossed in spicy & herbed masala.
MIRCHI BAJJI (6PC) -
    Mirchi or Chili is stuffed with a tangy spice mix & dipped in besan batter and fried.
CUT MIRCHI -
    Cut chili pakoras garnished with spiced onions.

    
NON VEG APPETIZERS:

CHICKEN MANCHURIAN -
    Boneless chicken cooked with manchurian sauce.
CHICKEN 65 -
    Boneless chicken cubes marinated with Indian spices and deep fried.
CHILI CHICKEN -
    Boneless chicken, chilies and onions sautéed and cooked with spicy curry
FISH PAKODA -
    Curry leaf, crushed chili & yogurt sauce.
APOLLO FISH -
    Curry leaf, crushed chili & yogurt sauce.
CHILI SHRIMP -
    Shrimp corn battered and deep fried, mixed with stir fried spring onions capsicum soy sauce and sweet red chili peppers.

    
SOUTH INDIAN SPECIALTIES:

IDLY SAMBAR 4PC -
    Steam cooked Rice cakes served with sambar.
DOSA (PLAIN/ONION/MASALA) -
    Crepe made with fermented lentil and rice flour.
MYSORE MASALA DOSA -
    Dosa with spicy sauce and stuffed with potatoes.
ANDHRA KARA DOSA -
    Dosa coated with specially made Andhra chili and spice paste.
RAVA DOSA (PLAIN/MASALA) -
    Crepe made with and rice flour and semolina (plain or with onion&chillies or with potato masala).
RUCHI SOUTH INDIAN COMBO -
    Masala dosa with 2 idly and sambar.


VEGETARIAN ENTREES:

ALOO GOBI -
    Potatoes and cauliflower cooked with special spices.
DAL FRY -
    Lentils cooked with spices.
KADAI PANEER -
    Homemade cheese cubes cooked with tomatoes, onions and bell peppers.
PANEER BUTTER MASALA -
    Homemade cheese cubes cooked with creamy tomato and butter sauce.
PALAK PANEER -
    Creamy Spinach with Indian spices.
MALAI KOFTA -
    Vegetables and cheese dumplings cooked in mildly spiced sauce.
NAVARATAN KURMA -
    Mixed vegetables in mildly spiced sauce with dry fruits and nuts.
CHANA MASALA -
    Garbanzo beans cooked with Indian spices.

    
NON-VEG ENTREES:

EGG MASALA -
    Eggs cooked with spices.
CHICKEN TIKKA MASALA -
    Boneless chicken tikka cooked in a spicy sauce.
CHICKEN CHETTINADU -
    Boneless chicken cooked with south Indian spices.
CHICKEN MAKHANI -
    Boneless chicken cooked in butter sauce with mild spices.
KADAI CHICKEN -
    Boneless chicken cooked with tomatoes & onions.
CHICKEN VINDALOO -
    Boneless chicken cooked with south Indian spices.
CHICKEN CURRY -
    Boneless chicken cooked with Indian spices.
CHICKEN SAAG -
    hicken cooked in saag sauce.
LAMB/GOAT CURRY -
    Boneless Lamb/Goat cooked in curry sauce.
LAMB/GOAT SAAG -
    Boneless lamb/goat bone in goat cooked in curry sauce.
LAMB VINDALOO -
    Boneless lamb & potatoes cooked in hot & spicy sauce.
CHETTINADU GOAT -
    Boneless lamb cooked with south Indian spices.
LAMB ROGANJOSH -
    Boneless lamb cooked with onions, ginger, garlic, tumeric, tomato, & yogurt sauce in butter sauce with mild spices.
FISH MASALA -
    Fish curry cooked with Indian spices.
SHRIMP MASALA -
    Shrimp curry cooked with Indian spices.


TANDOORI SPECIALTIES:

TANDOORI CHICKEN -
    Half a chicken marinated in yogurt with special herbs and spices.
TANDOORI CHICKEN TIKKA -
    Boneless chicken marinated in yogurt with herbs and spices.
TANDOORI SHRIMP -
    Jumbo shrimp cooked on skewers.
TANDOORI MIXED GRILL -
    A combination of all the above tandoori dishes.

    
BIRYANI SPECIALTIES:

VEGETABLE BIRYANI - 
    Mixed vegetables cooked with basmati rice in mild spices and herbs.
PANEER BIRYANI -
    Paneer cooked with basmati rice in mild spices and herbs.
EGG BIRYANI -
    Whole egg cooked with basmati rice in mild spices and herbs.
CHICKEN DUM BIRYANI -
    Chicken cooked with basmati rice in Hyderabadi style.
ULAVACHARU CHICKEN DUM BIRYANI -
    Chicken marinated in Ulavacharu and cooked with rice and herbs.
VIJAYAWADA CHICKEN DUM BIRYANI -
    Chicken cooked with basmati rice in Vijayawada style.
GONGURA CHICKEN BIRYANI -
    Chicken marinated in gongura sauce and cooked with rice and herbs.
LAMB/GOAT BIRYANI -
    Lamb/Goat cooked with basmati rice in mild spices and herbs.
ULAVACHARU GOAT BIRYANI -
    Goat marinated in Ulavacharu and cooked with rice and herbs.
GONGURA GOAT BIRYANI -
    Goat marinated in gongura sauce and cooked with rice and herbs.
SHRIMP BIRYANI -
    Shrimp cooked with basmati rice in mild spices and herbs.


SIDE ORDERS & BREAD:

NAAN -
    Indian bread made with all purpose flour baked in clay oven.
GARLIC NAAN -
    Naan stuffed with garlic.
CHEESE NAAN -
    Naan stuffed with cheese.
ONION KULCHA -
    Naan stuffed with onions.
ROTI -
    Whole-wheat Indian bread baked in clay oven.

    
DESSERTS & DRINKS:

GULAB JAMUN -
    Indian milk cheese balls fried and soaked in honey syrup.
MANGO LASSI -
    Homemade yogurt flavored with mango, a delightful drink.
"""



# Streamlit
st.set_page_config(

   layout="wide",
)

st.title("Food Suggestion Assistance")
# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []


# Display chat messages from history on app rerun
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Accept user input
if prompt := st.chat_input("How can I help you?"):
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})
    # Display user message in chat message container
    with st.chat_message("user"):
        st.markdown(prompt)

    # Display assistant response in chat message container
    with st.chat_message("assistant"):
        message_placeholder = st.empty()
        full_response = ""
        prompt_parts = [input_prompt, prompt]

        response = model.generate_content(prompt_parts)
        assistant_response = response.text
        for chunk in assistant_response.split("."):
            full_response += chunk + " "
            time.sleep(0.05)
            # Add a blinking cursor to simulate typing
            message_placeholder.markdown(full_response + "▌")
        message_placeholder.markdown(full_response)
    # Add assistant response to chat history
    st.session_state.messages.append({"role": "assistant", "content": full_response})