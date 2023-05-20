# RCRA-Shingoki

Shingoki puzzle solver using clingo, clingraph and python

Práctica para la asignatura de RCRA. Ingeniería informática UDC. 
Realizada por:
- Guillermo Fernández Sánchez
- [Rodrigo Naranjo González](https://github.com/rng1)

Nota: 2/2

Enlace con el enunciado completo: https://www.dc.fi.udc.es/~cabalar/kr/current/ex1.html


## Introduction

![](./shingoki_example.png)

In this exercise we will play with clingo to find solutions to the Shingoki puzzle. [Shingoki](https://www.puzzle-shingoki.com/) is a puzzle that consists in drawing segments among points in a grid of N x N so that all segments form a **single, cyclic path**. Some grid points contain numbers in a circle that can be additionally black or white. The puzzle constraints are the following:

1. All edges must form a single, linear loop. No crossing or branching is allowed.
2. The loop must pass through all numbered circles.
3. White circles must be passed through in a straight line.
4. Black circles must always be in the corner of a turn.
5. The number in each circle must be the sum of the lengths of the 2 straight lines segments going out of that circle.

To understand the game rules, you can try to play online at https://www.puzzle-shingoki.com/

##  Steps

1. We encoded the Shingoki problem as an ASP program that solves the puzzle for any instance. This program is our Knowledge Base and will be called **shingokiKB.lp**

   

2. Each puzzle instance is provided as an ASCII file shingokiX.txt with the following format. Each line contains **n** integer numbers separated by (one or more) blank spaces. A zero represents a regular grid point without any restriction, a strictly positive number represents a white circle and a strictly negative number represents a black circle. As an example, the input file for the scenario in the picture above could look like:

```
 0  0  0  0  0  4  0  0
 0  0 -2  0 -2  0  0  0
 4  0  0  0  0  2  0 -6
 0 -3  0 -4  0  0 -3  5
 0  2  0  2  0 -2  0  0
 0  0 -3  0  0  0  0  0
-2  0 -2  0 -3  0  0  0
 0  0  0  0  0  0 -2  0
```

The python program [**encode.py**](./encode.py) takes the shingokiX.txt file as an input and creates an **shingokiX.lp** file describing the instance as a set of ASP facts. An example of use could be:

​    python3 encode.py < shingoki1.txt > shingoki1.lp

------

3. Finally, we translate back the answer set into a complete Shingoki solution, printing the final result in standard output. The solution will have the following format: show a '+' in each empty grid point, and lines displaying the connections.

```
+--+  +  +--+--+--+--+
|  |     |           |
+  +--+  +  +--+  +--+
|     |  |  |  |  |
+  +--+  +--+  +  +--+
|  |           |     |
+  +--+--+  +  +--+  +
|        |        |  |
+--+--+  +  +--+  +  +
      |  |  |  |  |  |
+--+--+  +--+  +--+  +
|                    |
+--+  +--+  +--+--+  +
   |  |  |  |     |  |
+  +--+  +--+  +  +--+
```

The python program called [**decode.py**](./decode.py) takes the output of clingo and generates the solution file. A possible execution could be:

​    clingo shingokiKB.lp shingoki1.lp | python decode.py > solution1.txt

4.  There is also a visualizer in clingraph, [viz.lp](./viz.lp), to be executed with the following [command](./command). An execution examples could be as follows:

​    ./command shingoki1.lp



