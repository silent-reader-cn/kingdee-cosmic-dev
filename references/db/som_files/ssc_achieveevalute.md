# 综合绩效评价单-ssc_achieveevalute

## 学习成长单据体-子表 t_tk_eva_learngrowth

- **表名称：** 学习成长单据体-子表
- **表名：** t_tk_eva_learngrowth

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | flrscore | 指标分值 | numeric | 23 | 10 | √ | 0 | 指标分值 |
| 3 | flractual | 实际值 | numeric | 19 | 6 | √ | 0 | 实际值 |
| 4 | flrdescription | 得分说明 | varchar | 255 |  | √ | ' ' | 得分说明 |
| 5 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 6 | flrachieveid | 绩效指标 | int8 | 64 |  | √ | 0 | 绩效指标 ssc_achievetarget |
| 7 | flrstandard | 基准值 | numeric | 19 | 6 | √ | 0 | 基准值 |
| 8 | flrtargettype | 指标类型 | bpchar | 1 |  | √ | ' ' | 指标类型,枚举: 0 :计算指标 1 :综合指标 |
| 9 | flrtarget | 目标值 | numeric | 19 | 6 | √ | 0 | 目标值 |
| 10 | flrapproved | 核定值 | numeric | 19 | 6 | √ | 0 | 核定值 |
| 11 | flrunitid | 单位 | int8 | 64 |  | √ | 0 | 计量单位 bd_measureunits |
| 12 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 13 | flrweight | 权重(%) | int4 | 32 |  | √ | 0 | 权重(%) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_tk_eva_learngrowth |  | fentryid |
| 2 | idx_ssc_eva_lr_id |  | fid |

---

## 成本控制单据体-子表 t_tk_eva_costcontrol

- **表名称：** 成本控制单据体-子表
- **表名：** t_tk_eva_costcontrol

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fccdescription | 得分说明 | varchar | 255 |  | √ | ' ' | 得分说明 |
| 3 | fccactual | 实际值 | numeric | 19 | 6 | √ | 0 | 实际值 |
| 4 | fcctarget | 目标值 | numeric | 19 | 6 | √ | 0 | 目标值 |
| 5 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 6 | fccweight | 权重(%) | int4 | 32 |  | √ | 0 | 权重(%) |
| 7 | fccunitid | 单位 | int8 | 64 |  | √ | 0 | 计量单位 bd_measureunits |
| 8 | fcctargettype | 指标类型 | bpchar | 1 |  | √ | ' ' | 指标类型,枚举: 0 :计算指标 1 :综合指标 |
| 9 | fccstandard | 基准值 | numeric | 19 | 6 | √ | 0 | 基准值 |
| 10 | fccachieveid | 绩效指标 | int8 | 64 |  | √ | 0 | 绩效指标 ssc_achievetarget |
| 11 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 12 | fccapproved | 核定值 | numeric | 19 | 6 | √ | 0 | 核定值 |
| 13 | fccscore | 指标分值 | numeric | 23 | 10 | √ | 0 | 指标分值 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_tk_eva_costcontrol |  | fentryid |
| 2 | idx_ssc_eva_cc_id |  | fid |

---

## 客户满意单据体-子表 t_tk_eva_customerpleased

- **表名称：** 客户满意单据体-子表
- **表名：** t_tk_eva_customerpleased

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fcpachieveid | 绩效指标 | int8 | 64 |  | √ | 0 | 绩效指标 ssc_achievetarget |
| 3 | fcpstandard | 基准值 | numeric | 19 | 6 | √ | 0 | 基准值 |
| 4 | fcpactual | 实际值 | numeric | 19 | 6 | √ | 0 | 实际值 |
| 5 | fcpweight | 权重(%) | int4 | 32 |  | √ | 0 | 权重(%) |
| 6 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 7 | fcpunitid | 单位 | int8 | 64 |  | √ | 0 | 计量单位 bd_measureunits |
| 8 | fcpapproved | 核定值 | numeric | 19 | 6 | √ | 0 | 核定值 |
| 9 | fcptarget | 目标值 | numeric | 19 | 6 | √ | 0 | 目标值 |
| 10 | fcptargettype | 指标类型 | bpchar | 1 |  | √ | ' ' | 指标类型,枚举: 0 :计算指标 1 :综合指标 |
| 11 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 12 | fcpscore | 指标分值 | numeric | 23 | 10 | √ | 0 | 指标分值 |
| 13 | fcpdescription | 得分说明 | varchar | 255 |  | √ | ' ' | 得分说明 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_ssc_eva_cp_id |  | fid |
| 2 | pk_t_tk_eva_customerpleased |  | fentryid |

