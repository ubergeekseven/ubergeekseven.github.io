---
layout: post
title: "Fusion 360 Timekeeper: A Simple Time Tracking Solution"
date: 2024-03-21
categories: [Fusion 360, Add-ins, Development]
tags: [fusion360, timetracking, productivity, development]
description: "Introducing a new Fusion 360 add-in that helps track time spent on design projects - a feature many users have been requesting for years."
header:
  overlay_image: /img/fusion-timekeeper-header.png
  overlay_filter: 0.5
  teaser: /img/fusion-timekeeper-header.png
---

Since 2016, Fusion 360 users have been requesting a built-in time tracking feature. After years of waiting, I decided to take matters into my own hands and create a solution. I'm excited to introduce the Fusion 360 Timekeeper add-in - a simple yet effective tool for tracking time spent on your design projects.

![Fusion Timekeeper Main Interface](/img/TimekeeperMain.png)
*The Timekeeper interface features a clean design with simple Start/Stop controls and session tracking*

## What Does It Do?

The Timekeeper add-in provides a straightforward way to:
- Track time spent on individual Fusion 360 projects
- View your session history with start and end times
- Export your time data to CSV or Markdown files
- Maintain separate time tracking for each project

## How It Works

The add-in integrates seamlessly into your Fusion 360 interface with a clean, modern UI. When activated, you'll find a new Timekeeper icon in the Design toolbar. Simply click it to open the time tracking window, and use the Start/Stop button to track your work sessions.

What makes this add-in particularly powerful is its storage method - all time tracking data is saved directly within your Fusion 360 project using user parameters. This means:
- Your time data stays with your project file
- Data automatically syncs between computers when you open the file
- No external databases or cloud services needed
- Time tracking history remains accessible to anyone who opens the file

![Parameter View showing time data storage](/img/ParameterView.png)
*Time tracking data is stored directly in project parameters, ensuring it stays with your design file*

## Important Usage Note

⚠️ **Critical Warning**: The add-in uses Fusion 360's palette interface system, which requires special attention when switching between projects. Always close the Timekeeper window before switching to a different project. This is because palettes in Fusion 360 maintain their state between projects, which could lead to time being logged to the wrong project if left open during switching.

If you accidentally track time across multiple projects, you can clean up any incorrect data through the user parameters window shown above.

## Getting Started

Installation is straightforward:
1. Download the latest release from [GitHub](https://github.com/ubergeekseven/FusionTimekeeper/releases/tag/Release)
2. Extract the ZIP file
3. Run the included install.bat file
4. Open Fusion 360 and look for the Timekeeper icon in your Design toolbar

## Why Create This?

As a Fusion 360 user, I understand the importance of tracking time spent on design projects. Whether you're billing clients, managing project timelines, or just want to improve your productivity, having accurate time tracking is essential. Since Autodesk hasn't implemented this frequently requested feature, I hope this add-in helps fill that gap for the community.

The add-in is open source and available on [GitHub](https://github.com/ubergeekseven/FusionTimekeeper), so feel free to check it out, provide feedback, or contribute to its development.

Have you been wanting time tracking in Fusion 360? Give the Timekeeper add-in a try and let me know how it works for you! 