# 业务请求记录-ids_gpe_biz_request

## 业务请求记录-主表 t_ids_gpe_biz_request

- **表名称：** 业务请求记录-主表
- **表名：** t_ids_gpe_biz_request

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | frequesttype | 请求类型 | bpchar | 1 |  | √ | '0' | 请求类型,枚举: 0 :同步请求 1 :异步请求 |
| 3 | freqparams | 请求参数 | varchar | 255 |  | √ | ' ' | 请求参数 |
| 4 | fresponse_tag | 响应结果_详情 | text | 0 |  |  | null | 响应结果_详情 |
| 5 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 6 | fcreatetime | 创建日期 | timestamp | 0 |  |  | null | 创建日期 |
| 7 | fexecutestatus | 执行状态 | varchar | 10 |  | √ | '0' | 执行状态,枚举: 0 :等待执行 10 :执行中 20 :执行成功 30 :执行失败 |
| 8 | freqparams_tag | 请求参数_详情 | text | 0 |  |  | null | 请求参数_详情 |
| 9 | ffailmsg | 失败原因 | varchar | 255 |  | √ | ' ' | 失败原因 |
| 10 | fbizappid | 业务应用 | varchar | 50 |  | √ | ' ' | 业务应用,枚举: bgm :全面预算 |
| 11 | fmodifytime | 修改日期 | timestamp | 0 |  |  | null | 修改日期 |
| 12 | ffailmsg_tag | 失败原因_详情 | text | 0 |  |  | null | 失败原因_详情 |
| 13 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 14 | frequestid | 请求ID | varchar | 100 |  | √ | ' ' | 请求ID |
| 15 | fresponse | 响应结果 | varchar | 255 |  | √ | ' ' | 响应结果 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_ids_gpe_biz_request |  | fid |
| 2 | idx_ids_gpe_biz_req_reqid |  | frequestid |
