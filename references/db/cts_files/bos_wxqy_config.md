# 企业微信配置-bos_wxqy_config

## 企业微信配置-主表 t_bas_wxqyh

- **表名称：** 企业微信配置-主表
- **表名：** t_bas_wxqyh

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fagentid | 应用ID | varchar | 50 |  | √ | ' ' | 应用ID |
| 3 | fagentname | 应用名称 | varchar | 50 |  | √ | ' ' | 应用名称 |
| 4 | fhost | 当前域名地址 | varchar | 128 |  | √ | ' ' | 当前域名地址 |
| 5 | fwebformid | Web端应用主页 | varchar | 36 |  | √ | ' ' | [主实体对象 bos_entityobject](../mdl_files/bos_entityobject.md) |
| 6 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 7 | fmobileformid | 移动端应用主页 | varchar | 36 |  | √ | ' ' | [主实体对象 bos_entityobject](../mdl_files/bos_entityobject.md) |
| 8 | fcreatetime | 创建时间 | timestamp | 0 |  | √ | LOCALTIMESTAMP | 创建时间 |
| 9 | fweburl | Web端URL | varchar | 600 |  | √ | ' ' | Web端URL |
| 10 | fcorpname | 企业名称 | varchar | 50 |  | √ | ' ' | 企业名称 |
| 11 | fconnstatus | 连接测试状态 | bpchar | 1 |  | √ | '0' | 连接测试状态,枚举: 0 :未测试 1 :正常 2 :异常 |
| 12 | ftrustedip | 企业可信IP | varchar | 100 |  | √ | ' ' | 企业可信IP |
| 13 | fcorpsecret | 应用秘钥 | varchar | 100 |  | √ | ' ' | 应用秘钥 |
| 14 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 15 | fiptime | ip获取时间 | timestamp | 0 |  |  | null | ip获取时间 |
| 16 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 17 | fcorpid | 企业ID | varchar | 50 |  | √ | ' ' | 企业ID |
| 18 | fenable | 使用状态 | bpchar | 1 |  | √ | '1' | 使用状态 |
| 19 | fcustomdata | 自定义数据 | varchar | 1024 |  | √ | ' ' | 自定义数据 |
| 20 | fmobileurl | 移动端URL | varchar | 600 |  | √ | ' ' | 移动端URL |
| 21 | fisscan | 用于扫码登录 | varchar | 1 |  | √ | '0' | 用于扫码登录 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_t_bas_wxqyh_corpid |  | fcorpid |
| 2 | t_bas_wxqyh_pkey |  | fid |
