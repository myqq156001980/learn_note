    <project xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns="http://maven.apache.org/POM/4.0.0"
             xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 http://maven.apache.org/xsd/maven-4.0.0.xsd">
        <modelVersion>4.0.0</modelVersion>
        <groupId>flume-sink</groupId>
        <artifactId>flume-sink</artifactId>
        <version>0.0.1-SNAPSHOT</version>
        <dependencies>
            <!-- https://mvnrepository.com/artifact/org.apache.flume/flume-ng-core -->
            <dependency>
                <groupId>org.apache.flume</groupId>
                <artifactId>flume-ng-core</artifactId>
                <version>1.8.0</version>
            </dependency>

            <dependency>
                <groupId>com.amazonaws</groupId>
                <artifactId>aws-java-sdk</artifactId>
                <version>1.11.234</version>
            </dependency>
            <dependency>
                <groupId>com.amazonaws</groupId>
                <artifactId>amazon-kinesis-client</artifactId>
                <version>1.8.8</version>
            </dependency>

            <!-- https://mvnrepository.com/artifact/org.apache.httpcomponents/httpcore -->
            <dependency>
                <groupId>org.apache.httpcomponents</groupId>
                <artifactId>httpcore</artifactId>
                <version>4.4.8</version>
                <!--<version>4.4.1</version>-->
                <!--<scope>provided</scope>-->
            </dependency>

            <!-- https://mvnrepository.com/artifact/org.apache.httpcomponents/httpclient -->
            <dependency>
                <groupId>org.apache.httpcomponents</groupId>
                <artifactId>httpclient</artifactId>
                <version>4.5.3</version>
                <!--<version>4.2.1</version>-->
                <!--<scope>provided</scope>-->
            </dependency>

            <!-- https://mvnrepository.com/artifact/org.apache.commons/commons-lang3 -->
            <dependency>
                <groupId>org.apache.commons</groupId>
                <artifactId>commons-lang3</artifactId>
                <version>3.7</version>
            </dependency>

            <!-- https://mvnrepository.com/artifact/commons-logging/commons-logging -->
            <dependency>
                <groupId>commons-logging</groupId>
                <artifactId>commons-logging</artifactId>
                <version>1.2</version>
            </dependency>

            <!-- https://mvnrepository.com/artifact/com.google.guava/guava -->
            <dependency>
                <groupId>com.google.guava</groupId>
                <artifactId>guava</artifactId>
                <version>23.4-jre</version>
            </dependency>

            <!-- https://mvnrepository.com/artifact/com.fasterxml.jackson.core/jackson-annotations -->
            <dependency>
                <groupId>com.fasterxml.jackson.core</groupId>
                <artifactId>jackson-annotations</artifactId>
                <version>2.9.2</version>
            </dependency>

            <!-- https://mvnrepository.com/artifact/com.fasterxml.jackson.core/jackson-core -->
            <dependency>
                <groupId>com.fasterxml.jackson.core</groupId>
                <artifactId>jackson-core</artifactId>
                <version>2.9.2</version>
            </dependency>

            <!-- https://mvnrepository.com/artifact/com.fasterxml.jackson.core/jackson-databind -->
            <dependency>
                <groupId>com.fasterxml.jackson.core</groupId>
                <artifactId>jackson-databind</artifactId>
                <version>2.9.2</version>
            </dependency>

            <!-- https://mvnrepository.com/artifact/com.fasterxml.jackson.dataformat/jackson-dataformat-cbor -->
            <dependency>
                <groupId>com.fasterxml.jackson.dataformat</groupId>
                <artifactId>jackson-dataformat-cbor</artifactId>
                <version>2.9.2</version>
            </dependency>

            <!-- https://mvnrepository.com/artifact/joda-time/joda-time -->
            <dependency>
                <groupId>joda-time</groupId>
                <artifactId>joda-time</artifactId>
                <version>2.9.9</version>
            </dependency>


        </dependencies>
        <build>
            <finalName>kinesis-sink</finalName>
            <plugins>
                <plugin>
                    <groupId>org.apache.maven.plugins</groupId>
                    <artifactId>maven-assembly-plugin</artifactId>
                    <version>2.5.5</version>
                    <configuration>
                        <descriptorRefs>
                            <descriptorRef>jar-with-dependencies</descriptorRef>
                        </descriptorRefs>
                    </configuration>
                    <executions>
                        <execution>
                            <id>make-assembly</id>
                            <phase>package</phase>
                            <goals>
                                <goal>single</goal>
                            </goals>
                        </execution>
                    </executions>
                </plugin>


                <plugin>
                    <artifactId>maven-compiler-plugin</artifactId>
                    <version>3.0</version>
                    <configuration>
                        <source>1.8</source>
                        <target>1.8</target>
                    </configuration>
                </plugin>
            </plugins>
        </build>
    </project>
