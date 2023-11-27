
import streamlit as st
from joblib import load
import pandas as pd
import os 


df = pd.read_csv('Ready_to_ML.csv')
# Load the pre-trained Ridge model
ridge_model_loaded = load('model.joblib')

st.markdown("""
        <style>
            .main_container {
                background-color: #87CEEB;  
            }

            h1 {
                text-align: center;
                color: #87CEEB;
            }
            h2{
                text-align: center;
            }
            .sidebar .sidebar-content {
                background-color: #87CEEB;
            }
            .stButton>button {
                color: #ffffff;
                background-color: #87CEEB;
                border: none;
                border-radius: 4px;
                padding: 0.75rem 1.5rem;
                margin: 0.75rem 0;

            }
            .stButton>button:hover {
                background-color: #87CEEB;
                text-align: center;
            }
            body {
                background-color: #87CEEB;  
            }
        </style>
    """, unsafe_allow_html=True)

# st.set_page_config(page_title='Car Price Prediction', layout='wide')
# tab1, tab2 = st.tabs(["Welcome", "Predict"])
# Initialize session state
if 'submitted' not in st.session_state:
    st.session_state['submitted'] = False

# Define the welcome page form
if not st.session_state['submitted']:
    
        # st.write("Welcome to Eng.Majed AutoMobile Shop! Please submit to continue.")
        
        st.markdown("----", unsafe_allow_html=True)
        st.subheader("Welcome to..")
        st.title('AutoScout Car Prices Platform')
            
        # Set page title and background color
        with st.chat_message("user"):
            st.write("Hello to AutoMobile app!")
        # Define the main title and description
        st.title('Car Price Prediction')
        user_data = {}

        # Create a sidebar for additional information (optional)
        st.sidebar.title('About')
        st.sidebar.write("This app predicts car prices based on the provided features.")
        st.header('Hello')
        st.sidebar.header('Car Features')

        user_data['make_model'] = st.sidebar.selectbox('Make and Model', options=['','Volvo V40', 'Ford Mondeo', 'Renault Megane', 'Opel Astra',
            'Opel Adam', 'SEAT Leon', 'Nissan Pulsar', 'Hyundai i30',
            'Skoda Scala', 'Ford Focus', 'Dacia Sandero', 'Fiat Panda',
            'Ford Mustang', 'Fiat 500X', 'Renault Captur', 'Nissan Qashqai',
            'Renault Talisman', 'Peugeot 308', 'Volvo XC40', 'Ford Fiesta',
            'Renault Kadjar', 'Fiat 500C', 'Toyota Yaris', 'Skoda Fabia',
            'Renault Clio', 'Opel Insignia', 'Peugeot 2008', 'SEAT Ibiza',
            'Opel Cascada', 'Dacia Duster', 'Skoda Karoq', 'Hyundai i20',
            'Peugeot 206', 'Volvo XC60', 'Toyota RAV 4', 'Opel Corsa',
            'Toyota Corolla', 'Peugeot 3008', 'Hyundai TUCSON', 'Peugeot 208',
            'Fiat 500', 'SEAT Arona', 'Volvo S60', 'Opel Grandland X',
            'Dacia Logan', 'Peugeot RCZ', 'Nissan Micra', 'Skoda Kodiaq',
            'Toyota C-HR', 'Skoda Superb', 'SEAT Ateca', 'Hyundai IONIQ',
            'Skoda Octavia', 'Toyota Auris', 'Volvo V90', 'Fiat Tipo',
            'Peugeot 207', 'Volvo XC90', 'Volvo S90', 'Volvo C30',
            'Nissan 370Z', 'Volvo C70', 'Nissan Juke', 'Nissan X-Trail',
            'Mercedes-Benz A 180', 'Toyota Aygo', 'Volvo V60', 'Peugeot 508',
            'Nissan 350Z', 'Ford Kuga']) 

        user_data['warranty'] = st.sidebar.radio('Warranty', options=['Yes', 'No'])
        user_data['mileage'] = st.sidebar.number_input('Mileage', min_value=0.0, max_value=df['mileage'].max(), value=0.0, step=500.0)
        user_data['seller'] = st.sidebar.selectbox('Seller', options=['Dealer', 'Private seller'])

        user_data['full_service_history'] = 'Yes'
        user_data['upholstery'] = st.sidebar.selectbox('Upholstery', options=['Part/Full Leather', 'Cloth'])
        user_data['comfort_&_convenience_Package'] = st.sidebar.selectbox('Comfort & Convenience Package', options=['Standard', 'Premium', 'Premium Plus'])
        user_data['entertainment_&_media_Package'] = st.sidebar.selectbox('Entertainment & Media Package', options=['Standard', 'Plus'])
        user_data['safety_&_security_Package'] = 'Safety Standard Package'
        # Create a multi-column layout for better organization
        user_data['body_type'] ='Compact'
        user_data['type'] = 'Used'
        user_data['gearbox'] = 'Semi-automatic'
        user_data['fuel_type'] = 'Benzine'
        user_data['engine_size'] = 1500.0
        user_data['gears'] = 6.0
        user_data['co_emissions'] = 500
        user_data['drivetrain'] = 'Front'
        user_data['extras'] = 8
        user_data['empty_weight'] = 1280.0
        user_data['full_service_history'] = 'Yes'
        user_data['previous_owner'] =1.0
        user_data['energy_efficiency_class'] ='efficient'
        user_data['age'] = 2.0
        user_data['power_kW'] = 88.0
        user_data['cons_avg'] = 3.6
        # user_data['comfort_&_convenience_Package'] = st.selectbox('Comfort & Convenience Package', options=['Standard', 'Premium', 'Premium Plus'])
        # user_data['entertainment_&_media_Package'] = st.selectbox('Entertainment & Media Package', options=['Standard', 'Plus'])
        # user_data['safety_&_security_Package'] = st.selectbox('Safety & Security Package', options=['Safety Standard Package', 'Safety Premium Package', 'Safety Premium Plus Package'])

        # Submit button
        submit_button = st.sidebar.button('Predict Price')

        # Prediction and display in col2

        st.header('Car Price Prediction')
        if submit_button:
            # Create a DataFrame with user input
            #df[df['make_model'] == dic['ii']].head(1)['price'].values[0]
            if user_data['make_model'] != '':
                # print(df[df['make_model'] == user_data['make_model']].head(1)['gearbox'].values[0])
                user_data['gearbox']=df[df['make_model'] == user_data['make_model']].head(1)['gearbox'].values[0]
                user_data['energy_efficiency_class']=df[df['make_model'] == user_data['make_model']].head(1)['energy_efficiency_class'].values[0]
                user_data['power_kW']=df[df['make_model'] == user_data['make_model']].head(1)['power_kW'].values[0]
                user_data['cons_avg']=df[df['make_model'] == user_data['make_model']].head(1)['cons_avg'].values[0]
                user_data['previous_owner']=df[df['make_model'] == user_data['make_model']].head(1)['previous_owner'].values[0]
                user_data['full_service_history']=df[df['make_model'] == user_data['make_model']].head(1)['full_service_history'].values[0]
                user_data['body_type']=df[df['make_model'] == user_data['make_model']].head(1)['body_type'].values[0]
                # user_data['extras']=df[df['make_model'] == user_data['make_model']].head(1)['extras'].values[0] ### we need to deal with this or it will be fixed value -----
                user_data['fuel_type']=df[df['make_model'] == user_data['make_model']].head(1)['fuel_type'].values[0]
                user_data['engine_size']=df[df['make_model'] == user_data['make_model']].head(1)['engine_size'].values[0]
                user_data['gears']=df[df['make_model'] == user_data['make_model']].head(1)['gears'].values[0]
                user_data['co_emissions']=df[df['make_model'] == user_data['make_model']].head(1)['co_emissions'].values[0]
                user_data['drivetrain']=df[df['make_model'] == user_data['make_model']].head(1)['drivetrain'].values[0]
                user_data['empty_weight']=df[df['make_model'] == user_data['make_model']].head(1)['empty_weight'].values[0]
                user_data['previous_owner']=df[df['make_model'] == user_data['make_model']].head(1)['previous_owner'].values[0]
                user_data['age']=df[df['make_model'] == user_data['make_model']].head(1)['age'].values[0]
                user_input_df = pd.DataFrame([user_data])
                # Make a prediction using the loaded model
                df1 = pd.DataFrame({
                'Age':[user_data['age']],
                'previous owners':[user_data['previous_owner']],
                'fuel type':[user_data['fuel_type']],
                'gear box':[user_data['gearbox']],
                'Hourse Power':[user_data['power_kW']],
                'Brand':df[df['make_model'] == user_data['make_model']].head(1)['make'].values[0]

            })

            # Convert the DataFrame to a Markdown table string
                markdown_table = df1.to_markdown(index=False)
                
                predicted_price = ridge_model_loaded.predict(user_input_df)[0]
                car_model = user_data['make_model']  # Replace with user's choice
                # This should be replaced with the user's choice
                
        # Display the styled DataFrame in Streamlit
                st.dataframe(df1,hide_index=True)
                st.markdown(markdown_table, unsafe_allow_html=True)  
                # st.table(user_input_df)
                st.subheader('Estimated Car Price:')
                st.write(f'${predicted_price:.2f}')
            else: st.sidebar.write('Please choose car name')