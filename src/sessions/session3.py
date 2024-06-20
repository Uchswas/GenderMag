"""
Source: GM_Forms_Session#4.pdf

"""
from constant import BASE_IMAGE_PATH

gm_session3 = {
    "scenario": "Abi decided to attend ICSE 2019 and is making travel arrangements (not doing the third-party registration sequence) - she is the second author on a paper that got accepted, so she doesn't have to go, but she has decided to go.",
    "persona" : "ABI",
    "Subgoals": [
        {
            "subgoal": "Abby wants to know where people are staying",
            "question": "Will Abi have formed this sub-goal as a step to their overall goal?",
            "subgoal_page_image" : BASE_IMAGE_PATH+"ICSE2019Home.png",
            "answers": "Yes/ Maybe",
            "facets_used": ["Yes: Attitude Towards Risk", "Maybe: Attitude Towards Risk"],
            "why": "She attending and doesnt want to stay by herself (want to be where others are); KNow more about the conference venue before hotel. Look at cost of attending",
            "Actions": [
                {
                    "action": "Click on attending",
                    "before_action": {
                        "question": "Will ABI know what to do at this step? Why?",
                        "page_image_on_which_abi_take_the_action": BASE_IMAGE_PATH+"ICSE2019Home.png",
                        "answers": [
                            "answer1: Yes; facets: Motivation, Information Processing Style; why: Abby has been on other pages, so she is familiar with similar conference pages.",
                            "answer2: Maybe; facets: Information Processing Style, Attitude towards risk, Learning Style; why: Attending label: Promising, but she might scroll down to see what else is available, since she is a comprehensive information processor. She may not want to click on a link, in case it takes her more time and leads her to a wrong path. The attending label does not mention hotel, which is what she is motivated to find.",
                            "answer3: Information Processing Style; facets: None of the above; why: She will look at the program to know what she is getting into and determine how many days to stay."
                        ],
                    },
                    "after_action": {
                        "question": "If Abi does the right thing, will s/he know that s/he did the right thing and is making progress toward their goal? Why?",
                        "page_image_on_which_abi_is_after_the_action": BASE_IMAGE_PATH+"ICSE2019Timeline.png",
                        "answers": [
                            "answer1: Yes; facets: None of the above; why: She is making progress since there is accommodation and she is making progress towards her goal of where everyone is staying. She sees feedback on the screen which lets her know what she was looking for.",
                            "answer2: Maybe; facets: None of the above; why: She sees accommodation, so there might be hotels, but it doesn't say anything about where others are staying"
                        ],
                    }
                },
                {
                    "action": "Click on accommodation",
                    "before_action": {
                        "question": "Will ABI know what to do at this step? Why?",
                        "page_image_on_which_abi_take_the_action": BASE_IMAGE_PATH+"ICSE2019Home.png",
                        "answers": [
                            "answer1: Yes; facets: None of the above; why: Most promising thing she sees. She wants to find accommodation, so when she sees the words on the page, she knows what to do"
                        ],
                    },
                    "after_action": {
                        "question": "If Abi does the right thing, will s/he know that s/he did the right thing and is making progress toward their goal? Why?",
                        "page_image_on_which_abi_is_after_the_action": BASE_IMAGE_PATH+"ICSE2019Acco.png",
                        "answers": [
                            "answer1: Maybe; facets: None of the above; why: Jury is still out, since not seeing a lot except pictures. She has clicked on accommodation but she has not gotten more information about it--only a few images",
                            "answer2: No; facets: None of the above; why: She doesn't have any more information than before."
                        ],
                    }
                },
                {
                    "action": "Scroll",
                    "before_action": {
                        "question": "Will ABI know what to do at this step? Why?",
                        "page_image_on_which_abi_take_the_action": BASE_IMAGE_PATH+"ICSE2019Acco.png",
                        "answers": [
                            "answer1: Yes; facets: Information Processing Style; why: She is a reader, so she will always scroll to get a comprehensive idea about the page"
                        ],
                    },
                    "after_action": {
                        "question": "If Abi does the right thing, will s/he know that s/he did the right thing and is making progress toward their goal? Why?",
                        "page_image_on_which_abi_is_after_the_action": BASE_IMAGE_PATH+"ICSE2019Acco.png",
                        "answers": [
                            "answer1: Yes; facets: Motivations, Attitude Towards Risk;  why: She is making progress: it's the center of activity, she can network, and share a room, so cost won't be a problem. She found out where the conference is and got info about hotels. The site encourages people to stay together, which makes her feel better. She finally sees everything she looking for, specially stays, people, community, etc",
                        ],
                    }
                }
            ]
        },
        {
            "subgoal": "How many days to stay at the conference",
            "question": "Will Abi have formed this sub-goal as a step to their overall goal?",
            "answers": "Yes",
            "subgoal_page_image" : BASE_IMAGE_PATH+"ICSE2019Acco.png",
            "facets_used": ["Motivations", "Information Processing Style", "Attitude Towards Risk"],
            "why": "She has a task-oriented motivation style and can't proceed without knowing all the details. She reads a lot, so she will gather all the information before doing the task (e.g., booking a hotel). She doesn't want to commit to staying for the whole conference if it's not interesting.",
            "Actions": [
                {
                    "action": "Click on program",
                    "before_action": {
                        "question": "Will ABI know what to do at this step? Why?",
                        "page_image_on_which_abi_take_the_action": BASE_IMAGE_PATH+"ICSE2019Acco.png",
                        "answers": [
                            "answer1: Yes; facets: Motivations, Information Processing Style; why: She is interested in knowing more about the program.",
                            "answer2: Maybe; facets: None of this above; why: She might go for tracks, as that may also say something about the program. Since she is a comprehensive info processor, she might want to read more. "
                        ],
                    },
                    "after_action": {
                        "question": "If Abi does the right thing, will s/he know that s/he did the right thing and is making progress toward their goal? Why?",
                        "page_image_on_which_abi_is_after_the_action": BASE_IMAGE_PATH+"ICSE2019Acco.png",
                        "answers": [
                            "answer1: Yes; facets: Motivations; why: She is getting information about the program - because she sees a weak overview",
                            "answer2: Maybe; facets: Attitude Towards Risk; why: She is overwhelmed as she is not seeing the technical papers. There are no negative feelings at this point. She is getting some information and needs to read more about it. She might be looking for a detailed schedule rather than just a weekly overview because of her information processing style.."
                        ],
                    }
                },
                {
                    "action": "Click Week overview",
                    "before_action": {
                        "question": "Will ABI know what to do at this step? Why?",
                        "page_image_on_which_abi_take_the_action": BASE_IMAGE_PATH+"ICSE2019Acco.png",
                        "answers": [
                            "answer1: Yes; facets: Motivations; why: She is interested in knowing more about the program. This label is the best for what she is intending to do, and aligns with her tasks and task-oriented motivations"
                        ],
                    },
                    "after_action": {
                        "question": "If Abi does the right thing, will s/he know that s/he did the right thing and is making progress toward their goal? Why?",
                        "page_image_on_which_abi_is_after_the_action": BASE_IMAGE_PATH+"ICSE2019Week.png",
                        "answers": [
                            "answer1: Yes; facets: Motivations, Information Processing Style; why: She feels overwhelmed by the lot of information, all laid out by date, but she feels she is making progress since it says Main conference on top. She is further along than she was, but she is still unsure where to go next.",
                            "answer2: Maybe; facets: Computer self-efficacy, learning style; why: Lots of stuff is going on with different roles and acronyms that might not make sense to her. There's lots of whitespace, and different shades of gray for the main conference, but nothing stands out. She is making progress with more process-oriented learning, but she's going to get stumped, especially since she doesn't know the acronyms. All these acronyms make her worry about whether she can fit in."
                        ],
                    }
                },
                {
                    "action": "Go up the page and click on tracks",
                    "before_action": {
                        "question": "Will ABI know what to do at this step? Why?",
                        "page_image_on_which_abi_take_the_action": BASE_IMAGE_PATH+"ICSE2019Week.png",
                        "answers": [
                            "answer2: Information Processing Style, Attitude Towards Risk, Learning Style; facets: None of the above; why: Tracks are not particularly attracting her; she is more likely to focus on the program. She is uncomfortable but will stay on the program. She will be thorough and read through the next item on the program. Abby won't remember to scroll back up and click on the tracks; she might try to find items on the left side to click."
                        ],
                    }
                }
            ]
        }
    ]
}
