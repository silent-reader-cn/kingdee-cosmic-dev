# 业务对象缓存管理-bos_entityobject_cache

## 业务对象缓存管理-主表 t_meta_mainentityinfo

- **表名称：** 业务对象缓存管理-主表
- **表名：** t_meta_mainentityinfo

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | 编码 | varchar | 36 |  | √ | ' ' | 编码 |
| 2 | fnamefieldkey | fnamefieldkey | varchar | 30 |  | √ | ' ' |  |
| 3 | fnameislocale | fnameislocale | bpchar | 1 |  | √ | '0' |  |
| 4 | fisqinganalysis | 支持轻分析 | bpchar | 1 |  | √ | '1' | 支持轻分析 |
| 5 | fmodeltype | 类型 | varchar | 50 |  | √ | ' ' | 类型,枚举: BillFormModel :单据 BaseFormModel :基础资料 ReportFormModel :报表 DynamicFormModel :动态表单 QueryListModel :查询 MobileFormModel :移动表单 BalanceModel :余额模型 LogBillFormModel :日志表单 KMModel :知识库 ParameterFormModel_application :应用参数 ParameterFormModel_bill :单据参数 ParameterFormModel_public :公共参数 WidgetFormModel :小部件 |
| 6 | fbotp | 单据转换 | bpchar | 1 |  | √ | '0' | 单据转换 |
| 7 | fworkflow | 是否工作流 | bpchar | 1 |  | √ | '0' | 是否工作流 |
| 8 | fenableimport | 允许导入导出 | bpchar | 1 |  | √ | '1' | 允许导入导出 |
| 9 | fenablenameversion | 支持名称版本化 | bpchar | 1 |  | √ | '0' | 支持名称版本化 |
| 10 | fmainorgfieldkey | fmainorgfieldkey | varchar | 30 |  | √ | ' ' |  |
| 11 | fvoucher | 是否凭证 | bpchar | 1 |  | √ | '0' | 是否凭证 |
| 12 | fcodenumber | 支持编码规则 | bpchar | 1 |  | √ | '0' | 支持编码规则 |
| 13 | fnumberfieldkey | fnumberfieldkey | varchar | 30 |  | √ | ' ' |  |
| 14 | fnosearchenabled | fnosearchenabled | bpchar | 1 |  | √ | '0' |  |
| 15 | fdentityid | 实体 | varchar | 36 |  | √ | ' ' | 实体 |
| 16 | fbizappid | 应用 | varchar | 36 |  | √ | ' ' | [业务应用实体 bos_devportal_bizapp](../mdl_files/bos_devportal_bizapp.md) |
| 17 | fappid | fappid | varchar | 50 |  | √ | ' ' |  |
| 18 | fpkfieldtype | 主键字段类型 | int8 | 64 |  | √ | 0 | 主键字段类型 |
| 19 | fpkfieldname | 主键字段名 | varchar | 30 |  | √ | ' ' | 主键字段名 |
| 20 | ftablename | 主表格 | varchar | 30 |  | √ | ' ' | 主表格 |
| 21 | fistemplate | 是否模板 | bpchar | 1 |  | √ | '0' | 是否模板 |
| 22 | fbilltype | 是否单据类型 | bpchar | 1 |  | √ | '0' | 是否单据类型 |
| 23 | fisprint | 支持打印 | bpchar | 1 |  | √ | '0' | 支持打印 |

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

## 业务对象缓存管理-多语言表 t_meta_mainentityinfo_l

- **表名称：** 业务对象缓存管理-多语言表
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
