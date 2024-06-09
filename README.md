# Overview

*From the very first year, when I embarked on my journey in Competitive Programming (CP), I came across many remarkable platforms like CodeForces and Codechef. I always wondered about the internal working of those platforms.
Although, the primary objective is not to entirely replicate all the features but to create a product that delivers value to the user through a judicious selection of essential features. It is a go-to-use product in software domain as I look from my perspective.*

So here, I present Code Verdict, an Online Judge using Django from scratch. Django being a high-level, open-source web framework in Python, is simple and easy to learn. It has a built-in admin panel and authorization system. It follows the ***Don’t Repeat Yourself (DRY)*** principle, hence reducing redundancy. 
I tried my best to follow DRY principle. It is commonly used by many famous companies such as ***Instagram, Youtube and Spotify***. 

The final product aims to allow users to submit their code in multiple programming languages, execute it and generate a verdict in real-time environment. The system will be constructed with a focus on ensuring robust security and scalability.

**LET'S  DIG  IN  WITHOUT  FURTHER  ADO !!**
___
Now, a common misconception arises and people equate an Online Judge with an Online Compiler. In layman terms, Online Compiler is a subset of Online Judge.

Here is the basic difference between them : 
### **Online Judge**
> It is a platform where a user submits their code and receives a verdict based on the judgement system. Here, Input is provided in form of predefined test cases and compared with the corresponding predefined Output. 
> It is commonly used for competitive programming, coding contests, and practicing problems for DSA.
>> Example - CodeForces, Codechef

### **Online Compiler**
> It is a tool that allows users to write, compile, and execute code online without any local compiler in their system. It is mainly used for quick code testing, debugging, and experimentation.
> Here, no verdict is passed by the system, rather only output is generated. Also, providing Input may or may not be necessary.
>> Example - OnlineGDB, Programiz

## ✨ Key Features
- Multi-language support: `C++` `Java` `Python` `C-Programming`
- User registration and login page (Authentication)
- Permissions assigned based on roles (Authorization)
- Only ***Employee*** can perform CRUD operations after verification
- Problem statements with difficulty assigned
- Custom Input feature
- Supports TLE and Runtime Error
- Can access past submissions in profile
- Can copy submitted codes in past submissions
- View common stats in profile section
- Code-editor supports both HTML and Markdown language
- Support syntax highlighting and line numbers
- Shortcut keys support - `Tab` `Shift + Tab` `Enter`
- Security with custom compiler and Docker for isolation

___

## How to start 