---

## 综合绩效评价单-主表 t_tk_achieveevalute

- **表名称：** 综合绩效评价单-主表
- **表名：** t_tk_achieveevalute

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fsscid | 共享中心 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 3 | fname | 名称 | varchar | 255 |  | √ | ' ' | 名称 |
| 4 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 5 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 6 | fassessname | 考核对象名称 | varchar | 100 |  | √ | ' ' | 考核对象名称 |
| 7 | fdescription | 备注 | varchar | 1000 |  | √ | ' ' | 备注 |
| 8 | fapplicant | 申请人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 9 | fassessuserid | 考核对象 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 10 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 11 | fstatus | 数据状态 | bpchar | 1 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :审批中 C :审批完成 |
| 12 | fassessroleid | 考核对象 | varchar | 32 |  | √ | ' ' | 通用角色 perm_role |
| 13 | ftotalscore | 加权总分 | numeric | 19 | 6 | √ | 0 | 加权总分 |
| 14 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 15 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 16 | fassessdimension | 考核对象类型 | bpchar | 1 |  | √ | ' ' | 考核对象类型,枚举: 1 :用户组 2 :员工 3 :角色 |
| 17 | fenable | 使用状态 | bpchar | 1 |  | √ | '1' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 18 | fassessgroupid | 考核对象 | int8 | 64 |  | √ | 0 | 用户组 task_usergroup |
| 19 | fnumber | 编码 | varchar | 50 |  | √ | ' ' | 编码 |
| 20 | fperiodstart | 考核期间.开始 | timestamp | 0 |  |  | null | 考核期间.开始 |
| 21 | fperiodend | 考核期间.结束 | timestamp | 0 |  |  | null | 考核期间.结束 |
| 22 | fnextauditor | 当前处理人 | varchar | 50 |  | √ | ' ' | 当前处理人 |
| 23 | fassessplanid | 考核方案 | int8 | 64 |  | √ | 0 | 绩效考核方案 ssc_achievescheme |
| 24 | fassessperiod | 考核周期 | bpchar | 1 |  | √ | ' ' | 考核周期,枚举: 1 :月度 2 :季度 3 :半年度 4 :年度 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_tk_achieveevalute |  | fid |
| 2 | idx_ssc_achieve_evalute |  | fnumber |

---

## 综合绩效评价单-多语言表 t_tk_achieveevalute_l

- **表名称：** 综合绩效评价单-多语言表
- **表名：** t_tk_achieveevalute_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 100 |  | √ | ' ' | 名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_tk_achieve_evalute_locale |  | fid,flocaleid |
| 2 | pk_t_tk_achieveevalute_l |  | fpkid |

---

## 流程运营单据体-子表 t_tk_eva_processoperation

- **表名称：** 流程运营单据体-子表
- **表名：** t_tk_eva_processoperation

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fpounitid | 单位 | int8 | 64 |  | √ | 0 | 计量单位 bd_measureunits |
| 3 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 4 | fpostandard | 基准值 | numeric | 19 | 6 | √ | 0 | 基准值 |
| 5 | fpoachieveid | 绩效指标 | int8 | 64 |  | √ | 0 | 绩效指标 ssc_achievetarget |
| 6 | fpoapproved | 核定值 | numeric | 19 | 6 | √ | 0 | 核定值 |
| 7 | fpotarget | 目标值 | numeric | 19 | 6 | √ | 0 | 目标值 |
| 8 | fpoweight | 权重(%) | int4 | 32 |  | √ | 0 | 权重(%) |
| 9 | fposcore | 指标分值 | numeric | 23 | 10 | √ | 0 | 指标分值 |
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
| 1 | pk_t_tk_eva_processoperation |  | fentryid |
| 2 | idx_ssc_eva_po_id |  | fid |
