import tensorflow as tf
from scipy.misc import imsave

from utils import pp

flags = tf.app.flags
flags.DEFINE_integer('iters', 256, 'number of iterations to run [256]')
flags.DEFINE_float('X', 0.0, 'X position of image [0.0]')
flags.DEFINE_float('Y', 0.0, 'Y position of image [0.0]')
flags.DEFINE_float('R', 2.0, 'radius (half width/height) of image [2.0]')
FLAGS = flags.FLAGS

def main(_):
    pp.pprint(FLAGS.__flags)

if __name__ == '__main__':
    tf.app.run()
