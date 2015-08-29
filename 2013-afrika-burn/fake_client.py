import json
import os

class FakeClient(object):
	def can_connect(self):
		return True

	def put_pixels(self, pixels, channel):
		n_pixels = ['#%02x%02x%02x' % p for p in pixels]
		open('sim_tmp.json', 'w').write(json.dumps(n_pixels))
		os.rename('sim_tmp.json', 'sim.json')
