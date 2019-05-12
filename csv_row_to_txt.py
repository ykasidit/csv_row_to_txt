import pandas as pd
import argparse
import os


def get_args():
    parser = argparse.ArgumentParser()

    parser.add_argument('--csv_input',
                        help="source csv file", required=True)
   
    return vars(parser.parse_args())


def main():
    args = get_args()
    df = pd.read_csv(args['csv_input'])
    print 'read csv_input got n rows:', len(df)

    format_str = '''
%s
======

Sex: %s

Age: %s

Country of Origin: %s

Designation: %s
'''
    
    print 'using format_str:', format_str
    try:
        os.mkdir('output')
    except Exception as ex:
        print 'WARNING: output folder mkdir failed - likely already exists:', ex

    for index, row in df.iterrows():
        row = row.astype(str).str.strip()
        fn = str(row.iloc[0]).strip()+".txt"
        fp = os.path.join('output', fn)
        with open(fp, 'wb') as of:
            print 'row {} values: {}'.format(index, tuple(row.values.tolist()))
            outstr = format_str % tuple(row.values.tolist())
            print 'output:', outstr
            of.write(outstr)
            
    print '--- all done ---'
    
if __name__ == "__main__":
    main()
