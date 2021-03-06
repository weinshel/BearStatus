import datetime, yaml
import entry, do_run

# This codeblock checks whether a certain datastore entry exists, determining whether to add the hardcoded blocks to the datastore or not
def start():
    q = do_run.DoRun.all()
    result = q.get()
    
    if not result:
        # Creates a datastore entry to prevent readding hardcoded blocks
        hasRun = do_run.DoRun(runTrue = True)
        hasRun.put()

        # Opens the reg_blocks.yaml file and saves the contents to doc
        with open('backend/reg_blocks.yaml', 'r') as f:
            doc = yaml.load(f)
        
        # For every entry in the 'treeroot' directory of the reg_blocks.yaml file, do this:
        for x in doc['treeroot']:
            # Take the variables 'shour' and 'smin' and create a formated time stored in sTime
            sTime = datetime.time(doc['treeroot'][x]['shour'], doc['treeroot'][x]['smin'])
            # Take the variables 'ehour' and 'emin' and create a formated time stored in eTime
            eTime = datetime.time(doc['treeroot'][x]['ehour'], doc['treeroot'][x]['emin'])
            
            # Store the instance of Entry with the inputed data into entries
            entries = entry.Entry(key_name=doc['treeroot'][x]['key_name'],
                                  name = doc['treeroot'][x]['name'],
                                  sTime = sTime,
                                  eTime = eTime,
                                  day = doc['treeroot'][x]['day'])
            # Store the data that entries contains into the datastore
            entries.put()