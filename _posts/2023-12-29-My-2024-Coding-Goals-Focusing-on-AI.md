---
date: 2023-12-29
header:
  teaser: /img/coding20242.png
  overlay_image: /img/coding20242.png
  overlay_filter: 0.8
toc: true
toc_label: "Contents"
---

# My 2024 Coding Goals Focusing on AI

This past year I would say that I had no goals in mind for coding.  I was lucky enough to get a month sabbatical to work on an AI project. I accepted and this started an obsession. 

First, I had to learn python. I started the usual way with any language new to me and played with some simple projects and when I got stuck I would search for answers. I started using GPT at the time to bounce ideas off of. This eventually turned into adding a couple plugins into VS Code to use my API for openai for code completion. Using this I was able to ask questions while coding. I could get explanations on what I was working on.
Over a week with this setup and I was capable of understanding the python concepts and I could move on. It was a great teacher. This alone showed me the power with this early AI system. Learning how to prompt the AI for responses that are in line with what you need as output is something everyone needs to work on. I think this is a lot like how it was with google early on. learning how to ask the questions to get the information needed took some time. Eventually you would get your google-fu. Same with prompts.
I spent a month, by myself, in a room with a computer. I honestly did not get lonely because my stupid human brain was fooled enough by the interactions with the AI that I came home feeling as if I worked with a team of people throughout the day. This does not boad well for future generations in some ways. 

I believe that AI can help us learn better than anything in the past. It may be able to teach us how to best learn for ourselves. Imagine building systems that would develop an understanding of the user in a way that it can predict the best pathway for understanding. A guide that learns how to present information to you in ways that make learning easier. Something that can translate anything into the inputs an individual needs. 

I can imagine a near future with these capabilities. I think I can build something that can help with this. I am sure that others are already working on this but, why not try myself? I am currently working on a system that can gather information throughout the day for anyone. You talk to it throughout the day, it asks questions to get more information out of you. All messages between the user and the AI are recorded. At the end of the day, a wrap-up occurs and all the data is summarized into a narrative as a journal entry of sorts. All messages are appended to this document for later use and reference. 

This system has become my daily journal writing system but also an assistant. It can pull out information from you to determine if you need to schedule something and then it can schedule it for you. It has vision input so that you can attach images within the journal in the timeline. These images can also be used with a vision AI system to do anything you ask it to do with it. You could ask for the image to be analyzed to determine what was happening in the scene and then have the AI write up a short description with the input from you used along with what it sees to generate it in a relevant context. 

This is all a web UI and can be accessed at any time throughout the day. I currently use the voice input on my phone and then the default TTS system to speak in and out with the system. I plan on adding a better system for this so that it feels more like a person. I found a recent project that allows voice cloning locally and well. I would like to integrate this into the system and create a custom assistant voice. THis would eliminate any API costs for this sort of thing. 

The image processing is currently done by OpenAI gpt vision. I would eventually like to use a local vision model as well. I mean, if I could having everything local would be amazing. Maybe one day this is will be easy enough and compute will become something easily obtained. 

The scheduling is done through Googles APIs. I have it connected to gmail, calendar, docs, drive and tasks. So the journal itself becomes a doc at the end of day. I currently have the API access set up as a desktop application. This breaks the flow of things because if access has to be obtained again, I have to manually interact with the page to do so. In the future, I plan on switching my OAUTH to a web app setup. I have to overcome some complexities. I use a zero trust setup through cloudflare and I need to find a method of allowing googles servers and mine to exchange data for OAUTh through this. I know there is a way to do so. I have put it off because I am always working on the code of the assistant. 

## Next Steps

I do not think that by the end of this year I will be completed with my assistant and what it can do. I honestly do not know how long my immediate changes will take. I believe I can get past some of them soon. Building out a system that would be general enough to become tutor that can learn and interact with multiple agents to accomplish tasks together and understand the user over time might be possible by the end of the year. I am only one person though and this may take years.

I would be able to get my:
- Web app OAUTH set up
- Vision system identify and label people
- Email reading and writing based off of needs
- Modification / Deletion of calendar entries
- Web Notifications for server side communication to the end user with reminders
- Vision processing in multiple ways. Determining tasks and then help with guidance
- Web search and research capabilities
- AR UI for interacting with environment and vision
- Local cloned voice for custom assistant voice
- Agent instruction writing and modification autonomously


I think I can handle these over the next few months. I want this to be a modular system capable of acting in ways needed. To do this, there must be many settings available to the end user. Turning on certain types of features on the fly to be able to modify the capabilities as it is needed. 
The AR UI with vision input is a feature that has immense potential. Remembering the names of people is something I have a hard time with. Even people I know for years. There seems to be a disconnect between the place I store that and the pathways I generate output with. If I have an input for reminder, this could help me drastically. 
Using it with interactions that I have never dealt with like a problem with a piece of hardware of some sort. Getting web results through vision and then determining an answer and then teaching me in real time about this would be insane. 


## Ultimately, I Want a Teacher

My ultimate goal with this system is so open ended. Recording everything throughout my day so that I have a record. That alone is something I do not do. However, I have since November. Keeping a journal that allows me to search all content for information. Summarize entire months and years to get feedback and constructive criticism to advance. A dataset of myself that allows me to see growth and setbacks and improve with actual data. 

I cannot say where this whole thing ends up. I do enjoy this journey though. I really hope that the APIs I currently use do not change much through the year. having to rewrite my system would be a huge burden. I just have to go with the flow until I can do everything locally. One day.