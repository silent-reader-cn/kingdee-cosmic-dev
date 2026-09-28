# 我的报账-dhc_mybilllist

## 我的报账-主表 t_dhc_mybilllist

- **表名称：** 我的报账-主表
- **表名：** t_dhc_mybilllist

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 3 | fimagestatus | 影像状态 | bpchar | 1 |  | √ | ' ' | 影像状态,枚举: 0 :待上传 2 :已上传 3 :退回重扫 4 :已重传 |
| 4 | fbillsubject | 主题 | varchar | 255 |  | √ | ' ' | 主题 |
| 5 | fbillstatus | 单据状态 | bpchar | 1 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 6 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 7 | fbill | 业务单据 | varchar | 36 |  | √ | ' ' | [表单元数据 bos_formmeta](../mdl_files/bos_formmeta.md) |
| 8 | fcurrency | 本位币 | int8 | 64 |  | √ | 0 | [币种 bd_currency](../base_files/bd_currency.md) |
| 9 | fcompany | 组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 10 | famount | 金额 | numeric | 23 | 10 | √ | 0.0000000000 | 金额 |
| 11 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 12 | fapplicant | 报账申请人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 13 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 14 | freimbursestatus | 报账状态 | bpchar | 1 |  | √ | ' ' | 报账状态,枚举: 0 :待报账 1 :报账中 2 :报账完成 |
| 15 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 16 | fbillkind | 报账分类 | int8 | 64 |  | √ | 0 | [报账分类 dhc_billclassification](../dhc_files/dhc_billclassification.md) |
| 17 | fbillstatusext | 单据状态 | varchar | 30 |  | √ | ' ' | 单据状态 |
| 18 | fcurrentdealer | 当前处理人 | varchar | 60 |  | √ | ' ' | 当前处理人 |
| 19 | fbillid | 单据id | int8 | 64 |  | √ | 0 | 单据id |
| 20 | fbusinessstatus | 业务状态 | varchar | 18 |  | √ | ' ' | 业务状态 |
| 21 | fimageupdatetime | 影像更新时间 | timestamp | 0 |  |  | null | 影像更新时间 |
| 22 | fbillno | 单据编号 | varchar | 60 |  | √ | ' ' | 单据编号 |
| 23 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_dhc_mybilllist_creatorid |  | fcreatorid |
| 2 | t_dhc_mybilllist_pkey |  | fid |
| 3 | idx_dhc_mybilllist_billid |  | fbillid,fbill,fid |
| 4 | idx_dhc_mybilllist_bill |  | fbill |
| 5 | idx_dhc_mybilllist_remi |  | freimbursestatus |
| 6 | idx_dhc_mybilllist_applicant |  | fapplicant |
| 7 | idx_dhc_mybilllist_billno |  | fbillno |
