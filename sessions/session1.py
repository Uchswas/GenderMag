"""
Source: GM_Forms-FilledIn-2019-0118.pdf

"""

gm_session_1 = {
    "scenario": "Abi has decided to submit a paper to ASE 2019 and doing all the pre-submission actions available on the website",
    "persona" : "ABI",
    "Subgoals": [
        {
            "subgoal": "Finding out what the conference is about",
            "question": "Will Abi have formed this sub-goal as a step to their overall goal?",
            "answers": "Yes",
            "facets_used": ["Motivations", "Information Processing Style"],
            "why": "She wants to publish so she wants to see what’s in the site",
            "Actions": [
                {
                    "action": "Accept cookie on bottom of screen",
                    "before_action": {
                        "question": "Will ABI know what to do at this step? Why?",
                        "page_on_which_abi_take_the_action": "Dummy.html",
                        "answers": [
                            "answer1: Yes; facets: None of the above; why: Familiar with such notices across other web sites",
                            "answer2: Maybe; facets: Attitude Towards Risk; why: Why give away privacy data before really needing to do so",
                            "answer3: No; facets: Information Processing Style and Attitude Towards Risk; why: She thinks that IEEE doesn’t need this information"
                        ],
                    },
                    "after_action": {
                        "question": "If Abi does the right thing, will s/he know that s/he did the right thing and is making progress toward their goal? Why?",
                        "page_on_which_abi_is_after_the_action": "Dummy2.html",
                        "answers": [
                            "answer1: Yes; facets: None of the above; why: She sees more information on the website. Abi knows she is making progress towards her goal",
                            "answer2: Maybe; facets: None of the above; why: She is not sure what happened as an effect"
                        ],
                    }
                },
                {
                    "action": "Scroll down to see what other information is here",
                    "before_action": {
                        "question": "Will ABI know what to do at this step? Why?",
                        "page_on_which_abi_take_the_action": "Dummy.html",
                        "answers": [
                            "answer1: Yes; facets: Information Processing Style; why: Familiar with such notices across other web sites"
                        ],
                    },
                    "after_action": {
                        "question": "If Abi does the right thing, will s/he know that s/he did the right thing and is making progress toward their goal? Why?",
                        "page_on_which_abi_is_after_the_action": "Dummy2.html",
                        "answers": [
                            "answer1: No; facets: Information Processing Style; why: Abi is dissatisfied she doesn't get any more information than she had before"
                        ],
                    }
                },
                {
                    "action": "Click on research papers in ASE 2019 tracks (box)",
                    "before_action": {
                        "question": "Will ABI know what to do at this step? Why?",
                        "page_on_which_abi_take_the_action": "Dummy.html",
                        "answers": [
                            "answer1: Maybe; facets: Information Processing Style and Learning: by Process vs. by Tinkering; why: She will look through the main part of the screen and the two blue sections. She doesn't read everything but will find stuff that is relevant"
                        ],
                    },
                    "after_action": {
                        "question": "If Abi does the right thing, will s/he know that s/he did the right thing and is making progress toward their goal? Why?",
                        "page_on_which_abi_is_after_the_action": "Dummy2.html",
                        "answers": [
                            "answer1: Maybe; facets: Information Processing Style; why: She sees another link about research and may know what a research paper is",
                            "answer2: No; facets: Information Processing Style; why: She sees the same information as before. She might think she is not getting anywhere"
                        ],
                    }
                },
                {
                    "action": "Click on call for papers",
                    "before_action": {
                        "question": "Will ABI know what to do at this step? Why?",
                        "page_on_which_abi_take_the_action": "Dummy.html",
                        "answers": [
                            "answer1: Yes; facets: Motivations and Information Processing Style; why: Veering towards the call for paper if Abi’s topic is in the CFP",
                            "answer2: Maybe; facets: Information Processing Style; why: Instead, scroll down to see the PC in faint hope of seeing someone she knows"
                        ],
                    },
                    "after_action": {
                        "question": "If Abi does the right thing, will s/he know that s/he did the right thing and is making progress toward their goal? Why?",
                        "page_on_which_abi_is_after_the_action": "Dummy2.html",
                        "answers": [
                            "answer1: Yes; facets: Information Processing Style; why: Data mining is in the topic & what is tech papers about"
                        ],
                    }
                },
                {
                    "action": "Decide to submit the paper",
                    "before_action": {
                        "question": "Will ABI know what to do at this step? Why?",
                        "page_on_which_abi_take_the_action": "Dummy.html",
                        "answers": [
                            "answer1: Yes; facets: Motivations; why: Her topic is involved",
                            "answer2: Maybe; facets: Information Processing Style and Attitude Towards Risk; why: She wants to get more information before she decides to take the plunge",
                            "answer3: No; facets: Attitude Towards Risk; why: She doesn't think it will get in: innovative/ related work very well. I don't recognize the names of the PC/ what’s the acceptance rate/ premier in SE"
                        ],
                    }
                }
            ]
        }
    ]
}
