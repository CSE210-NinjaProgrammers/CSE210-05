# CSE210-05
Cycle game team work

# Cycle game
The best rides are the ones where you
bite off much more than you can chew,
and live through it.

- Doug Bradbury -

Cycle is a game where players have to run away from their opponent using cycles, the challenge is that cycles leave a trail behind the player. 

## Getting Started
---
Make sure you have Python 3.8.0 or newer installed and running on your machine. Open a terminal and browse to the project's root folder. Start the program by running the following command.
```
python3 -m pip install raylib
```
You can also run the program from an IDE like Visual Studio Code. Start your IDE and open the project folder. Select the main module inside the hunter folder and click the "run" icon.

## Starting the Game
---
Player One- Press any key from (W, S, A and D keys) to show snake.
Player Two- Press any key from (I, K, J and L keys) to show snake.

## Points
---
Each player start with 3 points, everytime an opponent head colides with a part of your tail, you loose one point. Samething applies to the other player. If both 
players colide head to head, it GAME OVER for both players. Once a player loses all it points, it GAME OVER and the other player wins.

## Project Structure
---
The project files and folders are organized as follows:
```
root                    (project root folder)
+-- cycle               (source code for game)
  +-- game              (specific game classes)
  +-- __main__.py       (entry point for program)
+-- README.md           (general info)
```


## Required Technologies
---
* Python 3.8.0
* Raylib Python CFFI 3.7

## Authors
---
* Eric Farley        (ericfarley96@gmail.com)
* Tulio Banegas      (trbanegas14@gmail.com)
* Livia Pimentel     (livia_macedo89@yahoo.com.br)
* Alfred Kamisesse   (reeves.kamisese@gmail.com)
* Juan David Estrada (jdemachado1105@gmail.com)

## Contributors 
* Eric Farley        ----> Add logics to perform game in most classes actions of the game including inheriting from parent class and giving points and colision.
* Tulio Banegas      ----> Inputs class methods and attributes to other classes with movement of snakes and others vertical movement plus keyboard service changes.
* Livia Pimentel     ----> Help with ideas of the positions of the snakes and it velocity of each snakes including the frame-rate.
* Alfred Kamisesse   ----> Do updates to describe how the game works and how points a used in the game and other ideas to README file and class.
* Juan David Estrada ----> Help with preparing the README file and updates the respository and with the growing tail of the snake at the end with colors.
