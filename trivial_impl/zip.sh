BASE_DIR=$(dirname $(realpath $0))
ROOT_DIR=$(dirname $BASE_DIR)
SUBMISSION_DIR=$ROOT_DIR/judge/user/submission

rm -rf $SUBMISSION_DIR/submission.zip
rm -rf $SUBMISSION_DIR/result.json

files=()
# 将 find 命令的结果添加到数组中
while IFS= read -r -d $'\0' file; do
    relative_path=$(realpath --relative-to=$BASE_DIR "$file")
    files+=("$relative_path")
done < <(find $BASE_DIR -type f \( -name "*.py" -o -name "*.sh" -o -name "*.txt" \) -print0)

printf 'zipping: %s\n' "${files[@]}"

zip $SUBMISSION_DIR/submission.zip "${files[@]}"