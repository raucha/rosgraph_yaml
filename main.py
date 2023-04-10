#! /usr/bin/python3
import re
# from pprint import pprint
import yaml
import sys

input_str = sys.argv[1]

class RosgraphParser():
    def __init__(self):
        self.node_info = {}
        self.node_name = ''
        self.port_type = ''
        self.str2port_type = {
            'Publications': 'publish',
            'Subscriptions': 'subscribe',
            # 'Services': 'service'
        }
        

    def feed(self, s: str):
        for line in s.splitlines():
            self.feed_oneline(line)
    
    def feed_oneline(self, line: str):
        # Nodename
        node_regex = re.compile(r'^Node \[(.*?)\]$')
        if node_regex.match(line):
            self.node_name = node_regex.search(line).group(1)
            self.node_info[self.node_name] = { n:[] for n in self.str2port_type.values()}
            return
        
        # Port Type
        for k, v in self.str2port_type.items():
            if re.compile(r'^{}:.*'.format(k)).match(line):
                self.port_type = v
                return
        
        # Port name
        topic_regex = re.compile(r'^ \* (.*) \[(.*)\]$')
        if topic_regex.match(line):
            topicname = topic_regex.search(line).group(1)
            topictype = topic_regex.search(line).group(2)
            self.node_info[self.node_name][self.port_type].append({'name':topicname, 'type':topictype})
            return
        
        # Ignore
        return
    
    def result(self):
        return self.node_info

rp = RosgraphParser()
rp.feed(input_str)
print(yaml.dump(rp.result()))
