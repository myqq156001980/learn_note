# angularjs 跨域post请求

```
I had the same problem. In the jQuery documentation I found:

For cross-domain requests, setting the content type to anything other than application/x-www-form-urlencoded, multipart/form-data, or text/plain will trigger the browser to send a preflight OPTIONS request to the server.
So if the server does not allow it, it will throw errors. By default angular content type is application/json, which is trying to send a OPTION request. Try to overwrite angular default header or allow it in server end. Here is an angular sample:

$http.post(url, data, {
    headers : {
        'Content-Type' : 'application/x-www-form-urlencoded; charset=UTF-8'
    }
});
```

* 在spring mvc中不能使用 @ResponseBody标签，会默认返回application/json 在angular中会导致失败。

---

```
@RequestMapping(value = "/anon_createProduct")
public void createProduct(@RequestParam(value = "j") String j, HttpServletResponse response) throws IOException {
    response.setHeader("Access-Control-Allow-Origin", "*");
    response.setHeader("Content-Type", "text/html; charset=UTF-8");
    System.out.println(j);
    PrintWriter out = response.getWriter();
    out.write("success");
}
```



