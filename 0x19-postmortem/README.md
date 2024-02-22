# Postmortem

## Blackbeing.tech Domain Name Suspension Incident Report

*By: **Anderson John Njahi***

### Issue Summary:

 - **Duration of Outage:** The domain "blackbeing.tech" was flagged by Radix for phishing and was suspended, resulting in a server hold, from July 4, 2023, 07:15 AM to July 18, 2023, 06:11 PM (GMT+3).

 - **Impact:** The suspension of the "blackbeing.tech" domain led to a complete unavailability of the web servers and associated services. Attempts to access web servers using the domain name failed. This affected 100% of user activity.

 - **Root Cause:** The Radix automated system flagged the domain "blackbeing.tech" as a potential phishing domain due to similarities with known phishing patterns.

### Timeline:

 - **Issue Detection:** July 4, 2023, 07:15 AM (GMT+3)
 - **Detection Method:** An engineer notices unavailability of web servers using domain name. 
 - **Actions Taken:** Initial investigation involved reviewing server logs and running services. Firewall rules were also reviewed. Domain name AAA records were reviewed.
 - **Misleading Paths:** Initial suspicion focused on wrongly configured web servers leading to re-creating new web servers. This took a couple of hours.
 - **Escalation:** The incident was escalated to cohort 11 ALX mentors and senior mentor. The incident also was raised to the .tech domain providers.
 - **Resolution:** The incident was resolved by contacting Radix's support and appealing the suspension. Following thorough verification of the domain's legitimacy, Radix lifted the suspension and removed the server hold, restoring access to "blackbeing.tech."

### Root Cause and Resolution:

 - **Root Cause:** The automated system employed by Radix flagged "blackbeing.tech" as a phishing site due to similarities in domain structure and content patterns with previously identified malicious domains.
 - **Resolution:** To resolve the issue, we initiated contact with Radix's support team, providing evidence of the domain's legitimate purpose and content. Radix conducted a thorough review and verified the domain's authenticity, leading to the unsuspension and removal of the server hold on "blackbeing.tech."

### Corrective and Preventative Measures:

- **Improvements/Fixes:** Implement regular content and domain audits to proactively identify potential false positives that might trigger automated security systems. Enhance communication channels with domain registrars and service providers to streamline the process of appealing false-positive flags.

- **Tasks to Address the Issue:** Establish a process for verifying and documenting domain ownership and legitimate usage to expedite future appeals. Collaborate with the Security Team to establish clear guidelines for addressing and appealing false-positive security flags.
Develop an incident response playbook specifically tailored for domain suspension scenarios to minimize downtime and impact on users.


