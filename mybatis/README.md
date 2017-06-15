# Mybatis 获取插入主键


	public class ApiInterface implements Serializable {
		private int interfaceId;
		private int productId;
		private String interfaceName;
		private String interfaceAddress;
		private String interfaceRequestType;
		private String interfaceResponseType;
		private boolean interfaceStatus;
		private String kongApiId;
		private List<AbelParameters> parametersList;
		setter()...
		getter()....
		}


---
    /**
	 * Mapper 文件
     * 插入接口
     *
     * @param apiInterface
     */
    int insertInterface(@Param("interface") ApiInterface apiInterface);
	
----
	 <!--插入接口信息-->
    <insert id="insertInterface" parameterType="com.apiMP.pojo.ApiInterface" useGeneratedKeys="true" keyProperty="interface.interfaceId" keyColumn="inte_id">
        <selectKey resultType="java.lang.Integer" order="AFTER" keyProperty="interface.interfaceId" keyColumn="inte_id">
            SELECT LAST_INSERT_ID()
        </selectKey>

        INSERT INTO product_interface(prod_id, inte_name, inte_address, inte_request_type, inte_response_type,
        kong_api_id)
        VALUES
        (#{interface.productId},#{interface.interfaceName},#{interface.interfaceAddress},#{interface.interfaceRequestType},
        #{interface.interfaceResponseType},#{interface.kongApiId})

    </insert>
	
>注意因为mapper中设置了@Para 名称 在xml中必须设置对应的名称 keyProperty="interface.interfaceId" 才能获取到主键,主键注入到了传递的对象的对应属性当中(通过set方法).  如果不指定@Para 注释 直接写属性名即可keyProperty="interfaceId"在insert标签中指定了useGeneratedKeys="true" keyProperty="interface.interfaceId" keyColumn="inte_id"可以不适用selectkey代码.或者单独使用selectkey

----