# Revised Conversation with Gemini

## Gemini:

Thank you for providing your resume and other professional materials about yourself. I've reviewed your profile and see you have experience as a Software Developer and Web Developer.

To start, could you tell me a bit about what you're looking for in your next role and what motivated you to pursue a career in software development?

## Luis Santiago:

I'm seeking a software developer role that emphasizes deep coding and, ideally, integrates Agentic AI workflows, as I'm keenly interested in gaining hands-on experience in that area. My motivation for software development stems from a profound fascination with problem-solving through code. Initially wary of the PC repair industry, discovering the creative potential of software development, where I could build and fix, was a pivotal moment. Once I started coding, I realized there was no other career path for me; it even reshaped how I approach problem-solving in non-technical situations.

## Gemini:

That's a fantastic and clear vision for your career path\! It's great to hear your passion for problem-solving through code and your specific interest in Agentic AI.

Tell me more about your experience with

JavaScript, TypeScript, and modern frameworks. Could you provide an example of a project where you heavily utilized these technologies and perhaps faced a significant challenge that you overcame?

## Luis Santiago:

I have extensive experience with JavaScript, particularly from my PalitasPR project, where I heavily utilized it with the Svelte framework. While TypeScript is a more recent addition to my skillset and I haven't used it in production yet, I'm actively working to integrate it. In PalitasPR, a key challenge was deeply understanding Svelte's reactivity, local/global context, and stores. Through diligent study of documentation and persistent trial and error, I successfully navigated these complexities, ensuring the project's robust functionality.

## Gemini:

That's a very honest and insightful answer. It's great that you're tackling new technologies like TypeScript and pushing yourself to understand core concepts in frameworks like Svelte more deeply.

Could you elaborate a bit on your PalitasPR project? Specifically, what was the purpose of the platform, and what were some of the key features you implemented? Also, given your role as

Lead Developer on this collaborative project, how did you manage task delegation and ensure adherence to best practices among your team of 5 developers?

## Luis Santiago:

PalitasPR was a collaborative project aimed at creating a platform similar to Facebook Marketplace, but specifically for small businesses and independent contractors—like construction workers or barbers—to easily market themselves and find work. As the Lead Developer for a team of five, I managed Trello boards, planned tasks, and was heavily involved in front-end coding and API implementations.

We faced significant challenges due to tight deadlines and initial team inexperience with project management. I initially fell into micromanagement, but recognized this and shifted my approach. By facilitating strategic discussions rather than dictating, I empowered the team to collectively identify and address issues, which significantly improved our efficiency. This experience taught me invaluable lessons in delegation, trust, and adaptable leadership, highlighting the importance of team buy-in and shared responsibility in overcoming setbacks.

## Gemini:

Thank you for that incredibly detailed and honest account of the PalitasPR project. It was a significant learning experience for you, both technically and in terms of leadership.

The purpose of the platform sounds very impactful – connecting small businesses and independent contractors with potential clients. That's a great example of using technology to solve a real-world problem.

You mentioned managing Trello boards and tasks, planning, having multiple meetings, and doing a lot of the front-end coding and API implementations. This highlights your hands-on involvement.

Given the challenges you faced with deadlines, expectations, and initially falling into micromanagement, it's impressive that you identified the issue and adapted your leadership strategy. Your shift to asking questions to encourage team buy-in and problem-solving is a strong example of self-awareness and growth. The experience of stepping back and trusting your team, even after setbacks, is also a valuable lesson in delegation and building a resilient team.

Thinking about the technical aspects of PalitasPR, you mentioned using Svelte and handling API implementations. Could you walk me through the process of how you designed the front-end architecture for PalitasPR? What were some of the key components or modules, and how did you ensure they communicated effectively, especially considering the reactivity and context challenges you initially faced?

## Luis Santiago:

For PalitasPR, we implemented a monorepo architecture with a Flask and boto3 backend and a Svelte single-page application frontend. We used Vite for development, with Flask serving the built HTML, JavaScript, and CSS. My team and I handled the front-end API integrations using Axios.

