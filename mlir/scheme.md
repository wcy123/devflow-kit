#

```
cd /workspace/ChezScheme; ls -l
./configure CFLAGS+='-ggdb -O0 -fPIC' --force --machine=ta6le
make re.boot
make


```


```
cd /workspace/ChezScheme; ls -l
gdb --args ta6le/bin/ta6le/scheme --help
shell echo '(display "HELLO")' > /tmp/a.scm
shell cat /tmp/a.scm
run --script /tmp/a.scm
l main
debug ta6le/bin/ta6le/scheme /tmp/a.scm
start
break S_alloc_init
b scheme.c:454
```


compile a scheme file.

```
diff --git a/makefiles/lib.zuo b/makefiles/lib.zuo
index 788bdb01..94e6b8bf 100644
--- a/makefiles/lib.zuo
+++ b/makefiles/lib.zuo
@@ -28,7 +28,7 @@
           [else
            (cons `(,(quote-syntax define) ,(car ids) (,(quote-syntax list-ref) ,vals-id ,index))
                  (loop (cdr ids) (+ index 1)))]))))
-
+
 (define (cp/ln src dest)
   (if (eq? 'windows (system-type))
       (cp* src dest)
@@ -138,7 +138,9 @@
   (define (run-scheme/status what script inputs [options (hash)])
     (call-with-scheme
      (lambda (scheme.exe scheme-args env)
-       (displayln (~a "running " scheme.exe " to build " what))
+       (define pipe-file (path-replace-extension what ".pipe"))
+       (define pipe-file-fd (fd-open-output pipe-file :truncate))
+       (displayln (~a "running " scheme.exe " with args " scheme-args "-q" inputs " to build " what " via " pipe-file))
        (define p (process scheme.exe scheme-args "-q" inputs
                           (hash 'stdin 'pipe
                                 'stdout (or (hash-ref options 'stdout #f)
@@ -147,14 +149,21 @@
                                             (fd-open-output 'stderr))
                                 'env env)))
        (define to (hash-ref p 'stdin))
-       (fd-write to (~s `(source-directories '(,(at-dir ".")
+       (define (write-to context)
+         (fd-write pipe-file-fd context)
+         (fd-write to context))
+       (write-to (~s `(source-directories '(,(at-dir ".")
+                                               ,(at-source ".")
+                                               ,@extra-source-dirs))))
+       (write-to (~s `(source-directories '(,(at-dir ".")
                                                ,(at-source ".")
                                                ,@extra-source-dirs))))
-       (fd-write to (~s `(library-directories '(,@extra-library-dirs
+       (write-to (~s `(library-directories '(,@extra-library-dirs
                                                 ,(cons (at-source ".")
                                                        (at-dir "."))))))
-       (fd-write to (string-join (map ~s script)))
+       (write-to (string-join (map ~s script)))
        (fd-close to)
+       (fd-close pipe-file-fd)
        (thread-process-wait (hash-ref p 'process))
        (process-status (hash-ref p 'process)))))
```

```
make build

echo '(pretty-file "all at once.pipe" "all.pipe")' | scheme -q
cat all.pipe

bin/zuo ta6le SCHEME=scheme
```

update ./build.zuo

```diff
+       [:target debug-s ()
+                ,(lambda (token . args)
+                   (displayln (~s "WCY args=" args))
+                   (for-each
+                    (lambda (arg)
+                      (displayln (~s "WCY target " arg " = " arg (at-dir (build-path ".." m))))
+                      (displayln (~s "WCY " vars))
+                      (define t (find-target arg (s-targets-at (make-at-dir (at-dir (build-path ".." m "s")))
+                                                               (hash-remove vars 'm))))
+                      (displayln (~s "WCY target " arg " = " t))
+                      (build t token))
+                    args))
+                :command]
+
```

```
(rm ta6le/s/compile.ta6le || true) && \
env bin/zuo ta6le debug-s ta6le/s/compile.ta6le &&  \
bin/zuo ta6le SCHEME=scheme debug-s petite.boot &&  \
bin/zuo ta6le SCHEME=scheme debug-s scheme.boot && \
echo

# we must install scheme, otherwise, fasl file is not compatible, we can not load cmacro.so etc.

make install # replace system level scheme with the newly built one.

# start to hack compile.ss

(rm ta6le/s/compile.ta6le || true) && \
env SCHEME=scheme bin/zuo ta6le debug-s ta6le/s/compile.ta6le && \
env SCHEME=scheme bin/zuo ta6le SCHEME=scheme debug-s petite.boot && \
env SCHEME=scheme bin/zuo ta6le SCHEME=scheme debug-s scheme.boot && \
echo '(compile-file "/home_chunywan/scripts/hello.ss")' | \
  ta6le/bin/ta6le/scheme  -q
```


code gen

EDC

`code_generate(Expr e, Func<Op(Value *)> K) -> Op`

init:

```
K_init: (Value * v) {
   return v
}
```

Constant V:

```
Op:

V = Expr_to_Value(e)
return K(v)
```

Symbol: param N, closure M

```
V = load func %closure m
V = load func %param n
return K(v)
```


Lambda: c0, c1, c2,...,cn, Body

```
closure_block = allocate(N+1)
i = 0
for i = 0 .. N:
    code_generate(v[i], K(v) = {
        store closure_block, v
    })

code_generate(Body, K(body) = {  // body is a Value, Func, named or unnamed.
    store closure_block, body
})
code_generate(c0, K= (v0) {
    store closure_block, i , v0
    i = i + 1;
    return code_generate (c)
}

CustomOp Closure Func, Varidic Values
```

Apply: (e1, e2, e3, ...)

```

```
