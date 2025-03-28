# -*- coding: utf-8 -*-

from stern_hackathon_demo import api


def test():
    _ = api


if __name__ == "__main__":
    from stern_hackathon_demo.tests import run_cov_test

    run_cov_test(__file__, "stern_hackathon_demo.api", preview=False)
