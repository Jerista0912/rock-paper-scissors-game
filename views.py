from django.shortcuts import render
import random
def func (request):
    choices=['rock','paper','scissor']
    result=' '
    if request.method == 'POST':
      userchoice=request.POST.get('choice')
      cpuchoice=random.choice(choices)
      if userchoice==cpuchoice:
                result="Tie"
      elif userchoice=='rock'  and cpuchoice=='scissor':
                result="You Win"
      elif userchoice=='scissor'  and cpuchoice=='rock':
                result="You Lose"
      elif userchoice=='rock' and  cpuchoice=='paper':
                 result="You Lose"
      elif userchoice=='paper' and  cpuchoice=='rock':
               result="You win"
      elif userchoice=='scissor' and  cpuchoice=='paper':
               result="You Win"
      elif userchoice=='paper' and  cpuchoice=='scissor':
                result="You Lose"
      else:
                print("Please select your choice.........")
      return render(request,'index.html',{ 'userchoice':userchoice,'cpuchoice':cpuchoice,'result':result})
    return render(request,'index.html')     