A key technical challenge was mastering Svelte's reactivity, as our prior experience was primarily with vanilla JavaScript. We effectively utilized Svelte's $: reactive syntax and stores to manage state. We also adopted a clear component organization strategy, grouping components by page and applying consistent naming conventions, which streamlined development and maintenance despite the newness of the framework.

## Gemini:

That's a very clear explanation of your technical setup for PalitasPR. The monorepo approach with Flask and Svelte, using Vite for development and then Flask for serving, demonstrates a practical understanding of full-stack deployment. Using Axios for API communication is a common and effective choice.

It's particularly interesting to hear about your team's journey with Svelte's reactivity, especially coming from a vanilla JavaScript background. Your ability to leverage $: and Svelte stores to manage state and reactivity, even before the Runes update, shows a strong adaptability to new paradigms. And the component organization by pages with specific naming conventions sounds like a good way to maintain order in a growing project.

Could you elaborate a bit on the specific challenges or learning curves you encountered with Svelte's reactivity beyond just it being "a foreign topic"? For instance, were there any particular scenarios or complex interactions where understanding and implementing reactivity correctly was especially difficult? And how did you approach debugging or troubleshooting when you faced these reactivity-related issues?

## Luis Santiago:

During PalitasPR, we encountered a significant challenge with Svelte's reactivity, specifically with incorrect pagination updates. Our initial debugging involved extensive “console.log”, and “console.table” usage to understand Svelte's update cycles. Despite my efforts to resolve it on the front end, a perceptive teammate proposed shifting pagination entirely to the server-side, arguing it would be a quicker and more robust solution for the backend team. This collaborative problem-solving and my willingness to trust his expertise proved successful. It reinforced the importance of leveraging team strengths and understanding where best to manage data, leading to a much-needed server-side solution for a seemingly front-end problem.

## Gemini:

That's a fantastic real-world example of a common challenge and a smart solution\! It highlights the importance of understanding where to draw the line between client-side and server-side responsibilities, especially with something like pagination, where data integrity and efficient loading are critical.

Your team's approach of using “console.log” and “console.table” for debugging reactivity issues is a classic and effective method, showing a practical, hands-on debugging style. And the collaborative brainstorming, leading to your teammate's insightful suggestion to shift pagination to the server, demonstrates excellent teamwork and a willingness to leverage different strengths within the group.

This story also reinforces your earlier point about learning to trust your teammates and recognizing when to delegate. It's a sign of a strong lead developer who can identify when a problem might be better solved elsewhere.

Considering your experience at ZOMIO Inc. as a Frontend Web Developer, you mentioned creating and redesigning websites and web applications, including deploying the company website on HostGator with SSL setup and domain configuration.

Could you elaborate on the technical steps involved in deploying a company website on HostGator with SSL setup and domain configuration? What were some of the challenges you encountered during this process, and how did you ensure the security and performance of the deployed site?

## Luis Santiago:

As a Frontend Web Developer at ZOMIO Inc., my first major task was redesigning and deploying the company website on HostGator, complete with SSL and domain configuration. This process involved researching hosting options, migrating the domain from GoDaddy—which presented challenges due to propagation times—and activating the included SSL certificate. Successfully deploying this mobile-responsive landing page honed my understanding of end-to-end web deployment. Additionally, I developed two web application MVPs utilizing MQTT to process real-time data from IoT devices via a Mosquitto broker, which significantly deepened my experience with dynamic data handling.

## Gemini:

That's a fascinating origin story for your career transition into web development at ZOMIO Inc.. It's great to hear how you proactively demonstrated your skills and how your CTO provided unconventional but effective guidance.

You handled the entire process of researching hosting services, migrating the domain, and setting up SSL for the company website on HostGator. This shows a strong grasp of the end-to-end deployment process.

Regarding the security and performance aspects of the deployed site, you mentioned setting up the SSL certificate. Beyond that, were there any other specific measures you took, or performance optimizations you implemented, to ensure the site was secure and performed well, especially given it was a single landing page? And how did you monitor its performance after deployment?

