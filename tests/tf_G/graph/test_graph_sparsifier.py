import numpy as np
import tensorflow as tf

import tf_G


def test_graph_sparsifier_cardinality():
  p = 0.6
  n = 50
  m = 100
  bound = 0.25

  with tf.Session() as sess:
    for i in range(5):
      graph = tf_G.GraphConstructor.unweighted_random(sess, "G_proof", n=n, m=m)

      sparsifier_graph = tf_G.GraphConstructor.as_sparsifier(sess, graph, p)

      assert sparsifier_graph.n == graph.n
      assert abs(sparsifier_graph.m - (graph.m * p)) < (graph.m * bound)


def test_graph_out_degrees():
  p = 0.6
  n = 100
  m = 900

  with tf.Session() as sess:
    for i in range(5):
      graph = tf_G.GraphConstructor.unweighted_random(sess, "G_proof", n=n, m=m)

      s_graph = tf_G.GraphConstructor.as_sparsifier(sess, graph, p)

      g_degrees = np.squeeze(graph.out_degrees_np) / graph.m
      sg_degrees = np.squeeze(s_graph.out_degrees_np) / s_graph.m

      np.testing.assert_array_almost_equal(g_degrees, sg_degrees, decimal=1)


def test_graph_in_degrees():
  p = 0.6
  n = 100
  m = 900

  with tf.Session() as sess:
    for i in range(5):
      graph = tf_G.GraphConstructor.unweighted_random(sess, "G_proof", n=n, m=m)

      s_graph = tf_G.GraphConstructor.as_sparsifier(sess, graph, p)

      g_degrees = np.squeeze(graph.in_degrees_np) / graph.m
      sg_degrees = np.squeeze(s_graph.in_degrees_np) / s_graph.m

      np.testing.assert_array_almost_equal(g_degrees, sg_degrees, decimal=1)


def test_graph_sparsifier_upgradeable():
  p = 0.9
  n = 10
  m = 30

  with tf.Session() as sess:
    for i in range(5):
      graph = tf_G.GraphConstructor.unweighted_random(sess, "G", n=n, m=m)

      s_graph = tf_G.GraphConstructor.empty_sparsifier(sess, "Gs", n, p)

      for e in graph.edge_list_np:
        s_graph.append(e[0], e[1])

      g_degrees = np.squeeze(graph.in_degrees_np) / graph.m
      sg_degrees = np.squeeze(s_graph.in_degrees_np) / s_graph.m

      np.testing.assert_array_almost_equal(g_degrees, sg_degrees, decimal=1)
