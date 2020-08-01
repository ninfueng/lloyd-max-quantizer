# Lloyd-Max Quantizer:
This is a Python implementation of Lloyd-Max Quantizer. Currently, this repository only supports for quantization of the Gaussian distribution signal.

## Requirements:
1. numpy
2. matplotlib
3. scipy


## Usage:
To quantization with 8-bit with 1,000,000 iterations, use a command below:
~~~shell
python3 main.py -b 8 -i 1000000
~~~

## Result of quantization with 8-bit:
<p align="center">
  <img width="50%" height="50%" src="https://github.com/stillame96/lloyd-max-quantizer/blob/master/outputs/results.png">

From this figure, upper graph shows an input signal or a Gaussian noise with zero mean and a unit variance. The middle graph displays the optimized quantization location given the input signal. The bottom graph shows an result signal or an quantized Gaussian noise. <br>

From this implementation, mean square error of 8-bit quantization of Gaussian noise is 3.595888887954022e-05.

## License:
MIT license.
