# vseocr

Extract hardcoded (burned-in) text from videos using the [PaddleOCR](https://github.com/PaddlePaddle/PaddleOCR) OCR engine with Python. A Colab notebook for installing and running this library is included for convenience:
[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/19a358FVODg0bE6A8v_pTM3MfnHaE3Igi#scrollTo=4d7i0torucRL)

```python
# example.py

from vseocr import save_subtitles_to_file

if __name__ == '__main__':
    save_subtitles_to_file('C7ez-29RMxU.mp4', 'example.srt', lang='en',
     sim_threshold=80, conf_threshold=75, use_fullframe=True,
     brightness_threshold=210, similar_image_threshold=1000, frames_to_skip=1)
```

`$ python3 example.py`

example.srt:

``` 
0
00:00:00,000 --> 00:00:02,066
the biggest mistake people
make when visiting Rome

1
00:00:02,133 --> 00:00:03,666
is not planning out an
efficient route

2
00:00:03,733 --> 00:00:05,466
so here's how to spend the
perfect day in Rome.

3
00:00:05,533 --> 00:00:08,000
hey! I'm Amanda & I share
my tips to help you travel.
smarter

4
00:00:08,066 --> 00:00:08,333
Rome is an incredibly
walkable city
```

## Install prerequisites
Python 3.7 - 3.10

paddlepaddle or paddlepaddle-gpu See https://www.paddlepaddle.org.cn/install/quick?docurl=/documentation/docs/en/install/pip/linux-pip_en.html

## Installation

`pip install git+https://github.com/diluwara/video_subtitle_extractor_OCR-`

Alternatively for development:
1. Clone this repo
2. From the root directory of this repository run `python -m pip install .`

## Performance

The OCR process can be very slow on CPU. Running with `paddlepaddle-gpu` is recommended if you have a CUDA 9 or CUDA 10 GPU.

## Tips

To shorten the amount of time it takes to perform OCR on each frame, you can use the `crop_x`, `crop_y`, `crop_width`, `crop_height` params to crop out only the areas of the videos where the subtitles appear. When cropping, leave a bit of buffer space above and below the text to ensure accurate readings.

### Quick Configuration Cheatsheet

|| More Speed | More Accuracy | Notes
-|------------|---------------|--------
Input Video Quality       | Use lower quality           | Use higher quality  | Performance impact of using higher resolution video can be reduced with cropping
`frames_to_skip`          | Higher number               | Lower number        |
`brightness_threshold`    | Higher threshold            | N/A                 | A brightness threshold can help speed up the OCR process by filtering out dark frames. In certain circumstances such as when subtitles are white and against a bright background, it may also help with accuracy.


## API

1. Return subtitle string in SRT format
    ```python
    get_subtitles(
        video_path: str, lang='en', time_start='0:00', time_end='',
        conf_threshold=75, sim_threshold=80, use_fullframe=False,
        det_model_dir=None, rec_model_dir=None, use_gpu=False,
        brightness_threshold=None, similar_image_threshold=100, similar_pixel_threshold=25, frames_to_skip=1,
        crop_x=None, crop_y=None, crop_width=None, crop_height=None)
    ```

2. Write subtitles to `file_path`
    ```python
    save_subtitles_to_file(
        video_path: str, file_path='subtitle.srt', lang='en', time_start='0:00', time_end='', 
        conf_threshold=75, sim_threshold=80, use_fullframe=False,
        det_model_dir=None, rec_model_dir=None, use_gpu=False,
        brightness_threshold=None, similar_image_threshold=100, similar_pixel_threshold=25, frames_to_skip=1,
        crop_x=None, crop_y=None, crop_width=None, crop_height=None)
    ```

### Parameters

- `lang`

  The language of the subtitles. See [PaddleOCR docs](https://github.com/PaddlePaddle/PaddleOCR/blob/release/2.6/doc/doc_en/multi_languages_en.md#5-support-languages-and-abbreviations) for list of supported languages and their abbreviations

- `conf_threshold`

  Confidence threshold for word predictions. Words with lower confidence than this value will be discarded. The default value `75` is fine for most cases. 

  Make it closer to 0 if you get too few words in each line, or make it closer to 100 if there are too many excess words in each line.

- `sim_threshold`

  Similarity threshold for subtitle lines. Subtitle lines with larger [Levenshtein](https://en.wikipedia.org/wiki/Levenshtein_distance) ratios than this threshold will be merged together. The default value `80` is fine for most cases.

  Make it closer to 0 if you get too many duplicated subtitle lines, or make it closer to 100 if you get too few subtitle lines.

- `time_start` and `time_end`

  Extract subtitles from only a clip of the video. The subtitle timestamps are still calculated according to the full video length.

- `use_fullframe`

  By default, the specified cropped area is used for OCR or if a crop is not specified, then the bottom third of the frame will be used. By setting this value to `True` the entire frame will be used.

- `crop_x`, `crop_y`, `crop_width`, `crop_height`

  Specifies the bounding area in pixels for the portion of the frame that will be used for OCR.

- `det_model_dir`

  the text detection inference model folder. There are two ways to transfer parameters, 1. None: Automatically download the built-in model to ~/.paddleocr/det; 2. The path of a specific inference model, the model and params files must be included in the model path.
  
  See PaddleOCR repo for list of prebuilt models: https://github.com/PaddlePaddle/PaddleOCR/.

- `rec_model_dir`
  
  the text recognition inference model folder. There are two ways to transfer parameters, 1. None: Automatically download the built-in model to ~/.paddleocr/rec; 2. The path of a specific inference model, the model and params files must be included in the model path.
  
  See PaddleOCR repo for list of prebuilt models: https://github.com/PaddlePaddle/PaddleOCR/.

- `use_gpu`

  Set to `True` if performing ocr with gpu (requires the `paddlepaddle-gpu` python package to be installed)

- `brightness_threshold`
  
  If set, pixels whose brightness are less than the threshold will be blackened out. Valid brightness values range from 0 (black) to 255 (white). This can help improve accuracy when performing OCR on videos with white subtitles.

- `similar_image_threshold`

  The number of non-similar pixels there can be before the program considers 2 consecutive frames to be different. If a frame is not different from the previous frame, then the OCR result from the previous frame will be used (which can save a lot of time depending on how fast each OCR inference takes).

- `similar_pixel_threshold`

  Brightness threshold from 0-255 used with the `similar_image_threshold` to determine if 2 consecutive frames are different. If the difference between 2 pixels exceeds the threshold, then they will be considered non-similar.

- `frames_to_skip`

  The number of frames to skip before sampling a frame for OCR. Keep in mind the fps of the input video before increasing.

## TODO
- [ ] parallel processing
- [ ] handle multiple lines of text in the same frame
- [ ] publish to pypi
- [ ] commandline interface
- [ ] user-friendly application for non-devs
