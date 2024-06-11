"""
Source: GM_Forms_Session#3.pdf

"""

gm_session_2 = {
    "scenario": "Abi is a second author to a paper accepted to POPL. So doesn't have to go to POPL2019, but she is deciding whether she should go to the conference.",
    "Subgoals": [
        {
            "subgoal": "Find out what is being presented at the conference",
            "question": "Will Abi have formed this sub-goal as a step to their overall goal?",
            "answers": "Yes",
            "facets_used": ["Motivations", "Information Processing Style", "Attitude Towards Risk"],
            "why": "She wants to know what is presented. She doesn't want to waste time.",
            "Actions": [
                {
                    "action": "Scroll down to POPL 2019",
                    "before_action": {
                        "question": "Will ABI know what to do at this step? Why?",
                        "page_on_which_abi_take_the_action": "Dummy.html",
                        "answers": [
                            "answer1: Yes; facets: Information Processing Style; why: See what's more on this page",
                            "answer2: Yes; facets: Motivations; why: She wants to look at the program, because she wants to get an overview of the conference, and she is going for that"
                        ],
                    },
                    "after_action": {
                        "question": "If Abi does the right thing, will s/he know that s/he did the right thing and is making progress toward their goal? Why?",
                        "page_on_which_abi_is_after_the_action": "Dummy2.html",
                        "answers": [
                            "answer1: Yes; facets: None of the above; why: She wanted a lot of information and she gets lots of practical information that she needs"
                        ],
                    }
                },
                {
                    "action": "Scroll down",
                    "before_action": {
                        "question": "Will ABI know what to do at this step? Why?",
                        "page_on_which_abi_take_the_action": "Dummy.html",
                        "answers": [
                            "answer1: Yes; facets: Information Processing Style; why: She is seeing information popping up and she wants to see more"
                        ],
                    },
                    "after_action": {
                        "question": "If Abi does the right thing, will s/he know that s/he did the right thing and is making progress toward their goal? Why?",
                        "page_on_which_abi_is_after_the_action": "Dummy2.html",
                        "answers": [
                            "answer1: Yes; facets: Information Processing Style; why: She is seeing keynote pics and names of keynotes. Although the names don’t make sense, she is getting to know more about the conference.",
                            "answer2: Yes; facets: None of the above; why: Loves that there are tutorials so that she can learn more."
                        ],
                    }
                },
                {
                    "action": "Click on Program of POPL2019 Link",
                    "before_action": {
                        "question": "Will ABI know what to do at this step? Why?",
                        "page_on_which_abi_take_the_action": "Dummy.html",
                        "answers": [
                            "answer1: Yes; facets: Motivations; why: Abby is looking for more information on the program so she will do it.",
                            "answer2: Maybe; facets: Information Processing Style; why: Big Orange thing, so she might think that’s it"
                        ],
                    },
                    "after_action": {
                        "question": "If Abi does the right thing, will s/he know that s/he did the right thing and is making progress toward their goal? Why?",
                        "page_on_which_abi_is_after_the_action": "Dummy2.html",
                        "answers": [
                            "answer1: Maybe; facets: None of the above; why: It's overwhelming - a lot of information. She sees she is making progress, that there is lots of information."
                        ],
                    }
                },
                {
                    "action": "Scroll down",
                    "before_action": {
                        "question": "Will ABI know what to do at this step? Why?",
                        "page_on_which_abi_take_the_action": "Dummy.html",
                        "answers": [
                            "answer1: Yes; facets: Motivations; why: She wants to know more about the program"
                        ],
                    },
                    "after_action": {
                        "question": "If Abi does the right thing, will s/he know that s/he did the right thing and is making progress toward their goal? Why?",
                        "page_on_which_abi_is_after_the_action": "Dummy2.html",
                        "answers": [
                            "answer1: No; facets: Information Processing Style; why: There is a lot of information, so she is getting the information but at the same time, it is too much."
                        ],
                    }
                },
                {
                    "action": "Click on the distinguished paper",
                    "before_action": {
                        "question": "Will ABI know what to do at this step? Why?",
                        "page_on_which_abi_take_the_action": "Dummy.html",
                        "answers": [
                            "answer1: Maybe; facets: Information Processing Style; why: She is interested, but she is not going to click on any of them because she is not a tinkerer.",
                            "answer2: Maybe; facets: Attitude Towards Risk; why: Never been to this conference before, distinguished paper is going to be too advanced."
                        ],
                    },
                    "after_action": {
                        "question": "If Abi does the right thing, will s/he know that s/he did the right thing and is making progress toward their goal? Why?",
                        "page_on_which_abi_is_after_the_action": "Dummy2.html",
                        "answers": [
                            "answer1: Maybe; facets: None of the above; why: She is seeing that the papers are distinguished paper. The labels help"
                        ],
                    }
                },
                {
                    "action": "Explore the program: Go back to the main page to check tutorial",
                    "before_action": {
                        "question": "Will ABI know what to do at this step? Why?",
                        "page_on_which_abi_take_the_action": "Dummy.html",
                        "answers": [
                            "answer1: Maybe; facets: Information Processing Style; why: No way to go from here. There are links to the distinguished paper, but these are pretty heavy."
                        ],
                    },
                    "after_action": {
                        "question": "If Abi does the right thing, will s/he know that s/he did the right thing and is making progress toward their goal? Why?",
                        "page_on_which_abi_is_after_the_action": "Dummy2.html",
                        "answers": [
                            "answer1: Yes; facets: None of the above; why: She is here"
                        ],
                    }
                },
                {
                    "action": "Click on one of the tutorial titles",
                    "before_action": {
                        "question": "Will ABI know what to do at this step? Why?",
                        "page_on_which_abi_take_the_action": "Dummy.html",
                        "answers": [
                            "answer1: Yes; facets: Information Processing Style; why: She is here to do that. She wants to get the task done."
                        ],
                    },
                    "after_action": {
                        "question": "If Abi does the right thing, will s/he know that s/he did the right thing and is making progress toward their goal? Why?",
                        "page_on_which_abi_is_after_the_action": "Dummy2.html",
                        "answers": [
                            "answer1: Maybe; facets: None of the above; why: Abby is a little more confused. Abby can't figure out if it's a tutorial."
                        ],
                    }
                }
            ]
        }
    ]
}
