# 映射报表-fsa_rptmappings

## 映射报表-多语言表 t_fsa_rptmappings_l

- **表名称：** 映射报表-多语言表
- **表名：** t_fsa_rptmappings_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 映射报表名称 | varchar | 100 |  | √ | ' ' | 映射报表名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 18 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_fsa_rptmappings_l |  | fpkid |
| 2 | idx_fsa_mapping_l |  | fid |

---

## 映射报表-主表 t_fsa_rptmappings

- **表名称：** 映射报表-主表
- **表名：** t_fsa_rptmappings

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 3 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 4 | fsrcstdrptid | 报表类型 | int8 | 64 |  | √ | 0 | 标准报表 fsa_stdrpts |
| 5 | facctorg | 核算组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 6 | faccounttable | 科目表 | int8 | 64 |  | √ | 0 | 科目表 bd_accounttable |
| 7 | fmappingrpttype | 源报表类型 | bpchar | 1 |  | √ | ' ' | 源报表类型,枚举: 0 :资产负债表 1 :利润表 2 :现金流量表 |
| 8 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 9 | fmappingsrctype | 取数来源 | bpchar | 1 |  | √ | ' ' | 取数来源,枚举: 0 :苍穹总账 1 :苍穹合并报表 |
| 10 | fstatus | 数据状态 | bpchar | 1 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 11 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 12 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 13 | facctperiodtype | 期间类型 | int8 | 64 |  | √ | 0 | 会计日历类型 bd_period_type |
| 14 | fenable | 使用状态 | bpchar | 1 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 15 | fnumber | 映射报表编码 | varchar | 30 |  | √ | ' ' | 映射报表编码 |
| 16 | facctbooktypeid | 账簿类型 | int8 | 64 |  | √ | 0 | 账簿类型 bd_accountbookstype |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_fsa_rptmappings |  | fid |
| 2 | idx_mapping_1 |  | fnumber |
| 3 | idx_mapping_2 |  | fstatus,fmappingsrctype |

---

## 报表映射分录信息-子表 t_fsa_rptmappingent

- **表名称：** 报表映射分录信息-子表
- **表名：** t_fsa_rptmappingent

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fcalcformular_tag | 指标计算公式_详情 | text | 0 |  |  | null | 指标计算公式_详情 |
| 3 | fmappingtype | 目标映射类型 | bpchar | 1 |  | √ | ' ' | 目标映射类型,枚举: 0 :报表项直接映射 1 :公式计算 |
| 4 | fdisplayformular_tag | 指标展示公式_详情 | text | 0 |  |  | null | 指标展示公式_详情 |
| 5 | fdescription_tag | 描述_详情 | text | 0 |  |  | null | 描述_详情 |
| 6 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 7 | fsrcrptitemid | 源报表项ID | int8 | 64 |  | √ | 0 | 标准报表项目 fsa_rptitems |
| 8 | fdisplayformular | 指标展示公式 | varchar | 510 |  | √ | ' ' | 指标展示公式 |
| 9 | fcalcformular | 指标计算公式 | varchar | 510 |  | √ | ' ' | 指标计算公式 |
| 10 | fdescription | 描述 | varchar | 510 |  |  | null | 描述 |
| 11 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_fsa_mapping_1 |  | fid |
| 2 | pk_t_fsa_rptmappingent |  | fentryid |
| 3 | idx_fsa_mapping_2 |  | fsrcrptitemid |
| 4 | idx_fsa_mapping_3 |  | fseq |
