#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
import webapp2
import json
import random
import urllib
import jinja2
import os

jinja_environment = jinja2.Environment(
    loader=jinja2.FileSystemLoader("templates"))

class MainHandler(webapp2.RequestHandler):
    def get(self):
        #me = {'ERICKA': gif_url}


        template = jinja_environment.get_template('templates2.html')
        self.response.write(template.render())

class newhandler(webapp2.RequestHandler):
    def get(self):
        base_url = "http://api.giphy.com/v1/gifs/search?"
        url_params = {'q': self.request.get('SearchBar'), 'api_key': 'dc6zaTOxFJmzC', 'limit': 10}

        giphy_response = urllib.urlopen(base_url + urllib.urlencode(url_params)).read()


        #giphy_json_content = giphy_response.read()
        parsed_giphy_dictionary = json.loads(giphy_response)
        gif_url = parsed_giphy_dictionary['data'][0]['images']['original']['url']
        me = {'ERICKA': gif_url}

        template = jinja_environment.get_template('template.html')
        self.response.write(template.render(me))



app = webapp2.WSGIApplication([
    ('/', MainHandler),
    ('/action',newhandler),
], debug=True)
