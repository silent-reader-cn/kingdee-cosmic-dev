# WeLink配置-bos_welink_config

## WeLink配置-主表 t_bas_welink

- **表名称：** WeLink配置-主表
- **表名：** t_bas_welink

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fhost | 当前域名地址 | varchar | 128 |  | √ | ' ' | 当前域名地址 |
| 3 | fwebformid | Web端应用主页 | varchar | 36 |  | √ | ' ' | [主实体对象 bos_entityobject](../mdl_files/bos_entityobject.md) |
| 4 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 5 | fappsecret | 应用秘钥 | varchar | 150 |  | √ | ' ' | 应用秘钥 |
| 6 | fmobileformid | 移动端应用主页 | varchar | 36 |  | √ | ' ' | [主实体对象 bos_entityobject](../mdl_files/bos_entityobject.md) |
| 7 | fcreatetime | 创建时间 | timestamp | 0 |  | √ | LOCALTIMESTAMP | 创建时间 |
| 8 | fweburl | Web端URL | varchar | 600 |  | √ | ' ' | Web端URL |
| 9 | fconnstatus | 连接测试状态 | bpchar | 1 |  | √ | '0' | 连接测试状态,枚举: 0 :未测试 1 :正常 2 :异常 |
| 10 | fappid | 应用ID | varchar | 150 |  | √ | ' ' | 应用ID |
| 11 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 12 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 13 | fappname | 应用名称 | varchar | 150 |  | √ | ' ' | 应用名称 |
| 14 | fenable | 使用状态 | bpchar | 1 |  | √ | '1' | 使用状态 |
| 15 | fmobileurl | 移动端URL | varchar | 600 |  | √ | ' ' | 移动端URL |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_bas_welink |  | fid |
| 2 | idx_welink_fappid |  | fappid |
