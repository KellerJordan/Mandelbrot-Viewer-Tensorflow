import os

from scipy.misc import imsave
import tensorflow as tf

from utils import pp, get_meshgrid, fractal_to_img

flags = tf.app.flags
flags.DEFINE_integer('num_iters', 256, 'number of iterations to run [256]')
flags.DEFINE_float('X', 0.0, 'X position of image [0.0]')
flags.DEFINE_float('Y', 0.0, 'Y position of image [0.0]')
flags.DEFINE_float('R', 2.0, 'radius (half of width) of output image [2.0]')
flags.DEFINE_integer('output_width', 1000, 'pixel width of output image [1000]')
flags.DEFINE_integer('output_height', 1000, 'pixel height of output image [1000]')
flags.DEFINE_string('img_dir', 'samples', 'directory to save generated images to [samples]')
FLAGS = flags.FLAGS

def main(_):
    pp.pprint(FLAGS.__flags)
    
    if not os.path.exists(FLAGS.img_dir):
        os.mkdir(FLAGS.img_dir)
    
    # get meshgrid over which to iterate to produce fractal
    Z = get_meshgrid(FLAGS.X, FLAGS.Y, FLAGS.R,
                     n_x=FLAGS.output_width, n_y=FLAGS.output_height)
    
    # build computational graph
    xs = tf.constant(Z, name='xs')
    zs = tf.Variable(xs, name='zs')
    ns = tf.Variable(tf.zeros_like(xs, tf.float32), name='ns')
    
    zs_ = zs * zs + xs
    not_diverged = tf.abs(zs_) < 4
    update_zs = zs.assign(zs_)
    update_ns = ns.assign_add(tf.cast(not_diverged, tf.float32)) # add one for each iteration that the point did not diverge
    update_step = tf.group(update_zs, update_ns)
    
    init_op = tf.global_variables_initializer()
    
    # run num_iters iterations to generate non-divergence counts for each pixel location
    with tf.Session() as sess:
        init_op.run()
        for i in range(FLAGS.num_iters):
            update_step.run()
        ns_np = ns.eval()
    
    img = fractal_to_img(ns_np)
    img_name = 'mandelbrot_%f-%f-%f' % (FLAGS.X, FLAGS.Y, FLAGS.R)
    imsave('%s/%s.png' % (FLAGS.img_dir, img_name), img)

if __name__ == '__main__':
    tf.app.run()
