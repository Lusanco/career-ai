# Luis Santiago

_Juana Díaz, PR • lasc1026@gmail.com • linkedin.com/in/lusanco • Bilingual (English/Spanish)_<br>
_Certifications: [AWS Certified Cloud Practitioner](https://www.credly.com/badges/f1289a38-cc96-4550-87a7-9a00f3cfb268/public_url) • [AWS Certified AI Practitioner](https://www.credly.com/badges/ee3ee435-d36b-477f-a2e7-3ea4cb846dd0/public_url)_

## EXPERIENCE

**Lockheed Martin • System Integration Analyst Associate • Remote • May 2026 — Present**

- _Refactored and documented an existing Python/PySide6 desktop tool for generating Jira PowerShell configuration files, replacing fragile components with a simpler sandbox implementation that became the main application._
- _Implemented a unified UI and dynamic configuration flow that fetches Jira issue types and fields via the Jira REST API and maps required fields into the generated configuration._
- _Extended the configuration generation to support updating issue keys and issues, wiring this behavior into both the UI and the underlying rendering logic in response to incoming work tickets._
- _Built a Python CLI prototype for Jira REST API calls to validate configuration behavior independently of the GUI._
- _Introduced an AI‑assisted development workflow using an agents file with explicit prompt constraints and rules, so design choices and code changes were documented and applied consistently._
- _Reorganized, documented, and cleaned up the codebase, including module layout, docstrings, and Markdown documentation._
- _Python • PySide6 • PowerShell Config Generation • Jira REST API • AI-Assisted Development._

**Lockheed Martin • Engineering Aide • Remote • Dec 2025 — May 2026**

- _Participated in an engineering rotation focused on CI security and automated testing, working on GitLab CI SBOM pipelines and Tricentis Tosca automated end‑to‑end UI regression tests for web application workflows._
- _Adapted existing GitLab CI modules to build an SBOM pipeline template that supported Maven, Node.js, and Python projects, including updates to jobs, rules, and artifacts for different language scanners._
- _Configured SBOM generation in GitLab CI using CycloneDX (with Syft as a fallback scanner) and wired the resulting artifacts into existing efoss and GitLab Pages jobs so teams could review HTML risk reports._
- _Maintained and extended automated end‑to‑end UI regression tests in Tricentis Tosca by updating test logic and wait conditions, reusing example assets, and adding steps to cover additional application workflows._
- _Prepared and ran execution lists and Distributed Execution (DEX) runs, using repeated successful executions as a gate before promoting automated policy test suites into production._
- _GitLab CI • SBOM (CycloneDX, Syft) • Tricentis Tosca Commander • DEX • Automated end‑to‑end UI regression testing._

**Independent Contractor • Front End Web Developer • Remote • Sept 2024 — Oct 2024 • [Demo](https://lusanco.github.io/svelte-hvac-portfolio/)**

- _Designed and developed a simple informational website for an HVAC client using Svelte, Vite, and TailwindCSS, including layout, color palette, and page structure based on the client’s logo, mission, and service descriptions._
- _Gathered and refined requirements through several meetings and ongoing phone/email communication, providing design iterations and incorporating feedback on content and visual presentation._
- _Implemented a responsive, mobile‑first UI and tested layouts across Chrome DevTools viewports and multiple physical devices (phones, tablets, desktop browsers) to ensure consistent behavior_
- _Deployed the production build by running the Vite static build and uploading the generated assets to HostGator via FTP, configuring the hosting so client‑side routing continued to work on page refresh._
- _Enabled HTTPS for the site by applying the SSL options included in the client’s HostGator plan to the project’s URLs._
- _Vite • Svelte • JavaScript • TailwindCSS • Chrome DevTools • HostGator • FTP._

**Independent Contractor • Front End Web Developer • Remote • Aug 2023 — Sept 2023 • [Demo](https://lusanco.github.io/alpinejs-static-website/)**

- _Designed and built a simple single‑page informational website for a non‑profit using HTML, TailwindCSS, JavaScript, and Alpine.js, including layout, color choices, and page structure based on the organization’s logo and written content._
- _Created the organization’s first website by gathering requirements through conversations and translating their mission and activities into clear sections and on‑page content._
- _Used Alpine.js directives to switch views within a single HTML page, showing and hiding content sections to provide a basic single‑page application experience._
- _Implemented responsive, mobile‑first styling with TailwindCSS and tested the site across Chrome DevTools viewports and multiple physical devices (phones, tablets, desktops)._
- _Deployed the site by uploading static files through HostGator cPanel and enabling HTTPS using the SSL options included in the hosting plan._
- _HTML • CSS • TailwindCSS • JavaScript • Alpine.js • Chrome DevTools • HostGator cPanel._

**ZOMIO Inc • Front End Web Developer • Ponce, PR • Remote • June 2022 — Sept 2023**

- _Developed two browser-based IoT dashboards using JavaScript and the Paho MQTT client to subscribe to broker topics and display live telemetry from hardware devices._
- _Implemented real-time UI updates by parsing JSON payloads from subscribed topics and updating views for temperature, gas concentrations (CO, CO₂), GPS location (with a map and moving marker), and presence indicators._
- _Designed the dashboards’ layouts and interactions while coordinating with the hardware engineer to align the UI with device capabilities and data formats._
- _Redesigned the company’s marketing website in HTML and TailwindCSS, replacing the previous site and iterating on structure and styling with feedback from the CEO._
- _Transferred the company domain from GoDaddy to HostGator and configured DNS records and SSL in the hosting panels so the new site was served correctly over HTTPS._
- _HTML • CSS • TailwindCSS • JavaScript • Paho MQTT • MQTT-based dashboards • Basic DNS and SSL configuration._

**ZOMIO Inc • Technical Administrative Assistant • Barceloneta, PR • Hybrid • Mar 2019 — June 2022**

- _Provided administrative support to the CEO by managing his calendar, scheduling internal meetings, handling email communication, and organizing shared documents in Google Drive._
- _Prepared and submitted payroll runs in ADP by entering and validating employee time and pay information according to established procedures._
- _Organized financial documentation by filing vendor invoices and expense records in a structured folder system._
- _Coordinated internal technical and status meetings, sending invites, preparing agendas, and taking notes, then storing meeting summaries in Google Drive for later reference._
- _Arranged business travel for the CEO, including booking flights and hotels according to specific requirements, and handled follow‑up calls and emails related to logistics._
- _In the later part of this role, created an internal beta redesign of the company website, which contributed to planning an updated digital presence and preceded a transition into a dedicated front‑end position._
- _Google Workspace (Gmail, Drive) • ADP payroll processing (basic) • Meeting and calendar coordination • Document organization._

## PROJECTS

**Career AI • Developer • July 2025 — Aug 2025; June 2026 • [Demo](https://lasc1026-career-ai.hf.space/)**

- _Originally built a Python‑based career chatbot using Gradio and the OpenAI client SDK, combining prompt templates with a small set of local Markdown files as structured context about Luis Santiago's career background._
- _In a later iteration, implemented AI‑assisted updates using an agents file and targeted prompt constraints to add a guardrails module for basic input validation (including simple jailbreak checks) and to refactor the codebase, reviewing and testing generated changes before keeping them._
- _Refined the UI into a Gradio Blocks layout with a custom header, footer, and light CSS tweaks to present the chatbot as a portfolio‑style application suitable for embedding._
- _Set up GitHub Actions so pushes to the main branch update the Hugging Face Space, and added a scheduled workflow intended to periodically ping the Space to reduce cold starts._
- _Maintain an agents specification file that documents the current architecture, guardrail approach, deployment setup, and a staged plan for future RAG and refactoring work as the project continues to evolve._
- _Python • Gradio • OpenAI SDK • Hugging Face Spaces • GitHub Actions • AI-Assisted Development._

## CERTIFICATIONS & EDUCATION

- **[AWS](https://www.credly.com/badges/ee3ee435-d36b-477f-a2e7-3ea4cb846dd0/public_url) • Certified AI Practitioner • May 2026**
- **[Tricentis](https://academy.tricentis.com/share/v1/gamification/assigned_badge/43da3dea-f51f-46b0-a543-e1195f4c2844/shared?lang=en&t=1780316438300) • Test Design Specialist Level 2 (TDS2) • Mar 2026**
- **[Tricentis](https://academy.tricentis.com/share/v1/gamification/assigned_badge/c8afd5b3-2485-4e53-a12c-8dd99338f8af/shared?lang=en&t=1780316417436) • Test Design Specialist Level 1 (TDS1) • Mar 2026**
- **[Tricentis](https://academy.tricentis.com/share/v1/gamification/assigned_badge/c725e183-98b0-4f90-8fde-470a0cce7106/shared?lang=en&t=1780316394706) • Automation Specialist Level 2 (AS2) • Mar 2026**
- **[Tricentis](https://academy.tricentis.com/share/v1/gamification/assigned_badge/d0331408-06b2-4dba-9b46-5b8b9f10052f/shared?lang=en&t=1780316375651e) • Automation Specialist Level 1 (AS1) • Mar 2026**
- **[Udemy](https://www.udemy.com/certificate/UC-31d92716-9112-43cd-b745-0060687c66de/) • Docker - SWARM - Hands-on - DevOps • Dec 2025**
- **[KodeKloud](https://learn.kodekloud.com/user/certificate/eab7f1dd-5c3e-4338-9290-72a8359b371f) • Docker for the Absolute Beginner - Hands On - DevOps • Dec 2025**
- **[Udemy](https://www.udemy.com/certificate/UC-b7ecbe7b-7a8f-49ca-a06e-d9574b519218/) • Ansible Advanced - Hands-On - DevOps • Dec 2025**
- **[KodeKloud](https://learn.kodekloud.com/user/certificate/de4fcbad-5b3f-4e69-9728-29bbbc9c8900) • Ansible for the Absolute Beginner - Hands-On - DevOps • Dec 2025**
- **[BIG school](https://drive.google.com/file/d/1ZKxWtKuIeqD_R-fYteFtOjMizvSip0K9/view?usp=sharing) • Curso de Iniciación al Desarrollo con IA • Oct 2025**
- **[Udemy](https://www.udemy.com/certificate/UC-33ff0078-2eac-4a80-8690-8b2d747ccfe7/) • Curso de IA web: Nuevo Modelo de Google para JavaScript • Oct 2025**
- **[AWS](https://www.credly.com/badges/f1289a38-cc96-4550-87a7-9a00f3cfb268/public_url) • Certified Cloud Practitioner • May 2025**
- **[Holberton School](https://drive.google.com/file/d/1OEBJ3mwrmCAXIXk3UxCuPaQHNqt1L0zz/view) • Foundations of Computer Science • July 2024**
- **[freeCodeCamp](https://www.freecodecamp.org/certification/fcc97f86d3b-c433-4dce-9c8b-f8d071526a04/responsive-web-design) • Responsive Web Design • Apr 2022**
