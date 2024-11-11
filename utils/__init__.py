import pandas as pd


def clean_channels_by_imp(recording, imps, imp_thr=5e6):
    return recording.remove_channels([i for i in recording.channel_ids if imps[i] > imp_thr])

