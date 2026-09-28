# 不可税前扣除项目台账-tccit_noreduce_befo_tax

## 不可税前扣除项目台账-主表 t_tccit_noreduce_befo_tax

- **表名称：** 不可税前扣除项目台账-主表
- **表名：** t_tccit_noreduce_befo_tax

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 3 | fbillstatus | 单据状态 | varchar | 30 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 4 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 5 | forgid | 税务组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 6 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 7 | fvoucherno | 凭证号 | varchar | 50 |  | √ | ' ' | 凭证号 |
| 8 | freason | 事由 | varchar | 100 |  | √ | ' ' | 事由 |
| 9 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 10 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 11 | fperiod | 所属税期 | timestamp | 0 |  |  | null | 所属税期 |
| 12 | fmoney | 金额 | numeric | 23 | 10 | √ | 0.0000000000 | 金额 |
| 13 | fnobeforedudetail | 不可税前扣除项目明细 | varchar | 50 |  | √ | ' ' | 不可税前扣除项目明细 |
| 14 | fbillno | 业务编码 | varchar | 30 |  | √ | ' ' | 业务编码 |
| 15 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 16 | fcombofield | 不可税前扣除项目类型 | varchar | 30 |  | √ | ' ' | 不可税前扣除项目类型,枚举: 3010701 :罚金、罚款和被没收财物的损失 3010702 :税收滞纳金、加收利息 3010703 :赞助支出 3010704 :与取得收入无关的支出 3010705 :不合规票据支出 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_tccit_noreduce_befo_tax |  | fperiod |
| 2 | pk_tccit_noreduce_befo_tax |  | fid |
