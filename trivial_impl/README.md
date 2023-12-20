***src/***: Src files for the lab.</br>
***util/***: Util files to implement. **TODO**</br>
***requirements.txt*** Enviroment requirements.</br>
***main.py***: Python file to conduct the search algorthim.</br>
***run.sh***: Bash script for judging. **DO NOT DELETE THIS FILE.**</br>
***zip.sh***: Wrap up `.py` `.txt` and `.sh` files under `trivial_impl/` and copy `submission.zip` to target dir.</br>
***three.sl***:  A test benchmark to guarantee the correctness.</br>

**Simple Hand-in Instructions:**
1. Test three.sl: `python3 main.py three.sl`
2. Generate zip file: `bash zip.sh` After this step you will see submission.zip under `/judge/user/submission`
3. Build the image and run (Under judge dir): `bash init.sh` `bash run.sh`