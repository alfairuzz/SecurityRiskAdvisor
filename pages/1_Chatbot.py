import streamlit as st
from ollama import chat
import pandas as pd

st.title("💬 Chatbot")
st.caption("🚀 A chatbot powered by 🦙 Llama3.2")

data_b = [
    {
        "S/N": 1,
        "Risk Statement": "Malicious actor exploits a misconfigured security group on an Amazon RDS instance, gaining unauthorised access to sensitive customer data stored in the database.",
        "Existing Controls in Place": """Implemented the following:
1. Strong IAM policies
2. Use multi-factor authentication (MFA) for database access
3. Regularly rotate database credentials
4. Enable encryption at rest for RDS instances""",
        "Current Impact Level": 4,
        "Current Likelihood Level": 2,
        "Current Risk Level": "Low",
        "Risk Treatment": """Propose to implement the following:
1. Implement version control to version management and also roll back in the event of application failure
2. Implement DAM monitoring (Amazon RDS Performance Insights)""",
        "Residual Impact Level": 4,
        "Residual Likelihood Level": 1,
        "Residual Risk Level": "Low"
    },
    {
        "S/N": 2,
        "Risk Statement": "An attacker exploits an unpatched cross-site scripting (XSS) vulnerability in a government web application to inject malicious scripts, stealing user session tokens and gaining unauthorised access to sensitive citizen data and CPF information.",
        "Existing Controls in Place": """Implemented the following:
1. Use secure coding practices
2. Conduct Penetration testing on the application for major changes and ensure all medium and above known vulnerabilities are closed prior to release in production""",
        "Current Impact Level": 3,
        "Current Likelihood Level": 1,
        "Current Risk Level": "Medium",
        "Risk Treatment": "-",
        "Residual Impact Level": "-",
        "Residual Likelihood Level": "-",
        "Residual Risk Level": "-"
    },
    {
        "S/N": 3,
        "Risk Statement": "Skilled hacker performs reconnaissance on a mobile application to gather critical information and exploit a lack of proper change management processes, compromising user data and potentially leading to data breach.",
        "Existing Controls in Place": """Implemented the following:
1. Use secure coding practices
2. Conduct security assessments of the application prior to release in production""",
        "Current Impact Level": 3,
        "Current Likelihood Level": 2,
        "Current Risk Level": "Low",
        "Risk Treatment": """Propose to implement the following:
1. Implement version control to version management and also roll back in the event of application failure""",
        "Residual Impact Level": 3,
        "Residual Likelihood Level": 1,
        "Residual Risk Level": "Low"
    }
]

data_a = [
    {
        "S/N": 1,
        "Risk Statement": "Malicious attacker exploits weak password settings on an Oracle database 21c to deliver and install malicious capabilities, leading to unauthorized access to employee personal data.",
        "Existing Controls in Place": """Implemented the following:
1. Strong password policies
2. Use multi-factor authentication
3. Access is only via on-site.""",
        "Current Impact Level": 3,
        "Current Likelihood Level": 1,
        "Current Risk Level": "Low",
        "Risk Treatment": "-",
        "Residual Impact Level": "-",
        "Residual Likelihood Level": "-",
        "Residual Risk Level": "-"
    },
    {
        "S/N": 2,
        "Risk Statement": "Third-party vendor with inadequate data protection practices accidentally exposes the Oracle database 21c containing personal data of government employees, potentially leading to identity theft and reputational damage to the agency.",
        "Existing Controls in Place": """Implemented the following:
1. Role-based access control
2. Regularly user access review and update privileged account permissions
3. Use of multi-factor authentication
4. Database activities monitoring (DAM)""",
        "Current Impact Level": 3,
        "Current Likelihood Level": 3,
        "Current Risk Level": "Medium",
        "Risk Treatment": """Propose to implement the following:
1. Privileged access management tool (e.g. CyberArk) and the use of workflow to only grant access to privileged users based on approval.""",
        "Residual Impact Level": 3,
        "Residual Likelihood Level": 1,
        "Residual Risk Level": "Low"
    },
    {
        "S/N": 3,
        "Risk Statement": "Due to the lack of proper change management process, the staff may introduce human error during deployment.",
        "Existing Controls in Place": """Implemented the following:
1. All staff that handles deployed are trained.
2. Roll-back plan is in place to revert changes in the event where an error occurred during deployment.""",
        "Current Impact Level": 3,
        "Current Likelihood Level": 2,
        "Current Risk Level": "Low",
        "Risk Treatment": """Propose to implement the following:
1. Document change management process
2. Automate change management process.""",
        "Residual Impact Level": 3,
        "Residual Likelihood Level": 1,
        "Residual Risk Level": "Low"
    },
    {
        "S/N": 4,
        "Risk Statement": "Flash flood waters breach the ground-floor data centre, which damages inadequately elevated Windows servers and other critical IT equipment, causing extended downtime of critical public services.",
        "Existing Controls in Place": """Implemented the following:
1. Servers and critical IT equipment are installed on raised floors or elevated platforms
2. Developed and regularly test a comprehensive disaster recovery plan
3. Installed systems to monitor temperature, humidity, and water presence and also implemented real-time alerts for any environmental anomalies""",
        "Current Impact Level": 4,
        "Current Likelihood Level": 1,
        "Current Risk Level": "Low",
        "Risk Treatment": "-",
        "Residual Impact Level": "-",
        "Residual Likelihood Level": "-",
        "Residual Risk Level": "-"
    }
]

