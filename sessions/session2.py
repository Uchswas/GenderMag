"""
Source: GM_Forms_Session#3.pdf

"""

gm_session2 = {
    "scenario": "Abi is a second author to a paper accepted to POPL. So doesn't have to go to POPL2019, but she is deciding whether she should go to the conference.",
    "persona" : "ABI",
    "Subgoals": [
        {
            "subgoal": "Find out what is being presented at the conference",
            "question": "Will Abi have formed this sub-goal as a step to their overall goal?",
            "answers": "Yes",
            "image" :  "2.action1.png",
            "facets_used": ["Motivations", "Information Processing Style", "Attitude Towards Risk"],
            "why": "She wants to know what is presented bcause it aligns with her overall tasks. She doesn't want to waste time because of her attitude towards risk.",
            "Actions": [
                {
                    "action": "Scroll down to POPL 2019",
                    "before_action": {
                        "question": "Will ABI know what to do at this step? Why?",
                        "page_on_which_abi_take_the_action": "2.action1.png",
                        "answers": [
                            "answer1: Yes; facets: Information Processing Style; why: See what's more on this page, she is a comprehensive information processor",
                            "answer2: Yes; facets: Motivations; why: She wants to look at the program, because she wants to get an overview of the conference, and she is going for that"
                        ],
                    },
                    "after_action": {
                        "question": "If Abi does the right thing, will s/he know that s/he did the right thing and is making progress toward their goal? Why?",
                        "page_on_which_abi_is_after_the_action": "2.action2.png",
                        "answers": [
                            "answer1: Yes; facets: ☐ Motivations ,Information Processing Stylee; why: She wanted a lot of information, because she is a comprehensive information processor and she gets lots of practical information that she needs"
                        ],
                    }
                },
                {
                    "action": "She is going to scroll down",
                    "before_action": {
                        "question": "Will ABI know what to do at this step? Why?",
                        "page_on_which_abi_take_the_action": "2.action2.png",
                        "answers": [
                            """
                            answer1: Yes; facets: Information Processing Style; 
                            why: She is seeing information popping up and she wants to see more, as she is a comprehensive information processor
                            """
                        ],
                    },
                    "after_action": {
                        "question": "If Abi does the right thing, will s/he know that s/he did the right thing and is making progress toward their goal? Why?",
                        "page_on_which_abi_is_after_the_action": "2.action3.png",
                        "answers": [
                            "answer1: Yes; facets: Information Processing Style, Learning: Style; why: She is seeing keynote pics and names of keynotes. Although the names don’t make sense, she is getting to know more about the conference. Loves that there are tutorials so that she can learn more, because of her process oriented learning style.",
                        ],
                    }
                },
                {
                    "action": "Click on Program of POPL2019 Link",
                    "before_action": {
                        "question": "Will ABI know what to do at this step? Why?",
                        "page_on_which_abi_take_the_action": "2.action3.png",
                        "answers": [
                            "answer1: Yes; facets: Motivations, Information Processing Style; why: Abby is looking for more information on the program so she will do it.",
                            "answer2: Maybe; facets: None of the above; why: Big Orange thing, so she might think that’s it"
                        ],
                    },
                    "after_action": {
                        "question": "If Abi does the right thing, will s/he know that s/he did the right thing and is making progress toward their goal? Why?",
                        "page_on_which_abi_is_after_the_action": "2.action4.png",
                        "answers": [
                            "answer1: Maybe; facets:  Attitude Towards Risk.  Learning Style; why: It's overwhelming - a lot of information. She sees she is making progress, that there is lots of information. But, she is overwhelmed with so much information it doesn’t match her learning style"
                        ],
                    }
                },
                {
                    "action": "Scroll down",
                    "before_action": {
                        "question": "Will ABI know what to do at this step? Why?",
                        "page_on_which_abi_take_the_action": "2.action4.png",
                        "answers": [
                            "answer1: Yes; facets: Motivations; why: She wants to know more about the program"
                        ],
                    },
                    "after_action": {
                        "question": "If Abi does the right thing, will s/he know that s/he did the right thing and is making progress toward their goal? Why?",
                        "page_on_which_abi_is_after_the_action": "2.action5.png",
                        "answers": [
                            "answer1: Maybe; facets: Information Processing Style, Attitude towards Risk; why: There is a lot of information, so she is getting the information but at the same time, it is too much.",
                            "answer2: Maybe; facets: Attitude Towards Risk ,Learning Style ; why: Too much information makes it hard for her to filter out what is good; she expects some highlights and doesn't want to waste time; not seeing the keynote/tutorials anymore increases her frustration."
                        ],
                    }
                },
                {
                    "action": "Click on the distinguished paper",
                    "before_action": {
                        "question": "Will ABI know what to do at this step? Why?",
                        "page_on_which_abi_take_the_action": "2.action5.png",
                        "answers": [
                            "answer1: Maybe; facets: Learning Style; why: Why?She is interested, but she is not going to click on any of them because she is not a tinkerer. There is a lot of labels that she doesn’t understand.",
                            "answer2: No; facets: Motivation, Computer Self Efficiency, Learning Style; why: Never been to this conference before, feels distinguished paper is too advanced, doesn't want to jump to the end; she wanted to look at the keynotes to get a sense of what the conference is about.."
                        ],
                    },
                    "after_action": {
                        "question": "If Abi does the right thing, will s/he know that s/he did the right thing and is making progress toward their goal? Why?",
                        "page_on_which_abi_is_after_the_action": "2.action6.png",
                        "answers": [
                            "answer1: Maybe; facets: None of the above; why: She is seeing that the papers are distinguished paper. The labels help"
                        ],
                    }
                },
                {
                    "action": "Explore the program: Go back to the main page to check tutorial",
                    "before_action": {
                        "question": "Will ABI know what to do at this step? Why?",
                        "page_on_which_abi_take_the_action": "2.action6.png",
                        "answers": [
                            "answer1: Yes; facets: Information Processing Style, computer self-efficacy, Learning Style; why: No way to proceed; links to the distinguished paper are heavy; she needs introductory material to learn about the community and determine its value. She wants a global view of the conference, so this is important. She is also looking for a step-by-step guide."
                        ],
                    },
                    "after_action": {
                        "question": "If Abi does the right thing, will s/he know that s/he did the right thing and is making progress toward their goal? Why?",
                        "page_on_which_abi_is_after_the_action": "2.action7.png",
                        "answers": [
                            "answer1: Yes; facets: None of the above; why: She is here, she can see the feedback on the screen"
                        ],
                    }
                },
                {
                    "action": "Click on one of the tutorial titles",
                    "before_action": {
                        "question": "Will ABI know what to do at this step? Why?",
                        "page_on_which_abi_take_the_action": "2.action7.png",
                        "answers": [
                            "answer1: Yes; facets: Motivation, Learning Style; why: She is here to do that. She wants to get the task done. Her goal to get more information and make decision to whether to attend"
                        ],
                    },
                    "after_action": {
                        "question": "If Abi does the right thing, will s/he know that s/he did the right thing and is making progress toward their goal? Why?",
                        "page_on_which_abi_is_after_the_action": "2.action7.png",
                        "answers": [
                            "answer1: Maybe; facets: Information Processing Style, Computer Self-Efficacy, Learning Style; why: Abby is a little more confused and can't figure out if it's a tutorial. She likes elegant, foundational, formal words due to her familiarity with algorithms. The importance pushes her to say yes, but the process makes her lean towards no. It doesn't feel like a tutorial, and it's unclear what she will get out of it as it reads very much like a research paper.",
                            "answer2: No; facets: Computer Self-Efficacy,Attitude Towards Risk, Learning Style; why:The tutorial seems not hands-on, more like a lecture, and quite complicated, so she is unsure if she will understand it and whether it is worth her time to attend the conference."

                        ],
                    }
                }
            ]
        }
    ]
}
