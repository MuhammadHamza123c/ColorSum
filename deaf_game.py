import streamlit as st
st.markdown("## ColorSum Visualizer")

st.markdown("##### ColorSum Visualizer is an accessible, number-based web app designed to enhance visual understanding of numerical sums. Users input two numbers, and the app calculates the total, then displays each digit using bold color blocks. Especially helpful for deaf or hard-of-hearing users")

st.sidebar.markdown("### Color Legend!", unsafe_allow_html=True)
summ=None

# List of labels and colors
color_labels = [
    ("ZERO", "beige"),  # Changed "warm white" to "beige"
    ("ONE", "red"),
    ("TWO", "green"),
    ("THREE", "blue"),
    ("FOUR", "yellow"),
    ("FIVE", "cyan"),  # Changed "white" to "lightgray"
    ("SIX", "orange"),
    ("SEVEN", "pink"),
    ("EIGHT", "purple"),
    ("NINE", "coral")
]

for label, color in color_labels:
    st.sidebar.markdown(
        f"""
        <div style='display: flex; align-items: center; margin-bottom: 20px;'>
            <span style='width: 220px; font-family: Arial, sans-serif; font-size: 14px; font-weight: bold; color:  #FFFFFF;'>{label}:</span>
            <div style='width: 50px; height: 20px; background-color: {color}; border: 2px outset #000;'></div>
        </div>
        """,
        unsafe_allow_html=True
    )

def zero():
     st.markdown(
    f"""
    <div style='display: flex; align-items: center; margin-bottom: 20px;'>
    <span style='width: 20px; font-family: Arial, sans-serif; font-size: 14px; font-weight: bold; color:  #FFFFFF;'>{"0"} :</span>
        <div style='width: 50px; height: 20px; background-color: {"beige"}; border: 2px outset #000;'></div>
    </div>
    """,
    unsafe_allow_html=True
)
     
     st.write("", unsafe_allow_html=True)

def one():
     st.markdown(
    f"""
    <div style='display: flex; align-items: center; margin-bottom: 20px;'>
    <span style='width: 20px; font-family: Arial, sans-serif; font-size: 14px; font-weight: bold; color:  #FFFFFF;'>{"1"} :</span>
        <div style='width: 50px; height: 20px; background-color: {"Red"}; border: 2px outset #000;'></div>
    </div>
    """,
    unsafe_allow_html=True
)
     st.write("", unsafe_allow_html=True)

def two():
     st.markdown(
    f"""
    <div style='display: flex; align-items: center; margin-bottom: 20px;'>
    <span style='width: 20px; font-family: Arial, sans-serif; font-size: 14px; font-weight: bold; color:  #FFFFFF;'>{"2"} :</span>
        <div style='width: 50px; height: 20px; background-color: {"Green"}; border: 2px outset #000;'></div>
    </div>
    """,
    unsafe_allow_html=True
)
     st.write("", unsafe_allow_html=True)

def three():
     st.markdown(
    f"""
    <div style='display: flex; align-items: center; margin-bottom: 20px;'>
    <span style='width: 20px; font-family: Arial, sans-serif; font-size: 14px; font-weight: bold; color:  #FFFFFF;'>{"3"} :</span>
        <div style='width: 50px; height: 20px; background-color: {"Blue"}; border: 2px outset #000;'></div>
    </div>
    """,
    unsafe_allow_html=True
)
     st.write("", unsafe_allow_html=True)

def four():
     st.markdown(
    f"""
    <div style='display: flex; align-items: center; margin-bottom: 20px;'>
    <span style='width: 20px; font-family: Arial, sans-serif; font-size: 14px; font-weight: bold; color:  #FFFFFF;'>{"4"} :</span>
        <div style='width: 50px; height: 20px; background-color: {"Yellow"}; border: 2px outset #000;'></div>
    </div>
    """,
    unsafe_allow_html=True
)
     st.write("", unsafe_allow_html=True)

def five():
     st.markdown(
    f"""
    <div style='display: flex; align-items: center; margin-bottom: 20px;'>
    <span style='width: 20px; font-family: Arial, sans-serif; font-size: 14px; font-weight: bold; color:  #FFFFFF;'>{"5"} :</span>
        <div style='width: 50px; height: 20px; background-color: {"cyan"}; border: 2px outset #000;'></div>
    </div>
    """,
    unsafe_allow_html=True
)
     st.write("", unsafe_allow_html=True)

def six():
     st.markdown(
    f"""
    <div style='display: flex; align-items: center; margin-bottom: 20px;'>
    <span style='width: 20px; font-family: Arial, sans-serif; font-size: 14px; font-weight: bold; color:  #FFFFFF;'>{"6"} :</span>
        <div style='width: 50px; height: 20px; background-color: {"orange"}; border: 2px outset #000;'></div>
    </div>
    """,
    unsafe_allow_html=True
)
     st.write("", unsafe_allow_html=True)

def seven():
     st.markdown(
    f"""
    <div style='display: flex; align-items: center; margin-bottom: 20px;'>
    <span style='width: 20px; font-family: Arial, sans-serif; font-size: 14px; font-weight: bold; color:  #FFFFFF;'>{"7"} :</span>
        <div style='width: 50px; height: 20px; background-color: {"pink"}; border: 2px outset #000;'></div>
    </div>
    """,
    unsafe_allow_html=True
)
     st.write("", unsafe_allow_html=True)

def eight():
     st.markdown(
    f"""
    <div style='display: flex; align-items: center; margin-bottom: 20px;'>
    <span style='width: 20px; font-family: Arial, sans-serif; font-size: 14px; font-weight: bold; color:  #FFFFFF;'>{"8"} :</span>
        <div style='width: 50px; height: 20px; background-color: {"purple"}; border: 2px outset #000;'></div>
    </div>
    """,
    unsafe_allow_html=True
)
     st.write("", unsafe_allow_html=True)

def nine():
     st.markdown(
    f"""
    <div style='display: flex; align-items: center; margin-bottom: 20px;'>
    <span style='width: 20px; font-family: Arial, sans-serif; font-size: 14px; font-weight: bold; color:  #FFFFFF;'>{"9"} :</span>
        <div style='width: 50px; height: 20px; background-color: {"coral"}; border: 2px outset #000;'></div>
    </div>
    """,
    unsafe_allow_html=True
)
     st.write("", unsafe_allow_html=True)





number_list=[]
number_1=st.number_input("Enter First Number: ",min_value=0)
number_2=st.number_input("Enter Second Number: ",min_value=0)
if st.button("Submit"):

  number_list.append(number_1)
  number_list.append(number_2)
  summ=sum(number_list)
  if summ:
      
   st.write(f"Total Sum is: {summ}")
  else:
      pass

for i in str(summ):
    if i=='0':
        zero()
        
    elif i=='1':
        one()
    elif i=='2':
        two()
    elif i=='3':
        three()
    elif i=='4':
        four()
    elif i=='5':
        five()
    elif i=='6':
        six()
    elif i=='7':
        seven()
    elif i=='8':
        eight()
    elif i=='9':
        nine()
# st.write(f"Total Sum is: {summ}")
  