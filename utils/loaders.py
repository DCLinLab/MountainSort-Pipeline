from spikeinterface import concatenate_recordings
from tqdm import tqdm
from pathlib import Path
import spikeinterface.extractors as se


def rhd_load(folder, range: tuple[int, int] = None,  stream_name='RHD2000 amplifier channel'):
    files = sorted(Path(folder).glob('*.rhd'))
    assert len(files) > 0, "No intan RHD2000 recording found in this directory."
    if range is not None:
        files = files[range[0]:range[1]]
    files = [se.read_intan(i, stream_name=stream_name, use_names_as_ids=True)
             for i in tqdm(files, 'Loading RHD2000 files')]
    return concatenate_recordings(files)


def load_intan_impedance(path, column='Impedance Magnitude at 1000 Hz (ohms)'):
    """
    sort the impedance from 0, removing some of them and let the number continue

    :param path:
    :return: a dict mapping channel id to impedance value
    """
    imped_tab = pd.read_csv(path).sort_values(by='Channel Number', ascending=True)
    # j = 0
    # out = {}
    # for ind, row in imped_tab.iterrows():
    #     if row['Channel Number'] in to_omit:
    #         continue
    #     out[str(j)] = row[column]
    #     j += 1
    return dict(zip(imped_tab['Channel Number'], imped_tab[column]))