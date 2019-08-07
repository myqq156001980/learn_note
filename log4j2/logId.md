```

<Property name="log.basedir">e:/log</Property>
<Property name="log.layout">%d %-5p %t (%c:%L) - %m%n</Property>
<Routing name="thread">
            <Routes pattern="$${ctx:ThreadName}">
                <Route>
                    <RollingFile name="RollingFile-${ctx:ThreadName}" fileName="${log.basedir}/${ctx:ThreadName}.log"
                                 filePattern="${log.basedir}/${ctx:ThreadName}-%d{HH-mm-ss}.log" append="false">
                        <PatternLayout pattern="${log.layout}"/>
                        <Policies>
                            <SizeBasedTriggeringPolicy size="100M"/>
                        </Policies>
                        <DefaultRolloverStrategy max="100"/>
                        <Filters>
　　　　　　　　<!--此处可添加过滤,被我删掉了,可以根据等级过滤-->
                        </Filters>
                    </RollingFile>
                </Route>
                <Route ref="STDOUT" key="${ctx:ThreadName}"/> 
            </Routes>
        </Routing>

```


```
ThreadContext.put("ThreadName", "name");
ThreadContext.remove("ThreadName");

```
