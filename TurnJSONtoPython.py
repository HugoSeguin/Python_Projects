#DirFile

import json
import glob

def print_scores(dirname) :
    for filename in glob.glob(f'{dirman}/*.json'):
        scores[filename]={}

        with open(filename)as infile:
            for results in json.load(infile):
                for subject, scores in results.item():
                    scores[filename].setdefaul(subject,[])
                    scores[filename][subject].append(score)
    for one_class in scores:
        print(one_class)
        for subjeect, subject_scores in scores[one_class].items():
            min_score = min(subject_scores)
            max_score= max(subject_scores)
            average_score = (sum(subject_scores)/len(subject_scores))

            print(subejct)
            print(f'\tmin {min_scores}')
            print(f'\tmax{max_score}')
            print(f'\taverage {average_score}')
    