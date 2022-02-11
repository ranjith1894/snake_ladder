# Snake Ladder

Snake Ladder game done with Python 3

## Installation

Use the requirements txt to install foobar.

```bash
pip install requirements.txt
```
Since there is no extra package used . So requirements will be empty
## How to run ?

```python
python main.py

# It will ask for the type of dice before starting the game !!!
    # Please select type of dice
    # 1.Normal Dice,
    # 2.Crooked Dice:


```
Currently the game is coded with Single player and 10 turns.
It can be scalable to use multiple players , more ladders, snakes, & maximum board position .. 

``` 
##### Game Started #####

 --------- Turn number 0 ---------
Current player Ranjith is currently at 1 position
Dice thrown -> 1
Position updated to 2

 --------- Turn number 1 ---------
Current player Ranjith is currently at 2 position
Dice thrown -> 3
Position updated to 5
............
..........
.........
 --------- Turn number 8 ---------
Current player Ranjith is currently at 99 position
Dice thrown -> 1
Position updated to 100 
Ranjith has won the game !!!!!

```
## To run Unit tests
```
python -m unittest discover tests
```

