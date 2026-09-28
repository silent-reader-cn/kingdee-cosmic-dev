# 高新技术企业优惠情况台账-tccit_high_tech_account

## 单据体-子表 t_tccit_high_tech_income

- **表名称：** 单据体-子表
- **表名：** t_tccit_high_tech_income

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 3 | fincomerate | 金额/比例 | numeric | 23 | 10 | √ | 0.0000000000 | 金额/比例 |
| 4 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 5 | fincometype | 项目 | varchar | 50 |  | √ | ' ' | 项目,枚举: 1 :本年高新产品（服务）收入 2 :本年高新技术性收入 3 :本年高新收入合计 4 :本年收入总额 5 :本年不征税收入 6 :本年企业总收入 7 :本年高新收入占比 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_tccit_high_tech_income |  | fentryid |
| 2 | idx_tccit_high_tech_income_fk |  | fid |

---

## 高新技术企业优惠情况台账-主表 t_tccit_high_tech_account

- **表名称：** 高新技术企业优惠情况台账-主表
- **表名：** t_tccit_high_tech_account

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 3 | fpeoples | 本年科技人员数 | int8 | 64 |  | √ | 0 | 本年科技人员数 |
| 4 | fmark | 备注 | varchar | 50 |  | √ | ' ' | 备注 |
| 5 | fbillstatus | 单据状态 | varchar | 50 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 6 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 7 | forgid | 税务组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 8 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 9 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 10 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 11 | ftotalpeoples | 本年职工总数 | int8 | 64 |  | √ | 0 | 本年职工总数 |
| 12 | fyear | 年度 | timestamp | 0 |  |  | null | 年度 |
| 13 | fpeoplerate | 本年科技人员占比 | numeric | 23 | 10 | √ | 0.0000000000 | 本年科技人员占比 |
| 14 | fhightechscope | 高新技术所属范围 | int8 | 64 |  | √ | 0 | 业务定义分录(树) tpo_tccit_bizdefen_tree |
| 15 | fkeyrate3 | 三年研发费用占销售（营业）收入的比例 | numeric | 23 | 10 | √ | 0.0000000000 | 三年研发费用占销售（营业）收入的比例 |
| 16 | fbillno | 业务编码 | varchar | 30 |  | √ | ' ' | 业务编码 |
| 17 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 18 | fkeyrate1 | 本年科技人员占比 | numeric | 23 | 10 | √ | 0.0000000000 | 本年科技人员占比 |
| 19 | fkeyrate2 | 本年高新收入占比 | numeric | 23 | 10 | √ | 0.0000000000 | 本年高新收入占比 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_tccit_high_tech_account |  | fbillno |
| 2 | pk_tccit_high_tech_account |  | fid |

---

## 单据体-子表 t_tccit_high_tech_develop

- **表名称：** 单据体-子表
- **表名：** t_tccit_high_tech_develop

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fdeveloprate | 合计/比例 | numeric | 23 | 10 | √ | 0.0000000000 | 合计/比例 |
| 3 | fpretwoyear | 前一年度 | numeric | 23 | 10 | √ | 0.0000000000 | 前一年度 |
| 4 | fdeveloptype | 项目 | varchar | 50 |  | √ | ' ' | 项目,枚举: 1 :人员人工费用 2 :直接投入费用 3 :折旧费用与长期待摊费用 4 :无形资产摊销费用 5 :设计费用 6 :装备调试费与实验费用 7 :其他费用 8 :其中：可计入研发费用的其他费用 9 :小计：内部研究开发投入 10 :境内的外部研发费 11 :境外的外部研发费 12 :其中：可计入研发费用的境外的外部研发费 13 :小计：委托外部研发费用 14 :归集的高新研发费用金额合计 15 :销售（营业）收入 16 :三年研发费用占销售（营业）收入的比例 |
| 5 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 6 | fcurryear | 本年度 | numeric | 23 | 10 | √ | 0.0000000000 | 本年度 |
| 7 | fprethreeyear | 前二年度 | numeric | 23 | 10 | √ | 0.0000000000 | 前二年度 |
| 8 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_tccit_high_tech_develop_fk |  | fid |
| 2 | pk_tccit_high_tech_develop |  | fentryid |
