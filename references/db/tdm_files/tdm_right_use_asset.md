# 使用权资产-tdm_right_use_asset

## 使用权资产-主表 t_tdm_right_use_asset

- **表名称：** 使用权资产-主表
- **表名：** t_tdm_right_use_asset

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | faccountorg | 核算组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 3 | ftaxorg | 税务组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 4 | fljzj | 累计折旧 | numeric | 23 | 10 | √ | 0 | 累计折旧 |
| 5 | fljzfzz | 累计支付租金 | numeric | 23 | 10 | √ | 0 | 累计支付租金 |
| 6 | fbqzfzz | 本期支付租金 | numeric | 23 | 10 | √ | 0 | 本期支付租金 |
| 7 | fbnljftzz | 本年累计分摊租金 | numeric | 23 | 10 | √ | 0 | 本年累计分摊租金 |
| 8 | ftaxarea | 税收辖区 | int8 | 64 |  | √ | 0 | [税收辖区 bastax_taxareagroup](../basedata_files/bastax_taxareagroup.md) |
| 9 | fljlxfy | 累计利息费用 | numeric | 23 | 10 | √ | 0 | 累计利息费用 |
| 10 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 11 | ftaxationsys | 税收制度 | int8 | 64 |  | √ | 0 | [税收制度 bd_taxationsys](../basedata_files/bd_taxationsys.md) |
| 12 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 13 | fbnljzj | 本年累计折旧 | numeric | 23 | 10 | √ | 0 | 本年累计折旧 |
| 14 | fend | 租赁结束日 | timestamp | 0 |  |  | null | 租赁结束日 |
| 15 | fbqftzz | 本期分摊租金 | numeric | 23 | 10 | √ | 0 | 本期分摊租金 |
| 16 | fbillno | 单据编号 | varchar | 30 |  | √ | ' ' | 单据编号 |
| 17 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 18 | fname | 合同名称 | varchar | 50 |  | √ | ' ' | 合同名称 |
| 19 | fbnljzfzz | 本年累计支付租金 | numeric | 23 | 10 | √ | 0 | 本年累计支付租金 |
| 20 | fbillstatus | 单据状态 | varchar | 50 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 21 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 22 | fstart | 租赁起始日 | timestamp | 0 |  |  | null | 租赁起始日 |
| 23 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 24 | fcontractno | 合同编号 | varchar | 50 |  | √ | ' ' | 合同编号 |
| 25 | flessor | 出租方 | varchar | 100 |  | √ | ' ' | 出租方 |
| 26 | fbqzj | 本期折旧 | numeric | 23 | 10 | √ | 0 | 本期折旧 |
| 27 | fbqlxfy | 本期利息费用 | numeric | 23 | 10 | √ | 0 | 本期利息费用 |
| 28 | fbnljlxfy | 本年累计利息费用 | numeric | 23 | 10 | √ | 0 | 本年累计利息费用 |
| 29 | fperiod | 会计期间 | timestamp | 0 |  |  | null | 会计期间 |
| 30 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 31 | fljftzz | 累计分摊租金 | numeric | 23 | 10 | √ | 0 | 累计分摊租金 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_tdm_right_use_asset |  | fid |
| 2 | right_use_fbillno_idx |  | fbillno |
