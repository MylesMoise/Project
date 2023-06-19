# Snake
#### Video Demo: https://youtu.be/9ZesUzth-eY
#### Description:
For my final project I recreated the video game Snake in python with the help of the Pygame library. The way that the game works is that there is a loop that causes the game to remain active until the window is closed. While the game is running, there are 3 main objects in play along with a few keyboard inputs. 

The first object is the snake itself. In this code, I have the player start out with a 3 block long snake in them middle of the map waiting for their input before it starts to move. Every 60th of a second, the game will "update" and during this time it runs through the program detecting any new events. The event in this snake section which is most important is drawing it. Drawing it means to have it update its position on the screen and to change its body image depending on where it is. To make the body image be properly built, I had to do very simple matrix math. When the snake eats the apple, it also grows a new body part which will be attached to the end of the current body. 

The second object is the fruit which is fairly simple. In here I just had to make it randomize it's position at the start and when it the randomize function in it is called, it will randomize the position once again. 

The main class is where both of these objects come together and everythign starts to blend in well. I added a collision feature to see if the snake head is touching the fruit and if it does, the player gains a point, the fruit will ranomize its position and then the snakee gains a body part. I created a simple game over mechanic where the game will restart once the snake either winds up running into itself, or it hits the edge. I also did some fairly basic math again to make the grass tiles have a checkerboard pattern and then a fairly simple scoreboard in the bottom right. 
Lastly, I incorporated a while True loop to keep the game running forever. In here, there are a few different event types to determine what is going to be checked. If the user hits the X in the top right, the game will quit out, every 60th of a second, the game will update meaning it will run through the Main class to check if anything has happened, and if the player presses a key it will check for which key was pressed and change the direction the snake is moving.

I also made sure to test the game for all possible edge cases such as making sure that the snake can't turn around onto itself, that the game shuts down properly, that the fruit can't move to where the snake is currently at, and did all possible outcomes of the snake body position to have the correct image appear on screen. 

The font file contains the font ttf file for the font used in the game. The graphics contains the apple, along with all the various snake positions that could exist. The Sound file contains the WAV file for the noise the snake makes when it eats the fruit. 
