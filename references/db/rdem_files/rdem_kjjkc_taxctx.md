# 可加计扣除税务摊销-rdem_kjjkc_taxctx

## 可加计扣除税务摊销-主表 t_rdem_kjjkc_taxctx

- **表名称：** 可加计扣除税务摊销-主表
- **表名：** t_rdem_kjjkc_taxctx

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fassetname | 资产名称 | varchar | 200 |  | √ | ' ' | 资产名称 |
| 3 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 4 | forgfield | 税务组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 5 | fcalctaxbase | 计税基础 | numeric | 23 | 10 | √ | 0 | 计税基础 |
| 6 | famountfield | 可加计扣除成本 | numeric | 23 | 10 | √ | 0 | 可加计扣除成本 |
| 7 | fbillstatus | 单据状态 | varchar | 50 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 8 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 9 | ftaxcurrentkjjamt | 税务实际当期可加计摊销额 | numeric | 23 | 10 | √ | 0 | 税务实际当期可加计摊销额 |
| 10 | faccountingperiod | 会计期间 | timestamp | 0 |  |  | null | 会计期间 |
| 11 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 12 | fdecimalfield | 可加计扣除率（%） | numeric | 23 | 10 | √ | 0 | 可加计扣除率（%） |
| 13 | forg | 核算组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 14 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 15 | ftaxcumulativekjjamt | 税务实际累计可加计摊销额 | numeric | 23 | 10 | √ | 0 | 税务实际累计可加计摊销额 |
| 16 | ftaxyearkjjamt | 税务实际本年可加计摊销额 | numeric | 23 | 10 | √ | 0 | 税务实际本年可加计摊销额 |
| 17 | ftaxyearamount | 税务实际本年折旧摊销额 | numeric | 23 | 10 | √ | 0 | 税务实际本年折旧摊销额 |
| 18 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 19 | ftaxcumulativeamount | 税务实际累计折旧摊销额 | numeric | 23 | 10 | √ | 0 | 税务实际累计折旧摊销额 |
| 20 | fassetcode | 资产编码 | varchar | 200 |  | √ | ' ' | 资产编码 |
| 21 | fdatasource | 数据来源 | varchar | 50 |  | √ | ' ' | 数据来源,枚举: system :系统同步 import :模板导入 |
| 22 | ftaxcurrentamount | 税务实际当期折旧摊销额 | numeric | 23 | 10 | √ | 0 | 税务实际当期折旧摊销额 |
| 23 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 24 | fbillno | 单据编号 | varchar | 30 |  | √ | ' ' | 单据编号 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_rdem_kjjkc_taxctx |  | fid |
| 2 | idx_rdem_kjjkc_taxctx_m0 |  | fbillno |
