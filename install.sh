#!/bin/bash
sudo apt-get install python-pip curl jq
sudo pip install unicodecsv
sudo chmod +x json2rdt
cd $HOME/MD380-Codeplug-Maker/c
make
cp $HOME/MD380-Codeplug-Maker/c/out/rdt2csv $HOME/MD380-Codeplug-Maker/
rm -r $HOME/MD380-Codeplug-Maker/c/out


