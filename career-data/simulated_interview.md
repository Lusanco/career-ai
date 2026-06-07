# Conversation with Gemini

## Gemini:

Thank you for providing your resume and other professional materials about yourself. I've reviewed your profile and see you have experience as a Software Developer and Web Developer.

To start, could you tell me a bit about what you're looking for in your next role and what motivated you to pursue a career in software development?

## Luis Santiago:

I am looking for a software developer role that deep dives into the coding aspect. If possible, a role where agentic AI is a core element of the workplace workflow to gain hands-on experience in this topic. I am growing more interested in Agentic AI workflows.

As to what motivated me to pursue this career, I can say that at first I did not know this career path existed, and was wary of the repair PC industry. When I got to know this path in technology and the possibilities of fixing and solving problems and its potential, I just could not be interested.

Once I learned coding, I knew there was no other career path for me. I learn to solve like a developer even in non-technical situations.

## Gemini:

That's a fantastic and clear vision for your career path\! It's great to hear your passion for problem-solving through code and your specific interest in Agentic AI.

Tell me more about your experience with

JavaScript, TypeScript, and modern frameworks. Could you provide an example of a project where you heavily utilized these technologies and perhaps faced a significant challenge that you overcame?

## Luis Santiago:

As for typescript, I learned that recently and have not used it in production projects. As for JavaScript, I heavily used it for my PalitasPR project with the frontend framework Svelte. As for the difficulties, I found that reactivity, local, global context, and stores were something I needed a deeper understanding of at that time. However, A bit of documentation and elbow grease, and a lot of trial and error proved to be the winner in this situation.

## Gemini:

That's a very honest and insightful answer. It's great that you're tackling new technologies like TypeScript and pushing yourself to understand core concepts in frameworks like Svelte more deeply.

Could you elaborate a bit on your PalitasPR project? Specifically, what was the purpose of the platform, and what were some of the key features you implemented? Also, given your role as

Lead Developer on this collaborative project, how did you manage task delegation and ensure adherence to best practices among your team of 5 developers?

## Luis Santiago:

So PalitasPR is a project created by a group of developers in response to having the opportunity to present our idea in front of different types of recruiters as a part of an event that also officially graduated us as software developers.

We chose to create this platform to solve the problem of small business or independent contractors and people that do all different types of odd jobs to market themselves and find work most accessible without the hurdles of not having to deal to not being known.

Think of Facebook Marketplace, but for construction workers, barbers, cleaning services, electricians, and similar professionals. We found that usually these people don't use social media or have the desire to do so, or simply do not know how to market themselves effectively.

As a Lead Developer, I managed Trello boards and tasks, planned, had multiple meetings, and coded most of the frontend and API implementations on the frontend. I had decision-making meetings with the backend team to gain perspective and be able to move forward effectively. I provided guidance for the rest of the frontend team and taught them every tip and trick I have picked up over the past months.

For context, it was my first time being a lead in development, and my teammates' first time on a team. And not everything was peaches and cream. We had a tight deadline, and we grew too ambitious. We had a lot of setbacks with some of my teammates not understanding deadlines, expectations vs realities in the MVP we set to follow. I was caught in the trap of micromanaging, because if it had not been done, we would never have made it. But I understand I did not manage it initially in the correct manner.

So I started to be strategic with our meetings, asking about the MVP and what we needed to accomplish our goal instead of stating it; I just asked. Since I had almost everything under control, the underlying problem was not apparent, but with this new strategy, the backend team started to raise some questions, and then, like a domino effect, everyone started to understand, bit by bit, the magnitude of needing to fix this immediately. After that, the majority voted decided the best outcome, of course, I removed myself from the vote to be fair.

After that, the developer I appointed as the backend team leader suggested I take a full week off. This is where my learning skyrocketed. I took his advice, shaved off my immense burnout, and got the real perspective in my role. I can rely on any other developer; I do not have to be the one burdened by it all. In the light of one or two setbacks, they are twice as likely as developers to focus on the deadline and the MVP and follow it through.

I learned to lead, and I learned to follow in the leading position. Even though this is something people hide, I am proud I overcame this. I am happy I can identify these types of traps from that moment onwards.