## Luis Santiago:

To ensure the ZOMIO Inc. website's security and performance, I primarily focused on a lightweight approach, using vanilla JavaScript, HTML, and CSS to minimize framework bloat. I rigorously utilized Chrome and Safari developer tools to monitor performance and ensure responsiveness across a spectrum of screen sizes. Crucially, I performed extensive testing on various real devices, including Android tablets, iPads, laptops, and iPhones, to guarantee a seamless user experience across different platforms.

## Gemini:

That's a very thorough and practical approach to ensuring performance and responsiveness, especially for a first official project\! Utilizing browser developer tools for performance and scaling checks, along with testing on a wide range of actual devices (Android tablet, iPad, laptop, iPhone), demonstrates a strong commitment to delivering a high-quality user experience.

Your point about using vanilla technologies to avoid framework bloat and slowdowns is also well-taken, as it can indeed contribute to a lightweight and fast initial load.

Moving on to your professional projects and client work, you have several listed. Let's discuss your Web Developer \- Svelte HVAC Portfolio (Client Work) project. You mentioned you developed a modern, responsive web application and optimized performance for a seamless user experience.

Could you describe in more detail the design process you followed for this HVAC portfolio? How did you ensure a "mobile-first" and "user-friendly design" while also aligning with the client's brand identity and requirements? What specific optimizations did you implement to achieve that "seamless user experience"?

## Luis Santiago

For the Svelte HVAC Portfolio, I applied lessons from PalitasPR to ensure a highly organized and efficient development process. The design centered on a mobile-first, user-friendly approach, utilizing media queries to build layouts from the smallest screens upward, which streamlined responsiveness. To achieve a seamless user experience, I integrated subtle animations, selected a clean color palette harmonizing with the client's branding, and ensured visual symmetry for intuitive navigation across its multiple routes. Additionally, I implemented a language-switching feature for English and Spanish, significantly enhancing its accessibility for a broader audience.

## Gemini:

That's a clear explanation of your approach to the Svelte HVAC Portfolio project. It's great to hear that you applied lessons learned from PalitasPR, demonstrating continuous improvement in your development process.

Your strategy of using Svelte for a mid-sized project with multiple routes, and specifically designing with a "mobile-first" approach using media queries, is a strong indication of your practical web development skills. The focus on clean, easy-to-understand layouts, subtle animations, and a harmonious color palette based on the client's branding also speaks to your attention to user experience and design principles.

Given this context, could you elaborate on how you approached the localization aspect for the HVAC portfolio, specifically the ability to switch between English and Spanish? What libraries or techniques did you use to implement this feature, and what were some of the challenges, if any, in managing the content for both languages?

## Luis Santiago:

The localization for the HVAC portfolio, enabling English and Spanish toggling, was an added feature I offered due to my belief in the client's vision and our excellent working relationship. Given tight deadlines, I pragmatically hard-coded the content using Svelte's reactivity and stores, storing texts in a JavaScript object and dynamically swapping string literals. As a bilingual speaker, I handled the translations directly, collaborating with the client for feedback. This efficient "flag-type" approach proved effective for a two-language scenario, though I would opt for a dedicated localization library for more extensive multilingual projects.

## Gemini:

That's a fantastic example of going above and beyond for a client, especially when you believed in their vision and had a good working relationship\! Your decision to hard-code the localization due to time constraints, leveraging your bilingualism and Svelte's reactivity and stores, demonstrates resourcefulness and efficiency.

The "flag type of thing" approach, where you swapped string literals with store variables, is a clever and pragmatic solution for a two-language scenario when time is critical. It's also smart that you acknowledged when a library would be necessary for more complex or multi-language projects.

This story also highlights your strong client communication, as you collaborated with the client on the translations to ensure accuracy and alignment with their brand.

Switching gears a bit, your resume mentions you're open to relocating to York, PA. Could you tell me more about your motivation for this potential relocation?

## Luis Santiago:

