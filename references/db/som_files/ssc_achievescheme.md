# 绩效考核方案-ssc_achievescheme

## 员工-多选基础资料表 t_tk_achieveuser

- **表名称：** 员工-多选基础资料表
- **表名：** t_tk_achieveuser

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fbasedataid | fbasedataid | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 3 | fpkid | fpkid | int8 | 64 |  | √ | 0 | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_tk_achieveuser_pk |  | fbasedataid |
| 2 | pk_t_tk_achieveuser |  | fpkid |
| 3 | idx_tk_achieveuser_fk |  | fid |

---

## 成本控制单据体-子表 t_tk_costcontrol

- **表名称：** 成本控制单据体-子表
- **表名：** t_tk_costcontrol

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fccdescription | 备注 | varchar | 255 |  | √ | ' ' | 备注 |
| 3 | fcctarget | 目标值 | numeric | 19 | 6 | √ | 0 | 目标值 |
| 4 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 5 | fcctargettype | 指标类型 | bpchar | 1 |  | √ | ' ' | 指标类型,枚举: 0 :计算指标 1 :综合指标 |
| 6 | fccstandard | 基准值 | numeric | 19 | 6 | √ | 0 | 基准值 |
| 7 | fccachieveid | 绩效指标 | int8 | 64 |  | √ | 0 | [绩效指标 ssc_achievetarget](../som_files/ssc_achievetarget.md) |
| 8 | fccweight | 指标权重(%) | int4 | 32 |  | √ | 0 | 指标权重(%) |
| 9 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 10 | fccunitid | 单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_ssc_costcontrol_id |  | fid |
| 2 | pk_t_tk_costcontrol |  | fentryid |

---

## 客户满意单据体-子表 t_tk_customerpleased

- **表名称：** 客户满意单据体-子表
- **表名：** t_tk_customerpleased

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fcpachieveid | 绩效指标 | int8 | 64 |  | √ | 0 | [绩效指标 ssc_achievetarget](../som_files/ssc_achievetarget.md) |
| 3 | fcpstandard | 基准值 | numeric | 19 | 6 | √ | 0 | 基准值 |
| 4 | fcptarget | 目标值 | numeric | 19 | 6 | √ | 0 | 目标值 |
| 5 | fcpweight | 指标权重(%) | int4 | 32 |  | √ | 0 | 指标权重(%) |
| 6 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 7 | fcptargettype | 指标类型 | bpchar | 1 |  | √ | ' ' | 指标类型,枚举: 0 :计算指标 1 :综合指标 |
| 8 | fcpunitid | 单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 9 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 10 | fcpdescription | 备注 | varchar | 255 |  | √ | ' ' | 备注 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_ssc_customerpleased_id |  | fid |
| 2 | pk_t_tk_customerpleased |  | fentryid |

---

## 角色-多选基础资料表 t_tk_achieverole

- **表名称：** 角色-多选基础资料表
- **表名：** t_tk_achieverole

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fbasedataid | fbasedataid | int8 | 64 |  | √ | 0 | [通用角色 perm_role](../base_files/perm_role.md) |
| 3 | fpkid | fpkid | int8 | 64 |  | √ | 0 | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_tk_achieverole |  | fpkid |
| 2 | idx_tk_achieverole_pk |  | fbasedataid |
| 3 | idx_tk_achieverole_fk |  | fid |

---

## 用户组-多选基础资料表 t_tk_achievegroup

- **表名称：** 用户组-多选基础资料表
- **表名：** t_tk_achievegroup

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fbasedataid | fbasedataid | int8 | 64 |  | √ | 0 | [用户组 task_usergroup](../ssc_files/task_usergroup.md) |
| 3 | fpkid | fpkid | int8 | 64 |  | √ | 0 | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_tk_achievegroup_pk |  | fbasedataid |
| 2 | idx_tk_achievegroup_fk |  | fid |
| 3 | pk_t_tk_achievegroup |  | fpkid |

