# 企享云个税账号信息-tsate_qxy_gsaccount

## 企享云个税账号信息-主表 t_tsate_qxy_gsaccount

- **表名称：** 企享云个税账号信息-主表
- **表名：** t_tsate_qxy_gsaccount

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 3 | fmaintaxoffice | 主管税务机关 | varchar | 300 |  | √ | ' ' | 主管税务机关 |
| 4 | fbillstatus | 单据状态 | varchar | 50 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 5 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 6 | fqxydq | 地区(企享云编码) | varchar | 50 |  | √ | ' ' | 地区(企享云编码) |
| 7 | fnsrsbh | 税号 | varchar | 50 |  | √ | ' ' | 税号 |
| 8 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 9 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 10 | fdjxh | 登记序号 | varchar | 50 |  | √ | ' ' | 登记序号 |
| 11 | fbm | 部门 | varchar | 300 |  | √ | ' ' | 部门 |
| 12 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 13 | fqyid | 企业id | varchar | 50 |  | √ | ' ' | 企业id |
| 14 | fbillno | 单据编号 | varchar | 50 |  | √ | ' ' | 单据编号 |
| 15 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 16 | faccountid | 账号 | varchar | 50 |  | √ | ' ' | 账号 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_t_tsate_qxy_gsaccount_1 |  | fqyid |
| 2 | pk_tsate_qxy_gsaccount |  | fid |
