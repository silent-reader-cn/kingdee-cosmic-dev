# 全局方案表单-globalscheme_form

## 全局方案表单-主表 t_meta_formdesign

- **表名称：** 全局方案表单-主表
- **表名：** t_meta_formdesign

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | varchar | 36 |  | √ | ' ' |  |
| 2 | fmodifierid | fmodifierid | varchar | 36 |  | √ | ' ' |  |
| 3 | fsubsysid | fsubsysid | int8 | 64 |  | √ | 0 |  |
| 4 | fisinherit | fisinherit | bpchar | 1 |  | √ | '1' |  |
| 5 | fmodeltype | 类型 | varchar | 50 |  | √ | ' ' | 类型,枚举: BillFormModel :单据 BaseFormModel :基础资料 ReportFormModel :报表 DynamicFormModel :动态表单 QueryListModel :查询 MobileFormModel :移动表单 BalanceModel :余额模型 LogBillFormModel :日志表单 |
| 6 | fparentid | fparentid | varchar | 36 |  | √ | ' ' |  |
| 7 | fisv | fisv | varchar | 50 |  | √ | ' ' |  |
| 8 | finheritpath | finheritpath | varchar | 300 |  | √ | ' ' |  |
| 9 | fbizappid | 应用 | varchar | 36 |  | √ | ' ' | [业务应用实体 bos_devportal_bizapp](../mdl_files/bos_devportal_bizapp.md) |
| 10 | fcreatedate | fcreatedate | timestamp | 0 |  |  | LOCALTIMESTAMP |  |
| 11 | fmasterid | fmasterid | varchar | 36 |  | √ | ' ' |  |
| 12 | ftype | ftype | bpchar | 1 |  | √ | '0' |  |
| 13 | fmodifydate | fmodifydate | timestamp | 0 |  |  | null |  |
| 14 | fisextended | fisextended | bpchar | 1 |  | √ | '1' |  |
| 15 | fnumber | 编码 | varchar | 36 |  | √ | ' ' | 编码 |
| 16 | fisvsign | fisvsign | varchar | 255 |  | √ | ' ' |  |
| 17 | fentityid | 实体 | varchar | 36 |  | √ | ' ' | 实体 |
| 18 | ftimestamp | ftimestamp | int8 | 64 |  | √ | 0 |  |
| 19 | fdata | fdata | text | 0 |  |  | null |  |
| 20 | findustry | findustry | int8 | 64 |  | √ | 0 |  |
| 21 | fenabled | fenabled | bpchar | 1 |  | √ | '1' |  |
| 22 | fistemplate | fistemplate | bpchar | 1 |  | √ | '0' |  |
| 23 | fversion | fversion | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_meta_formdesign_fnumber_key |  | fnumber |
| 2 | t_meta_formdesign_pkey |  | fid |
| 3 | idx_meta_formdesign_masterid |  | fmasterid |

---

## 全局方案表单-多语言表 t_meta_formdesign_l

- **表名称：** 全局方案表单-多语言表
- **表名：** t_meta_formdesign_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | varchar | 36 |  | √ | ' ' |  |
| 2 | fname | 名称 | varchar | 200 |  | √ | ' ' | 名称 |
| 3 | fnumber | fnumber | varchar | 36 |  | √ | ' ' |  |
| 4 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 5 | fdata | fdata | text | 0 |  |  | null |  |
| 6 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |
| 7 | fversion | fversion | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_meta_formdsgn_l_number |  | fnumber,flocaleid |
| 2 | idx_meta_formdsgn_l_fid |  | fid,flocaleid |
| 3 | t_meta_formdesign_l_pkey |  | fpkid |
| 4 | t_meta_formdesign_l_fnumber_flocaleid_key |  | fnumber,flocaleid |
| 5 | t_meta_formdesign_l_fid_flocaleid_key |  | fid,flocaleid |
