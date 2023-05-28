from recbole.quick_start import run_recbole


if __name__ == '__main__':
    run_recbole(model='SASRec', dataset='ml-100k', config_file_list=['test.yaml'])