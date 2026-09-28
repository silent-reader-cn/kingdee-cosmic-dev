# 绩效报告-ssc_employeeachieverpt

## 成本控制单据体-子表 t_tk_emp_costcontrol

- **表名称：** 成本控制单据体-子表
- **表名：** t_tk_emp_costcontrol

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fccdescription | 得分说明 | varchar | 255 |  | √ | ' ' | 得分说明 |
| 3 | fccactual | 实际值 | numeric | 19 | 6 | √ | 0 | 实际值 |
| 4 | fcctarget | 目标值 | numeric | 19 | 6 | √ | 0 | 目标值 |
| 5 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 6 | fccweight | 权重(%) | int4 | 32 |  | √ | 0 | 权重(%) |
| 7 | fccunitid | 单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 8 | fpoweight | fpoweight | int4 | 32 |  | √ | 0 |  |
| 9 | fcctargettype | 指标类型 | bpchar | 1 |  | √ | ' ' | 指标类型,枚举: 0 :计算指标 1 :综合指标 |
| 10 | fccstandard | 基准值 | numeric | 19 | 6 | √ | 0 | 基准值 |
| 11 | fccachieveid | 绩效指标 | int8 | 64 |  | √ | 0 | [绩效指标 ssc_achievetarget](../som_files/ssc_achievetarget.md) |
| 12 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 13 | fccapproved | 核定值 | numeric | 19 | 6 | √ | 0 | 核定值 |
| 14 | fccscore | 得分 | numeric | 19 | 6 | √ | 0 | 得分 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_tk_emp_costcontrol |  | fentryid |
| 2 | idx_ssc_emp_cc_id |  | fid |

---

## 学习成长单据体-子表 t_tk_emp_learngrowth

- **表名称：** 学习成长单据体-子表
- **表名：** t_tk_emp_learngrowth

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | flrscore | 得分 | numeric | 19 | 6 | √ | 0 | 得分 |
| 3 | flractual | 实际值 | numeric | 19 | 6 | √ | 0 | 实际值 |
| 4 | flrdescription | 得分说明 | varchar | 255 |  | √ | ' ' | 得分说明 |
| 5 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 6 | fpoweight | fpoweight | int4 | 32 |  | √ | 0 |  |
| 7 | flrachieveid | 绩效指标 | int8 | 64 |  | √ | 0 | [绩效指标 ssc_achievetarget](../som_files/ssc_achievetarget.md) |
| 8 | flrstandard | 基准值 | numeric | 19 | 6 | √ | 0 | 基准值 |
| 9 | flrtargettype | 指标类型 | bpchar | 1 |  | √ | ' ' | 指标类型,枚举: 0 :计算指标 1 :综合指标 |
| 10 | flrtarget | 目标值 | numeric | 19 | 6 | √ | 0 | 目标值 |
| 11 | flrapproved | 核定值 | numeric | 19 | 6 | √ | 0 | 核定值 |
| 12 | flrunitid | 单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 13 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 14 | flrweight | 权重(%) | int4 | 32 |  | √ | 0 | 权重(%) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_ssc_emp_lr_id |  | fid |
| 2 | pk_t_tk_emp_learngrowth |  | fentryid |

---

## 流程运营单据体-子表 t_tk_emp_processoperation

- **表名称：** 流程运营单据体-子表
- **表名：** t_tk_emp_processoperation

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fpounitid | 单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 3 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 4 | fpostandard | 基准值 | numeric | 19 | 6 | √ | 0 | 基准值 |
| 5 | fpoachieveid | 绩效指标 | int8 | 64 |  | √ | 0 | [绩效指标 ssc_achievetarget](../som_files/ssc_achievetarget.md) |
| 6 | fpoapproved | 核定值 | numeric | 19 | 6 | √ | 0 | 核定值 |
| 7 | fpotarget | 目标值 | numeric | 19 | 6 | √ | 0 | 目标值 |
| 8 | fpoweight | 权重(%) | int4 | 32 |  | √ | 0 | 权重(%) |
| 9 | fposcore | 得分 | numeric | 19 | 6 | √ | 0 | 得分 |
| 10 | fpotargettype | 指标类型 | bpchar | 1 |  | √ | ' ' | 指标类型,枚举: 0 :计算指标 1 :综合指标 |
| 11 | fpoactual | 实际值 | numeric | 19 | 6 | √ | 0 | 实际值 |
| 12 | fpodescription | 得分说明 | varchar | 255 |  | √ | ' ' | 得分说明 |
| 13 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_ssc_emp_po_id |  | fid |
| 2 | pk_t_tk_emp_processoperation |  | fentryid |