## Gemini:

Thank you for that incredibly detailed and honest account of the PalitasPR project. It was a significant learning experience for you, both technically and in terms of leadership.

The purpose of the platform sounds very impactful – connecting small businesses and independent contractors with potential clients. That's a great example of using technology to solve a real-world problem.

You mentioned managing Trello boards and tasks, planning, having multiple meetings, and doing a lot of the front-end coding and API implementations. This highlights your hands-on involvement.

Given the challenges you faced with deadlines, expectations, and initially falling into micromanagement, it's impressive that you identified the issue and adapted your leadership strategy. Your shift to asking questions to encourage team buy-in and problem-solving is a strong example of self-awareness and growth. The experience of stepping back and trusting your team, even after setbacks, is also a valuable lesson in delegation and building a resilient team.

Thinking about the technical aspects of PalitasPR, you mentioned using Svelte and handling API implementations. Could you walk me through the process of how you designed the front-end architecture for PalitasPR? What were some of the key components or modules, and how did you ensure they communicated effectively, especially considering the reactivity and context challenges you initially faced?

## Luis Santiago:

We decided on creating a monorepo where the backend was created with Flask and boto3, and the frontend as an SPA. We have set Svelte via Vite to communicate with the Flask backend for development, then build the project with its build step directly to the designated folder where Flask serves the HTML, JavaScript, and CSS to the client. The API in the backend was managed and developed by the backend team, but the frontend side of things was created with the Axios library by me and my frontend team.

As for the reactivity, it was a foreign topic to all of us since my frontend experience was directly with vanilla JS and manipulating the frontend without a framework. I am sure we can now do better, but for that time, we made do with the Svelte reactive syntax "$:" and the use of the stores. Worked like a charm. For context, this is the Svelte version before the massive update including Runes.

We had global styles, not CSS modules. And we organized the components by pages, if the login page had 3 different types of buttons and a textbox or any other component, it would belong to that directory and be named accordingly with the correct prefix.

For this topic of reactivity and the component organization, although it proved challenging, there was no communication challenge. We were all on board.

## Gemini:

That's a very clear explanation of your technical setup for PalitasPR. The monorepo approach with Flask and Svelte, using Vite for development and then Flask for serving, demonstrates a practical understanding of full-stack deployment. Using Axios for API communication is a common and effective choice.

It's particularly interesting to hear about your team's journey with Svelte's reactivity, especially coming from a vanilla JavaScript background. Your ability to leverage $: and Svelte stores to manage state and reactivity, even before the Runes update, shows a strong adaptability to new paradigms. And the component organization by pages with specific naming conventions sounds like a good way to maintain order in a growing project.

Could you elaborate a bit on the specific challenges or learning curves you encountered with Svelte's reactivity beyond just it being "a foreign topic"? For instance, were there any particular scenarios or complex interactions where understanding and implementing reactivity correctly was especially difficult? And how did you approach debugging or troubleshooting when you faced these reactivity-related issues?

## Luis Santiago:

Yes\! We faced issues with Svelte updating more than the times we expected. We did a lot of console logs and console tables to see every time something changed due to reactivity, and eventually understood it better, but it still affected one part of our project that even I, with that bit of experience, could not figure out, and that was pagination. It was updating the pagination incorrectly, and it was resulting in a major bug. We had some meetings and joint brainstorming ideas on how to tackle this, I was dead set that this was a frontend problem that I only needed a little time to fix it but my clever teammate (the one suggesting my week off and the one who solved the problem before making the suggestion) said that he thinks that pagination should be entirely managed in the server side of things. He had some compelling reasons at that time, but the one that stuck with me was the words "I think frontend has too much work, we in the backend can easily fix this with one day of reading documentation, trust me." So yeah, that's how we tackled that hurdle.

## Gemini:

That's a fantastic real-world example of a common challenge and a smart solution\! It highlights the importance of understanding where to draw the line between client-side and server-side responsibilities, especially with something like pagination, where data integrity and efficient loading are critical.

