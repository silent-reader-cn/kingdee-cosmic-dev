# 冻结日志-ap_freezelog

## 冻结日志-主表 t_ap_freezelog

- **表名称：** 冻结日志-主表
- **表名：** t_ap_freezelog

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmodifierid | 修改人 | int8 | 64 |  |  | 0 | 人员 bos_user |
| 3 | fbillstatus | 单据状态 | varchar | 30 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 4 | fasstact | 往来单位 | int8 | 64 |  | √ | 0 | 供应商 bd_supplier |
| 5 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 6 | foptype | 操作类型 | varchar | 30 |  | √ | ' ' | 操作类型,枚举: deaudit :反审核触发 manual :手工触发 |
| 7 | foprange | 操作范围 | varchar | 30 |  | √ | ' ' | 操作范围,枚举: wholeorder :整单 payplan :付款计划 detail :明细 |
| 8 | fasstacttype | 往来类型 | varchar | 30 |  | √ | ' ' | 往来类型,枚举: bd_supplier :供应商 bos_user :人员 bd_customer :客户 bos_org :业务单元 cas_othercontactunit :其他往来单位 |
| 9 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 10 | forg | 操作组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 11 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 12 | foptime | 操作时间 | timestamp | 0 |  |  | null | 操作时间 |
| 13 | fcreatorid | 操作用户 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 14 | fbusinessop | 业务操作 | varchar | 30 |  | √ | ' ' | 业务操作,枚举: allfreeze :冻结 unfreeze :解冻 |
| 15 | fbillentryid | 单据行ID | varchar | 30 |  |  | ' ' | 单据行ID |
| 16 | ffreezereason | 冻结/解冻原因 | varchar | 255 |  |  | ' ' | 冻结/解冻原因 |
| 17 | fbillid | 业务单据ID | varchar | 30 |  | √ | ' ' | 业务单据ID |
| 18 | flineno | 行号 | varchar | 50 |  |  | ' ' | 行号 |
| 19 | fbillno | 单据编号 | varchar | 80 |  | √ | ' ' | 单据编号 |
| 20 | fauditorid | 审核人 | int8 | 64 |  |  | 0 | 人员 bos_user |
| 21 | fbilltype | 业务单据 | varchar | 50 |  | √ | ' ' | 单据主实体 bos_billmainentity |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_ap_freezelog |  | fid |