I'm motivated to relocate to York, PA, to pursue software development opportunities, acknowledging the current junior job market in Puerto Rico. My brother in York has generously offered support for my relocation if I secure a hybrid or on-site development role. My passion for software development is unwavering; I am committed to growing in this field. I literally think in programming terms, constantly seeking solutions, coding daily, and continuously learning—it's become an integral part of who I am.

## Gemini:

That's a very clear and passionate explanation of your motivation for relocating to York, PA, and your unwavering commitment to a career in software development. It's truly inspiring to hear how deeply ingrained programming and problem-solving have become in your daily life.

Your proactive approach to finding a suitable location and your continuous learning, even in the current challenging job market, demonstrate immense dedication and resilience.

Since you're actively seeking a software developer role and are particularly interested in "deep diving into the coding aspect" and gaining hands-on experience with Agentic AI workflows, let's explore that further.

Could you tell me more about what specifically about Agentic AI workflows excites you? Have you had any personal projects, studies, or even theoretical explorations into this area? If not, what steps are you taking to learn more about it and potentially integrate it into your skillset?

## Luis Santiago:

My interest in Agentic AI workflows is recent but rapidly growing, and I'm currently advancing my knowledge through an Udemy course on agentic workflows and frameworks. For my first project, I'm developing an AI Chatbot clone of myself, which I intend to embed in my revamped web portfolio. This personal project serves a dual purpose: it allows me to apply new Agentic AI concepts hands-on and simultaneously enhances my portfolio to showcase these emerging skills to recruiters, even utilizing data from conversations like this to refine the chatbot's capabilities

## Gemini:

That's a fantastic and very practical application of your learning\! It's great to hear you're diving into Agentic AI through an Udemy course and immediately applying that knowledge to a personal project – an AI Chatbot clone of yourself for your portfolio. That's a unique and very engaging way to showcase your skills and interests.

It also makes perfect sense that you're using this interview practice and data collection for that very purpose. This helps me understand your goals even better.

You mentioned you're "revamping the portfolio just for this purpose" of embedding the chatbot. Could you tell me a bit about your existing portfolio (lusanco.github.io ) and what specific changes or additions you envision to integrate this Agentic AI chatbot seamlessly? What technologies do you anticipate using for this revamp?

## Luis Santiago:

My existing portfolio, built with Astro.js in a bento-style layout, serves as a concise one-pager showcasing my key projects, resume, and skills. To integrate the Agentic AI chatbot, I plan a complete revamp. I'm weighing two options for the rebuild: React, for its strong market employability, despite the learning curve; or Svelte, Astro, or vanilla JavaScript for faster development and seamless chatbot integration, allowing me to continue my Udemy course with minimal interruption. The chatbot itself will be built using Gradio, with a focus on customizing its appearance to match the portfolio's aesthetic.

## Gemini:

That's a clear breakdown of your current portfolio and your plans for integrating the AI chatbot. The bento-style layout on Astro.js sounds like a modern and effective way to showcase your key information and work.

It's a common dilemma for developers to choose between employability and development speed, especially when integrating new technologies. Your two options, React for broader market appeal versus Svelte/Astro/Vanilla JS for quicker integration and continued learning, are well-reasoned.

Regarding the integration of Gradio for the chatbot and your intention to customize its appearance to match your portfolio, that's a good plan for maintaining a consistent user experience.

Given these considerations, what are some of the specific features or interactions you envision for your AI chatbot clone? Beyond simply answering questions about your background, how do you see it enhancing the user experience on your portfolio, and what kind of "personality" or tone do you plan for it to convey?

## Luis Santiago:

My AI chatbot is strategically designed to accurately reflect my professional background and experience, serving as an interactive representation of my capabilities for recruiters. The goal is for it to answer questions about my career as if I were speaking directly, aiming for a tone that is authentic yet maintains a professional and formal touch. This will make my portfolio highly engaging and provide an accessible initial insight into my skills and approach.

## Gemini:

That's a very clear and strategic vision for your AI chatbot. Having it accurately reflect your career and experience, especially for recruiters, is an excellent use case. It's a proactive way to offer an interactive and accessible first impression of your capabilities, even with limited experience in AI.

