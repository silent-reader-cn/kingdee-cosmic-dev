# 银企服务配置-be_serviceconfig

## 银企服务配置-主表 t_be_serviceconfig

- **表名称：** 银企服务配置-主表
- **表名：** t_be_serviceconfig

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fhufu | 部分CA证书 | varchar | 510 |  |  | null | 部分CA证书 |
| 3 | fprivatekey | 客户私钥密码 | varchar | 30 |  | √ | ' ' | 客户私钥密码 |
| 4 | ffile | CA证书文件 | varchar | 510 |  |  | null | CA证书文件 |
| 5 | ffile_tag | CA证书文件_详情 | text | 0 |  |  | null | CA证书文件_详情 |
| 6 | fstatus | 连接状态 | bpchar | 1 |  | √ | ' ' | 连接状态 |
| 7 | fmasterid | fmasterid | int8 | 64 |  | √ | 0 |  |
| 8 | fserveraddress | 服务器地址 | varchar | 100 |  | √ | ' ' | 服务器地址 |
| 9 | fport | 端口号 | varchar | 8 |  | √ | ' ' | 端口号 |
| 10 | fisencrypt | 加密连接 | bpchar | 1 |  | √ | ' ' | 加密连接 |
| 11 | ffilepath | 客户CA证书 | varchar | 100 |  | √ | ' ' | 客户CA证书 |
| 12 | fhufu_tag | 部分CA证书_详情 | text | 0 |  |  | null | 部分CA证书_详情 |
| 13 | fcustomerid | 客户ID号 | varchar | 100 |  | √ | ' ' | 客户ID号 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_be_sc_fcid |  | fcustomerid |
| 2 | t_be_serviceconfig_pkey |  | fid |
