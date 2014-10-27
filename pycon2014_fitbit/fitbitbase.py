import os
import json
import fitbit
import config
import datetime
import cherrypy
from mako.lookup import TemplateLookup

mylookup = TemplateLookup(directories=['./templates'], output_encoding='utf-8', encoding_errors='replace')


class Graph(object):
    def serve_template(self, templatename, **kwargs):
        mytemplate = mylookup.get_template(templatename)
        return mytemplate.render(**kwargs)

    @cherrypy.expose
    def index(self):
        raise cherrypy.HTTPRedirect('/html/index.html') 
        
    @cherrypy.expose
    def steps(self):
        a_cl = fitbit.Fitbit(config.C_KEY, config.C_SECRET, system="en-GB",
                             resource_owner_key=config.resource_owner_key,
                             resource_owner_secret=config.resource_owner_secret)
        days = a_cl.time_series('activities/steps', period='max').get('activities-steps')
        if days:
            first_tracked = False
            days_json = []
            for d in days:
                print d, type(d)
                if first_tracked:
                    d_datetime = datetime.datetime.strptime(d['dateTime'], '%Y-%m-%d') 
                    # if weekend
                    if d_datetime.weekday() in (5, 6):
                        line_color = '#c77e24'
                    else:
                        line_color = '#abc123'
                    days_json.append({'min': 1000, 'date': d['dateTime'], 'steps': d['value'], 'lineColor': line_color})
                elif int(d['value']) > 0:
                    first_tracked = True
        days_json_str = json.dumps(days_json)
        return self.serve_template('steps.html', days=days_json_str)

cherrypy.config.update({'server.socket_host': '0.0.0.0',
                        'server.socket_port': 8080,
                        'tools.encode.on': True,
                        'tools.encode.encoding': 'utf-8',
                        'tools.staticdir.on': True,
                        'tools.staticdir.root': os.path.dirname(os.path.abspath(__file__)) + os.path.sep,
                        'tools.staticdir.dir': "."
                       })

cherrypy.quickstart(Graph(), '/')