Your team's approach of using “console.log” and “console.table” for debugging reactivity issues is a classic and effective method, showing a practical, hands-on debugging style. And the collaborative brainstorming, leading to your teammate's insightful suggestion to shift pagination to the server, demonstrates excellent teamwork and a willingness to leverage different strengths within the group.

This story also reinforces your earlier point about learning to trust your teammates and recognizing when to delegate. It's a sign of a strong lead developer who can identify when a problem might be better solved elsewhere.

Considering your experience at ZOMIO Inc. as a Frontend Web Developer, you mentioned creating and redesigning websites and web applications, including deploying the company website on HostGator with SSL setup and domain configuration.

Could you elaborate on the technical steps involved in deploying a company website on HostGator with SSL setup and domain configuration? What were some of the challenges you encountered during this process, and how did you ensure the security and performance of the deployed site?

## Luis Santiago:

Yes, this is when it all officially started. Before transitioning from admin assistant for the CEO and its company, I took a Responsive Design Course on freeCodeCamp.org. From there, I actively showed my progress to my employer, and then the CTO decided to offer some guidance. It was unconventional yet effective to learn from the CTO since I only knew frontend, and he had only developed on hardware. But I learned a lot even if I did not understand fully (and came to understand later on when working on PalitasPR).

So my first task was to redesign the company website, which entailed that I researched the hosting service and what were the complications of migrating from the old hosting. If I remember correctly, it was on Google Pages or something similar to a website builder, and the domain name was purchased from GoDaddy.

I did the research, had a meeting with the CEO (for context, we were a small team startup), and the CEO let the decision making to me. So I picked HostGator for its affordability and ratings across the web.

After that, I had to learn how to migrate the domain name. Learned the hard way about the propagation times leading up to 72 hours at max. And learned and set up the SSL certificate, which was straightforward since HostGator has it included, and only needed to activate/apply it.

The biggest issue was the domain name transfer. And the wait for the page to be available once the migration occurred. After that, everything was as expected. It was a simple task, a single landing page, mobile responsive, and all.

As for the other web apps, those were not deployed. There were 2 MVPs and their multiple iterations using MQTT to catch messages sent by a MQTT-enabled device through a Mosquitto broker.

## Gemini:

That's a fascinating origin story for your career transition into web development at ZOMIO Inc.. It's great to hear how you proactively demonstrated your skills and how your CTO provided unconventional but effective guidance.

You handled the entire process of researching hosting services, migrating the domain, and setting up SSL for the company website on HostGator. This shows a strong grasp of the end-to-end deployment process.

Regarding the security and performance aspects of the deployed site, you mentioned setting up the SSL certificate. Beyond that, were there any other specific measures you took, or performance optimizations you implemented, to ensure the site was secure and performed well, especially given it was a single landing page? And how did you monitor its performance after deployment?

## Luis Santiago:

At the time, I used the Chrome developer tools as well as other browser tools like the Safari one to ensure the page was performant and scaling properly from the smallest mobile screen to the largest TV or PC monitor. No performance issues were detected since it was my very first official project to deliver, and the technologies I used were vanilla, and did not carry the framework bloat and slowdowns. Besides the development suite I used, I also tested on real devices like an Android tablet, iPad, laptop, iPhone, etc.

## Gemini:

That's a very thorough and practical approach to ensuring performance and responsiveness, especially for a first official project\! Utilizing browser developer tools for performance and scaling checks, along with testing on a wide range of actual devices (Android tablet, iPad, laptop, iPhone), demonstrates a strong commitment to delivering a high-quality user experience.

Your point about using vanilla technologies to avoid framework bloat and slowdowns is also well-taken, as it can indeed contribute to a lightweight and fast initial load.

Moving on to your professional projects and client work, you have several listed. Let's discuss your Web Developer \- Svelte HVAC Portfolio (Client Work) project. You mentioned you developed a modern, responsive web application and optimized performance for a seamless user experience.

Could you describe in more detail the design process you followed for this HVAC portfolio? How did you ensure a "mobile-first" and "user-friendly design" while also aligning with the client's brand identity and requirements? What specific optimizations did you implement to achieve that "seamless user experience"?

