# Overview

### Scenario

**Name**: Flag Command

**Description**: Embark on the "Dimensional Escape Quest" where you wake up in a mysterious forest maze that's not quite of this world. Navigate singing squirrels, mischievous nymphs, and grumpy wizards in a whimsical labyrinth that may lead to otherworldly surprises. Will you conquer the enchanted maze or find yourself lost in a different dimension of magical challenges? The journey unfolds in this mystical escape!

# Solving

- Access to the website: `http://154.57.164.81:31468/` see the emulated terminal interface -> Enter the command with normal movements (HEAD NORTH,...)

![alt text](image/image-6.png)

- View source code and see relative scripts: main.js, game.js and command.js.

![alt text](image/image.png)

- Debugger -> view source code of these files. In file `main.js`, the function fetchOptions call `/api/options` -> retrieve the list of available commands from the server and store them in to `availableOptions`.

![alt text](image/image-1.png)

- Function CheckMessage(): if having secret commands in availabelOptions, maybe having the flag

![alt text](image/image-2.png)

- Access to the link: `/api/options` and see the secret.

![alt text](image/image-3.png)

- Enter the secret and get the flag.

![alt text](image/image-4.png)

![alt text](image/image-5.png)