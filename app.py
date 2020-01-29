# coding: utf-8

"""
[参考]
https://qiita.com/tez/items/939168dbb31905948f46
https://qiita.com/DeliciousBar/items/19ec5107853bd1019f53
https://qiita.com/nagataaaas/items/edb5017e0713a996e9ee
https://qiita.com/nskydiving/items/b98d5cea5a52459cb183
"""

import time

import responder


api = responder.API(cors=True, cors_params={
    'allow_origins': ['*'],
    'allow_methods': ['*'],
    'allow_headers': ['*'],
})

@api.route("/")
async def root(req, resp):
  @api.background.task
  def sleep(start, s):
    time.sleep(s)
    print(f"# {(time.time() - start):6.3f} sleep({s})")
    return

  start = time.time()
  print(f"# {(time.time() - start):6.3f} 応答開始")

  sleep(start, 1)
  sleep(start, 5)
  sleep(start, 10)

  if req.method == "get":
    #resp.content = f"{(time.time() - start):6.3f} get"
    resp.content = api.template('index.html')
  elif req.method == "post":
    data = await req.media()
    resp.media = data
    resp.content = f"{(time.time() - start):6.3f} post {data}"
  else:
    resp.content = f"{(time.time() - start):6.3f} ?"

  print(f"# {(time.time() - start):6.3f} 応答終了")
  return


if __name__ == '__main__':
  api.run(port=6002, address="0.0.0.0", debug=True)
