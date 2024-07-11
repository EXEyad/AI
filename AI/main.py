from textblob import WordList,Word
import string as st
from funcs import *
import csv

NAME = 'Zane'
VERSION = '0.0.1'
DEVELOPER ='Eyad Hassan'


def ask():
    prompt = input("ask something....\nYou:")
    return prompt


def getanswerindex(question:str,questions:list):
    for Index in range(len(questions)):
        if questions[Index] == question:
            break
        else:
            continue
    return Index


def getanswer(question_index :int,answer:list):
    return answer[question_index]



def addanswer(questions:list,answers:list,question:str,answer:str):
    questions.append(question)
    answers.append(answer)
    return [questions,answers]

def main():
    questions =[]
    answers =[]
    with open('questions.csv','r') as data:
        read =csv.reader(data,delimiter=',')
    is_r =True
    while is_r:
        prompt = ask()
        prompt = prompt.capitalize().strip()
        print(f"searching {prompt}")
        if prompt in questions:
            ind = getanswerindex(prompt,questions)
            print(f"Zain:{getanswer(ind,answers)}")
            if prompt in questions[2:5]:
                break
            else:
                continue
        else:
            print('I don\' Understand You!')
            newQ = prompt
            prompt = input('will you teach me it?\nyou:')
            prompt = prompt.strip().capitalize()
            prompt = Word(prompt)
            if prompt.correct() == 'Yes':
                questions.append(newQ)
                prompt = int(input(f"what does {newQ} mean:\n1.Function\n2.Question\nYou:"))
                if prompt == 1:
                    with open('funcs.py','a+') as fil:
                        args = []
                        t = int(input('How many args: '))
                        for b in range(t):
                            arg = input(f'arg {b}: ')
                            args.append(arg)
                        step = []
                        steps = int(input('how many steps: '))
                        for n in range(steps):
                            prompt = int(input(f'step type :\n1.Print\n2.Input\n3.Variable\nStep {n+1}: '))
                            if prompt == 1 :
                                prnt = int(input('what print type you need:\n1.String\n2.F.String\n3.Custom\nType: '))
                                if prnt == 1:
                                    prnt = input('what to print: ')
                                    step.append(f'  print(\'{prnt}\')\n')
                                elif prnt == 2:
                                    prnt = input('what to print: ')
                                    step.append(f'  print(f\'{prnt}\')\n')
                                elif prnt == 3:
                                    prnt = input('what to print: ')
                                    step.append(f'  print({prnt})\n')
                                else:
                                    print('bad Choose.')
                            elif prompt == 2 :
                                prompt = int(input('inputing:\n1.Custom\n2.String\ntype casting:'))
                                if prompt == 1:
                                    varn = input('variable name: ')
                                    vart = input('variable Typecast: ')
                                    vari = input('what to type when inputting: ')
                                    step.append(f'  {varn} = {vart}(input(\'{vari}\'))\n')
                                elif prompt == 2:
                                    varn = input('variable name: ')
                                    vari = input('what to type when inputting: ')
                                else:
                                    print('bad choose.')
                            elif prompt==3:
                                varn = input('variable name: ')
                                vard = input('variable data: ')
                                step.append(f'  {varn} = {vard}\n')
                            else:
                                print('bad choose.')
                        if len(args) >0:
                            func = [f'def {newQ}({args}):\n']
                        else:
                            func = [f'def {newQ}():\n']
                            
                        for z in range(len(step)):
                            func.append(step[z])
                        #(f"{newQ}()")
                        fil.writelines(func)            
                elif prompt == 2:
                    answers.append(input(str(newQ) + str(' means? ')))
                else:
                    print('bad choose.')


if __name__ == '__main__':
    main()
    