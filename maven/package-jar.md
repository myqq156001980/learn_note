    <?xml version="1.0" encoding="UTF-8"?>
    <project xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
             xmlns="http://maven.apache.org/POM/4.0.0"
             xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 http://maven.apache.org/xsd/maven-4.0.0.xsd">
        <modelVersion>4.0.0</modelVersion>

        <groupId>dcg</groupId>
        <artifactId>flume-httpsink</artifactId>
        <version>1.0-SNAPSHOT</version>
        <packaging>jar</packaging>


        <properties>
            <project.build.sourceEncoding>UTF-8</project.build.sourceEncoding>
            <exec.mainClass>Receiver</exec.mainClass>
        </properties>

        <parent>
            <groupId>org.springframework.boot</groupId>
            <artifactId>spring-boot-starter-parent</artifactId>
            <version>1.5.8.RELEASE</version>
        </parent>
        <dependencies>
            <dependency>
                <groupId>org.springframework.boot</groupId>
                <artifactId>spring-boot-starter-web</artifactId>
            </dependency>

            <!-- https://mvnrepository.com/artifact/javax.servlet/javax.servlet-api -->
            <dependency>
                <groupId>javax.servlet</groupId>
                <artifactId>javax.servlet-api</artifactId>
                <version>4.0.0</version>
                <scope>provided</scope>
            </dependency>


        </dependencies>


        <build>

            <finalName>${project.artifactId}</finalName>
            <plugins>
                <plugin>
                    <groupId>org.apache.maven.plugins</groupId>
                    <artifactId>maven-compiler-plugin</artifactId>
                    <version>3.2</version>
                    <configuration>
                        <source>1.8</source>
                        <target>1.8</target>
                        <encoding>UTF-8</encoding>
                    </configuration>
                </plugin>


                <plugin>
                    <groupId>org.springframework.boot</groupId>
                    <artifactId>spring-boot-maven-plugin</artifactId>
                </plugin>

                <plugin>
                    <groupId>org.apache.maven.plugins</groupId>
                    <artifactId>maven-jar-plugin</artifactId>
                    <version>2.6</version>
                    <configuration>
                        <archive>
                            <manifest>
                                <addClasspath>true</addClasspath>
                                <classpathPrefix>lib/</classpathPrefix>
                                <mainClass>Receiver</mainClass>
                            </manifest>
                        </archive>
                    </configuration>
                </plugin>


                <plugin>
                    <groupId>org.apache.maven.plugins</groupId>
                    <artifactId>maven-dependency-plugin</artifactId>
                    <version>2.10</version>
                    <executions>
                        <execution>
                            <id>copy-dependencies</id>
                            <phase>package</phase>
                            <goals>
                                <goal>copy-dependencies</goal>
                            </goals>
                            <configuration>
                                <outputDirectory>${project.build.directory}/lib</outputDirectory>
                            </configuration>
                        </execution>
                    </executions>
                </plugin>




            </plugins>
        </build>

        <repositories>
            <repository>
                <id>spring-milestone</id>
                <url>http://repo.spring.io/libs-release</url>
            </repository>
        </repositories>


    </project>
