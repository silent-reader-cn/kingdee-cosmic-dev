# 数据协同规则-ct_botp_crlist

## 数据协同规则-主表 t_ctbotp_convertrule

- **表名称：** 数据协同规则-主表
- **表名：** t_ctbotp_convertrule

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | 标识 | varchar | 36 |  | √ | ' ' | 标识 |
| 2 | fmodeltype | fmodeltype | varchar | 50 |  | √ | ' ' |  |
| 3 | ftargetdatacenter | ftargetdatacenter | varchar | 50 |  | √ | ' ' |  |
| 4 | ftenantpath | ftenantpath | varchar | 50 |  | √ | ' ' |  |
| 5 | fisv | 开发商标识 | varchar | 50 |  | √ | ' ' | 开发商标识 |
| 6 | fsbizappid | fsbizappid | varchar | 36 |  | √ | ' ' |  |
| 7 | fsourceentityname | 源单名称 | varchar | 204 |  | √ | ' ' | 源单名称 |
| 8 | fbizappid | fbizappid | varchar | 36 |  | √ | ' ' |  |
| 9 | fsourcedatacenter | fsourcedatacenter | varchar | 50 |  | √ | ' ' |  |
| 10 | fcreatedate | 创建日期 | timestamp | 0 |  | √ | LOCALTIMESTAMP | 创建日期 |
| 11 | fmasterid | 原始规则 | varchar | 36 |  | √ | ' ' | [数据协同规则 ct_botp_crlist](../ctsy_files/ct_botp_crlist.md) |
| 12 | fmodifydate | 修改日期 | timestamp | 0 |  |  | null | 修改日期 |
| 13 | ftargettenant | ftargettenant | varchar | 50 |  | √ | ' ' |  |
| 14 | fsourceaccountnumber | fsourceaccountnumber | varchar | 50 |  | √ | ' ' |  |
| 15 | fenabled | fenabled | bpchar | 1 |  | √ | ' ' |  |
| 16 | fdata | fdata | text | 0 |  |  | null |  |
| 17 | fversion | fversion | int8 | 64 |  | √ | 0 |  |
| 18 | fmodifierid | fmodifierid | int8 | 64 |  | √ | 0 |  |
| 19 | fparentid | fparentid | varchar | 36 |  | √ | ' ' |  |
| 20 | ftargetentityname | 目标单名称 | varchar | 204 |  | √ | ' ' | 目标单名称 |
| 21 | fsynctype | 同步类型 | varchar | 50 |  | √ | ' ' | 同步类型,枚举: 0 :正向同步 1 :反向同步 |
| 22 | ftbizappname | 目标单应用 | varchar | 204 |  | √ | ' ' | 目标单应用 |
| 23 | finheritpath | finheritpath | varchar | 300 |  | √ | ' ' |  |
| 24 | ftargetaccountnumber | ftargetaccountnumber | varchar | 50 |  | √ | ' ' |  |
| 25 | fsysstatus | 出厂状态 | bpchar | 1 |  | √ | ' ' | 出厂状态,枚举: 0 :正常 1 :禁用 |
| 26 | ftype | 扩展状态 | bpchar | 1 |  | √ | ' ' | 扩展状态,枚举: 0 :原始规则 1 :派生规则 2 :扩展规则 |
| 27 | fcurrentverid | 当前版本 | int8 | 64 |  | √ | 0 | 当前版本 |
| 28 | ftbizappid | ftbizappid | varchar | 36 |  | √ | ' ' |  |
| 29 | fsourceentitynumber | 源单编码 | varchar | 36 |  | √ | ' ' | 源单编码 |
| 30 | fistemplate | fistemplate | bpchar | 1 |  | √ | '0' |  |
| 31 | fsbizappname | 源单应用 | varchar | 204 |  | √ | ' ' | 源单应用 |
| 32 | ftargetentitynumber | 目标单编码 | varchar | 36 |  | √ | ' ' | 目标单编码 |
| 33 | fisdefault | fisdefault | bpchar | 1 |  | √ | '0' |  |
| 34 | fsourcetenant | fsourcetenant | varchar | 50 |  | √ | ' ' |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_ctbotp_cv_ttenacc |  | ftargettenant,ftargetdatacenter |
| 2 | idx_ctbotp_cv_tentitynumber |  | ftargetentitynumber |
| 3 | idx_ctbotp_cv_sentitynumber |  | fsourceentitynumber |
| 4 | pk_t_ctbotp_convertrule |  | fid |
| 5 | idx_ctbotp_cv_stenacc |  | fsourcetenant,fsourcedatacenter |

---

## 数据协同规则-多语言表 t_ctbotp_convertrule_l

- **表名称：** 数据协同规则-多语言表
- **表名：** t_ctbotp_convertrule_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | varchar | 40 |  | √ | ' ' |  |
| 2 | fname | 名称 | varchar | 204 |  | √ | ' ' | 名称 |
| 3 | ftargetentityname | 目标单名称 | varchar | 204 |  | √ | ' ' | 目标单名称 |
| 4 | ftbizappname | 目标单应用 | varchar | 204 |  | √ | ' ' | 目标单应用 |
| 5 | flocaleid | flocaleid | varchar | 14 |  | √ | ' ' | localeid |
| 6 | fdata | fdata | text | 0 |  |  | null |  |
| 7 | fpkid | fpkid | varchar | 40 |  | √ | ' ' | pkid |
| 8 | fsourceentityname | 源单名称 | varchar | 204 |  | √ | ' ' | 源单名称 |
| 9 | fsbizappname | 源单应用 | varchar | 204 |  | √ | ' ' | 源单应用 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_ctbotp_convertrule_l |  | fpkid |

---

## 数据协同规则-分表 t_ctbotp_convertrule_s

- **表名称：** 数据协同规则-分表
- **表名：** t_ctbotp_convertrule_s

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | varchar | 36 |  | √ | ' ' |  |
| 2 | fsourcedatacenter | 源单租户账套ID | varchar | 50 |  | √ | ' ' | 源单租户账套ID |
| 3 | ftargetdatacenter | 目标单租户账套ID | varchar | 50 |  | √ | ' ' | 目标单租户账套ID |
| 4 | ftenantpath | 租户路线 | varchar | 50 |  | √ | ' ' | 租户路线 |
| 5 | ftargettenant | 目标单租户 | varchar | 50 |  | √ | ' ' | 目标单租户 |
| 6 | fsourceaccountnumber | 源单数据中心 | varchar | 50 |  | √ | ' ' | 源单数据中心 |
| 7 | fenabled | 启用状态 | varchar | 50 |  | √ | ' ' | 启用状态,枚举: 0 :已停用 1 :启用 |
| 8 | ftargetaccountnumber | 目标单数据中心 | varchar | 50 |  | √ | ' ' | 目标单数据中心 |
| 9 | fsourcetenant | 源单租户 | varchar | 50 |  | √ | ' ' | 源单租户 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_ctbotp_convertrule_s |  | fid |
