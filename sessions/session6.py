"""
Source: GM_Forms_Session#5.pdf

"""

from constant import BASE_IMAGE_PATH

gm_session5 = {
    "scenario": "Abi is physically at ICSE 2019 and is planning which sessions to go to. (It’s Tuesday night in her hotel room.)",
    "persona" : "ABI",
    "Subgoals": [
        {
            "subgoal": "What sessions I should go to tomorrow",
            "question": "Will Abi have formed this sub-goal as a step to their overall goal?",
            "subgoal_page_image" : BASE_IMAGE_PATH+"ICSE2019Home.png",
            "answers": "Yes",
            "facets_used": ["Motivations", "Information Processing Style"],
            "why": "Make good use of her time. She’s a reader.",
            "Actions": [
                {
                    "action": "Click on the program menu item",
                    "before_action": {
                        "question": "Will ABI know what to do at this step? Why?",
                        "page_on_which_abi_take_the_action": BASE_IMAGE_PATH+"ICSE2019Home.png",
                        "answers": [
                            "answer1: Yes; facets: None of the above; why: Most promising menu option.",
                            "answer2: Maybe; facets: Motivations, Information Processing Style; why: Attending is the first tab and she’s attending so maybe. She is familiar with the menu items so she will know to click on Program",
                            "answer3: No; facets: Information Processing Style; why: Scroll down to see whats on the rest of the page (she’s a reader).",
                        ],
                    },
                    "after_action": {
                        "question": "If Abi does the right thing, will s/he know that s/he did the right thing and is making progress toward their goal? Why?",
                        "page_on_which_abi_is_after_the_action": BASE_IMAGE_PATH+"ICSE2019Home.png",
                        "answers": [
                            "answer1: Yes; facets: Motivations, Information Processing Style; why: It’s all about the program, that’s what she wanted."
                        ],
                    }
                },
                {
                    "action": "Click at complete program",
                    "before_action": {
                        "question": "Will ABI know what to do at this step? Why?",
                        "page_on_which_abi_take_the_action": BASE_IMAGE_PATH+"ICSE2019Home.png",
                        "answers": [
                            "answer1: Yes; facets: Information Processing Style; why: She is a reader and she is wanting to go through the program.",
                            "answer2: Maybe; facets: Motivations, Information Processing Style, Attitude Towards Risk, Learning style; why:  Week overview gives more of a top level view than details which is negetive; She will probably look to see what's tomorrow and not get overwhelmed which is positive",
                        ],
                    },
                    "after_action": {
                        "question": "If Abi does the right thing, will s/he know that s/he did the right thing and is making progress toward their goal? Why?",
                        "page_on_which_abi_is_after_the_action": BASE_IMAGE_PATH+"ICSE2019Program.png",
                        "answers": [
                            "answer1: Yes; facets: Motivations; why: She finds “session”.",
                            "answer2: Yes; facets: Information Processing Style; why: She does lots of program info, and lots of sessions, altho it does look like a lot!",
                            "answer3: Maybe; facets: Learning; why: Learning style makes this fairly negative. A little rocky -- Might be getting overwhelmed -- this program is HUGE."
                        ],
                    }
                },
                {
                    "action": "Click on session timeline",
                    "before_action": {
                        "question": "Will ABI know what to do at this step? Why?",
                        "page_on_which_abi_take_the_action": BASE_IMAGE_PATH+"ICSE2019Timeline.png",
                        "answers": [
                            "answer1: Yes; facets: Motivations, Information Processing Style; why: She would have read the part on the top and not have even scrolled.",
                            "answer2: Yes; facets: Information Processing Style; why: Wants the scaffolding that this tab might give her.",
                            "answer3: Yes; facets: Information Processing Style; why: Whether make sense of this page entirely before moving on to the next page."
                        ],
                    },
                    "after_action": {
                        "question": "If Abi does the right thing, will s/he know that s/he did the right thing and is making progress toward their goal? Why?",
                        "page_on_which_abi_is_after_the_action": BASE_IMAGE_PATH+"ICSE2019Timeline.png",
                        "answers": [
                            "answer1: Yes; facets: Motivations, Information Processing Style; why: She likes this view better than the previous view she was on because it’s more of a top-overviewish view that might help her identify her interests.",
                            "answer2: Maybe; facets: None of the above; why: What are the gray things? Are they not presentations at all? Room #? What is room1, room2, …. Yes side: She knows she’s going to ICSE paper presentations. No side: this is taking forever. (Doesnt have too much time to spare and its not easy)"
                        ],
                    }
                }
            ]
        }
    ]
}
