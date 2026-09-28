# 合同款项方案-clm_contract_payment_plan

## 合同款项方案-多语言表 t_clm_con_paymentplan_l

- **表名称：** 合同款项方案-多语言表
- **表名：** t_clm_con_paymentplan_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 50 |  | √ | ' ' | 名称 |
| 3 | fcomment | 备注 | varchar | 512 |  |  | null | 备注 |
| 4 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 5 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_contract_paymentplanl_fid |  | fid,flocaleid |
| 2 | pk_t_clm_con_paymentplan_l |  | fpkid |

---

## 合同款项方案-主表 t_clm_con_paymentplan

- **表名称：** 合同款项方案-主表
- **表名：** t_clm_con_paymentplan

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fformdatas | 款项方案表格数据 | text | 0 |  |  | null | 款项方案表格数据 |
| 3 | fname | 名称 | varchar | 50 |  | √ | ' ' | 名称 |
| 4 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 5 | fformdatas_tag | 款项方案表格数据_详情 | text | 0 |  |  | null | 款项方案表格数据_详情 |
| 6 | fcomment | 备注 | varchar | 512 |  |  | null | 备注 |
| 7 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 8 | ftextdatas_tag | 款项方案数据_详情 | text | 0 |  |  | null | 款项方案数据_详情 |
| 9 | fdisabledate | 禁用时间 | timestamp | 0 |  |  | null | 禁用时间 |
| 10 | fdisablerid | 禁用人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 11 | fnotes | fnotes | varchar | 50 |  | √ | ' ' |  |
| 12 | faudittime | 审核时间 | timestamp | 0 |  |  | null | 审核时间 |
| 13 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 14 | fstatus | 数据状态 | varchar | 50 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 15 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 16 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 17 | fauditor | 审核人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 18 | fenable | 使用状态 | varchar | 50 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 19 | fnumber | 编码 | varchar | 30 |  | √ | ' ' | 编码 |
| 20 | fisallowedchange | fisallowedchange | bpchar | 1 |  | √ | '0' |  |
| 21 | ftextdatas | 款项方案数据 | text | 0 |  |  | null | 款项方案数据 |
| 22 | fcontracttype | 适用合同类型 | int8 | 64 |  | √ | 0 | 合同类型 conm_type |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_clm_con_paymentplan |  | fid |
| 2 | idx_clm_paymentplan_number |  | fnumber |

---

## 款项内容-子表 t_clm_con_paymentplan_e

- **表名称：** 款项内容-子表
- **表名：** t_clm_con_paymentplan_e

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fpaymentnode | 款项节点 | int8 | 64 |  | √ | 0 | 合同款项节点 clm_contract_payment_node |
| 3 | fisprepayment | 是否预付 | bpchar | 1 |  | √ | '0' | 是否预付 |
| 4 | fmoneyinwords | 款项金额（中文） | varchar | 50 |  | √ | ' ' | 款项金额（中文） |
| 5 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 6 | ftimelimit | 时间期限 | numeric | 23 | 1 | √ | 0 | 时间期限 |
| 7 | fisprereceive | 是否预收 | bpchar | 1 |  | √ | '0' | 是否预收 |
| 8 | fbeforeorafter | 前/后 | varchar | 50 |  | √ | ' ' | 前/后,枚举: BEFORE :前 AFTER :后 |
| 9 | frate | 款项比例（%） | numeric | 15 | 2 | √ | 0 | 款项比例（%） |
| 10 | ftimeunit | 时间单位 | varchar | 50 |  | √ | ' ' | 时间单位,枚举: workday :个工作日 naturalday :个自然日 day :日 week :周 month :月 year :年 |
| 11 | forder | 序号 | varchar | 50 |  | √ | ' ' | 序号 |
| 12 | fmoneytinnum | 款项金额（数字） | numeric | 23 | 10 | √ | 0 | 款项金额（数字） |
| 13 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 14 | ftextsupplement | 条款文本补充 | varchar | 50 |  | √ | ' ' | 条款文本补充 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_clm_con_paymentplan_e |  | fentryid |
| 2 | idx_clm_paymenplan_e |  | fid |