Regarding the personality, aiming for a tone that is "closer to how I would answer normally, but with a pinch of formal/professional" is a great balance. This would allow your authentic communication style to come through while still maintaining the appropriate professional decorum for a portfolio interaction.

Beyond simply answering questions, do you envision any specific types of questions or interactions that you would want the chatbot to excel at? For example, would you want it to be able to delve deeper into technical explanations of your projects, or perhaps provide more insight into your problem-solving approach based on past challenges?

## Luis Santiago:

That's an excellent suggestion, and I hadn't initially considered that depth. I will certainly incorporate the ability for the chatbot to delve deeper into technical explanations of my projects, like PalitasPR, and provide more insight into my problem-solving approaches based on past challenges. This will significantly enhance its utility for recruiters seeking to understand my thought process and technical expertise.

## Gemini:

That's fantastic to hear\! It sounds like a natural and powerful extension of your chatbot's capabilities. Focusing on technical explanations of your projects and providing insights into your problem-solving approach based on past challenges will make your chatbot a much more valuable and interactive tool for recruiters. It'll allow them to understand not just what you did, but how you think and learn as a developer.

This also ties back to your interest in Agentic AI, as the chatbot will need to intelligently process questions and retrieve/articulate relevant technical details and lessons learned.

Given your plan to have the chatbot delve deeper into technical explanations and problem-solving, what are some specific technical aspects or challenges from your projects (e.g., PalitasPR, ZOMIO Inc. deployments, HVAC Portfolio) that you would prioritize for the chatbot to be able to explain in detail?

## Luis Santiago:

My approach to implementing those detailed explanations will be iterative. I plan to develop the initial version of the chatbot, then refine its capabilities based on insights gained from this conversation and further development. This agile strategy will allow me to determine the most impactful technical aspects and problem-solving scenarios to prioritize for in-depth discussion within the chatbot.

## Gemini:

That's a very pragmatic and iterative approach. It makes perfect sense to build the initial version of your chatbot and then use the insights gained from this conversation, along with further development, to refine its capabilities and determine the specific technical deep-dives it should handle. It's a great example of applying agile principles to a personal project.

I see on your resume that before transitioning to a Frontend Web Developer role at ZOMIO Inc., you served as an Administrative Assistant for over three years at the same company. Could you tell me more about that role and what transferable skills you gained during that time that you believe are valuable in your current software development career?

## Luis Santiago:

My role as an Administrative Assistant at ZOMIO Inc. cultivated critical transferable skills for software development, particularly in organization and process management. I gained a strong framework for time management, effectively categorizing work materials, and streamlining office tasks. Taking on responsibilities like managing executive communications and coordinating meetings also provided me with invaluable insights into broader business operations, deliverables, and expectations. This background gave me a unique perspective on project flow and team collaboration, which directly enhances my understanding of development processes beyond just coding.

## Gemini:

That's a very insightful perspective on your administrative assistant role and how it prepared you for software development. You gained valuable skills beyond just clerical tasks.

You mentioned you "got close to the development team and oversaw their progress as needed to update." Could you elaborate on what aspects of the development team's work specifically "struck and fascinated" you, leading you to pursue a career as a developer? What did you observe that made you feel this was the right path for you?

## Luis Santiago:

What truly fascinated me about the development team at ZOMIO Inc. was their problem-solving approach. It felt like magic to me at first, but observing how they meticulously broke down complex issues, articulated technical possibilities and limitations, and engineered solutions from the ground up was incredibly inspiring. The ability to create and fix things that seemed to appear out of thin air resonated deeply with me. This profound insight redirected my career path entirely, moving me away from a prior negative perception of the tech industry and firmly towards software development, driven by a desire to build and innovate ethically.

## Gemini:

That's a powerful revelation. It sounds like witnessing the problem-solving process and the tangible creation of "magic" by the development team was a stark contrast to your previous perception of the tech world.

