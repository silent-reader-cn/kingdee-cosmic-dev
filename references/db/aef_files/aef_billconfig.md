# 业务单据配置-aef_billconfig

## 业务单据配置-主表 t_aef_billconfig

- **表名称：** 业务单据配置-主表
- **表名：** t_aef_billconfig

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 3 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 4 | fcreatetime | 创建日期 | timestamp | 0 |  |  | null | 创建日期 |
| 5 | fisreceipt | 是否包含电子回单 | bpchar | 1 |  | √ | '0' | 是否包含电子回单 |
| 6 | fservicename | 微服务名 | varchar | 50 |  | √ | ' ' | 微服务名 |
| 7 | fplugin | 业务插件 | varchar | 500 |  | √ | ' ' | 业务插件 |
| 8 | fbilltype | 单据类型 | varchar | 50 |  | √ | ' ' | [主实体对象 bos_entityobject](../mdl_files/bos_entityobject.md) |
| 9 | fisinvoice | 是否包含发票 | bpchar | 1 |  | √ | '0' | 是否包含发票 |
| 10 | fmodifytime | 修改日期 | timestamp | 0 |  |  | null | 修改日期 |
| 11 | fappid | appid | varchar | 50 |  | √ | ' ' | appid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_aef_billconfig_bill |  | fbilltype |
| 2 | pk_t_aef_billconfig |  | fid |
