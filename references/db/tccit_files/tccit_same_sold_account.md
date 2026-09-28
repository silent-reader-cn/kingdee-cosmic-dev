# 视同销售台账-tccit_same_sold_account

## 视同销售台账-主表 t_tccit_same_sold_account

- **表名称：** 视同销售台账-主表
- **表名：** t_tccit_same_sold_account

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 3 | fbillstatus | 单据状态 | varchar | 50 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 4 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 5 | fdescribe | 业务描述 | varchar | 250 |  | √ | ' ' | 业务描述 |
| 6 | forgid | 税务组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 7 | fremarks | 备注 | varchar | 250 |  | √ | ' ' | 备注 |
| 8 | fincome | 视同销售收入 | numeric | 23 | 10 | √ | 0.0000000000 | 视同销售收入 |
| 9 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 10 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 11 | fselforhe | 自产或外购 | varchar | 50 |  | √ | ' ' | 自产或外购,枚举: self :自产 others :外购 |
| 12 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 13 | fsamesoldtype | 视同销售类型 | varchar | 50 |  | √ | ' ' | 视同销售类型,枚举: sctghxs :市场推广或销售 jjyc :交际应酬 zgjlhfl :职工奖励或福利 gxfp :股息分配 dwjz :对外捐赠 dwtzxm :对外投资项目 tglw :提供劳务 fhbxzcjh :非货币性资产交换 others :其他 |
| 14 | fdate | 时间 | timestamp | 0 |  |  | null | 时间 |
| 15 | fbillno | 业务编号 | varchar | 30 |  | √ | ' ' | 业务编号 |
| 16 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 17 | fcost | 视同销售成本 | numeric | 23 | 10 | √ | 0.0000000000 | 视同销售成本 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_tccit_same_sold_account |  | forgid |
| 2 | pk_tccit_same_sold_account |  | fid |