## Luis Santiago

I leveraged Svelte for this project since it was a mid-sized project having about 7 defined routes/pages, and 1 dynamic route laying out 2 additional pages, I should say. I used everything learned from the PalitasPR project, and was more organized, learning from past encounters. I created this page so the user can switch between English and Spanish. Mobile first, I refer to developing the layouts in mobile first before complicating the whole app by developing desktop first and then changing every layout when it is more effective to develop with media queries from the mobile up. And user-friendly is the ability to be able to create clean layouts easy to understand, and not confusing to the end-user. The page has subtle animations to highlight or emphasize some sections, and a clean color palette I chose for the client based on the client's logo and preferences. And fonts and box sizes, or layout work in harmony due to their very close symmetry approach to designing the website.

## Gemini:

That's a clear explanation of your approach to the Svelte HVAC Portfolio project. It's great to hear that you applied lessons learned from PalitasPR, demonstrating continuous improvement in your development process.

Your strategy of using Svelte for a mid-sized project with multiple routes, and specifically designing with a "mobile-first" approach using media queries, is a strong indication of your practical web development skills. The focus on clean, easy-to-understand layouts, subtle animations, and a harmonious color palette based on the client's branding also speaks to your attention to user experience and design principles.

Given this context, could you elaborate on how you approached the localization aspect for the HVAC portfolio, specifically the ability to switch between English and Spanish? What libraries or techniques did you use to implement this feature, and what were some of the challenges, if any, in managing the content for both languages?

## Luis Santiago:

Well, the localization was not part of the deal initially. But I believe in the client's vision, and the respect he showed to my work was unbelievable. So, even though we were short on time, I offered to make the localization. Since time was of the essence and I wanted him to have his web app as soon as possible and see his genuine smile, I opted to hard-code the localization and switch language based on a click of a button, leveraging the reactive nature and stores of Svelte. The texts themselves were saved in a JavaScript file in the object format. There was no challenge since this was a nifty trick, like a flag type of thing in coding. I just replaced the text with string literals and stored variables. I have to mention that I chose this approach because I am bilingual and understand these languages natively. If the client needed more languages, I would have chosen a library, no matter the time frame, since I believe he would extend it if that were the case. Also, I translated all the text and had the client's feedback since he was also bilingual.

## Gemini:

That's a fantastic example of going above and beyond for a client, especially when you believed in their vision and had a good working relationship\! Your decision to hard-code the localization due to time constraints, leveraging your bilingualism and Svelte's reactivity and stores, demonstrates resourcefulness and efficiency.

The "flag type of thing" approach, where you swapped string literals with store variables, is a clever and pragmatic solution for a two-language scenario when time is critical. It's also smart that you acknowledged when a library would be necessary for more complex or multi-language projects.

This story also highlights your strong client communication, as you collaborated with the client on the translations to ensure accuracy and alignment with their brand.

Switching gears a bit, your resume mentions you're open to relocating to York, PA. Could you tell me more about your motivation for this potential relocation?

## Luis Santiago:

I acknowledge that jobs in software development, especially for juniors, are strongly lacking, especially in Puerto Rico. I will be honest, I just want to work in software development. I have my brother in York, PA, and he is willing to let me stay if I land a development role, hybrid, or at that location. I want to grow as a software developer. I feel this is my career path, and frankly, even if I don't land a job in this field, I am kind of locked in, as I think in programming terms, I search for solutions, I still code every day, and learn every day. I love software development. After knowing, I cannot unknow.

## Gemini:

That's a very clear and passionate explanation of your motivation for relocating to York, PA, and your unwavering commitment to a career in software development. It's truly inspiring to hear how deeply ingrained programming and problem-solving have become in your daily life.

Your proactive approach to finding a suitable location and your continuous learning, even in the current challenging job market, demonstrate immense dedication and resilience.

Since you're actively seeking a software developer role and are particularly interested in "deep diving into the coding aspect" and gaining hands-on experience with Agentic AI workflows, let's explore that further.

Could you tell me more about what specifically about Agentic AI workflows excites you? Have you had any personal projects, studies, or even theoretical explorations into this area? If not, what steps are you taking to learn more about it and potentially integrate it into your skillset?

