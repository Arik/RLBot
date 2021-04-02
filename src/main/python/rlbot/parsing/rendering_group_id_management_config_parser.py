import itertools

from rlbot.parsing.custom_config import ConfigObject

RENDERING_GROUP_ID_MANAGEMENT_CONFIGURATION_HEADER = "Rendering Group ID Management"
WHITELIST_GROUP_ID_KEY = "whitelist_id"
BLACKLIST_GROUP_ID_KEY = "blacklist_id"


def add_scripts_header(config_object):
    participant_header = config_object.add_header_name(RENDERING_GROUP_ID_MANAGEMENT_CONFIGURATION_HEADER,
                                                       is_indexed=True)
    participant_header.add_value(WHITELIST_GROUP_ID_KEY, str, default=None,
                                 description="""The rendering group id to be whitelisted.
                                                If none are provided, the whitelist is disabled.""")
    participant_header.add_value(BLACKLIST_GROUP_ID_KEY, str, default=None,
                                 description="The rendering group id to be blacklisted.")


def get_rendering_whitelist(match_config: ConfigObject):
    rendering_whitelist = []
    for i in itertools.count():
        group_id = match_config.get(RENDERING_GROUP_ID_MANAGEMENT_CONFIGURATION_HEADER, WHITELIST_GROUP_ID_KEY, i)
        if group_id is None or group_id == 'None':
            break
        rendering_whitelist.append(group_id)
    return rendering_whitelist


def get_rendering_blacklist(match_config: ConfigObject):
    rendering_blacklist = []
    for i in itertools.count():
        group_id = match_config.get(RENDERING_GROUP_ID_MANAGEMENT_CONFIGURATION_HEADER, BLACKLIST_GROUP_ID_KEY, i)
        if group_id is None or group_id == 'None':
            break
        rendering_blacklist.append(group_id)
    return rendering_blacklist
