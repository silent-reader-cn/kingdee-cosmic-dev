# 抵免所得税额汇总数据-tccit_dmsdse_summary

## 抵免所得税额汇总数据-主表 t_tccit_dmsdse_summary

- **表名称：** 抵免所得税额汇总数据-主表
- **表名：** t_tccit_dmsdse_summary

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | frule | 专用设备投资类型取数规则 | int8 | 64 |  | √ | 0 | [优惠项目取数规则 tccit_preferential_item](../tccit_files/tccit_preferential_item.md) |
| 3 | ftype | 类型 | varchar | 50 |  | √ | ' ' | 类型,枚举: income :营业收入 jcost :营业成本 profit :利润总额 |
| 4 | ftaxorg | 组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 5 | fskssqz | 日期范围.结束 | timestamp | 0 |  |  | null | 日期范围.结束 |
| 6 | fdmbl | 抵免比例 | numeric | 23 | 10 | √ | 0 | 抵免比例 |
| 7 | fzysbtze | 专用设备投资额 | numeric | 23 | 10 | √ | 0 | 专用设备投资额 |
| 8 | famount | 本年可抵免税额 | numeric | 23 | 10 | √ | 0 | 本年可抵免税额 |
| 9 | fskssqq | 日期范围.开始 | timestamp | 0 |  |  | null | 日期范围.开始 |
| 10 | forg | 运行组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_tccit_dmsdse_summary |  | fid |
| 2 | idx_tccit_dmsdse_summary_1 |  | fskssqq,fskssqz,forg |
