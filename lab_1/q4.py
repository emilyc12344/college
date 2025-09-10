#!/usr/bin/env python3

class Test(object):
    def __init__(self, name, correct, p_m):
        self.subject_name = name
        self.correct_answers = correct
        self.passing_mark = p_m

class Student(object):
    def __init__(self, name):
        self.name = name
    def take_test(self, paper, ans):
        corr_ans = paper.correct_answers
        q = 0
        mark = 0
        for i in ans:
            if i == corr_ans[q]:
                mark += 1
            q += 1
        p = (mark / len(ans)) * 100
        #print(type(int(paper.passing_mark[:-1])))
        if p >= int(paper.passing_mark[:-1]):
            print(f'{self.name} passed the {paper.subject_name} test with the score of {p}%')
        else:
            print(f'{self.name} failed the {paper.subject_name}!')

paper1 = Test('Maths', ['1A', '2C', '3D', '4A', '5A'], '60%')
paper2 = Test('Chemistry', ['1C', '2C', '3D', '4A'], '75%')
paper3 = Test('Computing', ['1D', '2C', '3C', '4B', '5D', '6C', '7A'], '75%')

stu1 = Student('Tom')
stu1.take_test(paper2, ['1C', '2C', '3D', '4A'])

stu2 =  Student('John')
stu2.take_test(paper1, ['1B', '2C', '3A', '4A', '5B'])