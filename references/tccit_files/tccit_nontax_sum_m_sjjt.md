# 税金计提免税收入台账中间表-tccit_nontax_sum_m_sjjt

## 税金计提免税收入台账中间表-主表 t_tccit_nontax_sum_m_sjjt

- **表名称：** 税金计提免税收入台账中间表-主表
- **表名：** t_tccit_nontax_sum_m_sjjt

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | ftype | 规则类型 | varchar | 50 |  | √ | ' ' | 规则类型 |
| 3 | fdiscounttype | 优惠类型 | varchar | 50 |  | √ | ' ' | 优惠类型,枚举: 1 :全额免税 2 :收入减计10% 3 :收入减计50% 4 :减半征收 |
| 4 | fskssqz | 日期范围.结束 | timestamp | 0 |  |  | null | 日期范围.结束 |
| 5 | forgid | 运行组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 6 | fitem | 优惠项目取数 | int8 | 64 |  | √ | 0 | 优惠项目（树） tpo_discount_tree |
| 7 | fseq | 流水号 | varchar | 50 |  | √ | ' ' | 流水号 |
| 8 | fruleid | 规则id | int8 | 64 |  | √ | 0 | 规则id |
| 9 | frulename | 规则名称 | varchar | 250 |  | √ | ' ' | 规则名称 |
| 10 | fskssqq | 日期范围.开始 | timestamp | 0 |  |  | null | 日期范围.开始 |
| 11 | fnontaxtotal | 免税收入累计数 | numeric | 23 | 10 | √ | 0 | 免税收入累计数 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_t_tccit_nontax_sum_m_sjjt1 |  | forgid,fskssqq,fskssqz |
| 2 | pk_tccit_nontax_sum_m_sjjt |  | fid |
