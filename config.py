import argparse
from pathlib import Path

parser = argparse.ArgumentParser(
    description='Training Binary Classifiers on AVA dataset for Edge computing/mobile device deployment')


parser.add_argument('--batch_size', default=None,
                    type=bool, help='batch_size')
parser.add_argument('--timm_model', default='mobile_vit_xxs',
                    type=str, help='modle_selected_from_timm_repository')
parser.add_argument('--n_workers', default='cpu', type=str, help='inference ')
parser.add_argument('--pin_memory', default=True, type=bool,
                    help='Handling of device memory pin == faster')
parser.add_argument('--inference', action='store_true',
                    help='set computer brain state to infer or to train')
parser.add_argument('--device', default='cpu', type=str,
                    help='chose your device flavour this could ')
parser.add_argument('--model_location', default='models/mobilevit_xxs', type=str,
                    help='location relative to project directory where model is stored')
parser.add_argument('--download_from', default='', type=str,
                    help='location relative to project directory where model is stored')
parser.add_argument('--dataset', default=True, type=bool,
                    help='to get dataset or not to get dataset')
parser.add_argument('--download', default=False,
                    help='whether or not to download data for trining or for inference')
parser.add_argument('--plot', action='store_true',
                    help='whether or not to download data for trining or for inference')
parser.add_argument('--entity', type=str, default=None,
                    help='wandb entity (userename or team)')
parser.add_argument('--project', type=str, default=None,
                    help='project where runs saved')
parser.add_argument('--tags', type=str, default=None,
                    help='run tags')
parser.add_argument('--unzip_only', action='store_true',
                    help='unzip_file')

parser.add_argument('-d', type=Path, default='wandb/wandb/settings')
args = parser.parse_args()
print(args.d)
