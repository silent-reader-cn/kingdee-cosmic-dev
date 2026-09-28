# 印花税税种版本详情-tctb_tax_ver_yhs

## 印花税版本单据体-子表 t_tctb_tax_ver_yhs_e

- **表名称：** 印花税版本单据体-子表
- **表名：** t_tctb_tax_ver_yhs_e

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fenddate | 核定期限结束日期 | timestamp | 0 |  |  | null | 核定期限结束日期 |
| 3 | fisverify | 是否核定征收 | bpchar | 1 |  | √ | ' ' | 是否核定征收 |
| 4 | fstartdate | 核定期限开始日期 | timestamp | 0 |  |  | null | 核定期限开始日期 |
| 5 | feffectivedate | 有效期起 | timestamp | 0 |  |  | null | 有效期起 |
| 6 | ftaxrateid | 税收品目 | int8 | 64 |  | √ | 0 | 印花税税率 tpo_tcsd_taxrateentry |
| 7 | fperiod | 缴纳期限 | varchar | 50 |  | √ | ' ' | 缴纳期限,枚举: month :月 season :季 halfyear :半年 year :年 |
| 8 | fhdrate | 核定比例 | numeric | 23 | 10 | √ | 0.0000000000 | 核定比例 |
| 9 | fexpirydate | 有效期止 | timestamp | 0 |  |  | null | 有效期止 |
| 10 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 11 | fdeclaretype | 申报期限类型 | varchar | 50 |  | √ | ' ' | 申报期限类型,枚举: aqsb :按期申报 acsb :按次申报 |
| 12 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_tctb_tax_ver_yhs_e |  | fentryid |
| 2 | idx_tctb_tax_ver_yhs_e_fk |  | fid |

---

## 印花税税种版本详情-主表 t_tctb_tax_ver_yhs

- **表名称：** 印花税税种版本详情-主表
- **表名：** t_tctb_tax_ver_yhs

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmodifydate | 修改日期 | timestamp | 0 |  |  | null | 修改日期 |
| 3 | fmodifier | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 4 | fenable | 启用状态 | varchar | 50 |  | √ | ' ' | 启用状态,枚举: 1 :启用 0 :禁用 |
| 5 | ftaxtype | 税种 | varchar | 50 |  | √ | ' ' | 税种,枚举: zzs :增值税 qysds :企业所得税 yhs :印花税 fjsf :附加税费 fcscztdsys :房产税和城镇土地使用税 xfs :消费税 |
| 6 | fver | 版本 | int8 | 64 |  | √ | 0 | 版本 |
| 7 | forg | 组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_tctb_tax_ver_yhs |  | forg |
| 2 | pk_tctb_tax_ver_yhs |  | fid |
