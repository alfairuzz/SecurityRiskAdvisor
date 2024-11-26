import streamlit as st
import pandas as pd

# Define the data
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




st.title("📝 Risk Assessment Report")


# Check session state
if "function_ran" in st.session_state and st.session_state.function_ran:
    st.button("Download Report")
    
    df = pd.read_excel("database/selected_system.xlsx")
    
    selected_system = df['System'][0]
    
    if selected_system == "System A (On-prem)":
        st.title(selected_system)
        
        for risk in data_a:
            st.subheader(f"Risk #{risk['S/N']}")
            st.write(f"**Risk Statement:** {risk['Risk Statement']}")
            st.write(f"**Existing Controls in Place:**\n{risk['Existing Controls in Place']}")
            st.write(f"**Current Impact Level:** {risk['Current Impact Level']}")
            st.write(f"**Current Likelihood Level:** {risk['Current Likelihood Level']}")
            st.write(f"**Current Risk Level:** {risk['Current Risk Level']}")
            st.write(f"**Risk Treatment:**\n{risk['Risk Treatment']}")
            st.write(f"**Residual Impact Level:** {risk['Residual Impact Level']}")
            st.write(f"**Residual Likelihood Level:** {risk['Residual Likelihood Level']}")
            st.write(f"**Residual Risk Level:** {risk['Residual Risk Level']}")
            st.markdown("---")  # Add a horizontal divider for better separation
    
    elif selected_system == "System B (Cloud)":
        st.title(selected_system)
        
        for risk in data_b:
            st.subheader(f"Risk #{risk['S/N']}")
            st.write(f"**Risk Statement:** {risk['Risk Statement']}")
            st.write(f"**Existing Controls in Place:**\n{risk['Existing Controls in Place']}")
            st.write(f"**Current Impact Level:** {risk['Current Impact Level']}")
            st.write(f"**Current Likelihood Level:** {risk['Current Likelihood Level']}")
            st.write(f"**Current Risk Level:** {risk['Current Risk Level']}")
            st.write(f"**Risk Treatment:**\n{risk['Risk Treatment']}")
            st.write(f"**Residual Impact Level:** {risk['Residual Impact Level']}")
            st.write(f"**Residual Likelihood Level:** {risk['Residual Likelihood Level']}")
            st.write(f"**Residual Risk Level:** {risk['Residual Risk Level']}")
            st.markdown("---")  # Add a horizontal divider for better separation
    
   
   
else:
    st.warning("🔒 This page is currently locked. Run the risk assessment to enable this page!")
    
