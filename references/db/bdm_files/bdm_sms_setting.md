# 短信设置-bdm_sms_setting

## 短信设置-主表 t_bdm_sms_setting

- **表名称：** 短信设置-主表
- **表名：** t_bdm_sms_setting

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 3 | fname | 方案名称 | varchar | 30 |  | √ | ' ' | 方案名称 |
| 4 | fdxqmid | 短信签名模板ID | varchar | 50 |  | √ | ' ' | 短信签名模板ID |
| 5 | fbillstatus | 审核状态 | varchar | 10 |  | √ | ' ' | 审核状态,枚举: 1 :未提交 2 :审核中 3 :审核成功 4 :审核失败 |
| 6 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 7 | fformwork_content | 模板内容 | varchar | 50 |  | √ | ' ' | 模板内容 |
| 8 | fdxnr_status | 短信内容审核状态 | varchar | 50 |  | √ | ' ' | 短信内容审核状态 |
| 9 | fpriority | 优先级 | varchar | 10 |  | √ | ' ' | 优先级,枚举: 1 :1 2 :2 3 :3 4 :4 5 :5 6 :6 7 :7 8 :8 9 :9 10 :10 |
| 10 | fdxqm_status | 短信签名审核状态 | varchar | 50 |  | √ | ' ' | 短信签名审核状态 |
| 11 | fformwork_type | 模板类型 | varchar | 10 |  | √ | ' ' | 模板类型,枚举: 1 :短信签名 2 :短信内容 |
| 12 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 13 | ffilter_tag | 匹配条件设置 | text | 0 |  |  | null | 匹配条件设置 |
| 14 | fapply_reason | 申请原因 | varchar | 210 |  | √ | ' ' | 申请原因 |
| 15 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 16 | fstatus | 模板状态 | varchar | 10 |  | √ | ' ' | 模板状态,枚举: 1 :启用 2 :禁用 |
| 17 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 18 | fdxnrid | 短信内容模板ID | varchar | 50 |  | √ | ' ' | 短信内容模板ID |
| 19 | fdatasource | 数据来源 | varchar | 10 |  | √ | ' ' | 数据来源,枚举: 1 :发票数据 |
| 20 | fbillno | 编号 | varchar | 50 |  | √ | ' ' | 编号 |
| 21 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 22 | ffail_reason | 审核失败原因 | varchar | 200 |  | √ | ' ' | 审核失败原因 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_bdm_sms_setting |  | fid |
| 2 | idx_bdm_sms_setting |  | fbillno |
