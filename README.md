# Lloyd-Max Quantizer:<br/>
This is a numpy implementation of Lloyd-Max Quantizer. This repository only supports for quantization of the signal with Gaussian distribution.

## Requirements:<br/> 
1. numpy <br/>
2. matplotlib <br/>

## Usage: <br/> 
In case of quantization with 8-bit and compute with 1,000,000 iterations, <br/>
Using command as below:
~~~shell
python3 main.py -b 8 -i 1000000
~~~
## Result of quantization with 8-bit: <br/>
<p align="center">
  <img width="50%" height="50%" src="https://github.com/ninnart-fuengfusin/lloyd-max-quantizer/blob/master/outputs/results.png">

The upper sub-graph showed the input signal that is a Gaussian distribution noise with zero mean and a unit variance.
The middle sub-graph displayed the optimized quatization points of the input signal.
The bottom sub-graph exhibited the output signal that is the quantized Gaussian distribution noise. <br>

The Mean Square Error of 8 bit quantization of noise with Gaussian distribution is 3.595888887954022e-05.

## License: <br/>
MIT license.
