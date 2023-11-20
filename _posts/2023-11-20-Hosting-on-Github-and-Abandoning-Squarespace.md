---
date: 2024-11-20
header:
  teaser: /img/squarespacetogithub.jpg
  overlay_image: /img/squarespacetogithub.jpg
  overlay_filter: 0.8
toc: true
toc_label: "Contents"
--- 

# Moved to Github Pages From Squarespace

I have spent some time finding a method of moving from sqaurespace to github pages. The monthly costs of squarespace is not hard to deal with in general. The inability to access the uploaded site data after the fact is annoying. On top of that, you can only update your site and make changes with their app or browser based program. THis causes a lot of issues for where I am trying to go.

This started with me doing a dep dive into openai API access to build out a RAG system for work. Once I understood the abilities of the API, before the changes, I started thinking of ways to autoomate as much as possible. This current post is not generated with the bot I am building. Hopefully this is the last. However, I was trying to get API access to sqaurespace and it was not possible. You can develop for them in some way but not control your own site with this API. So, this made it impossible to create a bot that would then do the work for me. 

I started to look in to alternatives to sqaurespace and stumbled on github.io as a potential. I already had several project sites running in it and it has been around since 2007. It is free to host on it as well. All I had to do was figure out how to get my current site info transferred over to Github. I also had to update DNS to get my URL to work with github.io. 

## Getting Your Site Transferred

When exporting your site from squarespace, it only has an option for Wordpress. I then stumbled on a forum discussion about converting from wordpress to markdown. Markdown is what is used with Jekyll and Jekyll is what github supports for static site creation. After getting the wordpress file exported, you can run a python script that will go through the wordpress file and download each page content into an html page and then download the iamges associated. I found out the hard way that many of these image files will be named axactly the same if you have been using squarespace long enough. So, depending on the age of the site, you may not be able to get evey single image back without manually downloading from the site. 

I did not realize this until after I turned off sqaurespace and the second you do that, the site is gone and cannot e recovered.

Anyway, the HTML sites worked and pulled in images the same as the site did. Many of the old posts had the same images trhoughout them. I then needed a method of converting each html page into a mardown equivilent. This was fairly straightforwad because I was able to get ChatGPT to write a python script to do it. I did have to play around with some functions to get exactly the output I wanted. Once I had it spitting out the one HTML page as markdown and it worked as it should, I ran it on the entire directory. 

After converting, I then created a few more python files to get the markdown changed to remove certain characters that were not helpful. Another to be able to create frontmatter that was correct for dates and header images an whatnot. It did take a day to really pin this all down but it should be worth it in the future.

## Why would I choose this?

The control I now have over my site is complete. The security is oauth and the API access I have allows me to integrate anything I need to into my workflow. 

### Using AI to really decrease my workload

I rarely post what I do because it takes time. The internet and websites in general are invisible to most people any longer. I still want to document my work over time and I do it every so often. A single post on a subject could take me days. Even if the project took a couple hours. Getting information together, loading picutres or a video. All takes time.

I want to be able to take a folder of information. Screenshots, video, code I wrote and drop it into a chat. The setup of this bot would knwo exactly what sortr of output I want to build. Then it writes the post, inserts the images itself and then sends a smaller writeup as well as links to all the different social sites I need to . All without me doing anything other than taking pictures, video and outputting code. Then I talk to the bot with my voice to explain what the porject was about for an overview. Hvae it look through everything, including images, to determine how to write itup and display everything. If no images exist, have it make one up for it to best represent the content.

Creating things or learning new things is what I want to do. To prove to others what I do, I have to have record of it. I am not the type of person that wants to do this though. Plenty are out there. I just want to be into what I am into and have content generate itself. This is my first step.

# Next steps and conclusion

I have been working on fully understanding the assistants API from openai over the last couple of weeks. I finally understand the capabilties and am working out function calling now. 

I can easily integrate teh github API calls for writing and committing files. Now I need a workflow and template for ti to work with. Ultimately, this will integrate into my AI bot that has many agents for different tasks. I will have the ability to talk with my bot throughout a day. It will retain the conversations and ask questions to help me give better details to fully flesh out context.
If it decides that I should have a schedule worked out to accomplish a goal that may exist within the conversations, it will tell me this and then generate a plan that includes due dates or follow up using the google calendar and tasks API. Every morning, I will start a new conversation that prompts it to look at what is coming up as well as a summary of the past few days so it has more context on what I am doing. It can poke me to get me focused throughout a project. 

At the end of each night, a function will run that takes the entire days thread and writes up a detailed journal entry about that day. Creates the summary for the top and starts the thread for the morning that includes the summary. I think this could help me organize my mind. The writign will be stored in google drive as a doc that I would never take the time to do myself. Ultimately leaving a detailed set of journals with information that I could pass along to family in the end. Journals are one thing. Extreme detail could help generate a vertual envirnment in the future from the explanations. Using googles gps history and images from my timestampted information could allow people in the future to relive entire days or years as an individual from the past. All we need is enough information to do so. 

I am calling this CaptAInsLog. One day, i hope to use the information in a version of the holodecks from Star Trek.

