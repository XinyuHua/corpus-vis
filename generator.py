# Author: Xinyu Hua
# Last modified: 2017-08-26
import json, os

class visGenerator(object):
    """A class to generate HTML page for corpus visualization."""
    def __init__(self, data_path, dataset_title='Generic corpus'):
        self.prefix = open('prefix.txt').read()
        self.title = dataset_title
        self.data_path = data_path
        if not os.path.exists(self.data_path):
            print('Data path does not exist!')
            exit()
        self.__loadData__()
    
    def __loadData__(self):
        print('loading corpus...')
        self.objs = [ json.loads(line.strip()) for line in open(os.path.join(self.data_path, 'corpus.jsonlist')) ]

    def renderHTML(self, out_path):
        print('generating html...')
        fout = open(out_path, 'w')
        fout.write(self.prefix.strip() + '\n')
        fout.write('<h1>' + self.title + '</h1>\n\n')
        for sid, sample in enumerate(self.objs):
            secondary_title = sample['title']
            body = sample['body']
            fout.write('<h2>Title: ' + secondary_title + '</h2>\n')
            fout.write('<div><p>' + body.encode('utf-8').replace('\n', '<br>') + '</p></div>\n')
        fout.write('</body>\n</html>')
        fout.close()

gen = visGenerator(data_path='data')
gen.renderHTML('output/demo.html')
