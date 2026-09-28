# 股权激励台账-tccit_tax_equity_incentiv

## 股权激励台账-主表 t_tccit_tax_equity_incent

- **表名称：** 股权激励台账-主表
- **表名：** t_tccit_tax_equity_incent

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | ftaxperiod | 所属税期 | timestamp | 0 |  |  | null | 所属税期 |
| 3 | fremark | 备注 | varchar | 50 |  | √ | ' ' | 备注 |
| 4 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 5 | fincentivestate | 股权激励状态 | varchar | 50 |  | √ | ' ' | 股权激励状态,枚举: grant :授予 exercise :行权 |
| 6 | fbillstatus | 单据状态 | varchar | 50 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 7 | fincentivetype | 股权激励类型 | varchar | 50 |  | √ | ' ' | 股权激励类型,枚举: slimit :限制性股票 sopition :股票期权 other :其他 |
| 8 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 9 | forgid | 税务组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 10 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 11 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 12 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 13 | ftcount | 数量 | int8 | 64 |  | √ | 0 | 数量 |
| 14 | fpricesum | 授予金额合计 | numeric | 23 | 10 | √ | 0.0000000000 | 授予金额合计 |
| 15 | fgprice | 授予价格（每股） | numeric | 23 | 10 | √ | 0.0000000000 | 授予价格（每股） |
| 16 | fxprice | 行权价格（每股） | numeric | 23 | 10 | √ | 0.0000000000 | 行权价格（每股） |
| 17 | fbookdate | 授予/行权日期 | timestamp | 0 |  |  | null | 授予/行权日期 |
| 18 | fnomoney | 不可税前列支的股权激励金额 | numeric | 23 | 10 | √ | 0.0000000000 | 不可税前列支的股权激励金额 |
| 19 | fbillno | 业务编号 | varchar | 30 |  | √ | ' ' | 业务编号 |
| 20 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 21 | foutmoney | 股权激励支出金额 | numeric | 23 | 10 | √ | 0.0000000000 | 股权激励支出金额 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_tccit_tax_equity_incent |  | forgid,ftaxperiod |
| 2 | pk_tccit_tax_equity_incent |  | fid |
