from typing import List, Dict

from wd14_tagger_api.tagger.interrogator import Interrogator, WaifuDiffusionInterrogator, MLDanbooruInterrogator

interrogators: Dict[str, Interrogator] = {
    'wd-ViT-Large-v3': WaifuDiffusionInterrogator(
        'WD ViT-Large-v3',
		repo_id='SmilingWolf/wd-vit-large-tagger-v3',
    ),
    'wd-EVA02-Large-v3': WaifuDiffusionInterrogator(
        'wd-EVA02-Large-v3',
		repo_id='SmilingWolf/wd-eva02-large-tagger-v3',
    ),
    'wd14-vit.v1': WaifuDiffusionInterrogator(
        'WD14 ViT v1',
        repo_id='SmilingWolf/wd-v1-4-vit-tagger'
    ),
    'wd14-vit.v2': WaifuDiffusionInterrogator(
        'WD14 ViT v2',
        repo_id='SmilingWolf/wd-v1-4-vit-tagger-v2',
    ),
    'wd14-convnext.v1': WaifuDiffusionInterrogator(
        'WD14 ConvNeXT v1',
        repo_id='SmilingWolf/wd-v1-4-convnext-tagger'
    ),
    'wd14-convnext.v2': WaifuDiffusionInterrogator(
        'WD14 ConvNeXT v2',
        repo_id='SmilingWolf/wd-v1-4-convnext-tagger-v2',
    ),
    'wd14-convnextv2.v1': WaifuDiffusionInterrogator(
        'WD14 ConvNeXTV2 v1',
        # the name is misleading, but it's v1
        repo_id='SmilingWolf/wd-v1-4-convnextv2-tagger-v2',
    ),
    'wd14-convnextv2-v2': WaifuDiffusionInterrogator(
         'wd14-convnextv2-v2',
         repo_id='SmilingWolf/wd-v1-4-convnextv2-tagger-v2',
         revision='v2.0'
    ),
    'wd14-swinv2-v1': WaifuDiffusionInterrogator(
        'WD14 SwinV2 v1',
        # again misleading name
        repo_id='SmilingWolf/wd-v1-4-swinv2-tagger-v2',
    ),
    'wd14-swinv2-v2': WaifuDiffusionInterrogator(
          'wd14-swinv2-v2',
          repo_id='SmilingWolf/wd-v1-4-swinv2-tagger-v2',
          revision='v2.0'
    ),
    'wd-v1-4-moat-tagger.v2': WaifuDiffusionInterrogator(
        'WD14 moat tagger v2',
        repo_id='SmilingWolf/wd-v1-4-moat-tagger-v2'
    ),
    'mld-caformer.dec-5-97527': MLDanbooruInterrogator(
        'ML-Danbooru Caformer dec-5-97527',
        repo_id='deepghs/ml-danbooru-onnx',
        model_path='ml_caformer_m36_dec-5-97527.onnx'
    ),
    'mld-tresnetd.6-30000': MLDanbooruInterrogator(
        'ML-Danbooru TResNet-D 6-30000',
        repo_id='deepghs/ml-danbooru-onnx',
        model_path='TResnet-D-FLq_ema_6-30000.onnx'
    ),
}
