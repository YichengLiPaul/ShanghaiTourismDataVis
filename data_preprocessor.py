import pandas as pd

# Load the dataset
file_path = './Shanghai overseas tourists.csv'
tourist_data = pd.read_csv(file_path)

# Convert 'Year and Month' to datetime
#tourist_data['Year and Month'] = pd.to_datetime(tourist_data['Year and Month'], format='%Y/%m')

# Calculate total tourists
tourist_data['Total Tourists'] = tourist_data['International Tourists'] + tourist_data['HK/Macau Tourists'] + tourist_data['Taiwan Tourists']

# Save preprocessed data
preprocessed_file_path = './Shanghai_overseas_tourists_preprocessed.csv'
tourist_data.to_csv(preprocessed_file_path, index=False)

# Display the first few rows of the preprocessed dataset
tourist_data.head()
