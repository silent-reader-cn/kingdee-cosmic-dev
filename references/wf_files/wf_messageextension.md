# 消息渠道扩展-wf_messageextension

## 消息渠道扩展-主表 t_wf_messageconfig

- **表名称：** 消息渠道扩展-主表
- **表名：** t_wf_messageconfig

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fservicekey | 消息渠道编码 | varchar | 100 |  | √ | ' ' | 消息渠道编码 |
| 3 | fdefaultservice | 默认渠道 | bpchar | 1 |  | √ | '0' | 默认渠道 |
| 4 | fcreatedate | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 5 | fmodifydate | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 6 | favaliable | 是否启用 | bpchar | 1 |  | √ | '1' | 是否启用 |
| 7 | fserviceclass | 实现类 | varchar | 400 |  | √ | ' ' | 实现类 |
| 8 | fservicename | 消息渠道名称 | varchar | 100 |  | √ | ' ' | 消息渠道名称 |
| 9 | ftpl | 模板 | text | 0 |  |  | null | 模板 |
| 10 | forg | 组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 11 | fcustomparams | 自定义参数 | varchar | 2000 |  | √ | ' ' | 自定义参数 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_wf_messageconfig_pkey |  | fid |
| 2 | idx_wf_messageconfig_fkey |  | fservicekey |