## Luis Santiago:

I am fairly new to this. I am taking an Udemy course on this. From agentic workflows to agentic frameworks. I finished week 1 and am tasked with creating the first project. This is an AI Chatbot clone of me. I plan to embed this chatbot in my web portfolio, so it would take time before I continue the agentic course, since I have to revamp the portfolio just for this purpose. The reason for collecting all this data is for this purpose, as well as practicing my interview skills.

## Gemini:

That's a fantastic and very practical application of your learning\! It's great to hear you're diving into Agentic AI through an Udemy course and immediately applying that knowledge to a personal project – an AI Chatbot clone of yourself for your portfolio. That's a unique and very engaging way to showcase your skills and interests.

It also makes perfect sense that you're using this interview practice and data collection for that very purpose. This helps me understand your goals even better.

You mentioned you're "revamping the portfolio just for this purpose" of embedding the chatbot. Could you tell me a bit about your existing portfolio (lusanco.github.io ) and what specific changes or additions you envision to integrate this Agentic AI chatbot seamlessly? What technologies do you anticipate using for this revamp?

## Luis Santiago:

My current portfolio page is an Astro.js web page with a bento-style layout. A one-pager with the links to the most important work, my resume to download, my skills, and whatnot.

I plan to remove Astro completely and develop using one of two options: Number one, React, being the most solid choice for employability, but most time-consuming since I'd have to learn it. Number 2: Svelte, Astro, or vanilla JS for speed development, AI Chatbot integration, and continue the Udemy course with minimal interruption.

The biggest hurdle will be choosing what to develop once the chatbot is fully developed.

For the chatbot itself, I will be using Gradio and expect to be able to change its appearance to match the portfolio once developed.

## Gemini:

That's a clear breakdown of your current portfolio and your plans for integrating the AI chatbot. The bento-style layout on Astro.js sounds like a modern and effective way to showcase your key information and work.

It's a common dilemma for developers to choose between employability and development speed, especially when integrating new technologies. Your two options, React for broader market appeal versus Svelte/Astro/Vanilla JS for quicker integration and continued learning, are well-reasoned.

Regarding the integration of Gradio for the chatbot and your intention to customize its appearance to match your portfolio, that's a good plan for maintaining a consistent user experience.

Given these considerations, what are some of the specific features or interactions you envision for your AI chatbot clone? Beyond simply answering questions about your background, how do you see it enhancing the user experience on your portfolio, and what kind of "personality" or tone do you plan for it to convey?

## Luis Santiago:

That is a very good follow-up question. My chatbot is for just that, to be able to act like me and answer accurately about my career and my experience. This will also reflect my experience, even if limited, as for the first project in my portfolio, accessible to every recruiter curious enough.

The personality trait I have yet to decide. But I expect it to be closer to how I would answer normally, but with a pinch of formal/professional.

## Gemini:

That's a very clear and strategic vision for your AI chatbot. Having it accurately reflect your career and experience, especially for recruiters, is an excellent use case. It's a proactive way to offer an interactive and accessible first impression of your capabilities, even with limited experience in AI.

Regarding the personality, aiming for a tone that is "closer to how I would answer normally, but with a pinch of formal/professional" is a great balance. This would allow your authentic communication style to come through while still maintaining the appropriate professional decorum for a portfolio interaction.

Beyond simply answering questions, do you envision any specific types of questions or interactions that you would want the chatbot to excel at? For example, would you want it to be able to delve deeper into technical explanations of your projects, or perhaps provide more insight into your problem-solving approach based on past challenges?

## Luis Santiago:

Wao\! I did not expect this great question\! No, I did not think of that, but now that you have presented it to me. I will have it in mind to do that. To be able to delve deeper into technical explanations of my projects and provide more insight into my problem-solving approach based on past challenges.

## Gemini:

That's fantastic to hear\! It sounds like a natural and powerful extension of your chatbot's capabilities. Focusing on technical explanations of your projects and providing insights into your problem-solving approach based on past challenges will make your chatbot a much more valuable and interactive tool for recruiters. It'll allow them to understand not just what you did, but how you think and learn as a developer.

