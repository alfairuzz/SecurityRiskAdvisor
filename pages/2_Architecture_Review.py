import streamlit as st


content = """
### 1. System Components

#### Hardware Components
- **Public Users’ Devices:** Smartphones, laptops, and desktops accessing services over the internet.
- **Public-Facing Servers (Public Zone):** Hosts external services like websites or APIs.
- **Gateway Controls (DMZ):** Includes firewalls, proxies, and load balancers.
- **Internal Servers (Private Zone):** Hosts enterprise applications and databases.
- **VPN Server (Remote Access Zone):** Enables secure connections from remote corporate devices.
- **Corporate Devices:** Employee devices (laptops, smartphones) used to access internal systems via VPN.
- **Privileged Access Workstation (Management Zone):** Dedicated, secure devices used by administrators for privileged operations.

#### Software Components
- **Public-Facing Applications:** Includes web services, portals, and APIs accessible externally.
- **Enterprise Applications (Private Zone):** Backend software handling business operations.
- **VPN Software:** Manages secure remote access for employees.
- **Database Systems:** Store structured business data in the Private Zone.
- **Operating Systems and Middleware:** Present on servers and endpoints, enabling software functionality.

---

### 2. Trust Boundaries

#### Identified Boundaries
1. **Internet ↔ Public Zone**
   - **Description:** Public users access public-facing servers.
   - **Risk:** Exposed to external attackers.
   
2. **Public Zone ↔ DMZ**
   - **Description:** Data flows through gateway controls (e.g., firewall) before reaching the DMZ.
   - **Risk:** Gateway misconfigurations could allow unauthorised access.
   
3. **DMZ ↔ Private Zone**
   - **Description:** Internal enterprise servers handle sensitive business data.
   - **Risk:** Compromise here could lead to significant data loss or operational disruption.
   
4. **Private Zone ↔ Remote Access Zone**
   - **Description:** Staff access enterprise services through a VPN tunnel.
   - **Risk:** Vulnerabilities in the VPN could expose internal systems.
   
5. **Private Zone ↔ Management Zone**
   - **Description:** Administrative tasks performed from secure workstations.
   - **Risk:** Privileged access abuse or compromise could lead to full system control.

---

### 3. Data Flows

#### Data Flow Directions
1. **Public Users ↔ Public-Facing Servers:**
   - **Protocols:** HTTP/HTTPS for web traffic.
   - **Risks:** Unencrypted traffic or injection attacks.

2. **Public-Facing Servers ↔ Gateway Controls:**
   - **Protocols:** HTTPS, SSH, API calls.
   - **Risks:** Improper validation or insecure APIs.

3. **Gateway Controls ↔ Internal Servers:**
   - **Protocols:** Encrypted SQL queries, RDP for remote management.
   - **Risks:** Lateral movement in case of gateway compromise.

4. **Corporate Devices ↔ VPN Server:**
   - **Protocols:** Encrypted VPN tunnels.
   - **Risks:** Misconfigured VPN access or credential theft.

5. **Privileged Workstation ↔ Internal Servers:**
   - **Protocols:** RDP, SSH, API management interfaces.
   - **Risks:** Weak privileged access controls or stolen credentials.
"""


attack_tree = """
digraph G {
    // Graph styling
    graph [rankdir=TB, fontname="Arial", splines=ortho];
    node [shape=box, style="rounded", fontname="Arial", fontsize=10];
    edge [fontname="Arial", fontsize=8];

    // Root nodes
    root1 [label="Public-Facing Server\nExploitation", shape=doubleoctagon];
    root2 [label="VPN Server\nExploitation", shape=doubleoctagon];
    root3 [label="Privileged Workstation\nCompromise", shape=doubleoctagon];
    root4 [label="Insider Threat", shape=doubleoctagon];

    // Attack Tree 1: Public-Facing Server
    web_vuln [label="Exploit Web\nVulnerability"];
    public_access [label="Gain Access to\nPublic Zone"];
    pivot_gateway [label="Pivot Through\nGateway Controls"];
    steal_data1 [label="Steal/Disrupt\nData"];

    root1 -> web_vuln;
    web_vuln -> public_access;
    public_access -> pivot_gateway;
    pivot_gateway -> steal_data1;

    // Attack Tree 2: VPN Server
    vpn_creds [label="Steal VPN\nCredentials"];
    vpn_session [label="Establish VPN\nSession"];
    internal_access [label="Access Internal\nServers"];
    malware_deploy [label="Deploy Malware/\nExfiltrate Data"];

    root2 -> vpn_creds;
    vpn_creds -> vpn_session;
    vpn_session -> internal_access;
    internal_access -> malware_deploy;

    // Attack Tree 3: Privileged Workstation
    admin_creds [label="Target Admin\nCredentials"];
    priv_access [label="Access Privileged\nWorkstation"];
    exec_commands [label="Execute Privileged\nCommands"];
    system_compromise [label="System-wide\nCompromise"];

    root3 -> admin_creds;
    admin_creds -> priv_access;
    priv_access -> exec_commands;
    exec_commands -> system_compromise;

    // Attack Tree 4: Insider Threat
    abuse_access [label="Abuse Authorized\nAccess"];
    alter_data [label="Download/Alter\nSensitive Data"];
    lateral_move [label="Lateral\nMovement"];

    root4 -> abuse_access;
    abuse_access -> alter_data;
    alter_data -> lateral_move;

    // Subgraph for layout
    {
        rank=same; root1; root2; root3; root4;
    }

    // Add labels
    labelloc="t";
    label="Attack Trees Analysis\n\n";
}
"""

st.title("🔎 Architecture Review")

# Check session state
if "function_ran" in st.session_state and st.session_state.function_ran:
    
    st.write("Based on your system architecture diagram, view the LLM's review and assessment.")
    
    architecture_diagram = "images/architecture_diagram.png"
    st.image(architecture_diagram)
    
    expander = st.expander("Threat Analysis Report")    
    expander.markdown(content)

    expander_2 = st.expander("Potential Attack Tree(s)")    
    expander_2.graphviz_chart(attack_tree)
    
    
else:
    st.warning("This page is locked. Run the required function on the main page to unlock it.")
    

