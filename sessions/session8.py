"""
Source: GM_Forms_Session#7.pdf

"""
from constant import BASE_IMAGE_PATH

gm_session7 = {
    "scenario": "Abi is going to register for ICSE and MSR",
    "persona" : "ABI",
    "Subgoals": [
        {
            "subgoal": "From home page, wants to go to registration forms page",
            "question": "Will Abi have formed this sub-goal as a step to their overall goal?",
            "subgoal_page_image" : BASE_IMAGE_PATH+"ICSE2019Registration.png",
            "answers": "Yes",
            "facets_used": ["Motivations"],
            "why": "Agrees with the No’s recorded, but on the plus side, has already decided to register, so wants to move ahead with it. She wants to read the info about how much it all costs.",
            "Actions": [
                {
                    "action": "Read the fees",
                    "before_action": {
                        "question": "Will ABI know what to do at this step? Why?",
                        "page_on_which_abi_take_the_action": BASE_IMAGE_PATH+"ICSE2019Fees.png",
                        "answers": [
                            "answer1: Yes; facets: Motivations; why: Also has a limited amount of startup $."
                        ],
                    },
                    "after_action": {
                        "question": "If Abi does the right thing, will s/he know that s/he did the right thing and is making progress toward their goal? Why?",
                        "page_on_which_abi_is_after_the_action": BASE_IMAGE_PATH+"ICSE2019Fees.png",
                        "answers": [
                            "answer1: Yes; facets: Motivations; why: Yes, making progress, but wondering exactly when her paper is being presented, because that would be cheaper..."
                        ],
                    }
                },
                {
                    "action": "Click on registration",
                    "before_action": {
                        "question": "Will ABI know what to do at this step? Why?",
                        "page_on_which_abi_take_the_action": BASE_IMAGE_PATH+"ICSE2019Registration.png",
                        "answers": [
                            "answer1: Yes; facets: Motivations; why: It’s obviously the way to proceed she sees the link on top."
                        ],
                    },
                    "after_action": {
                        "question": "If Abi does the right thing, will s/he know that s/he did the right thing and is making progress toward their goal? Why?",
                        "page_on_which_abi_is_after_the_action": BASE_IMAGE_PATH+"ICSE2019Registration.png",
                        "answers": [
                            "answer1: Yes; facets: Motivations; why: Abi will finally do see button if she scrolls all the way to bottom.",
                            "answer2: No; facets: None of the above; why: Abi says -- I don’t feel like I’m making progress -- where’s the form? Not clear that there’s a button at the bottom, so she may not scroll all the way to the bottom. The register now button is greyed out, she’s not sure she can register using that. Seems there is only a summary info."
                        ],
                    }
                }
            ]
        }
    ]
}
