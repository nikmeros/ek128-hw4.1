def is_hill(seq):
    if seq[0] < seq[1] and seq[1] > seq[2]:
        return "true";
    else:
        return "false";

def is_plain(seq):
    if seq[0] == seq[1] and seq[1] == seq[2]:
        return "true";
    else:
        return "false";

def is_ramp(seq):
    if seq[0] < seq[1] and seq[1] < seq[2]:
        return "true";
    else:
        return "false";

def is_slope(seq):
    if seq[0] > seq[1] and seq[1] > seq[2]:
        return "true";
    else:
        return "false";

def is_valley(seq):
    if seq[0] > seq[1] and seq[1] < seq[2]:
        return "true";
    else:
        return "false";

def get_topology(seq):
    if seq[0] < seq[1] and seq[1] > seq[2]:
        return "hill";
    else: 
        if seq[0] == seq[1] and seq[1] == seq[2]:
            return "plain";
        else: 
            if seq[0] < seq[1] and seq[1] < seq[2]:
                return "ramp";
            else: 
                if seq[0] > seq[1] and seq[1] > seq[2]:
                    return "slope";
                else:
                    if seq[0] > seq[1] and seq[1] < seq[2]:
                        return "valley";
                    else:
                        return "none";
