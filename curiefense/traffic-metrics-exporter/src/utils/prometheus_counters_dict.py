from enum import Enum


class CounterTypes(Enum):
    REGULAR = 1
    # counter additionally labeled by "key"
    COUNTER_BY_KEY = 2


REGULAR = CounterTypes.REGULAR
COUNTER_BY_KEY = CounterTypes.COUNTER_BY_KEY


# mapping of counters to REGULAR, SESSION and PROCESSING_TIME. the two other ones are recognized by regex
counters_format = {
    "hits": {"type": REGULAR},
    "blocks": {"type": REGULAR},
    "report": {"type": REGULAR},
    "human": {"type": REGULAR},
    "bot": {"type": REGULAR},
    "challenge": {"type": REGULAR},
    "active": {"type": REGULAR},
    "reported": {"type": REGULAR},
    "total_downstream_bytes": {"type": REGULAR},
    "total_upstream_bytes": {"type": REGULAR},
    "unique_blocked_ip": {"type": REGULAR},
    "unique_blocked_uri": {"type": REGULAR},
    "unique_blocked_user_agent": {"type": REGULAR},
    "unique_passed_user_agent": {"type": REGULAR},
    "unique_asn": {"type": REGULAR},
    "unique_blocked_asn": {"type": REGULAR},
    "unique_passed_asn": {"type": REGULAR},
    "unique_passed_ip": {"type": REGULAR},
    "unique_passed_uri": {"type": REGULAR},
    "unique_ip": {"type": REGULAR},
    "unique_uri": {"type": REGULAR},
    "unique_user_agent": {"type": REGULAR},
    "unique_country": {"type": REGULAR},
    "unique_blocked_country": {"type": REGULAR},
    "unique_passed_country": {"type": REGULAR},
    "max_process_time": {"type": REGULAR},
    "min_process_time": {"type": REGULAR},
    "avg_process_time": {"type": REGULAR},
    "requests_triggered_acl_active": {"type": REGULAR},
    "requests_triggered_acl_report": {"type": REGULAR},
    "requests_triggered_cf_active": {"type": REGULAR},
    "requests_triggered_cf_report": {"type": REGULAR},
    "requests_triggered_globalfilter_active": {"type": REGULAR},
    "requests_triggered_globalfilter_report": {"type": REGULAR},
    "requests_triggered_ratelimit_active": {"type": REGULAR},
    "requests_triggered_ratelimit_report": {"type": REGULAR},
    "risk_level_active": {"type": COUNTER_BY_KEY, "label": "level"},
    "risk_level_report": {"type": COUNTER_BY_KEY, "label": "level"},
    "top_aclid_active": {"type": COUNTER_BY_KEY, "label": "aclid"},
    "top_aclid_passed": {"type": COUNTER_BY_KEY, "label": "aclid"},
    "top_aclid_reported": {"type": COUNTER_BY_KEY, "label": "aclid"},
    "top_active_country": {"type": COUNTER_BY_KEY, "label": "country"},
    "top_passed_country": {"type": COUNTER_BY_KEY, "label": "country"},
    "top_reported_country": {"type": COUNTER_BY_KEY, "label": "country"},
    "top_active_asn": {"type": COUNTER_BY_KEY, "label": "asn"},
    "top_passed_asn": {"type": COUNTER_BY_KEY, "label": "asn"},
    "top_reported_asn": {"type": COUNTER_BY_KEY, "label": "asn"},
    "top_ruleid_active": {"type": COUNTER_BY_KEY, "label": "ruleid"},
    "top_ruleid_passed": {"type": COUNTER_BY_KEY, "label": "ruleid"},
    "top_ruleid_reported": {"type": COUNTER_BY_KEY, "label": "ruleid"},
    "top_secpolentryid_active": {"type": COUNTER_BY_KEY, "label": "secpolentryid"},
    "top_secpolentryid_passed": {"type": COUNTER_BY_KEY, "label": "secpolentryid"},
    "top_secpolentryid_reported": {"type": COUNTER_BY_KEY, "label": "secpolentryid"},
    "top_secpolid_active": {"type": COUNTER_BY_KEY, "label": "secpolid"},
    "top_secpolid_passed": {"type": COUNTER_BY_KEY, "label": "secpolid"},
    "top_secpolid_reported": {"type": COUNTER_BY_KEY, "label": "secpolid"},
    "top_tags_active": {"type": COUNTER_BY_KEY, "label": "tag"},
    "top_tags_passed": {"type": COUNTER_BY_KEY, "label": "tag"},
    "top_tags_reported": {"type": COUNTER_BY_KEY, "label": "tag"},
    "methods": {"type": COUNTER_BY_KEY, "label": "method"},
    "status": {"type": COUNTER_BY_KEY, "label": "code"},
    "status_classes": {"type": COUNTER_BY_KEY, "label": "code_class"},
    # TODO: special case
    # "section_active":{"args":0,"attrs":0,"body":0,"headers":0,"uri":0}
    # "section_active": {"type": COUNTER_BY_KEY, "label": "section"},
    # "section_passed": {"type": COUNTER_BY_KEY, "label": "section"},
    # "section_reported": {"type": COUNTER_BY_KEY, "label": "section"},
}

# TODO there are no those keys anymore, delete or rebuild to an actual ones
# counters
name_changes = {"d_bytes": "total_downstream_bytes", "u_bytes": "total_upstream_bytes"}

# validating format validity, in case new keys will be entered
for counter, value in counters_format.items():
    if value["type"] not in [REGULAR, COUNTER_BY_KEY]:
        raise TypeError(f"{counter} is not of a legal type in counters_format")
