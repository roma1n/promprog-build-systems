import os
import matplotlib.pyplot as plt
import numpy as np

template = '''
#include <opencv2/core/core.hpp>
#include <opencv2/highgui/highgui.hpp>
#include <iostream>
#include <vector>

using namespace cv;
using namespace std;


typedef Vec<unsigned char, 3> VT;

const vector<int> map = {{ {} }};


void map_colors(Mat& image) {{
    for (auto pix = image.begin<VT>(); pix < image.end<VT>(); ++pix) {{
        for (int c = 0; c < 3; ++c) {{
            pix[0][c] = map[256 * c + pix[0][c]];
        }}
    }}
}}


int main( int argc, char** argv ) {{
    if( argc != 3) {{
     cout <<" Usage: bin_name ImageToTransform TransformedImage" << endl;
     return -1;
    }}

    Mat image;
    image = imread(argv[1], IMREAD_COLOR);

    if(!image.data) {{
        cout << "Could not open or find the image" << std::endl ;
        return -1;
    }}

    map_colors(image);

    imwrite(argv[2], image);

    return 0;
}}

'''


m = (255 * plt.imread(os.path.join(os.path.split(os.path.abspath(__file__))[0], 'map.png'))).astype(int)
m = np.concatenate([m[c,:,c] for c in range(3)])
s = ', '.join([str(x) for x in m])

with open(
    os.path.join(os.path.split(os.path.abspath(__file__))[0], 'code_gen.cpp'),
    'w'
) as f:
    f.write(template.format(s))

