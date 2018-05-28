# Mandelbrot-Tensorflow

Based on the [Mandelbrot set tutorial](https://www.tensorflow.org/tutorials/mandelbrot). Implements additional command-line interface to save images on arbitrary regions of the fractal and with zoom up to 1E10x.

### Results

`python3 main.py --X=-0.5 --Y=0 --R=1.8`
![](https://github.com/KellerJordan/Mandelbrot-Tensorflow/blob/master/samples/mandelbrot_-0.500000-0.000000-1.800000.png)

`python3 main.py --X=-0.745428 --Y=0.113009 --R=3.0E-5`
![](https://github.com/KellerJordan/Mandelbrot-Tensorflow/blob/master/samples/mandelbrot_-0.745428-0.113009-0.000030.png)

`python3 main.py --X=-0.16070135 --Y=1.0375665 --R=1.0E-7 --num_iters=1024`
![](https://github.com/KellerJordan/Mandelbrot-Tensorflow/blob/master/samples/mandelbrot_-0.160701-1.037567-0.000000.png)

`python3 main.py --X=-0.235125 --Y=0.827215 --R=4.0E-5`
![](https://github.com/KellerJordan/Mandelbrot-Tensorflow/blob/master/samples/mandelbrot_-0.235125-0.827215-0.000040.png)

`python3 main.py --X=0.267235642726 --Y=-0.003347589624 --R=1.15E-10 --num_iters=512`
![](https://github.com/KellerJordan/Mandelbrot-Tensorflow/blob/master/samples/mandelbrot_0.267236--0.003348-0.000000.png)

`python3 main.py --X=-0.722 --Y=0.246 --R=0.019`
![](https://github.com/KellerJordan/Mandelbrot-Tensorflow/blob/master/samples/mandelbrot_-0.722000-0.246000-0.019000.png)

`python3 main.py --X=-0.7453 --Y=0.1127 --R=6.5E-4`
![](https://github.com/KellerJordan/Mandelbrot-Tensorflow/blob/master/samples/mandelbrot_-0.745300-0.112700-0.000650.png)

`python3 main.py --X=-1.25066 --Y=0.02012 --R=1.7E-4`
![](https://github.com/KellerJordan/Mandelbrot-Tensorflow/blob/master/samples/mandelbrot_-1.250660-0.020120-0.000170.png)
