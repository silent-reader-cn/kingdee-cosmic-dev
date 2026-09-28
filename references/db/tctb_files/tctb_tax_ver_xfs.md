# 消费税税种版本详情-tctb_tax_ver_xfs

## 消费税版本单据体-子表 t_tctb_tax_ver_xfs_e

- **表名称：** 消费税版本单据体-子表
- **表名：** t_tctb_tax_ver_xfs_e

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fenddate | 结束日期 | timestamp | 0 |  |  | null | 结束日期 |
| 3 | ftaxrate | 税种品目 | varchar | 50 |  | √ | ' ' | 税种品目,枚举: |
| 4 | fstartdate | 开始日期 | timestamp | 0 |  |  | null | 开始日期 |
| 5 | fxfstaxitemrate | 税目 | int8 | 64 |  | √ | 0 | 消费税税收分类编码表 tpo_tcct_taxrateentry |
| 6 | fperiod | 缴纳期限 | varchar | 50 |  | √ | ' ' | 缴纳期限,枚举: aysb :按月申报 ajsb :按季申报 |
| 7 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 8 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_tctb_tax_ver_xfs_e |  | fentryid |
| 2 | idx_tctb_tax_ver_xfs_e_fk |  | fid |

---

## 征收环节-多选基础资料表 t_tctb_taxinfo_point_ver

- **表名称：** 征收环节-多选基础资料表
- **表名：** t_tctb_taxinfo_point_ver

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fbasedataid | fbasedataid | int8 | 64 |  | √ | 0 | 征收环节 tctb_taxpoint |
| 2 | fpkid | fpkid | int8 | 64 |  | √ | 0 | pkid |
| 3 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_tctb_taxinfo_point_ver_fk |  | fentryid |
| 2 | pk_tctb_taxinfo_point_ver |  | fpkid |

---

## 消费税税种版本详情-主表 t_tctb_tax_ver_xfs

- **表名称：** 消费税税种版本详情-主表
- **表名：** t_tctb_tax_ver_xfs

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
| 1 | idx_tctb_tax_ver_xfs |  | forg |
| 2 | pk_tctb_tax_ver_xfs |  | fid |