---

## 流程运营单据体-子表 t_tk_processoperation

- **表名称：** 流程运营单据体-子表
- **表名：** t_tk_processoperation

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fpoweight | 指标权重(%) | int4 | 32 |  | √ | 0 | 指标权重(%) |
| 3 | fpotargettype | 指标类型 | bpchar | 1 |  | √ | ' ' | 指标类型,枚举: 0 :计算指标 1 :综合指标 |
| 4 | fpounitid | 单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 5 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 6 | fpodescription | 备注 | varchar | 255 |  | √ | ' ' | 备注 |
| 7 | fpostandard | 基准值 | numeric | 19 | 6 | √ | 0 | 基准值 |
| 8 | fpoachieveid | 绩效指标 | int8 | 64 |  | √ | 0 | [绩效指标 ssc_achievetarget](../som_files/ssc_achievetarget.md) |
| 9 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 10 | fpotarget | 目标值 | numeric | 19 | 6 | √ | 0 | 目标值 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_ssc_processoperation_id |  | fid |
| 2 | pk_t_tk_processoperation |  | fentryid |

---

## 绩效考核方案-多语言表 t_tk_achievescheme_l

- **表名称：** 绩效考核方案-多语言表
- **表名：** t_tk_achievescheme_l

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
| 1 | idx_tk_achieve_scheme_locale |  | fid,flocaleid |
| 2 | pk_t_tk_achievescheme_l |  | fpkid |

---

## 学习成长单据体-子表 t_tk_learngrowth

- **表名称：** 学习成长单据体-子表
- **表名：** t_tk_learngrowth

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | flrachieveid | 绩效指标 | int8 | 64 |  | √ | 0 | [绩效指标 ssc_achievetarget](../som_files/ssc_achievetarget.md) |
| 3 | flrdescription | 备注 | varchar | 255 |  | √ | ' ' | 备注 |
| 4 | flrstandard | 基准值 | numeric | 19 | 6 | √ | 0 | 基准值 |
| 5 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 6 | flrtargettype | 指标类型 | bpchar | 1 |  | √ | ' ' | 指标类型,枚举: 0 :计算指标 1 :综合指标 |
| 7 | flrtarget | 目标值 | numeric | 19 | 6 | √ | 0 | 目标值 |
| 8 | flrunitid | 单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 9 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 10 | flrweight | 指标权重(%) | int4 | 32 |  | √ | 0 | 指标权重(%) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_tk_learngrowth |  | fentryid |
| 2 | idx_ssc_learngrowth_id |  | fid |

---

## 绩效考核方案-主表 t_tk_achievescheme

- **表名称：** 绩效考核方案-主表
- **表名：** t_tk_achievescheme

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fsscid | 共享中心 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 3 | fname | 名称 | varchar | 255 |  | √ | ' ' | 名称 |
| 4 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 5 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 6 | fdescription | 说明 | varchar | 255 |  | √ | ' ' | 说明 |
| 7 | faccessname | 考核对象名称 | varchar | 100 |  | √ | ' ' | 考核对象名称 |
| 8 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 9 | fstatus | 数据状态 | varchar | 30 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 10 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 11 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 12 | fenable | 状态 | bpchar | 1 |  | √ | ' ' | 状态,枚举: 0 :禁用 1 :可用 |
| 13 | fnumber | 编码 | varchar | 50 |  | √ | ' ' | 编码 |
| 14 | fassessobject | 考核对象类型 | bpchar | 1 |  | √ | ' ' | 考核对象类型,枚举: 1 :用户组 2 :员工 |
| 15 | fassessperiod | 考核周期 | bpchar | 1 |  | √ | ' ' | 考核周期,枚举: 1 :月度 2 :季度 3 :半年度 4 :年度 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_tk_achieve_scheme_id |  | fnumber |
| 2 | pk_t_tk_achievescheme |  | fid |
