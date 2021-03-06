from bedlam_slack import app, slack_helper
from flask import jsonify
from random import choice

# returns a randomly generated Shakespeare insult.
@app.route("/slash/shakespeare", methods=['POST'])
def shakespeare():
    if not slack_helper.validate_request():
        abort(403)
     
    response = {
        "response_type": "in_channel",
        "text": "You are a" + " " + choice(group1) + " " + choice(group2) + " " + choice(group3)
        }
        
    return jsonify(response)

group1 = ["artless",
    "bawdy",
    "beslubbering",
    "bootless",
    "churlish",
    "cockered",
    "clouted",
    "craven",
    "currish",
    "dankish",
    "dissembling",
    "droning",
    "errant",
    "fawning",
    "fobbing",
    "froward",
    "frothy",
    "gleeking",
    "goatish",
    "gorbellied",
    "impertinent",
    "infectious",
    "jarring",
    "loggerheaded",
    "lumpish",
    "mammering",
    "mangled",
    "mewling",
    "paunchy",
    "pribbling",
    "puking",
    "puny",
    "qualling",
    "rank",
    "reeky",
    "roguish",
    "ruttish",
    "saucy",
    "spleeny",
    "spongy",
    "surly",
    "tottering",
    "unmuzzled",
    "vain",
    "venomed",
    "villainous",
    "warped",
    "wayward",
    "weedy",
    "yeasty"]

group2 = ["dread-bolted",
    "earth-vexing",
    "elf-skinned",
    "fat-kidneyed",
    "fen-sucked",
    "flap-mouthed",
    "fly-bitten",
    "folly-fallen",
    "fool-born",
    "full-gorged",
    "guts-griping",
    "half-faced",
    "hasty-witted",
    "hedge-born",
    "hell-hated",
    "idle-headed",
    "ill-breeding",
    "ill-nurtured",
    "knotty-pated",
    "milk-livered",
    "motley-minded",
    "onion-eyed",
    "plume-plucked",
    "pottle-deep",
    "pox-marked",
    "reeling-ripe",
    "rough-hewn",
    "rude-growing",
    "rump-fed",
    "shard-borne",
    "sheep-biting",
    "spur-galled",
    "swag-bellied",
    "tardy-gaited",
    "tickle-brained",
    "toad-spotted",
    "unchin-snouted",
    "weather-bitten"]

group3 = [
    "death-token",
    "dewberry",
    "flap-dragon",
    "flax-wench",
    "flirt-gill",
    "foot-licker",
    "fustilarian",
    "giglet",
    "gudgeon",
    "haggard",
    "harpy",
    "hedge-pig",
    "horn-beast",
    "hugger-mugger",
    "joithead",
    "lewdster",
    "lout",
    "maggot-pie",
    "malt-worm",
    "mammet",
    "measle",
    "minnow",
    "miscreant",
    "moldwarp",
    "mumble-news",
    "nut-hook",
    "pigeon-egg",
    "pignut",
    "puttock",
    "pumpion",
    "ratsbane",
    "scut",
    "skainsmate",
    "strumpet",
    "varlot",
    "vassal",
    "whey-face",
    "wagtail"]