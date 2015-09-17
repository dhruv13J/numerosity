## Goal: Study Weber's law for Numerosity - The sense of quantity

#### Weber's Law: The threshold for detection of change from a perceptual quantity is directly proportional to the magnitude of the quantity.

#### Numerosity: The sense of visual quantity going beyond counting.

### Experiment design

- __Image Stimulus :__ two images presented side by side, black background, white dots.

- __Task :__ identify the image with more number of dots, and accordingly respond within 15 seconds with:
		a) left arrow key - if you think that the left image has more dots.
		b) right arrow key - if you think that the right image has more dots.
		c) down arrow key - if you think that both have the same number.

- __First thoughts :__ I need to calculate the weber fraction. For this, I need to have a "left" image,
				   the actual number of dots from which the change needs to be measured. To make a weber fraction 
				   conclusion, I guess I will need at least 6 data points: 1 low, 3 mid, 2 high. Each will have to 
				   be coupled with a certain number of images with increasing number of dots to precisely capture 
				   the threshold for change detection from it.
				   This essentially helps me fix the number of trials and adjust time for presentation of the 
				   stimulus. I also have to think about how to randomize the spread, and probably control for it.

- __Analysis :__ Go from "yes" - "no" responses to quantification of the threshold for stimulus change. Then calculate 
			 the Weber fraction.

#### Parameters for the experiment.
- _Numbers of dots (6)_: [8, 16, 24, 40, 56, 80, 112]; deltas: [8, 8, 16, 16, 24, 32]
- _Spread_: X
- _Numbers of image couples_: 4, 6, 8, 10, 15, 15, 20

#### Issues:

1) Order of presentation: 'Random' or 'Not Random'? 
	- Random presentation can counter the counting issue. Sequential presentation will let the subject count both sides and make a more informed guess. 
	  Thus, a random sequence is preferable.
	- The sequence should be preserved across subjects, which prevents the noise introduced by the adaptation to the task.

2) Control for spread and counting: How does spread of the dots affect the estimate?
	- Introduce a small set of same number of images to the set with different spread. Could be done towards the end of the experiment.

3) Number of subjects: Variable. More the better!

#### Code:
	Everything used to generate the images is in the ipython notebook. The conditions file for Psychopy will also be generated automatically.
	Please change the base_path global variable according to your needs.
