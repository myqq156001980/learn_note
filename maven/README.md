# set repository

    <settings>
        <mirrors>
            <mirror>
                <id>UK</id>
                <name>UK Central</name>
                <url>http://maven.aliyun.com/nexus/content/groups/public</url>
                <mirrorOf>central</mirrorOf>
            </mirror>
        </mirrors>

    </settings>
    
    
----


        <plugin>
          <groupId>org.springframework.boot</groupId>
          <artifactId>spring-boot-maven-plugin</artifactId>
          <configuration>
              <mainClass>com.lianjia.search.spider.SpiderScheduleApplication</mainClass>
          </configuration>
          <executions>
              <execution>
                  <goals>
                      <goal>repackage</goal>
                  </goals>
              </execution>
          </executions>
        </plugin>
