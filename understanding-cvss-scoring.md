# Understanding CVSS scoring

The Common Vulnerability Scoring System (CVSS) is a standardized framework for measuring information systems’ severity of security flaws. It assigns each vulnerability a score between 0 and 10, with higher scores meaning more severe issues. This system helps organizations decide which security threats need attention first based on their potential impact.

### How does CVSS Scoring Work? <a href="#how-does-cvss-scoring-work-0" id="how-does-cvss-scoring-work-0"></a>

CVSS scoring assigns a number from 0 to 10 based on three main factors: Base, Temporal, and Environmental metrics. The Base score shows the inherent characteristics of a vulnerability. The Temporal score considers how those characteristics may change over time. The Environmental score evaluates how the vulnerability could affect a specific environment.

CVSS Score | Qualitative Rating -- | -- 0.0 | None 0.1 – 3.9 | Low 4.0 – 6.9 | Medium 7.0 – 8.9 | High 9.0 – 10.0 | Critical

A score of 0 means the vulnerability has minimal severity, while a score of 10 represents the most severe issues. This scoring helps organizations prioritize their responses to different security threats.

### How is a CVSS score calculated? <a href="#how-is-a-cvss-score-calculated-1" id="how-is-a-cvss-score-calculated-1"></a>

A CVSS score is based on three sets of metrics: [ Base](https://www.balbix.com/insights/base-cvss-scores/),[ Temporal](https://www.balbix.com/insights/temporal-cvss-scores/),[ and Environmental](https://www.balbix.com/insights/environmental-cvss-scores/). Each of these has its own scoring elements.

<figure><img src="https://www.balbix.com/app/uploads/CVSS-Score-Metrics-Blog.png" alt="CVSS Score Metrics" height="381" width="800"><figcaption><p>CVSS Score Metrics</p></figcaption></figure>

#### CVSS Base Metrics <a href="#cvss-base-metrics-2" id="cvss-base-metrics-2"></a>

The Base Metrics are the core components used to determine how severe a security vulnerability is. They focus on the vulnerability’s characteristics, regardless of whether it has been exploited or mitigated. These metrics include Exploitability, Scope, and Impact.

Exploitability: This metric assesses how easily a vulnerability is exploited. It is broken down into four sub-components:

* Attack Vector: Measures how an attack can be executed, with higher scores for remote attacks versus those requiring physical access.
* Attack Complexity: Evaluate the difficulty of executing the attack, with lower scores for easier vulnerabilities to exploit.
* Privileges Required: This indicator indicates the level of access needed to exploit the vulnerability, with higher scores for attacks requiring fewer privileges.
* User Interaction: Considers whether the attacker needs to involve a user in the exploit, with autonomous attacks scoring higher.

Scope: This metric assesses whether the vulnerability can affect other components beyond the initial target. The score will be higher if the vulnerability can propagate, such as compromising an entire system through a single application flaw.

Impact: This metric evaluates the potential consequences of a successful exploit, focusing on three areas:

* Confidentiality: Measures the extent of data exposure.
* Integrity: Assesses the ability of the attacker to modify data.
* Availability: Evaluate the potential disruption to system access and functionality.

While CVSS-based Base Metrics provide a crucial starting point for understanding a vulnerability’s severity, they have limitations. They do not account for Temporal Metrics, which change over time, or Environmental Metrics, which reflect an organization’s specific context, such as existing security controls and asset criticality.

Organizations must consider these additional factors to fully assess and prioritize vulnerabilities, which can significantly alter the perceived risk and required response.

#### CVSS Temporal Metrics <a href="#cvss-temporal-metrics-3" id="cvss-temporal-metrics-3"></a>

CVSS Temporal Metrics evaluate the changing nature of a vulnerability over time. These metrics assess a vulnerability’s current exploitability and the availability of remediating controls, such as patches. Key subcomponents of Temporal Metrics include:

* Exploit Code Maturity: A vulnerability is less threatening until a method to exploit it becomes available. As exploit code matures and becomes more widespread, its associated score increases, reflecting the heightened risk.
* Remediation Level: A vulnerability may not initially have a patch or workaround. As temporary fixes or official patches are released, the vulnerability score decreases, indicating reduced risk.
* Report Confidence: This measures how well a vulnerability is validated, ensuring it is both real and exploitable—higher confidence results in a higher score.

#### CVSS Environmental Metrics <a href="#cvss-environmental-metrics-4" id="cvss-environmental-metrics-4"></a>

CVSS Environmental Metrics allow organizations to adjust the Base CVSS score based on their specific Security Requirements and modifications of Base Metrics.

* Security Requirements: These metrics consider the criticality of the affected asset. Mission-critical systems, like a database containing all customer data, receive higher scores than less critical assets, such as a non-privileged user’s workstation.
* Modified Base Metrics: Organizations can modify Base CVSS Metrics based on existing mitigations. For instance, “air gapping” a server—disconnecting it from external networks—lowers the Attack Vector score since remote exploitation is no longer possible.

By considering both Temporal and Environmental Metrics, organizations can achieve a more tailored and accurate assessment of a vulnerability’s actual risk to their specific environment.

The Common Vulnerability Scoring System (CVSS) is a standardized framework for measuring information systems’ severity of security flaws. It assigns each vulnerability a score between 0 and 10, with higher scores meaning more severe issues. This system helps organizations decide which security threats need attention first based on their potential impact.

How does CVSS Scoring Work? CVSS scoring assigns a number from 0 to 10 based on three main factors: Base, Temporal, and Environmental metrics. The Base score shows the inherent characteristics of a vulnerability. The Temporal score considers how those characteristics may change over time. The Environmental score evaluates how the vulnerability could affect a specific environment.

CVSS Score Qualitative Rating 0.0 None 0.1 – 3.9 Low 4.0 – 6.9 Medium 7.0 – 8.9 High 9.0 – 10.0 Critical A score of 0 means the vulnerability has minimal severity, while a score of 10 represents the most severe issues. This scoring helps organizations prioritize their responses to different security threats.

How is a CVSS score calculated? A CVSS score is based on three sets of metrics: [Base](https://www.balbix.com/insights/base-cvss-scores/),[ Temporal](https://www.balbix.com/insights/temporal-cvss-scores/),[ and Environmental](https://www.balbix.com/insights/environmental-cvss-scores/). Each of these has its own scoring elements.

CVSS Score Metrics CVSS Score Metrics CVSS Base Metrics The Base Metrics are the core components used to determine how severe a security vulnerability is. They focus on the vulnerability’s characteristics, regardless of whether it has been exploited or mitigated. These metrics include Exploitability, Scope, and Impact.

Exploitability: This metric assesses how easily a vulnerability is exploited. It is broken down into four sub-components:

Attack Vector: Measures how an attack can be executed, with higher scores for remote attacks versus those requiring physical access. Attack Complexity: Evaluate the difficulty of executing the attack, with lower scores for easier vulnerabilities to exploit. Privileges Required: This indicator indicates the level of access needed to exploit the vulnerability, with higher scores for attacks requiring fewer privileges. User Interaction: Considers whether the attacker needs to involve a user in the exploit, with autonomous attacks scoring higher. Scope: This metric assesses whether the vulnerability can affect other components beyond the initial target. The score will be higher if the vulnerability can propagate, such as compromising an entire system through a single application flaw.

Impact: This metric evaluates the potential consequences of a successful exploit, focusing on three areas:

Confidentiality: Measures the extent of data exposure. Integrity: Assesses the ability of the attacker to modify data. Availability: Evaluate the potential disruption to system access and functionality. While CVSS-based Base Metrics provide a crucial starting point for understanding a vulnerability’s severity, they have limitations. They do not account for Temporal Metrics, which change over time, or Environmental Metrics, which reflect an organization’s specific context, such as existing security controls and asset criticality.

Organizations must consider these additional factors to fully assess and prioritize vulnerabilities, which can significantly alter the perceived risk and required response.

CVSS Temporal Metrics CVSS Temporal Metrics evaluate the changing nature of a vulnerability over time. These metrics assess a vulnerability’s current exploitability and the availability of remediating controls, such as patches. Key subcomponents of Temporal Metrics include:

Exploit Code Maturity: A vulnerability is less threatening until a method to exploit it becomes available. As exploit code matures and becomes more widespread, its associated score increases, reflecting the heightened risk. Remediation Level: A vulnerability may not initially have a patch or workaround. As temporary fixes or official patches are released, the vulnerability score decreases, indicating reduced risk. Report Confidence: This measures how well a vulnerability is validated, ensuring it is both real and exploitable—higher confidence results in a higher score. CVSS Environmental Metrics CVSS Environmental Metrics allow organizations to adjust the Base CVSS score based on their specific Security Requirements and modifications of Base Metrics.

Security Requirements: These metrics consider the criticality of the affected asset. Mission-critical systems, like a database containing all customer data, receive higher scores than less critical assets, such as a non-privileged user’s workstation. Modified Base Metrics: Organizations can modify Base CVSS Metrics based on existing mitigations. For instance, “air gapping” a server—disconnecting it from external networks—lowers the Attack Vector score since remote exploitation is no longer possible. By considering both Temporal and Environmental Metrics, organizations can achieve a more tailored and accurate assessment of a vulnerability’s actual risk to their specific environment.
