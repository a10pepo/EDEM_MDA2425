# EDEM MDA Spark Scala

This repository contains the code in order to be able to do the class exercises also in Scala.

## How to install

- install [Docker](https://docker.com)
- either clone the repo or download as zip
- open with IntelliJ as an SBT project
- the datasets are available in https://github.com/paponsro/spark_edem_2324/tree/master/dataset


### A Note For Windows users: Adding Winutils

By default, Spark will be unable to write files using the local Spark executor. To write files, you will need to install the Windows Hadoop binaries, aka [winutils](https://github.com/cdarlint/winutils). You can take the latest binary (Hadoop 3.2 as of June 2022), or use Hadoop 2.7 as a fallback.

After you download winutils.exe, create a directory anywhere (e.g. `C:\\winutils`), then create a `bin` directory under that, then place the winutils executable there.

You will also need to set the `HADOOP_HOME` environment variable to your directory where you added `bin\winutils.exe`. In the example above, that would be `C:\\winutils`.

An alternative to setting the environment variable is to add this line at the beginning of every Spark application we write:

```scala
System.setProperty("hadoop.home.dir","C:\\hadoop") // replace C:\\hadoop with your actual directory
```