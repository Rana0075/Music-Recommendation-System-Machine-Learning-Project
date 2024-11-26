import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import streamlit as st


data = pd.read_csv('user_album_mood_data.csv')


data.dropna(inplace=True) 

data['mood'] = data['mood'].astype('category')
data['genre'] = data['genre'].astype('category')

mood_mapping = {mood: code for code, mood in enumerate(data['mood'].cat.categories)}
genre_mapping = {genre: code for code, genre in enumerate(data['genre'].cat.categories)}


data['mood'] = data['mood'].map(mood_mapping)  
data['genre'] = data['genre'].map(genre_mapping)  


X = data[['mood', 'genre']]
y = data['artist']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=2)

model = RandomForestClassifier()
model.fit(X_train, y_train)


# Streamlit app layout
st.title("🎶 Artist Prediction (Based on Mood and Genre) 🎶")
st.markdown("Please select your mood and genre!")

# Reverse mappings for displaying options
reverse_mood_mapping = {v: k for k, v in mood_mapping.items()}
reverse_genre_mapping = {v: k for k, v in genre_mapping.items()}

# User input for prediction
col1, col2 = st.columns(2)

with col1:
    mood_input = st.selectbox("Select Mood", options=list(reverse_mood_mapping.keys()), format_func=lambda x: reverse_mood_mapping[x])

with col2:
    genre_input = st.selectbox("Select Genre", options=list(reverse_genre_mapping.keys()), format_func=lambda x: reverse_genre_mapping[x])

# Predict button
if st.button("🎤 Predict Artist"):
    with st.spinner("Predicting..."):
        # Create a new input DataFrame for prediction
        new_input = pd.DataFrame({'mood': [mood_input], 'genre': [genre_input]})
        
        # Predict the artist
        predicted_artist = model.predict(new_input)
        
        # Display the predicted artist
        st.success(f"**Predicted Artist:** {predicted_artist[0]}")

        # Find the 3 most popular albums of the predicted artist
        popular_albums = data[data['artist'] == predicted_artist[0]]['album'].value_counts().nlargest(3)

        # Display the results
        if not popular_albums.empty:
            st.write("**Popular albums of the predicted artist:**")
            for album, count in popular_albums.items():
                st.write(f"- {album} (Count: {count})")
        else:
            st.write(f"No albums found for the predicted artist: {predicted_artist[0]}")





# Footer
st.markdown("---")
st.markdown("pre-final year project by B.Tech-CSE(AI&ML) - Group 2")