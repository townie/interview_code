Random interview question


abstract description:

rby.csv
id,data,parent_id
1,r,
2,r,1
3,b,1
4,y,1
5,b,3
6,b,6
7,r,5
8,r,6
9,y,7
10,b,8



Init state

	 (R1)
	/  |  \
(R2)  (B3) (Y4)
	 / |  
  (B5) (B6)
	/    |   
(R7)     (R8)
|  		   \
(Y9)       (B10)


Resulting data structure state
[
 { "top_level": "(R1)", "data": { "r": ["B6", "B5", "B3", "B6"], "y": ["Y4"] } },
 { "top_level": "(R2)", "data": { } },
 { "top_level": "(R7)", "data": {  "y": ["Y9"] } },
 { "top_level": "(R8)", "data": {  "b": ["B10"] } },

]
