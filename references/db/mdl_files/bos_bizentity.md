# 业务对象-bos_bizentity

## 业务对象-主表 t_meta_mainentityinfo

- **表名称：** 业务对象-主表
- **表名：** t_meta_mainentityinfo

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | 编码 | varchar | 36 |  | √ | ' ' | 编码 |
| 2 | fnamefieldkey | fnamefieldkey | varchar | 30 |  | √ | ' ' |  |
| 3 | fnameislocale | fnameislocale | bpchar | 1 |  | √ | '0' |  |
| 4 | fisqinganalysis | fisqinganalysis | bpchar | 1 |  | √ | '1' |  |
| 5 | fmodeltype | 类型 | varchar | 50 |  | √ | ' ' | 类型,枚举: BillFormModel :单据 BaseFormModel :基础资料 |
| 6 | fbotp | fbotp | bpchar | 1 |  | √ | '0' |  |
| 7 | fworkflow | fworkflow | bpchar | 1 |  | √ | '0' |  |
| 8 | fenableimport | fenableimport | bpchar | 1 |  | √ | '1' |  |
| 9 | fenablenameversion | fenablenameversion | bpchar | 1 |  | √ | '0' |  |
| 10 | fmainorgfieldkey | fmainorgfieldkey | varchar | 30 |  | √ | ' ' |  |
| 11 | fvoucher | fvoucher | bpchar | 1 |  | √ | '0' |  |
| 12 | fcodenumber | fcodenumber | bpchar | 1 |  | √ | '0' |  |
| 13 | fnumberfieldkey | fnumberfieldkey | varchar | 30 |  | √ | ' ' |  |
| 14 | fnosearchenabled | fnosearchenabled | bpchar | 1 |  | √ | '0' |  |
| 15 | fdentityid | 实体 | varchar | 36 |  | √ | ' ' | 实体 |
| 16 | fbizappid | 应用 | varchar | 36 |  | √ | ' ' | [业务应用实体 bos_devportal_bizapp](../mdl_files/bos_devportal_bizapp.md) |
| 17 | fappid | fappid | varchar | 50 |  | √ | ' ' |  |
| 18 | fpkfieldtype | fpkfieldtype | int8 | 64 |  | √ | 0 |  |
| 19 | fpkfieldname | fpkfieldname | varchar | 30 |  | √ | ' ' |  |
| 20 | ftablename | ftablename | varchar | 30 |  | √ | ' ' |  |
| 21 | fistemplate | fistemplate | bpchar | 1 |  | √ | '0' |  |
| 22 | fbilltype | fbilltype | bpchar | 1 |  | √ | '0' |  |
| 23 | fisprint | fisprint | bpchar | 1 |  | √ | '0' |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_meta_mainentityinfo_did |  | fdentityid |
| 2 | t_meta_mainentityinfo_pkey |  | fid |

---

## 业务对象-多语言表 t_meta_mainentityinfo_l

- **表名称：** 业务对象-多语言表
- **表名：** t_meta_mainentityinfo_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | varchar | 36 |  | √ | ' ' |  |
| 2 | fname | 名称 | varchar | 200 |  | √ | ' ' | 名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_meta_mainentityinfo_l_pkey |  | fpkid |
| 2 | t_meta_mainentityinfo_l_fid_flocaleid_key |  | fid,flocaleid |
| 3 | idx_meta_mainentinf_l_fid |  | fid,flocaleid |