Your motivation is deeply rooted in a desire to build and create ethically.

Beyond the specific projects we've discussed, like PalitasPR and the HVAC portfolio, your resume mentions you developed an "Alpine.js Static Website" for a client. Could you tell me more about that project? What was the client's goal, what unique challenges did you face using Alpine.js, and how did you manage content integration for that site?

## Luis Santiago:

My Alpine.js static website project was developed for a church client, aiming to enhance their online presence by closely matching their brand identity. It was a simpler, single-page application where I used Alpine.js to manage dynamic content display, effectively emulating multiple "pages" by switching the visible "state" of the code in the browser. The client provided all branding materials, simplifying content integration as it was primarily hard-coded given the static nature of the site. A key learning curve was fully grasping the core philosophy and scope of Alpine.js, emphasizing the importance of thorough research when selecting technologies to ensure optimal fit for project requirements.

## Gemini:

It sounds like the Alpine.js website project was a valuable learning experience, particularly in understanding framework scope.

You mentioned it was a "SPA-type of project" where you used Alpine.js to switch the "state" of the code. Could you elaborate on how you managed the content for this static website? Given that the client provided all the branding materials, how did you integrate that content, including text, images, and brand color schemes, to ensure it aligned perfectly with their requirements and maintained ease of maintenance?

## Luis Santiago:

For the Alpine.js static website, all content, including text, images, and branding materials, was hard-coded directly into the site. Given it was a static page with unchanging information, this was the most efficient approach instead of complex storage solutions. The design incorporated the church's logo colors—predominantly three colors, including white—allowing me to create a clean, professional, and visually aligned layout that perfectly matched their brand identity. This project was completed just before I began my formal education at Holberton Coding School, providing foundational experience in client communication and basic web design.

## Gemini:

That clarifies your approach to the Alpine.js static website, especially with hard-coding content due to its static nature and directly using the church's logo colors for the design. It sounds like a practical solution for the project's scope at that time.

You mentioned that this project was a month before you started at Holberton Coding School, where you focused on "Foundations of Computer Science". That program covered several key areas, including C, Python, SQL, Bash Scripting, and Git & GitHub.

Could you tell me more about your experience at Holberton? Specifically, for one of the projects or tasks, how did you "implement a custom printf and shell interpreter while applying core concepts like memory management" in C? What were some of the key challenges you faced during that project, and how did you overcome them?

## Luis Santiago:

At Holberton School, our C projects, such as implementing a custom printf and a shell interpreter, were designed to solidify our understanding of low-level concepts like memory management, mutability, and immutability. Having previously worked only with JavaScript, adapting to C's intricacies was challenging. For the printf project, my teammate and I overcame hurdles through extensive practice and trial and error. For the shell interpreter, I completed it individually, which significantly deepened my understanding and resilience. Ultimately, C taught me fundamental development principles and provided "aha" moments that connected back to real-world insights shared by my previous CTO, proving invaluable despite my current focus on higher-level languages.

## Gemini:

It's clear that your C projects at Holberton, despite the initial hurdles, were foundational in solidifying your understanding of core development concepts and even connected back to insights from your previous CTO. The experience of working on challenging projects, even without a teammate, speaks to your perseverance.

Beyond C, your time at Holberton also involved significant work with Python, where you "Built full-stack applications with Flask, integrating RESTful APIs and SQLAlchemy while applying OOP principles."

Could you share more about a specific project where you applied these Python skills? What kind of full-stack application did you build? What challenges did you encounter integrating Flask with RESTful APIs and SQLAlchemy, and how did you leverage Object-Oriented Programming (OOP) principles to structure your code effectively?

## Luis Santiago:

My Python coursework at Holberton School involved building full-stack applications with Flask, culminating in an Airbnb clone demo called HBnB. This project was instrumental in solidifying my understanding of server-side concepts and full-stack workflows. While I encountered significant configuration challenges with MySQL and PostgreSQL on my local machine, I persevered, demonstrating my ability to troubleshoot environmental issues effectively. We extensively applied Object-Oriented Programming (OOP) principles, structuring our code with classes for RESTful actions, ensuring data integrity by allowing specific actions only through designated endpoints, and leveraging inheritance to avoid redundant code.

