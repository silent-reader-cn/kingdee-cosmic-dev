# 净改变关系记录-msplan_net_change_record

## 净改变关系记录-主表 t_msplan_change_record

- **表名称：** 净改变关系记录-主表
- **表名：** t_msplan_change_record

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fparent_id | 父项预留变更记录ID | int8 | 64 |  | √ | 0 | 父项预留变更记录ID |
| 3 | fpriority | 预留优先级 | int8 | 64 |  | √ | 0 | 预留优先级 |
| 4 | fisdepend | 是否相关需求预留 | bpchar | 1 |  | √ | '0' | 是否相关需求预留 |
| 5 | fbalentryid | 供应分录ID | int8 | 64 |  | √ | 0 | 供应分录ID |
| 6 | f_s_entryseq | 供应单据分录行号 | int8 | 64 |  | √ | 0 | 供应单据分录行号 |
| 7 | f_base_qty | 预留基本数量 | numeric | 23 | 10 | √ | 0 | 预留基本数量 |
| 8 | f_billentry_id | 需求单据分录ID | int8 | 64 |  | √ | 0 | 需求单据分录ID |
| 9 | f_create_date | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 10 | fexpiredate | 预留到期日期 | timestamp | 0 |  |  | null | 预留到期日期 |
| 11 | f_qty | 预留数量 | numeric | 23 | 10 | √ | 0 | 预留数量 |
| 12 | f_bill_obj_id | 需求单据 | varchar | 50 |  | √ | ' ' | 单据主实体 bos_billmainentity |
| 13 | f_s_billnum | 供应单据编码 | varchar | 100 |  | √ | ' ' | 供应单据编码 |
| 14 | freservesource | 预留来源 | varchar | 30 |  | √ | ' ' | 预留来源 |
| 15 | f_s_unit | 计量单位 | int8 | 64 |  | √ | 0 | 计量单位 bd_measureunits |
| 16 | f_ori_qty | 原始预留数量 | numeric | 23 | 10 | √ | 0 | 原始预留数量 |
| 17 | f_s_baseunit | 基本单位 | int8 | 64 |  | √ | 0 | 计量单位 bd_measureunits |
| 18 | f_s_org | 供应组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 19 | f_bill_no | 需求单据编码 | varchar | 100 |  | √ | ' ' | 需求单据编码 |
| 20 | fchange_type | 变更类型 | varchar | 50 |  | √ | ' ' | 变更类型,枚举: 0 :初始化 1 :新增 2 :转移 3 :替换 4 :拆分 |
| 21 | f_bal_id | 供应ID | int8 | 64 |  | √ | 0 | 供应ID |
| 22 | f_creater_id | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 23 | f_bal_obj_id | 供应对象 | varchar | 50 |  | √ | ' ' | 主实体对象 bos_entityobject |
| 24 | f_s_materiel | 物料编码 | int8 | 64 |  | √ | 0 | 物料 bd_material |
| 25 | ftransfertype | 转移类型 | varchar | 30 |  | √ | ' ' | 转移类型,枚举: 0 :需求转移 1 :供应转移 |
| 26 | f_r_sale_org | 需求组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 27 | f_r_biz_date | 需求日期 | timestamp | 0 |  |  | null | 需求日期 |
| 28 | f_billentry_seq | 需求单据分录行号 | int8 | 64 |  | √ | 0 | 需求单据分录行号 |
| 29 | fisweak | 弱预留 | bpchar | 1 |  | √ | '0' | 弱预留 |
| 30 | f_bill_id | 需求单据ID | int8 | 64 |  | √ | 0 | 需求单据ID |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_msplan_change_ced_bid |  | f_bill_id |
| 2 | idx_msplan_change_ced_m |  | f_s_materiel |
| 3 | pk_t_msplan_change_record |  | fid |
| 4 | idx_msplan_change_ced_weak |  | fisweak |
| 5 | idx_msplan_change_ced_type |  | freservesource |
| 6 | idx_msplan_change_ced_p |  | fparent_id |
| 7 | idx_msplan_change_ced_sid |  | f_bal_id |
