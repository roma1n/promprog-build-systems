#include <opencv2/core/core.hpp>
#include <opencv2/highgui/highgui.hpp>
#include <iostream>

using namespace cv;
using namespace std;


typedef Vec<unsigned char, 3> VT;


void map_colors(Mat& image, Mat& map) {
    for (auto pix = image.begin<VT>(); pix < image.end<VT>(); ++pix) {
        for (int c = 0; c < 3; ++c) {
            pix[0][c] = map.at<VT>(2 - c, pix[0][c])[c];
        }
    }
}


int main( int argc, char** argv )
{
    if( argc != 4)
    {
     cout <<" Usage: bin_name ImageToTransform Map TransformedImage" << endl;
     return -1;
    }

    Mat image;
    image = imread(argv[1], IMREAD_COLOR); // Read the file

    Mat map;
    map = imread(argv[2], IMREAD_COLOR); // Read the map

    if(!image.data) // Check for invalid input
    {
        cout << "Could not open or find the image" << std::endl ;
        return -1;
    }

    if(!map.data) // Check for invalid input
    {
        cout << "Could not open or find the map" << std::endl ;
        return -1;
    }

    map_colors(image, map);

    imwrite(argv[3], image);

    return 0;
}