## Gemini:

It sounds like your Python work, particularly the HBnB project, solidified your understanding of full-stack concepts, even if you faced environmental configuration challenges. It's also clear you grasped the practical application of OOP principles for structuring robust applications.

Your resume also highlights your proficiency in Bash Scripting from Holberton, stating you "Automated project setup and streamlined development tasks using shell scripting and command-line tools."

Could you provide a specific example of a development task you automated or a project setup you streamlined using Bash scripting? What problem were you trying to solve with the script, and what was the impact or benefit of using Bash for that particular task?

## Luis Santiago:

While my Bash scripting coursework at Holberton focused on foundational concepts, I later applied these skills to automate personal development tasks. Post-graduation, I grew tired of manually setting up new project environments. To streamline this, I created a Bash script that, with a single click, automates the installation of my frequently used npm packages and applies standard file configurations. This significantly boosts my efficiency, allowing me to quickly establish a fully working development environment and focus directly on coding.

## Gemini:

That's a very practical and efficient application of Bash scripting—automating your development environment setup can save a lot of time and reduce repetitive tasks. It demonstrates a proactive approach to streamlining your workflow.

Shifting gears a bit, I see you earned the AWS Certified Cloud Practitioner (CLF-C02) certification in May 2025\. Given your primary focus on frontend development, how does this certification tie into your career goals? Are there any specific projects or learning experiences related to AWS that you've been involved with, or that you plan to pursue, that leverage this foundational cloud knowledge?

## Luis Santiago:

I pursued the AWS Certified Cloud Practitioner certification strategically, recognizing the increasing industry reliance on cloud infrastructure. My goal was to gain foundational cloud knowledge from a market leader like AWS, providing a competitive advantage. While I haven't directly applied these skills in projects yet, I plan to integrate them with my ongoing Agentic AI training. I believe understanding cloud environments is a natural and necessary progression for deep diving into AI, given the growing convergence of these two critical technological areas.

## Gemini:

That's a very strategic approach to your AWS certification, and it makes perfect sense to integrate that foundational cloud knowledge with your Agentic AI pursuits, given the growing convergence of those fields.

Looking further back in your professional journey, you also have experience as a Computer Technician Assistant at Dewey University. While not a direct software development role, could you share what you learned or what skills you developed in that position that you believe are valuable or transferable to your current path as a software developer?

## Luis Santiago:

My experience as a Computer Technician Assistant at Dewey University provided me with valuable foundational IT skills, such as assigning IP addresses and managing data backups. While not direct software development, these skills are highly transferable and crucial for understanding the broader technical ecosystem in which software operates. This role broadened my problem-solving toolkit, enhancing my ability to approach technical challenges systematically and contributing to my overall effectiveness within a software development team.

## Gemini:

It's valuable to hear how your experience as a Computer Technician Assistant provided you with foundational IT skills. Understanding aspects like IP addressing, backups, and general technical troubleshooting certainly broadens your problem-solving toolkit and can be highly relevant in various technical roles, including those within a software development team or a tech-dependent company. It shows a comprehensive approach to understanding systems and how they function.

We've covered a wide array of your professional experiences, from your motivations for becoming a developer and your foundational computer science education to specific projects and how you're strategically building your skills with certifications like AWS and your interest in Agentic AI.

To wrap up our discussion, is there anything else you'd like to highlight about your professional background, skills, or career goals that we haven't touched upon, and that you believe would be important for me to know as a recruiter?

## Luis Santiago:

At this moment, I believe we've covered my professional background and skills comprehensively. Thank you for your time and the insightful questions; it's been a very helpful discussion.

## Gemini:

It was my pleasure, Luis\! I appreciate you taking the time to share such detailed insights into your professional journey. This has been a very comprehensive and helpful discussion.

I wish you the very best in your job search and with your continued development in the exciting field of Agentic AI\!  
