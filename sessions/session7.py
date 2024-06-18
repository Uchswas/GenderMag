"""
Source: GM_Forms_Session#6.pdf

"""
from constant import BASE_IMAGE_PATH

gm_session6 = {
    "scenario": "Abi (is Chinese citizen, lives in US (NOT a permanent resident)) has decided to go to ICSE and is looking into Travel Visa stuff now",
    "persona" : "ABI",
    "Subgoals": [
        {
            "subgoal": "Look for visa information in the conference website",
            "question": "Will Abi have formed this sub-goal as a step to their overall goal?",
            "subgoal_page_image" : BASE_IMAGE_PATH+"ICSE2019Visa.png",
            "answers": "Yes",
            "facets_used": ["Motivations", "Attitude Towards Risk"],
            "why": "She wants to go to ICSE, so she will want to find information. She is risk averse so she wants to be sure she has info about the visa. She wants to get the whole picture and have the idea of what kind of visa to get to go to ICSE.",
            "Actions": [
                {
                    "action": "Click attending",
                    "before_action": {
                        "question": "Will ABI know what to do at this step? Why?",
                        "page_on_which_abi_take_the_action": BASE_IMAGE_PATH+"ICSE2019Visa.png",
                        "answers": [
                            "answer1: Yes; facets: Motivations; why: Only match.",
                            "answer2: Maybe; facets: None of the above; why: She would like to investigate the page first before clicking."
                        ],
                    },
                    "after_action": {
                        "question": "If Abi does the right thing, will s/he know that s/he did the right thing and is making progress toward their goal? Why?",
                        "page_on_which_abi_is_after_the_action": BASE_IMAGE_PATH+"ICSE2019Visa.png",
                        "answers": [
                            "answer1: Yes; facets: Motivations; why: She is going to read the whole list. (mot) She is looking for Visa...and she sees visa."
                        ],
                    }
                },
                {
                    "action": "Click on Visa",
                    "before_action": {
                        "question": "Will ABI know what to do at this step? Why?",
                        "page_on_which_abi_take_the_action": BASE_IMAGE_PATH+"ICSE2019Visa.png",
                        "answers": [
                            "answer1: Yes; facets: Motivations; why: Same as facets: Motivation."
                        ],
                    },
                    "after_action": {
                        "question": "If Abi does the right thing, will s/he know that s/he did the right thing and is making progress toward their goal? Why?",
                        "page_on_which_abi_is_after_the_action": BASE_IMAGE_PATH+"ICSE2019Visa.png",
                        "answers": [
                            "answer1: Yes; facets: Motivations; why: She is seeing all the breadcrumbs to know that she is making progress."
                        ],
                    }
                }
            ]
        }
    ]
}
