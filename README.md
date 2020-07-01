# superboum/rpm

[![Copr build status](https://copr.fedorainfracloud.org/coprs/superboum/chez-scheme/package/chez-scheme/status_image/last_build.png)](https://copr.fedorainfracloud.org/coprs/superboum/chez-scheme/package/chez-scheme/)

## Build a RPM

To execute the same script that will be executed by `copr`, it is recommended you build the RPM like that:

```
cd ./<project>
make -f ../.copr/Makefile rpm spec=chez-scheme.spec outdir=../out
```

Then, you will find your RPM file in the `out/` folder in the root directory of the project.

## Contributions

Feel free to propose contributions and evolutions to this copr package.
