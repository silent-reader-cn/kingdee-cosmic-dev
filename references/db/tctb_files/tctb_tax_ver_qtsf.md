# 其他税费税种版本详情-tctb_tax_ver_qtsf

## 其他税费版本单据体-子表 t_tctb_tax_ver_qtsf_e

- **表名称：** 其他税费版本单据体-子表
- **表名：** t_tctb_tax_ver_qtsf_e

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | ftaxperiod | 缴纳期限 | varchar | 50 |  | √ | ' ' | 缴纳期限,枚举: month :月 season :季 halfyear :半年 year :年 count :次 |
| 3 | famountrate | 费率 | numeric | 23 | 10 | √ | 0 | 费率 |
| 4 | feffectiveend | 有效期止 | timestamp | 0 |  |  | null | 有效期止 |
| 5 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 6 | fcollectsubrate | 征收子目（旧） | varchar | 50 |  | √ | ' ' | 征收子目（旧） |
| 7 | feffectivestart | 有效期起 | timestamp | 0 |  |  | null | 有效期起 |
| 8 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 9 | fcollectrate | 征收品目 | int8 | 64 |  | √ | 0 | 征收品目 tpo_zspm |
| 10 | fcollectitem | 征收子目 | int8 | 64 |  | √ | 0 | 业务定义分录 tpo_tysbsf_bizdef_entry |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_tctb_tax_ver_qtsf_e_fk |  | fid |
| 2 | pk_tctb_tax_ver_qtsf_e |  | fentryid |

---

## 其他税费税种版本详情-主表 t_tctb_tax_ver_qtsf

- **表名称：** 其他税费税种版本详情-主表
- **表名：** t_tctb_tax_ver_qtsf

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmodifydate | 修改日期 | timestamp | 0 |  |  | null | 修改日期 |
| 3 | fmodifier | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 4 | fenable | 启用状态 | varchar | 50 |  | √ | ' ' | 启用状态,枚举: 1 :启用 0 :禁用 |
| 5 | ftaxtype | 税种 | varchar | 50 |  | √ | ' ' | 税种,枚举: zzs :增值税 qysds :企业所得税 yhs :印花税 fjsf :附加税费 fcscztdsys :房产税和城镇土地使用税 xfs :消费税 qtsf :其他税费 hjbhs :环境保护税 |
| 6 | fver | 版本 | int8 | 64 |  | √ | 0 | 版本 |
| 7 | forg | 组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_tctb_tax_ver_qtsf |  | fid |
| 2 | idx_tctb_qtsf_org |  | forg,ftaxtype |
