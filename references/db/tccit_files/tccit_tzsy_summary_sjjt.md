# 投资收益明细计提底稿-tccit_tzsy_summary_sjjt

## 投资收益明细计提底稿-主表 t_tccit_tzsy_summary_sjjt

- **表名称：** 投资收益明细计提底稿-主表
- **表名：** t_tccit_tzsy_summary_sjjt

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | ftype | 类型 | varchar | 50 |  | √ | ' ' | 类型,枚举: income :营业收入 jcost :营业成本 profit :利润总额 |
| 3 | ftaxorg | 组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 4 | fskssqz | 日期范围.结束 | timestamp | 0 |  |  | null | 日期范围.结束 |
| 5 | fitem | 投资收益事项 | int8 | 64 |  | √ | 0 | [优惠项目取数规则 tccit_preferential_item](../tccit_files/tccit_preferential_item.md) |
| 6 | fbqlje | 本期累计额 | numeric | 23 | 10 | √ | 0 | 本期累计额 |
| 7 | fbqfse | 本期发生额 | numeric | 23 | 10 | √ | 0 | 本期发生额 |
| 8 | fskssqq | 日期范围.开始 | timestamp | 0 |  |  | null | 日期范围.开始 |
| 9 | forg | 运行组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_tccit_tzsy_summary_sjjt |  | fid |
| 2 | idx_tccit_tzsy_summary_sjjt_1 |  | fskssqq,fskssqz,forg |