df = pd.read_excel("database/selected_system.xlsx")
    
selected_system = df['System'][0]

if selected_system == "System A (On-prem)":
    memory_chat = f"{data_a}"
elif selected_system == "System B (Cloud)":
    memory_chat = f"{data_b}"

# with open("database/risk_scenarios.txt", "r") as file:
#     memory_chat = file.read()

# Check session state
if "function_ran" in st.session_state and st.session_state.function_ran:
    
    # Initialize chat history
    if "messages" not in st.session_state:
        st.session_state.messages = []

    # Summarise older messages if the chat history becomes too long
    def summarise_messages(messages, model="llama3.2:latest"):
        # Prepare messages to be summarised
        system_message = {"role": "system", "content": "Summarise the following messages briefly while preserving the context and semantics as best as possible:"}
        summary_request = [system_message] + messages
        response = chat(
            model=model,
            messages=summary_request,
            stream=False  
        )
        return response["message"]["content"]

    # Limit the number of messages in memory
    max_message_count = 10
    if len(st.session_state.messages) > max_message_count:
        # Summarise all but the last `max_message_count` messages
        summary = summarise_messages(st.session_state.messages[:-max_message_count])
        # Replace older messages with the summary
        st.session_state.messages = [{"role": "assistant", "content": summary}] + st.session_state.messages[-max_message_count:]

    # Display chat messages from history on app rerun
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])
            
    st.chat_message("assistant").write("Ask me about your risk assessment report 📝")
    
    # Accept user input
    if prompt := st.chat_input("Start by asking about your risk assessment results!"):
        # Add user message to chat history
        st.session_state.messages.append({"role": "user", "content": prompt})
        # Display user message in chat message container
        with st.chat_message("user"):
            st.markdown(prompt)


        # Add system-level context dynamically
        system_context = {
            "role": "assistant",
            "content": memory_chat
        }
        full_messages = [system_context] + st.session_state.messages
        
        # Display assistant response in chat message container
        with st.chat_message("assistant"):
            response_placeholder = st.empty()  # Create a placeholder for streaming response
            response_parts = []  # To collect parts of the response

            for response in chat(
                model="llama3.2:latest",
                messages=full_messages,
                stream=True,  # Enable streaming
            ):
                # Append streamed content
                response_parts.append(response["message"]["content"])
                # Update the placeholder with the current accumulated response
                response_placeholder.markdown("".join(response_parts))

            # Combine the full response
            full_response = "".join(response_parts)

        # Add assistant response to chat history
        st.session_state.messages.append({"role": "assistant", "content": full_response})
        
        
else:
    st.warning("This page is locked. Run the required function on the main page to unlock it.")


