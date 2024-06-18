"""
Source: GM_Forms-FilledIn-2019-0118.pdf

"""


import sys
import os
from constant import BASE_IMAGE_PATH



from utils import *

gm_session1 = {
    "scenario": "Abi has decided to submit a paper to ASE 2019 and doing all the pre-submission actions available on the website",
    "persona" : "ABI",
    "Subgoals": [
        {
            "subgoal": "Finding out what the conference is about",
            "question": "Will Abi have formed this sub-goal as a step to their overall goal?",
            "answers": "Yes",
            "subgoal_page_image" : BASE_IMAGE_PATH+"ASE2019HomePage.png",
            "facets_used": ["Motivations", "Information Processing Style"],
            "why": "She wants to publish so she wants to see what’s in the site. Abi is task-motivated, she has a clear goal in mind, which is to publish a paper. Therefore, she would have a subgoal to find out what this conference is all about.",
            "Actions": [
                {
                    "action": "Accept cookie on bottom of screen",
                    "before_action": {
                        "question": "Will ABI know what to do at this step? Why?",
                        "page_on_which_abi_take_the_action": BASE_IMAGE_PATH+"ASE2019HomePage.png",
                        "answers": [
                            "answer1: Yes; facets: None of the above; why: Abi is familiar with such notices across other web sites",
                            "answer2: Maybe; facets: Attitude Towards Risk; why: Why give away privacy data before really needing to do so. Abi rarely has spare time, she does not want to give away data that she might later have to spend time and undo. Due to her attitude towards risk, she may not accept the cookies.",
                            "answer3: No; facets: Information Processing Style and Attitude Towards Risk; why: She thinks that IEEE doesn’t need this information. She is not sure why IEEE would need this information before she does anything. Once again, she doesn't want to spend time doing something she doesnt need to do"
                        ],
                    },
                    "after_action": {
                        "question": "If Abi does the right thing, will s/he know that s/he did the right thing and is making progress toward their goal? Why?",
                        "page_on_which_abi_is_after_the_action": BASE_IMAGE_PATH+"ASE2019HomePage.png",
                        "answers": [
                            "answer1: Yes; facets: None of the above; why: She sees more information on the website. Abi knows she is making progress towards her goal",
                            "answer2: Maybe; facets: None of the above; why: She is not sure what happened as an effect, there is no feedback."
                        ],
                    }
                },
                {
                    "action": "Scroll down to see what other information is here",
                    "before_action": {
                        "question": "Will ABI know what to do at this step? Why?",
                        "page_on_which_abi_take_the_action": BASE_IMAGE_PATH+"ASE2019HomePage.png",
                        "answers": [
                            "answer1: Yes; facets: Information Processing Style; why: she likes to read comprehensively, so she will scroll"
                        ],
                    },
                    "after_action": {
                        "question": "If Abi does the right thing, will s/he know that s/he did the right thing and is making progress toward their goal? Why?",
                        "page_on_which_abi_is_after_the_action": BASE_IMAGE_PATH+"ASE2019HomePage.png",
                        "answers": [
                            "answer1: No; facets: Information Processing Style; why: Abi is dissatisfied she doesn't get any more information than she had before"
                        ],
                    }
                },
                {
                    "action": "Click on research papers in ASE 2019 tracks (box)",
                    "before_action": {
                        "question": "Will ABI know what to do at this step? Why?",
                        "page_on_which_abi_take_the_action": BASE_IMAGE_PATH+"ASE2019HomePage.png",
                        "answers": [
                            "answer1: Maybe; facets: Information Processing Style and Learning: by Process vs. by Tinkering; why: She will look through the main part of the screen and the two blue sections. She doesn't read everything but will find stuff that is relevant"
                        ],
                    },
                    "after_action": {
                        "question": "If Abi does the right thing, will s/he know that s/he did the right thing and is making progress toward their goal? Why?",
                        "page_on_which_abi_is_after_the_action": BASE_IMAGE_PATH+"ASE2019ResearchPage.png",
                        "answers": [
                            "answer1: Maybe; facets: Information Processing Style; why: She sees another link about research and may know what a research paper is",
                            "answer2: No; facets: Information Processing Style; why: She sees the same information as before. She might think she is not getting anywhere since there has been no progress"
                        ],
                    }
                },
                {
                    "action": "Click on call for papers",
                    "before_action": {
                        "question": "Will ABI know what to do at this step? Why?",
                        "page_on_which_abi_take_the_action": BASE_IMAGE_PATH+"ASE2019ResearchPage.png",
                        "answers": [
                            "answer1: Yes; facets: Motivations and Information Processing Style; why: Veering towards the call for paper if Abi’s topic is in the CFP. She is task-motivated and wants to publish.",
                            "answer2: Maybe; facets: Information Processing Style; why: Instead, scroll down to see the PC in faint hope of seeing someone she knows"
                        ],
                    },
                    "after_action": {
                        "question": "If Abi does the right thing, will s/he know that s/he did the right thing and is making progress toward their goal? Why?",
                        "page_on_which_abi_is_after_the_action": BASE_IMAGE_PATH+"ASE2019ResearchPage.png",
                        "answers": [
                            "answer1: Yes; facets: Information Processing Style; why: Data mining is in the topic & that is what tech papers are about"
                        ],
                    }
                },
                {
                    "action": "Decide to submit the paper",
                    "before_action": {
                        "question": "Will ABI know what to do at this step? Why?",
                        "page_on_which_abi_take_the_action":  BASE_IMAGE_PATH+"ASE2019ResearchPage.png",
                        "answers": [
                            "answer1: Yes; facets: Motivations; why: Her topic is involved, so based on her motivations, she will know what to do",
                            "answer2: Maybe; facets: Information Processing Style and Attitude Towards Risk; why: She wants to get more information before she decides to take the plunge, because this can lead her to waste her time",
                            "answer3: No; facets: Attitude Towards Risk; why: She doesn't think it will get in: innovative/ related work very well. I don't recognize the names of the PC/ what’s the acceptance rate/ premier in SE, there are a lot of unknowns and Abi doesnt have time to spend on things that might not be fruitful"
                        ],
                    }
                }
            ]
        }
    ]
}


print(gm_session1)