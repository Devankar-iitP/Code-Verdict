# Overview

*From the very first year, when I embarked on my journey in Competitive Programming (CP), I came across many remarkable platforms like CodeForces and Codechef. I always wondered about the internal working of those platforms.
Although, the primary objective is not to entirely replicate all the features but to create a product that delivers value to the user through a judicious selection of essential features. It is a go-to-use product in software domain as I look from my perspective.*

So here, I present Code Verdict, an Online Judge using Django from scratch. Django being a high-level, open-source web framework in Python, it is simple and easy to learn. It has a built-in admin panel and authorization system. It follows the ***Don’t Repeat Yourself (DRY)*** principle, reducing redundancy. 
I tried my best to follow DRY principle. It is commonly used by many famous companies such as ***Instagram, Youtube and Spotify***. 
The final product aims to allow users to submit their code in multiple programming languages, execute it and generate a verdict in real-time environment. The system will be constructed with a focus on ensuring robust security and scalability.
___
Now, a common misconception arises and people equate an Online Judge with an Online Compiler. So, here is the basic difference between them.
### **Online Judge**
> It is a platform where a user submits one code and receives a verdict based on the judgement system. Here, Input is provided in form of predefined test cases and compared with the corresponding predefined Output. 
> It is commonly used for competitive programming, coding contests, and practice problems.
>> Example - CodeForces, Codechef

### **Online Compiler**
> It is a tool that allows users to write, compile, and execute code online. It is mainly used for quick code testing, debugging, and experimentation.
> Here, no verdict is passed by the system. Also, providing Input may or may not be necessary.
>> Example - OnlineGDB, Programiz

## ✨ Key Features
- Multi-language support: `C++` `Java` `Python`
- User registration and login page
- Problem statement with difficulty
- Permissions assigned based on roles
- Security with custom API for isolation
- Shows past submissions
- Pre-defined testcases to generate verdict
- Number of attempts with date and time
- Time taken by the code
- Memory occupied by the code
- Leaderboard (optional)
- Filters to sort the problem based on difficulty and tags (optional)
- Hints to problem (optional)
- Streak of solved problems (optional)
