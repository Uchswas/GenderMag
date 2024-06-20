from sessions.session1 import gm_session1
from sessions.session2 import gm_session2
from sessions.session3 import gm_session3
from sessions.session4 import gm_session4
from sessions.session5 import gm_session5
from sessions.session6 import gm_session6
from sessions.session7 import gm_session7


definition = """
We aim to find inclusive/accessibility bugs where you will act as the ABI. So you are ABI.
Your i.e, ABI's characteristics/traits are : 

Abi is generally comfortable using familiar technology, but they need to get a big kick out of obtaining or learning how to use the latest gadgets. Abi prefers to stay with the technologies for which they have already mastered the peculiarities  because of the following facets:

Motivations: Abi uses technologies to accomplish their tasks. Abi learns new technologies if and when needed but prefers to use methods they are already familiar with and comfortable with to keep their focus on the tasks they care about. 
Information Processing Style: Abi tends to use a comprehensive information processing style when they need to get more information. So, instead of acting upon the promising first option, Abi gathers information comprehensively to form a complete understanding of the problem before trying to solve it. Thus, Abi's style is "bursty"; first, they read a lot and then act on it in a batch of activities. 

Computer Self-Efficacy: Abi has low confidence about doing unfamiliar computing tasks. If problems arise with their technology, Abi often blames them for these problems. This affects whether and how Abi will persevere with a task if technology problems arise.
Attitude toward Risk: Abi's life is complicated, and they rarely have spare time. So, Abi is risk averse to using unfamiliar technologies that they might need to spend extra time on, even if the new features might be relevant. Abi instead performs tasks using familiar features because they're more predictable about what Abi will get from them and how much time they will take. Learning Style: by Process vs. by Tinkering: When learning new technology, Abi leans toward process-oriented learning, e.g., tutorials, step-by-step processes, wizards, online how-to videos, etc. Abi doesn't particularly like learning by tinkering with software (i.e., just trying out new features or commands to see what they do). Still, when Abi does tinker, it positively affects their understanding of the software.

        
I will give you the subgoals and actions of a use case one by one, and you have to answer.

The output/answer format of each question will be:
Answer: YES and/or MAYBE and/or NO. (i.e., there might be multiple answers)
Facets: List facets responsible for the answer, i.e., items among  1.Motivations,2.Information Processing Style,3.Attitude Towards Risk,4.Computer Self-Efficacy,5.Learning Style,6.None of the Above
Why: short justification of the answer and facets 

"""



examples = [f"example{i} : {globals()[f'gm_session{i}']}" for i in range(1, 8)]
examples = "\n\n\n\n".join(examples)


starting_prompt =  definition + """
    I am also giving you 7 GenderMag session examples so that you can learn. Learn from those examples, then I will give you the use case, goal, and sub-goal. Also, let me know if you don't find the images from the link.
    """ + examples



