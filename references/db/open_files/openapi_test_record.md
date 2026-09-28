# 测试结果-openapi_test_record

## 测试结果-主表 t_openapi_test_record

- **表名称：** 测试结果-主表
- **表名：** t_openapi_test_record

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 3 | fbillstatus | 单据状态 | varchar | 1 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 4 | ftestfailreason | 失败原因 | varchar | 2000 |  |  | ' ' | 失败原因 |
| 5 | fcreatetime | 创建时间 | timestamp | 0 |  | √ | LOCALTIMESTAMP | 创建时间 |
| 6 | fhttpstatus | HTTP状态码 | varchar | 50 |  | √ | ' ' | HTTP状态码 |
| 7 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 8 | frequestparam | 请求参数 | varchar | 2000 |  |  | ' ' | 请求参数 |
| 9 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 10 | fresponseparam | 返回参数 | varchar | 2000 |  |  | ' ' | 返回参数 |
| 11 | fcreatorid | 调用人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 12 | fapiid | API | int8 | 64 |  | √ | 0 | API服务 openapi_apilist |
| 13 | ftestcase | 用例名称 | int8 | 64 |  | √ | 0 | 测试用例 openapi_test_case |
| 14 | ftestresult | 测试结果 | varchar | 1 |  | √ | '0' | 测试结果,枚举: 0 :通过 1 :未通过 |
| 15 | fexecutiontime | 执行时间/ms | int8 | 64 |  | √ | 0 | 执行时间/ms |
| 16 | fbillno | 记录编号 | varchar | 30 |  | √ | ' ' | 记录编号 |
| 17 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | 人员 bos_user |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_t_open_test_record_csid |  | ftestcase |
| 2 | pk_t_openapi_test_record |  | fid |
| 3 | idx_t_open_test_record_no |  | fbillno |
