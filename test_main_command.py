import os


def test():
    cmd = 'python csv_row_to_txt.py --csv_input test_data.csv'

    print 'run cmd:', cmd    
    ret = os.system(cmd)
    print 'cmd ret:', ret

    assert ret == 0


if __name__ == "__main__":
    test()

