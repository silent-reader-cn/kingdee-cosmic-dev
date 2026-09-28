# 业务取数规则（废弃）-fpm_matchrule

## 维度与单据字段映射关系-子表 t_fpm_matchrule_rule

- **表名称：** 维度与单据字段映射关系-子表
- **表名：** t_fpm_matchrule_rule

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fbusinessbillfield | 业务单据字段 | varchar | 50 |  | √ | ' ' | 业务单据字段,枚举: |
| 3 | fmaprelation | 映射关系 | varchar | 50 |  | √ | ' ' | 映射关系,枚举: EQ :等于 IN :包含 |
| 4 | fdimensionmembermap | 维度成员映射 | int8 | 64 |  | √ | 0 | [维度成员映射（废弃） fpm_dimensionmember](../fpm_files/fpm_dimensionmember.md) |
| 5 | fsecondbusinessbill | 辅助业务单据字段 | varchar | 50 |  | √ | ' ' | 辅助业务单据字段,枚举: |
| 6 | fdimensiontype | 维度类别 | varchar | 50 |  | √ | ' ' | 维度类别,枚举: fpm_dimension :维度 fpm_detailplanfields :明细计划字段 |
| 7 | fdimensiondetail | 维度或明细计划字段 | int8 | 64 |  | √ | 0 | 维度（废弃） fpm_dimension |
| 8 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 9 | fmatchprop | 匹配属性 | varchar | 50 |  | √ | ' ' | 匹配属性,枚举: Name :名称 Number :编码 |
| 10 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 11 | fallowempty | 允许结果为空 | bpchar | 1 |  | √ | '0' | 允许结果为空 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_fpm_matchrule_rule_fid |  | fid |
| 2 | pk_t_fpm_matchrule_rule |  | fentryid |

---

## 业务取数规则（废弃）-多语言表 t_fpm_matchrule_l

- **表名称：** 业务取数规则（废弃）-多语言表
- **表名：** t_fpm_matchrule_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 规则名称 | varchar | 50 |  | √ | ' ' | 规则名称 |
| 3 | fcomment | 备注 | varchar | 255 |  | √ | ' ' | 备注 |
| 4 | flocaleid | flocaleid | varchar | 50 |  | √ | ' ' | localeid |
| 5 | fpkid | fpkid | bpchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_fpm_matchrule_l |  | fid |
| 2 | pk_t_fpm_matchrule_l |  | fpkid |

---

## 业务取数规则（废弃）-主表 t_fpm_matchrule

- **表名称：** 业务取数规则（废弃）-主表
- **表名：** t_fpm_matchrule

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmodifierid | 最后更新人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 3 | ffetchpurpose | 取数用途 | varchar | 50 |  | √ | 'ExecuteControl' | 取数用途,枚举: ExecuteControl :执行与控制取数 PlanReport :计划编制取数 |
| 4 | fabnormalcondition | 例外条件 | varchar | 1024 |  | √ | ' ' | 例外条件 |
| 5 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 6 | flinkentity | 取数关联实体 | varchar | 50 |  | √ | ' ' | 取数关联实体,枚举: |
| 7 | fenabledate | 启用日期 | timestamp | 0 |  |  | null | 启用日期 |
| 8 | fdisabledate | 禁用日期 | timestamp | 0 |  |  | null | 禁用日期 |
| 9 | fdisablerid | 禁用人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 10 | fabnormalconditionreal_tag | 例外条件(存储)_详情 | text | 0 |  |  | null | 例外条件(存储)_详情 |
| 11 | fbusinessbill | 业务单据 | varchar | 50 |  | √ | ' ' | [主实体对象 bos_entityobject](../mdl_files/bos_entityobject.md) |
| 12 | fapplyconditionreal_tag | 适用条件(存储)_详情 | text | 0 |  |  | null | 适用条件(存储)_详情 |
| 13 | fmodifytime | 最后更新时间 | timestamp | 0 |  |  | null | 最后更新时间 |
| 14 | fapplycondition | 适用条件 | varchar | 1024 |  | √ | ' ' | 适用条件 |
| 15 | fstatus | 状态 | bpchar | 5 |  | √ | ' ' | 状态,枚举: A :暂存 B :已提交 C :已审核 |
| 16 | fabnormalconditionreal | 例外条件(存储) | varchar | 255 |  | √ | ' ' | 例外条件(存储) |
| 17 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 18 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 19 | fenable | 使用状态 | bpchar | 1 |  | √ | '1' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 20 | fenablerid | 启用人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 21 | fbodysys | 体系 | int8 | 64 |  | √ | 0 | [体系管理1（废弃） fpm_bodysysmanage](../fpm_files/fpm_bodysysmanage.md) |
| 22 | fnumber | 编码 | varchar | 50 |  | √ | ' ' | 编码 |
| 23 | fapplyconditionreal | 适用条件(存储) | varchar | 255 |  | √ | ' ' | 适用条件(存储) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_fpm_matchrule |  | fnumber |
| 2 | pk_t_fpm_matchrule |  | fid |
