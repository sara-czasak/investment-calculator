import streamlit as st


st.title('Investment calculator')

company_name = st.text_input('What company are you investing with?')
investment_amount = st.number_input('How much are you investing?')
investment_period = st.number_input('How many years are you investing for?')
investment_percentage = st.number_input("What's the annual percent growth?")
investment_percentage /= 100

total_profit = investment_amount * (1+ investment_percentage) ** investment_period

if investment_amount > 0 and investment_period > 0 and company_name != "" and investment_percentage > 0:
    st.write(f"{company_name.title()}'s offer of {int(investment_percentage * 100)}% will make you a profit of {total_profit:.2f} over {int(investment_period)} years with an initial investment of {investment_amount:.2f}.")

