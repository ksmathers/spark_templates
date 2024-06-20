from sparkle import SparkleRuntime, Vfs
import myproject
import os


rt = SparkleRuntime()
vfs = Vfs(rt, {
    "/myproject/data": "./data"
    })
rt.start("sparkle")
for tf in myproject.TRANSFORMS:
    rt.add_transform(tf)
rt.submit()