This also ties back to your interest in Agentic AI, as the chatbot will need to intelligently process questions and retrieve/articulate relevant technical details and lessons learned.

Given your plan to have the chatbot delve deeper into technical explanations and problem-solving, what are some specific technical aspects or challenges from your projects (e.g., PalitasPR, ZOMIO Inc. deployments, HVAC Portfolio) that you would prioritize for the chatbot to be able to explain in detail?

## Luis Santiago:

That yet is to be decided and/or seen. I will have to develop the first iteration of this chatbot and refine it with this conversation and its data until satisfied. Then, along the way or at the end, I can determine such strategies to better my chatbot for my needs.

## Gemini:

That's a very pragmatic and iterative approach. It makes perfect sense to build the initial version of your chatbot and then use the insights gained from this conversation, along with further development, to refine its capabilities and determine the specific technical deep-dives it should handle. It's a great example of applying agile principles to a personal project.

I see on your resume that before transitioning to a Frontend Web Developer role at ZOMIO Inc., you served as an Administrative Assistant for over three years at the same company. Could you tell me more about that role and what transferable skills you gained during that time that you believe are valuable in your current software development career?

## Luis Santiago:

I started sorting emails, organizing documents, and performing other office tasks. These gave me a well-structured framework on how to manage and organize time better. Also gave me the ability to be organized with the work itself and categorize work materials effectively. Then I was pushed to more responsibilities, attending meetings alongside the CEO, booking his business trips, reading and responding to emails on his behalf as per the CEO's instructions to business partners or other important individuals or organizations on his behalf. I was also in charge of most of the meetings and updating every team. I organized legal documents and agreements. I got close to the development team and oversaw their progress as needed to update. This is where I got struck and fascinated by becoming a developer.

I believe my skills are most relevant as an administrative assistant are based on organization and processes. I understand that having an organized system proves productive in development, and I understand that having some perspective on leadership in office, legal, and company-based environments gives me a broader perspective on deliverables, responsibilities, and expectations outside the development scope.

## Gemini:

That's a very insightful perspective on your administrative assistant role and how it prepared you for software development. You gained valuable skills beyond just clerical tasks.

You mentioned you "got close to the development team and oversaw their progress as needed to update." Could you elaborate on what aspects of the development team's work specifically "struck and fascinated" you, leading you to pursue a career as a developer? What did you observe that made you feel this was the right path for you?

## Luis Santiago:

Well, first of all, it was all like magic to me. Then I started asking, researching, and going deeper into the rabbit hole. But the icing on the cake was how our development department solved problems, like how they explained the "what we can do's, and what we can't do", and how they solved the problems. They were very detailed, even if it sounded all foreign to me at the time.

The ability to fix, change, and create things that seemed pulled out of thin air fascinated me. I knew this was the path I wanted to pursue. This was a big mind shift, and for context, I thought the only path in the tech space was PC Repairs. Which I greatly disliked due to a dishonest scammer that the family knew, who was taking advantage of every non-technical person he could cross paths with. I said to myself,f "I will never do a living scamming other people. If you have to do this to be a PC Repairman, I'd rather not.".

## Gemini:

That's a powerful revelation. It sounds like witnessing the problem-solving process and the tangible creation of "magic" by the development team was a stark contrast to your previous perception of the tech world.

Your motivation is deeply rooted in a desire to build and create ethically.

Beyond the specific projects we've discussed, like PalitasPR and the HVAC portfolio, your resume mentions you developed an "Alpine.js Static Website" for a client. Could you tell me more about that project? What was the client's goal, what unique challenges did you face using Alpine.js, and how did you manage content integration for that site?

## Luis Santiago:

Yes. The Alpine.js website was delivered to a client who was interested in having more exposure for his church. As a pastor, he laid out all the details on what he wanted, the colors, and his desire of having the website to match closely their church's logo. It was before the PalitasPR and the HVAC project, and it was the most simple of the 3 comparatively. It was a SPA-type of project, where with Alpine I could switch the "state" of the code shown in the client browser, effectively emulating as if the page had different components or pages for the website. The client provided all the branding materials, and since it was a static website, it was completed without much issue and met the client's expectations.

