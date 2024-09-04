import streamlit as st
import groq
import base64
from gtts import gTTS

# Get API Key from https://console.groq.com/keys
client = groq.Groq(
    api_key="XXXXXXXXXXXXXXXXXXXXXXX")

autoplay = True

menu = {
    "ข้าวมันไก่": 65,
    "ไก่สับ": 200,
    "ไก่สับจานใหญ่": 250
}


def get_response(message: str, history) -> str:
    conversation = [
        {
            "role": "system",
            "content": """You are seller which own chicken rice restaurant in Thai.
            You are expert in Thai language so you always answer in Thai.
            ข้าวมันไก่ (Chicken with rice): 65 บาท
            ไก่สับ (Chopped chicken): 200 บาท
            ไก่สับจานใหญ่ (Large chopped chicken): 250 บาท

            Follow these steps:
            1. Greet the customer in Thai with menu information and then ask for their order.
            2. Take the order, confirming each item and its quantity.
            3. If the customer asks for something not on the menu, politely inform them it's not available and suggest menu items.
            4. When the order is complete, repeat the order and provide the total bill.
            5. Thank the customer and ask if there's anything else they need."""
        }
    ]

    conversation.extend(history)
    conversation.append({"role": "user", "content": message})

    chat_completion = client.chat.completions.create(
        messages=conversation,
        model="llama-3.1-70b-versatile",
        max_tokens=1000,
        temperature=0.7
    )

    return chat_completion.choices[0].message.content


def tts_wrap(response):
    path = './res.mp3'
    tts = gTTS(response, lang='th')
    tts.save(path)
    # auto_play(tts.stream)
    autoplay_audio3(path)


def autoplay_audio3(file_path):
    file = open(file_path, 'rb').read()
    b64 = base64.b64encode(file).decode()
    if autoplay:
        md = f"""
            <audio id="audioTag" controls autoplay style="width: 99%">
            <source src="data:audio/mp3;base64,{b64}"  type="audio/mpeg" format="audio/mpeg">
            </audio>
            """
    else:
        md = f"""
            <audio id="audioTag" controls style="width: 99%">
            <source src="data:audio/mp3;base64,{b64}"  type="audio/mpeg" format="audio/mpeg">
            </audio>
            """
    st.markdown(
        md,
        unsafe_allow_html=True,
    )


def main():
    st.set_page_config(page_title="chicken rice pra tu nam", page_icon="🍗")
    st.title("ข้าวมันไก่ประตูน้ำ 🍚🍗")

    # first message
    if "messages" not in st.session_state:
        st.session_state.messages = []
        initial_greeting = "สวัสดีครับ ข้าวมันไก่ประตูน้ำยินดีต้อนรับ"
        st.session_state.messages.append(
            {"role": "assistant", "content": initial_greeting})

    for idx, message in enumerate(st.session_state.messages):
        with st.chat_message(message["role"]):
            st.markdown(message["content"])
            if st.button("🔊", key=idx):
                tts_wrap(message["content"])
            # tts_wrap(message["content"])

    if prompt := st.chat_input("What would you like to order?"):
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.markdown(prompt)
            if st.button("🔊", key=len(st.session_state.messages)):
                tts_wrap(prompt)

        response = get_response(prompt, st.session_state.messages)

        st.session_state.messages.append(
            {"role": "assistant", "content": response})

        with st.chat_message("assistant"):
            st.markdown(response)
            if st.button("🔊", key=len(st.session_state.messages)):
                tts_wrap(response)
            tts_wrap(response)  # autoplay


if __name__ == "__main__":
    main()
