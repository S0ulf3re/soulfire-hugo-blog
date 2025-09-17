---
title: "Vibe Coding: How to Amplify Your Technical Debt"
date: 2025-04-10
categories: 
  - "opinions"
tags: 
  - "technology"
---

So recently, there's been this new term describing a new phenomenon that's starting to go around.

It's called Vibe Coding, and it basically involves people writing code entirely through the use of Generative AI. Not just small snippets they need help.The. Whole. Thing.

I just want to get this off the table. I think this is a really bad idea. And I'll admit, that I've ended vibe coding a few times. Writing out elaborate prompts that build a whole app or system. But more often than not, I've ended up abandoning those things for one reason or another. Or they've ended up having bigger consequences (such as deleting an entire bunch of video files I had wanted to download and organize in my media server based on file name).

My worst moment with it involved a script I had made for self hosting various docker services split across various compose files. The script was supposed to go into each directory, spin up or down the compose file in each one (depending on the flag), and thus save me a lot of typing out for different files.

Eventually though, the script started getting too complex to maintain as different sections started making no sense. Exacerbating the entire problem was an inexplicable bug involving compose containers being given the wrong names, and it was enough for me knock down everything and just move to Proxmox.

The lack of inspection of what Copilot was outputting, coupled with a general lack of knowledge of what I was doing made it difficult to figure out why things weren't working.

Things like code autocompletions and quick prompts to generate small snippets aren't inherently bad. But once you start taking advantage of a tool like GitHub Copilot, it can be really hard to stop relying on it and start abusing it for things you _have_ to do. Especially as you want to start getting things done sooner and out of the way.

It's why companies are constantly pushing AI down our throats, and wasting millions giving it away to students and other businesses in hope it will get them hooked on it. They are fully aware of the power that these tools have, especially in a society that favors quantity over quality, and have the upper hand in pedaling these things.

It's not just that Large Language Models don't have an understanding of the text they output, it's also the lack of knowledge you discover along the way. It's certainly not always easy to find. And can often take longer than writing the actual code itself. Which is also what makes using a Large Language Model for code assistance appealing to begin with. Write now, understand later, build up more technical debt in the process.

I'm looking through the r/vibecoding subreddit, and it's kind of horrifying to see how others are just enthusing around writing sentences to write code with very little knowledge about writing code in while also encouraging others to do the same.

Some of the posts here (and I know I shouldn't be believing everything I read on the internet) are just horrifying to see in terms of incompetence, others are [really funny](https://www.reddit.com/r/vibecoding/comments/1jjwfff/this_is_why_i_love_vibe_coding/), like this one with one user mentioning all the different things they've built, and then just.

> Later today I am going to build a billboard system for my local theater so that they can plan and track all of their movies between offices.
> 
> I am loving this.
> 
> EDIT: The billboard project is MUCH bigger than I thought that it would be and is taking a lot more time than I anticipated. That's okay, it is helping me to learn good practices for Vibe coding.

Basically, the realization that trying to work with a business to meet it's needs requires much more than the ability to just prompt your way out of coding.

As for the more horrifying stories, slightly less related to coding. I heard on that subreddit about a person who managed to become a data analyst after having worked in the automotive industry... [By learning from AI](https://www.reddit.com/r/vibecoding/comments/1ji3eax/vibe_check_for_vibe_coders/).

It's impressive as a challenge, to try and see what you can do when the control is locked away from you. And I'm certainly not against there being systems that enable anyone in the world to start creating their own software. But it's also easy to start building up a sense of false confidence as you begin to think that you are an expert at what you are doing.

The risks may not be as high for personal offline projects, or code that's just needed to automate something once and never again, but my general anxiety lies in the fact that people are deploying entire services onto the internet with not only very little knowledge about hosting online services, but not even _what_ exactly they're hosting to begin with.

When you host an off the shelf service like Nextcloud or Uptime Kuma, you don't need to know everything about the service you're hosting. As long as you have a good knowledge of how the internet works, awareness of common vulnerabilities and maintenance, and you read enough of the documentation to gain an understanding of the software you're deploying, you're usually good to go.

But many of these people are just typing out a few sentences, taking the output, and deploying something they don't fully understand beyond a rough description (that may not even match what they wrote), and exposing it to the internet.

There's already been a few cases of people having their vibe coded services pwned with minimal ease. And with no knowledge of how your system might work or what parts might be included, I couldn't imagine trying to do an autopsy on such a system.

It's not "trendy" or "hip" to be building entire projects without an understanding of what you're doing. It may be fun as well, but it can also be really dangerous. Especially if you don't have a plan or vision for what you are doing.

So please, be careful with AI tools, and don't end up like me, or any so-called "vibe coders".
