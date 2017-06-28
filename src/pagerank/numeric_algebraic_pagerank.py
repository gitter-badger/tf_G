import warnings

import tensorflow as tf

from pagerank.transition.transition_matrix import TransitionMatrix
from src.pagerank.numeric_pagerank import NumericPageRank


class NumericAlgebraicPageRank(NumericPageRank):
    def __init__(self, sess, name, graph, beta):
        T = TransitionMatrix(sess, name + "_alge", graph)
        NumericPageRank.__init__(self, sess, name, graph, beta, T)

    def _pr_exact_tf(self, topics=None):
        if topics is not None:
            warnings.warn('Personalized PageRank not implemented yet!')
        a = tf.fill([1, self.G.n], (1 - self.beta) / self.G.n_tf)
        b = tf.matrix_inverse(
            tf.eye(self.G.n, self.G.n) - self.beta * self.T())
        self.run(self.v.assign(tf.matmul(a, b)))
        return self.v

    def _pr_convergence_tf(self, convergence, topics,
                           c_criterion):
        if topics is not None:
            warnings.warn('Personalized PageRank not implemented yet!')
        warnings.warn('NumericPageRank not implements iterative PageRank! ' +
                      'Using exact algorithm.')
        return self._pr_exact_tf(topics)

    def _pr_steps_tf(self, steps, topics):
        if topics is not None:
            warnings.warn('Personalized PageRank not implemented yet!')
        warnings.warn('NumericPageRank not implements iterative PageRank! ' +
                      'Using exact algorithm.')
        return self._pr_exact_tf(topics)
