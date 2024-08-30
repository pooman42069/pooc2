I AM NOT RESPONSABLE FOR ANY MISS USE INCLUDING INSTALLING THE PAYLOAD ON VULNERABLE MACHINES OR USING THIS TOOL FOR DENAIL OF SERVICE ATTACKS

credits to @NixWasHere for the original code

I remade this by adding a new ui and an automatic setup
- auto build payload
- rewrote methods
- windows support
- automatic setup
- dns support

INSTRUCTIONS 

1. Download / extract to the machine you are hosting off (this also works for home machines)
2. Install requirements in requirements.txt
3. Run setup.py to install eveything
4. Configure logins and port in /src/config.json, logins.txt
5. *MAKE SURE THAT THE PORT YOU HAVE CONFIGURED IS OPEN*
6. Run the setup again everytime you want to start the cnc (or run from the builder (im not sure if it works, i will double check in later update))
7. Now if everything was setup correctly,

You should be able to connect to the panel with a simple raw or telnet connection (USE RAW FOR PUTTY).
To do this, use the IP/DNS and the PORT you configured in the fourth and fith step, For example when connecting via Mac Terminal the ideal command would look something like:

telnet 0.0.0.0 0000

or if connecting with putty

![image](https://github.com/user-attachments/assets/5ff11e4c-6dab-4cc1-8260-3c75ef055f92)

From here it should be fairly straight forward if you have any issues or questions feel free to message me on discord.

discord : poodrop.

Detailed tutorial on my youtube:
youtube.com
