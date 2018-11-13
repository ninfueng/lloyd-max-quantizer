# Lloyd-Max Quantizer:<br />
This is a Lloyd-Max quantizer implemented with Python3 (Numpy). Currently, this repository supports only for the quantization of the signal with the distribution as normal distribution.

## The required Python libraries:<br /> 
1. Numpy <br />
2. Matplotlib <br />

## Usage: <br /> 
In case of wanting to quantization with 3-bit and doing the computation with 1,000 iterations, <br />
The example of command can be shown as below. <br />
~~~shell
python3 main.py -b 3 -i 1000
~~~
## The result: <br />
<p align="center">
  <img width="50%" height="50%" src="https://github.com/FuengfusinNinnart/lloyd-max-quantizer/blob/master/outputs/results.png">
  
## Result of quantization with 3-bit (8 possibles) <br /> 
In the graph, the top sub-graph shows the input signal that is a noise with the normal distribution (zero mean, unit variance). The middle one shows the discrete quatnization points of the input signal. The last one is the output or the quantized normal distribution noise.

The Mean Square Error of 3 bit quantization of noise with normal distribution: 0.03359269271137846.
