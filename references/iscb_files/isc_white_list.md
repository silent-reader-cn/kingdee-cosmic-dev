# 集成云方案白名单-isc_white_list

## 集成云方案白名单-主表 t_isc_white_list

- **表名称：** 集成云方案白名单-主表
- **表名：** t_isc_white_list

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fsign | 签名 | varchar | 500 |  | √ | ' ' | 签名 |
| 3 | fname | 名称 | varchar | 250 |  | √ | ' ' | 名称 |
| 4 | fbuild_time | 制作时间（服务器时间） | varchar | 50 |  | √ | ' ' | 制作时间（服务器时间） |
| 5 | fstate | 状态 | varchar | 50 |  | √ | ' ' | 状态,枚举: NORMAL :正常 INVALID :签名不合法 UNDEPLOYED :资源未部署 CORRUPT :资源已篡改 WITHOUT_BIZ_LIC :无业务许可 |
| 6 | ftype | 类别 | varchar | 50 |  | √ | ' ' | 类别,枚举: isc_data_copy :数据集成方案 isc_service_flow :服务流程 isc_apic_script :自定义API isc_apic_for_external_api :外部系统API isc_metadata_schema :集成对象 isc_apic_webapi :WebAPI登记 iscx_resource :数据流资源 |
| 7 | fspk | ID | varchar | 50 |  | √ | ' ' | ID |
| 8 | fhash | 哈希码 | varchar | 50 |  | √ | ' ' | 哈希码 |
| 9 | fnumber | 编码 | varchar | 250 |  | √ | ' ' | 编码 |
| 10 | fdescription | 资源特征描述 | varchar | 2000 |  | √ | ' ' | 资源特征描述 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | ix_isc_while_list_0 |  | fspk,ftype |
| 2 | pk_t_isc_white_list |  | fid |
