find ../pix2pix-tensorflow/photos_combined/* -type f -name "*.png" -exec bash -c 'mv "$0" "${0// /_}"' {} \;