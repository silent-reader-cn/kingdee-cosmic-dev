# 软件、集成电路企业优惠情况台账-tccit_soft_ic_qyyh

## 软件、集成电路企业优惠情况台账-主表 t_tccit_soft_ic_qyyh

- **表名称：** 软件、集成电路企业优惠情况台账-主表
- **表名：** t_tccit_soft_ic_qyyh

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 3 | fbillstatus | 单据状态 | varchar | 50 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 4 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 5 | forgid | 税务组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 6 | fyjkfryrs | 研究开发人员人数 | int8 | 64 |  | √ | 0 | 研究开发人员人数 |
| 7 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 8 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 9 | ffhtjdxssr | 符合条件的销售（营业）收入 | numeric | 23 | 10 | √ | 0.0000000000 | 符合条件的销售（营业）收入 |
| 10 | fyffyze | 研发费用总额 | numeric | 23 | 10 | √ | 0.0000000000 | 研发费用总额 |
| 11 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 12 | fjnyffyje | 境内研发费用金额 | numeric | 23 | 10 | √ | 0.0000000000 | 境内研发费用金额 |
| 13 | fyear | 年度 | timestamp | 0 |  |  | null | 年度 |
| 14 | fqysrze | 企业收入总额 | numeric | 23 | 10 | √ | 0.0000000000 | 企业收入总额 |
| 15 | fbnypjzgzrs | 企业本年月平均职工总人数 | int8 | 64 |  | √ | 0 | 企业本年月平均职工总人数 |
| 16 | fjydxzkysxlzgrs | 具有大学专科以上学历职工人数 | int8 | 64 |  | √ | 0 | 具有大学专科以上学历职工人数 |
| 17 | fbillno | 业务编号 | varchar | 30 |  | √ | ' ' | 业务编号 |
| 18 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_tccit_soft_ic_qyyh |  | forgid,fyear |
| 2 | pk_tccit_soft_ic_qyyh |  | fid |

---

## 单据体-子表 t_tccit_soft_ic_qtzb

- **表名称：** 单据体-子表
- **表名：** t_tccit_soft_ic_qtzb

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 指标名称 | varchar | 200 |  | √ | ' ' | 指标名称 |
| 3 | fmodifydate | 编辑时间 | timestamp | 0 |  |  | null | 编辑时间 |
| 4 | fcdtitle | 其他指标 | varchar | 50 |  | √ | ' ' | 其他指标 |
| 5 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 6 | fzbz | 指标值 | numeric | 23 | 10 | √ | 0.0000000000 | 指标值 |
| 7 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_tccit_soft_ic_qtzb_fk |  | fid |
| 2 | pk_tccit_soft_ic_qtzb |  | fentryid |
