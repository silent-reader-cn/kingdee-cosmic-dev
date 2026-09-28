# MRP净改变明细表-mrp_net_change_detail

## MRP净改变明细表-主表 t_mrp_change_detail

- **表名称：** MRP净改变明细表-主表
- **表名：** t_mrp_change_detail

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fbalentryid | 供应分录ID | int8 | 64 |  | √ | 0 | 供应分录ID |
| 3 | f_s_entryseq | 供应单据分录行号 | int8 | 64 |  | √ | 0 | 供应单据分录行号 |
| 4 | f_base_qty | 预留基本数量 | numeric | 23 | 10 | √ | 0 | 预留基本数量 |
| 5 | f_billentry_id | 需求单据分录ID | int8 | 64 |  | √ | 0 | 需求单据分录ID |
| 6 | frunlog | 计划运算号 | varchar | 50 |  | √ | ' ' | 计划运算号 |
| 7 | frecord_id | 预留记录id | int8 | 64 |  | √ | 0 | 预留记录id |
| 8 | f_bill_obj_id | 需求单据 | varchar | 50 |  | √ | ' ' | 单据主实体 bos_billmainentity |
| 9 | f_s_billnum | 供应单据编码 | varchar | 100 |  | √ | ' ' | 供应单据编码 |
| 10 | f_ori_qty | 原始预留数量 | numeric | 23 | 10 | √ | 0 | 原始预留数量 |
| 11 | f_req_qty | 需求数量 | numeric | 23 | 10 | √ | 0 | 需求数量 |
| 12 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 13 | f_s_baseunit | 基本单位 | int8 | 64 |  | √ | 0 | 计量单位 bd_measureunits |
| 14 | f_s_org | 供应组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 15 | f_bill_no | 需求单据编码 | varchar | 100 |  | √ | ' ' | 需求单据编码 |
| 16 | f_bal_id | 供应ID | int8 | 64 |  | √ | 0 | 供应ID |
| 17 | f_bal_obj_id | 供应对象 | varchar | 50 |  | √ | ' ' | 主实体对象 bos_entityobject |
| 18 | fs_biz_date | 供应日期 | timestamp | 0 |  |  | null | 供应日期 |
| 19 | ftype | 产生类型 | varchar | 50 |  | √ | ' ' | 产生类型,枚举: 1 :创建 0 :释放 |
| 20 | f_s_materiel | 物料编码 | int8 | 64 |  | √ | 0 | 物料 bd_material |
| 21 | f_r_sale_org | 需求组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 22 | f_r_biz_date | 需求日期 | timestamp | 0 |  |  | null | 需求日期 |
| 23 | f_billentry_seq | 需求单据分录行号 | int8 | 64 |  | √ | 0 | 需求单据分录行号 |
| 24 | fisweak | 弱预留 | bpchar | 1 |  | √ | '0' | 弱预留 |
| 25 | f_bill_id | 需求单据ID | int8 | 64 |  | √ | 0 | 需求单据ID |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_mrp_change_detail_weak |  | fisweak |
| 2 | idx_mrp_change_detail_bid |  | f_bill_id |
| 3 | idx_mrp_change_detail_sid |  | f_bal_id |
| 4 | idx_mrp_change_detail_type |  | ftype |
| 5 | idx_mrp_change_detail_red |  | frecord_id |
| 6 | idx_mrp_change_detail_m |  | f_s_materiel |
| 7 | pk_t_mrp_change_detail |  | fid |