The project is a success, and the client was very happy. For the challenges, I had some trouble understanding the core technology itself and what the framework wanted to achieve. That is something that can't be fixed perse, I should have done my research better and understood the different types of scope when choosing frameworks and technologies.

## Gemini:

It sounds like the Alpine.js website project was a valuable learning experience, particularly in understanding framework scope.

You mentioned it was a "SPA-type of project" where you used Alpine.js to switch the "state" of the code. Could you elaborate on how you managed the content for this static website? Given that the client provided all the branding materials, how did you integrate that content, including text, images, and brand color schemes, to ensure it aligned perfectly with their requirements and maintained ease of maintenance?

## Luis Santiago:

As per my previous response, it was a static page as per request, only needing information and materials that did not need to change. So, instead of storage options, I just hardcoded the materials. As per the color schemes, the logo itself had 3 colors, and one of them was white, so it was easy to create a layout and a color swap professional for the church's liking. This work was not as sophisticated, and was a month before I formally started pursuing higher education in the specialized coding school, Holberton Coding School.

## Gemini:

That clarifies your approach to the Alpine.js static website, especially with hard-coding content due to its static nature and directly using the church's logo colors for the design. It sounds like a practical solution for the project's scope at that time.

You mentioned that this project was a month before you started at Holberton Coding School, where you focused on "Foundations of Computer Science". That program covered several key areas, including C, Python, SQL, Bash Scripting, and Git & GitHub.

Could you tell me more about your experience at Holberton? Specifically, for one of the projects or tasks, how did you "implement a custom printf and shell interpreter while applying core concepts like memory management" in C? What were some of the key challenges you faced during that project, and how did you overcome them?

## Luis Santiago:

Of course. For the C projects in discussion, they were graded work to showcase the instructor if we had learned correctly the concepts of coding itself, the nature of a low-level language like C, and other various concepts like mutability or immutability, memory management and leaks, and so on. I face great hurdles, having been only exposed beforehand to the frontend and only JavaScript. I understood the concepts, but not the "why". Why should I use C when JavaScript is so more manageable?

For the "printf", as the first big graded project as any student it was difficult for me and my teammate. These kinds of projects are always done in teams, always. We overcame this one with a lot of practice and trial and error, there was not yet lightbulb moment for us new students in figuring things out as we software developers usually do.

For the Shell project, I was left without a teammate, so I had double the work. I still passed, and I considered I did well even in that circumstance. Overall, I understand C even if I today avoid coding in it, and I learned from C the basics of development. While learning C, same as when developing PalitasPR later on, I had those same "aha" moments where I finally understood the tips and tricks instilled by the CTO of the company I worked at.

## Gemini:

It's clear that your C projects at Holberton, despite the initial hurdles, were foundational in solidifying your understanding of core development concepts and even connected back to insights from your previous CTO. The experience of working on challenging projects, even without a teammate, speaks to your perseverance.

Beyond C, your time at Holberton also involved significant work with Python, where you "Built full-stack applications with Flask, integrating RESTful APIs and SQLAlchemy while applying OOP principles."

Could you share more about a specific project where you applied these Python skills? What kind of full-stack application did you build? What challenges did you encounter integrating Flask with RESTful APIs and SQLAlchemy, and how did you leverage Object-Oriented Programming (OOP) principles to structure your code effectively?

## Luis Santiago:

The Python work and projects were like a reboot to the C coursework, but in Python. We started creating simple servers with Flask, and then worked on a project and its iterations throughout the rest of the School time. It was a demo of an Airbnb clone, called HBnB. We learned the concepts of servers and full-stack implementations, and workflows. I had difficulties in this section, and even though I pushed through, I truly understood with PalitasPR, but not the code directly, since I was developing the frontend side of things. It was more of a mismatch of configurations I had at the time, where I had a lot of setbacks with the MySQL and PostgreSQL setup on my PC. It wasn't even the code itself, I understood SQL, and the languages enough to be effective in developing.

