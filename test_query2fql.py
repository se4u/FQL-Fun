from query2fql import *
def test_fqlmaker():
    samples = fbnlpdata.samples
    errors = 0
    for unitTest in samples:
        output = fqlmaker(unitTest['input'])
        if unitTest['output']['query'] != output:
            print 'Expected: ',  unitTest['output']['query'], 'Actual: ',  output, 'input words', unitTest['input']
            errors += 1
    print 'Total errors ', errors

def test_extract_limit():
    samples = fbnlpdata.samples
    errors = 0
    for unitTest in samples:
        output = extract_limit(unitTest['input'])
        if unitTest['output']['limit'] != output:
            print 'expected: ', unitTest['output']['limit'], 'actual: ', output
            errors += 1
        else:
            print 'successful for ', unitTest['input'], 'output is', output
    print 'Total errors', errors

def test_find_table():
    samples = fbnlpdata.samples
    errors = 0
    for unitTest in samples:
        try:
            output = find_table(unitTest['input'])
        except:
            output = None
        if unitTest['output']['table'] != output:
            print 'expected: ', unitTest['output']['table'], 'actual: ', output
            errors += 1
        else:
            print 'successful for ', unitTest['input'], 'output is', output
    print 'Total errors', errors
