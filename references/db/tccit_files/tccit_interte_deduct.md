# 跨期扣除项目台账-tccit_interte_deduct

## 跨期扣除项目台账-主表 t_tccit_interte_deduct

- **表名称：** 跨期扣除项目台账-主表
- **表名：** t_tccit_interte_deduct

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 3 | fbillstatus | 单据状态 | varchar | 50 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 4 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 5 | fprovisionmoney | 计提金额 | numeric | 23 | 10 | √ | 0.0000000000 | 计提金额 |
| 6 | fremarks | 备注 | varchar | 255 |  | √ | ' ' | 备注 |
| 7 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 8 | fcontractno | 合同编号 | varchar | 50 |  | √ | ' ' | 合同编号 |
| 9 | forg | 税务组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 10 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 11 | fprojectname | 项目名称 | varchar | 50 |  | √ | ' ' | 项目名称 |
| 12 | fstatus | 跨期项目扣除状态 | varchar | 50 |  | √ | ' ' | 跨期项目扣除状态,枚举: zmjt :账面计提 sjzf :实际支付 |
| 13 | fmigration | 迁移状态 | varchar | 50 |  | √ | ' ' | 迁移状态 |
| 14 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 15 | ftype | 跨期扣除项目类型 | varchar | 50 |  | √ | ' ' | 跨期扣除项目类型 |
| 16 | fcostcenter | 成本中心 | varchar | 50 |  | √ | ' ' | 成本中心 |
| 17 | fdocnumber | 相关凭证编号 | varchar | 50 |  | √ | ' ' | 相关凭证编号 |
| 18 | faccountdate | 记账日期 | timestamp | 0 |  |  | null | 记账日期 |
| 19 | factualpay | 实际支付金额 | numeric | 23 | 10 | √ | 0.0000000000 | 实际支付金额 |
| 20 | fbillno | 业务编码 | varchar | 30 |  | √ | ' ' | 业务编码 |
| 21 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | 人员 bos_user |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_tccit_interte_deduct |  | fid |
| 2 | idx_tccit_interte_deduct |  | forg |