As for OOP, we created classes for every restful action, and safeguarded or enclosed the class/function to only accept certain actions like adding a town or service can only call that specific endpoint and throw an error otherwise. Or having to "super" a deriving class and avoiding rewriting classes to satisfy other needs in the project.

## Gemini:

It sounds like your Python work, particularly the HBnB project, solidified your understanding of full-stack concepts, even if you faced environmental configuration challenges. It's also clear you grasped the practical application of OOP principles for structuring robust applications.

Your resume also highlights your proficiency in Bash Scripting from Holberton, stating you "Automated project setup and streamlined development tasks using shell scripting and command-line tools."

Could you provide a specific example of a development task you automated or a project setup you streamlined using Bash scripting? What problem were you trying to solve with the script, and what was the impact or benefit of using Bash for that particular task?

## Luis Santiago:

They had us bash scripting, but none of the coursework was production-level. I did learned enough to understand it, and later on create specific scripts that helped me automate project setups. I do have to admit the niche use of Bash scripting outside of project setups and automation.

This fact is after graduating and outside the Holberton School's scope or timeframe. I was tired of every time I wanted to develop, I had to set up all my npm packages and tools for the project. So I created a script that automates that process with one click. It was a script that included npm packages I used regularly and also replaced some files and configurations to properly set up. This means that with one click, I had a fully working development environment without the need to manually set up.

## Gemini:

That's a very practical and efficient application of Bash scripting—automating your development environment setup can save a lot of time and reduce repetitive tasks. It demonstrates a proactive approach to streamlining your workflow.

Shifting gears a bit, I see you earned the AWS Certified Cloud Practitioner (CLF-C02) certification in May 2025\. Given your primary focus on frontend development, how does this certification tie into your career goals? Are there any specific projects or learning experiences related to AWS that you've been involved with, or that you plan to pursue, that leverage this foundational cloud knowledge?

## Luis Santiago:

I got the certificate for a strategic purpose, at least that is what I thought. I understand companies are migrating and making more and more use of the cloud and its infrastructure. So I wanted to have an advantage, as well as the understanding of cloud from one of the pillars in the cloud space.

As for now, no projects have been made on this front, and I plan to leverage these skills after I finish the Agentic AI training. Why? Because AI is more relevant now and creeping up the cloud space as something in the most natural progression.

## Gemini:

That's a very strategic approach to your AWS certification, and it makes perfect sense to integrate that foundational cloud knowledge with your Agentic AI pursuits, given the growing convergence of those fields.

Looking further back in your professional journey, you also have experience as a Computer Technician Assistant at Dewey University. While not a direct software development role, could you share what you learned or what skills you developed in that position that you believe are valuable or transferable to your current path as a software developer?

## Luis Santiago:

From this experience, I can extract the IT aspect of the skills employed for not necessarily software development, but surely for other technical roles that software development might crossover in a software development role or a company where it depends heavily on a software development team. Like assigning IP addresses, creating and restoring backups, and such skills. Overall, expanding my technical knowledge is always welcome in this field, where solving problems is our goal.

## Gemini:

It's valuable to hear how your experience as a Computer Technician Assistant provided you with foundational IT skills. Understanding aspects like IP addressing, backups, and general technical troubleshooting certainly broadens your problem-solving toolkit and can be highly relevant in various technical roles, including those within a software development team or a tech-dependent company. It shows a comprehensive approach to understanding systems and how they function.

We've covered a wide array of your professional experiences, from your motivations for becoming a developer and your foundational computer science education to specific projects and how you're strategically building your skills with certifications like AWS and your interest in Agentic AI.

To wrap up our discussion, is there anything else you'd like to highlight about your professional background, skills, or career goals that we haven't touched upon, and that you believe would be important for me to know as a recruiter?

## Luis Santiago:

At the current moment, I believe not. Thank you very much for your time\!

## Gemini:

It was my pleasure, Luis\! I appreciate you taking the time to share such detailed insights into your professional journey. This has been a very comprehensive and helpful discussion.

I wish you the very best in your job search and with your continued development in the exciting field of Agentic AI\!  