---

## 客户满意单据体-子表 t_tk_emp_customerpleased

- **表名称：** 客户满意单据体-子表
- **表名：** t_tk_emp_customerpleased

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fcpachieveid | 绩效指标 | int8 | 64 |  | √ | 0 | [绩效指标 ssc_achievetarget](../som_files/ssc_achievetarget.md) |
| 3 | fcpstandard | 基准值 | numeric | 19 | 6 | √ | 0 | 基准值 |
| 4 | fcpactual | 实际值 | numeric | 19 | 6 | √ | 0 | 实际值 |
| 5 | fcpweight | 权重(%) | int4 | 32 |  | √ | 0 | 权重(%) |
| 6 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 7 | fcpunitid | 单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 8 | fcpapproved | 核定值 | numeric | 19 | 6 | √ | 0 | 核定值 |
| 9 | fpoweight | fpoweight | int4 | 32 |  | √ | 0 |  |
| 10 | fcptarget | 目标值 | numeric | 19 | 6 | √ | 0 | 目标值 |
| 11 | fpodescription | fpodescription | varchar | 255 |  | √ | ' ' |  |
| 12 | fcptargettype | 指标类型 | bpchar | 1 |  | √ | ' ' | 指标类型,枚举: 0 :计算指标 1 :综合指标 |
| 13 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 14 | fcpscore | 得分 | numeric | 19 | 6 | √ | 0 | 得分 |
| 15 | fcpdescription | 得分说明 | varchar | 255 |  | √ | ' ' | 得分说明 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_tk_emp_customerpleased |  | fentryid |
| 2 | idx_ssc_emp_cp_id |  | fid |

---

## 绩效报告-主表 t_tk_empachieverpt

- **表名称：** 绩效报告-主表
- **表名：** t_tk_empachieverpt

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fsscid | 共享中心 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 3 | fname | 名称 | varchar | 50 |  | √ | ' ' | 名称 |
| 4 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 5 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 6 | fextrapoint | 额外加减分 | numeric | 19 | 6 | √ | 0 | 额外加减分 |
| 7 | fassessname | 考核对象名称 | varchar | 100 |  | √ | ' ' | 考核对象名称 |
| 8 | fdescription | 说明 | varchar | 1000 |  | √ | ' ' | 说明 |
| 9 | fapplicant | 申请人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 10 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 11 | fstatus | 数据状态 | bpchar | 1 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 12 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 13 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 14 | fexamineeid | 被考核人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 15 | fenable | 使用状态 | bpchar | 1 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 16 | fassessgroupid | 被考核用户组 | int8 | 64 |  | √ | 0 | [用户组 task_usergroup](../ssc_files/task_usergroup.md) |
| 17 | fnumber | 编码 | varchar | 30 |  | √ | ' ' | 编码 |
| 18 | fperiodstart | 考核期间.开始 | timestamp | 0 |  |  | null | 考核期间.开始 |
| 19 | fperiodend | 考核期间.结束 | timestamp | 0 |  |  | null | 考核期间.结束 |
| 20 | fscore | 考核分数 | numeric | 19 | 6 | √ | 0 | 考核分数 |
| 21 | fnextauditor | 当前处理人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 22 | fassessperiod | 考核周期 | bpchar | 1 |  | √ | ' ' | 考核周期,枚举: 1 :月度 2 :季度 3 :半年度 4 :年度 |
| 23 | fassessplanid | 考核方案 | int8 | 64 |  | √ | 0 | [绩效考核方案 ssc_achievescheme](../som_files/ssc_achievescheme.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_ssc_empachieve_rpt_examid |  | fexamineeid,fsscid,fassessplanid,fperiodstart,fperiodend |
| 2 | pk_t_tk_empachieverpt |  | fid |

---

## 绩效报告-多语言表 t_tk_empachieverpt_l

- **表名称：** 绩效报告-多语言表
- **表名：** t_tk_empachieverpt_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 100 |  | √ | ' ' | 名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 32 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_tk_empachieverpt_l |  | fpkid |
| 2 | idx_ssc_empachirpt_locale |  | fid,flocaleid |
