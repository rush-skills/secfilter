def check_attack(request):
    attack = None
    if request["request_header_user_agent"] == "curl/7.43.0":
        attack = "User-Agent: curl"
    if len(request["request_url_query"]) > 0:
        attack = "Unexpected Format String"
    if len(request["request_header_referer"]) > 1:
        attack = "Unexpected Referer"
    return attack
