# My First Postmortem

There is no perfect system; hence, the need to constantly run a routine check to ensure that every part of the system is operating optimally is necessary. There are times of uncertainty; they happen often, and when they do, we do not cry over spilled milk; rather, we pick up the bits and pieces to make a shiny new system.

To learn from previous experiences, even though they must not be our own, we must document the past, as they help us know what to do and what not to do when the past comes calling like a debt collector coming to collect debts.

To capture incidents and report them to the right authorities, we write post-mortems. A post-mortem is an analysis of events that lead to system failure. They help us navigate technical challenges when they arise and mitigate future recurrences through a process of learning and carrying out preventive and corrective measures.

In this article, I will be writing a post-mortem of an incident I encountered recently.

This is a submission to ALX’s 0x19 Postmortem Software Engineering program task.


## Issue Summary

Duration of outage: 8 hours, from 10:42 PM (WAT) to 6:05 AM (WAT) on June 8, 2024. That’s like an entire night of binge-watching your favorite show, but instead of being entertained, our users were left frustrated! 🤯

Impact: Our e-commerce website, https://the10xmarketingsolutions.com.ng/intercom was intermittently unavailable, leading to slow load times, which affected 40% of our users as they were unable to make purchases on the website. Imagine going to the grocery store, but the checkout line moves at a snail’s pace! 🐢

Root Cause: This was caused by an overloaded server and a misconfiguration in the varnish cache, which caused the website to load slowly as a sloth climbing a tree. 🦥

## Timeline:

June 8, 2024, 10:42 PM (WAT): The issue was detected by Jetpack’s monitoring system, like a trusty watchdog 🐶 barking to alert us about the unavailability and unresponsiveness of the website to some users.

June 8, 2024, 10:42 PM (WAT): It triggered an email alert, which was received with an error reference of 190578319/intermittent. Because who doesn’t love a good error code to decipher? 🤓

June 8, 2024, 10:45 PM (WAT): We attempted loading the website and confirmed the intermittent loading issues. Sometimes, you have to dig deep to find the root cause! 🕵️

June 8, 2024, 10:47 PM (WAT): We accessed the hosting control panel to check for server logs and the status of the resources to ascertain the server overload or misconfiguration.

June 8, 2024, 11:30 PM (WAT): We did not find any evidence in the server logs for the overloads; hence, we escalated the issue to the server hosting support team for further assistance.

June 9, 2024, 1:00 AM (WAT): The server hosting support team confirmed that our server was experiencing intermittent performance issues, but they were unable to identify the exact cause of the issue

June 9, 2024, 1:30 AM (WAT): The issue was then escalated to the server administrative team for a deeper check and resolution.

June 9, 2024, 3:30 AM (WAT): The team identified a misconfiguration in the server resource allocation, which led to the performance issues.

June 9, 2024, 5:00 AM (WAT): The server configuration was adjusted by the team to optimize performance and resource allocation.

June 9, 2024, 6:05 AM (WAT): The website functionality was fully restored, and Jetpack’s monitoring system triggered an alert confirming the availability and stability of the website.

## Root cause and resolution

The intermittent loading issue was caused by a misconfiguration in the server resource allocation, resulting in performance issues. The server administrative team rectified the misconfiguration by adjusting resource allocation settings to ensure optimal performance.

## Corrective and preventive measures

To prevent future recurrences,

1. We will conduct regular server performance audits to identify and address any potential resource allocation issues.
2. We will implement automated monitoring systems to promptly detect and alert us to server performance anomalies.
3. We will enhance communication channels with hosting support for quicker resolution of server-related issues.
4. We will develop a contingency plan for rapid deployment in case of future server performance degradation.

## Tasks

1. We will conduct a comprehensive review of server resource allocation settings to ensure optimal configuration.
2. We will implement automated performance monitoring scripts to provide real-time insights into server health.
3. We will schedule regular server performance audits to proactively identify and address potential issues.
4. We will document and disseminate the incident response plan to relevant stakeholders for future reference.

## Conclusion

When implemented, the corrective and preventive measures will help us mitigate the risk of similar server performance issues in the future and ensure the continued availability and reliability of our website for our users.
