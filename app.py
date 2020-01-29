# coding: utf-8

"""
[参考] https://qiita.com/tez/items/939168dbb31905948f46
"""

import time

import responder


api = responder.API()

@api.route("/")
def root(req, resp):
  @api.background.task
  def sleep(start, s):
    time.sleep(s)
    print(f"# {(time.time() - start):6.3f} sleep({s})")

  start = time.time()
  print(f"# {(time.time() - start):6.3f} 応答開始")

  sleep(start, 1)
  sleep(start, 5)
  sleep(start, 10)

  resp.content = f"{(time.time() - start):6.3f} resp"
  print(f"# {(time.time() - start):6.3f} 応答終了")
  return


if __name__ == '__main__':
  api.run(port=6002, address="0.0.0.0", debug=True)
