# 所得减免台账-tccit_getreduce_acc

## 所得明细-子表 t_tccit_getre_detail

- **表名称：** 所得明细-子表
- **表名：** t_tccit_getre_detail

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fnstz | 纳税调整额 | numeric | 23 | 10 | √ | 0.0000000000 | 纳税调整额 |
| 3 | fdividescale | 分摊比例 | numeric | 23 | 10 | √ | 0.0000000000 | 分摊比例 |
| 4 | fxmsde | 项目所得额 | numeric | 23 | 10 | √ | 0.0000000000 | 项目所得额 |
| 5 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 6 | fincome | 项目收入 | numeric | 23 | 10 | √ | 0.0000000000 | 项目收入 |
| 7 | fqjfyfte | 期间费用分摊额 | numeric | 23 | 10 | √ | 0.0000000000 | 期间费用分摊额 |
| 8 | fdnyhbl | 当年优惠比例 | varchar | 50 |  | √ | ' ' | 当年优惠比例,枚举: 0.5 :50% 1 :100% 0.5or1 :500万以内100%,超500万部分50% —— :—— 1or0.5 :2000万以内100%，超2000万部分50% |
| 9 | fyear | 年度 | timestamp | 0 |  |  | null | 年度 |
| 10 | fnreducename | 优惠事项名称 | int8 | 64 |  | √ | 0 | 优惠项目（树） tpo_discount_tree |
| 11 | fmonth | 月份 | varchar | 30 |  | √ | ' ' | 月份,枚举: 1 :1月 2 :2月 3 :3月 4 :4月 5 :5月 6 :6月 7 :7月 8 :8月 9 :9月 10 :10月 11 :11月 12 :12月 : |
| 12 | fperiodcost | 待分摊期间费用 | numeric | 23 | 10 | √ | 0.0000000000 | 待分摊期间费用 |
| 13 | frelaxtax | 相关税费 | numeric | 23 | 10 | √ | 0.0000000000 | 相关税费 |
| 14 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 15 | fcost | 项目成本 | numeric | 23 | 10 | √ | 0.0000000000 | 项目成本 |
| 16 | fsonremarks | 备注 | varchar | 1000 |  | √ | ' ' | 备注 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_tccit_getre_detail |  | fentryid |
| 2 | idx_tccit_getre_detail_fk |  | fid |

---

## 所得减免台账-主表 t_tccit_getreduce_acc

- **表名称：** 所得减免台账-主表
- **表名：** t_tccit_getreduce_acc

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 3 | freducename | 优惠事项名称 | int8 | 64 |  | √ | 0 | 优惠项目（树） tpo_discount_tree |
| 4 | fbillstatus | 单据状态 | varchar | 50 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 5 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 6 | forgid | 税务组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 7 | ffirstyear | 开始享受优惠的年度 | timestamp | 0 |  |  | null | 开始享受优惠的年度 |
| 8 | fremarks | 备注 | varchar | 1000 |  | √ | ' ' | 备注 |
| 9 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 10 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 11 | fprojectname | 减免项目名称 | varchar | 200 |  | √ | ' ' | 减免项目名称 |
| 12 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 13 | fbillno | 业务编号 | varchar | 30 |  | √ | ' ' | 业务编号 |
| 14 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_tccit_getreduce_acc |  | fid |
| 2 | idx_tccit_getreduce_acc |  | fbillno |
