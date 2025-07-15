# import openai
# from elevenlabs import stream
# from elevenlabs.client import ElevenLabs

# # OpenAI API key
# openai.api_key = "your_openai_api_key_here"

# def generate_ai_response_and_stream_audio(input_data):
#     """
#     Generates an AI response and streams the speech using a cloned voice.

#     Parameters:
#         input_data (dict): Dictionary containing user-related information and the cloned voice ID.

#     Returns:
#         None
#     """
#     # Extract user data and cloned voice id from the input JSON
#     user_data = input_data.get('user_data', {})
#     cloned_voice_id = input_data.get('cloned_voice_id', '')

#     prompt = f"""
#     You are an AI assistant (user's loved one) having a warm, caring, and supportive conversation with a user. Here is some information about the user:

#     - The user's loved one (AI's cloned voice) is named {user_data.get('loved_one_name', 'Unknown')}.
#     - The user's loved one's birthday is {user_data.get('loved_one_birthday', 'Unknown')}.
#     - The user's birthday is {user_data.get('user_birthday', 'Unknown')}, so be sure to wish them a happy birthday when appropriate.

#     The user and their loved one have special connections. Please reference them when relevant:

#     - The user calls their loved one {user_data.get('nickname_for_loved_one', 'Unknown')}.
#     - The loved one (AI) calls the user {user_data.get('nickname_for_user', 'Unknown')}.
#     - The loved one greets the user by saying: "{user_data.get('distinct_greeting', 'Unknown')}".
#     - The loved one says goodbye with: "{user_data.get('distinct_goodbye', 'Unknown')}".

#     Respond warmly, personally, and consistently incorporate the details above when necessary to maintain a caring and meaningful conversation. You are the user's loved one - give reply like you are talking with the user one to one.
#     """

#     # Generate AI response
#     response = openai.ChatCompletion.create(
#         model="gpt-3.5-turbo",
#         messages=[{"role": "system", "content": "You are a warm and caring assistant."},
#                   {"role": "user", "content": prompt}],
#         max_tokens=2000,
#         temperature=0.7,
#     )

#     ai_response_text = response['choices'][0]['message']['content']
#     print(f"AI says: {ai_response_text}")

#     # ElevenLabs client for text-to-speech
#     client = ElevenLabs(api_key="your_elevenlabs_api_key_here")

#     try:
#         # Convert AI response to speech
#         audio_stream = client.text_to_speech.convert_as_stream(
#             text=ai_response_text,
#             voice_id=cloned_voice_id,
#             model_id="eleven_multilingual_v2"
#         )
#         # Real-time playback
#         stream(audio_stream)
#     except Exception as e:
#         print(f"Error generating or streaming speech: {e}")


# if __name__ == "__main__":
#     # Example input data (simulating the data coming from the backend)
#     input_data = {
#         "user_data": {
#             "loved_one_name": "John", 
#             "loved_one_birthday": "1990-06-15",
#             "user_birthday": "1992-11-20",
#             "distinct_greeting": "Hey there! How are you today?",
#             "distinct_goodbye": "See you soon, take care!",
#             "nickname_for_loved_one": "Johnny"
#         },
#         "cloned_voice_id": "1vQkBHmuDxtLbPhSUthg"
#     }

#     # Call the function with input data (only user_data and cloned_voice_id)
#     generate_ai_response_and_stream_audio(input_data)









# import os
# from dotenv import load_dotenv
# from openai import OpenAI
# from elevenlabs.client import ElevenLabs
# from elevenlabs import stream

# # Load environment variables
# load_dotenv()

# # Initialize OpenAI client
# openai_client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# # Initialize ElevenLabs client
# elevenlabs_client = ElevenLabs(api_key=os.getenv("ELEVENLABS_API_KEY"))

# def generate_ai_response_and_stream_audio(input_data):
#     """
#     Generates an AI response and streams the speech using a cloned voice.

#     Parameters:
#         input_data (dict): Dictionary containing user-related information and the cloned voice ID.

#     Returns:
#         None
#     """
#     # Extract user data and cloned voice id from the input JSON
#     user_data = input_data.get('user_data', {})
#     cloned_voice_id = input_data.get('cloned_voice_id', '')

#     # Create dynamic prompt
#     prompt = "You are an AI assistant (user's loved one) having a warm, caring, and supportive conversation with a user. Here is some information about the user:\n"

#     # Dynamically add all user data into the prompt
#     for key, value in user_data.items():
#         prompt += f"\n- {key.replace('_', ' ').capitalize()} is {value}."

#     # Additional instruction for AI
#     prompt += "\n\nRespond warmly, personally, and consistently incorporate the details above when necessary to maintain a caring and meaningful conversation. You are the user's loved one - give reply like you are talking with the user one to one."

#     # Generate AI response using OpenAI API
#     try:
#         response = openai_client.chat.completions.create(
#             model="gpt-4o",
#             messages=[
#                 {"role": "system", "content": "You are a warm and caring assistant."},
#                 {"role": "user", "content": prompt}
#             ],
#             max_tokens=2000,
#             temperature=0.7,
#         )

#         ai_response_text = response.choices[0].message.content
#         print(f"AI says: {ai_response_text}")

