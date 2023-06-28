
```
cd /workspace/vaip
cp -av /workspace/onnxruntime/.lintrunner.toml  .
sed -i 's:origin/main:origin/dev:g' .lintrunner.toml
cp -av /workspace/onnxruntime/requirements-lintrunner.txt .
# ls -la /workspace/onnxruntime/ | grep lint

lintrunner init
lintrunner
view -nw .lintrunner.toml
vi /workspace/vaip/.lintrc
```
