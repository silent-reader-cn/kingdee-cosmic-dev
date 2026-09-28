# 附报事项税金计提-tccit_fbsx_acc_sum_sjjt

## 附报事项税金计提-主表 t_tccit_fbsx_acc_sum_sjjt

- **表名称：** 附报事项税金计提-主表
- **表名：** t_tccit_fbsx_acc_sum_sjjt

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fskssqz | 日期范围.结束 | timestamp | 0 |  |  | null | 日期范围.结束 |
| 3 | fitem | 项目 | varchar | 50 |  | √ | ' ' | 项目,枚举: item1 :已计入成本费用的职工薪酬 item2 :实际支付给职工的应付职工薪酬 item3 :扶贫捐赠支出全额扣除 |
| 4 | famount | 金额 | numeric | 23 | 10 | √ | 0 | 金额 |
| 5 | fskssqq | 日期范围.开始 | timestamp | 0 |  |  | null | 日期范围.开始 |
| 6 | forg | 组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_tccit_fbsx_acc_sum_sjjt_1 |  | forg,fskssqq,fskssqz |
| 2 | pk_tccit_fbsx_acc_sum_sjjt |  | fid |