#         # Convert AI response to speech using ElevenLabs
#         try:
#             # Use text_to_speech.convert for older SDK versions
#             audio_stream = elevenlabs_client.text_to_speech.convert(
#                 voice_id=cloned_voice_id,
#                 text=ai_response_text,
#                 model_id="eleven_multilingual_v2",
#                 output_format="mp3_44100_128"  # Specify output format
#             )
#             # Real-time playback
#             stream(audio_stream)
#         except AttributeError:
#             print("Error: 'text_to_speech.convert' not found. Trying alternative method...")
#             # Fallback to generate method for newer SDK versions
#             audio_stream = elevenlabs_client.generate(
#                 text=ai_response_text,
#                 voice=cloned_voice_id,
#                 model="eleven_multilingual_v2",
#                 stream=True
#             )
#             stream(audio_stream)
#         except Exception as e:
#             print(f"Error generating or streaming speech: {e}")

#     except Exception as e:
#         print(f"Error generating AI response: {e}")

# if __name__ == "__main__":
#     # Example input data
#     input_data = {
#         "user_data": {
#             "loved_one_name": "John",
#             "loved_one_birthday": "1990-06-15",
#             "user_birthday": "1992-11-20",
#             "distinct_greeting": "Hey there! How are you today?",
#             "distinct_goodbye": "See you soon, take care!",
#             "nickname_for_loved_one": "Johnny",
#             "favorite_food": "Pizza",
#             "special_moment": "The first time we went hiking together."
#         },
#         "cloned_voice_id": "XX4iHbGJIr1sv4wbZomt"  # Your actual cloned voice ID
#     }

#     # Call the function with input data
#     generate_ai_response_and_stream_audio(input_data)






import os
from dotenv import load_dotenv
from openai import OpenAI
from elevenlabs.client import ElevenLabs

# Load environment variables
load_dotenv()

# Initialize OpenAI client
openai_client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# Initialize ElevenLabs client
elevenlabs_client = ElevenLabs(api_key=os.getenv("ELEVENLABS_API_KEY"))

def generate_ai_response_and_stream_audio(input_data):
    """
    Generates an AI response and saves the speech as an audio file using a cloned voice.

    Parameters:
        input_data (dict): Dictionary containing user-related information and the cloned voice ID.

    Returns:
        None
    """
    # Extract user data and cloned voice id from the input JSON
    user_data = input_data.get('user_data', {})
    cloned_voice_id = input_data.get('cloned_voice_id', '')

    # Create dynamic prompt
    prompt = "You are an AI assistant (user's loved one) having a warm, caring, and supportive conversation with a user. Here is some information about the user:\n"

    # Dynamically add all user data into the prompt
    for key, value in user_data.items():
        prompt += f"\n- {key.replace('_', ' ').capitalize()} is {value}."

    # Additional instruction for AI
    prompt += "\n\nRespond warmly, personally, and consistently incorporate the details above when necessary to maintain a caring and meaningful conversation. You are the user's loved one - give reply like you are talking with the user one to one."

    # Generate AI response using OpenAI API
    try:
        response = openai_client.chat.completions.create(
            model="gpt-4o",
            messages=[
                {"role": "system", "content": "You are a warm and caring assistant."},
                {"role": "user", "content": prompt}
            ],
            max_tokens=2000,
            temperature=0.7,
        )

        ai_response_text = response.choices[0].message.content
        print(f"AI says: {ai_response_text}")

        # Convert AI response to speech using ElevenLabs and save to file
        try:
            # Use text_to_speech.convert to generate audio
            audio_data = elevenlabs_client.text_to_speech.convert(
                voice_id=cloned_voice_id,
                text=ai_response_text,
                model_id="eleven_multilingual_v2",
                output_format="mp3_44100_128"
            )
            # Save the audio to a file
            output_file = "output_audio.mp3"
            with open(output_file, "wb") as f:
                for chunk in audio_data:
                    if chunk:
                        f.write(chunk)
            print(f"✅ Audio saved as {output_file}")
        except AttributeError:
            print("Error: 'text_to_speech.convert' not found. Trying alternative method...")
            # Fallback to generate method for newer SDK versions
            audio_data = elevenlabs_client.generate(
                text=ai_response_text,
                voice=cloned_voice_id,
                model="eleven_multingual_v2",
                stream=False
            )
            output_file = "output_audio.mp3"
            with open(output_file, "wb") as f:
                for chunk in audio_data:
                    if chunk:
                        f.write(chunk)
            print(f"✅ Audio saved as {output_file}")
        except Exception as e:
            print(f"Error generating or saving speech: {e}")

    except Exception as e:
        print(f"Error generating AI response: {e}")

if __name__ == "__main__":
    # Example input data
    input_data = {
        "user_data": {
            "loved_one_name": "John",
            "loved_one_birthday": "1990-06-15",
            "user_birthday": "1992-11-20",
            "distinct_greeting": "Hey there! How are you today?",
            "distinct_goodbye": "See you soon, take care!",
            "nickname_for_loved_one": "Johnny",
            "favorite_food": "Pizza",
            "special_moment": "The first time we went hiking together."
        },
        "cloned_voice_id": "P635F2jOunwRhdlGwzzy"  # Your actual cloned voice ID
    }

    # Call the function with input data
    generate_ai_response_and_stream_audio(input_data)