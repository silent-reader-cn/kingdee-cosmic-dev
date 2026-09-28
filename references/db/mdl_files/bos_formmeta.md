# 表单元数据-bos_formmeta

## 表单元数据-主表 t_meta_formdesign

- **表名称：** 表单元数据-主表
- **表名：** t_meta_formdesign

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | varchar | 36 |  | √ | ' ' | id |
| 2 | fmodifierid | 修改人id | varchar | 36 |  | √ | ' ' | 修改人id |
| 3 | fsubsysid | fsubsysid | int8 | 64 |  | √ | 0 |  |
| 4 | fisinherit | 是否允许继承 | bpchar | 1 |  | √ | '1' | 是否允许继承 |
| 5 | fmodeltype | 模型类型 | varchar | 50 |  | √ | ' ' | 模型类型,枚举: DynamicFormModel :动态表单 BillFormModel :单据 BaseFormModel :基础资料 PrintModel :打印模板 MobileFormModel :移动表单 MobileBillFormModel :移动单据 WidgetFormModel :小部件 MobileListModel :移动列表 ParameterFormModel :参数 ReportFormModel :报表 BalanceModel :余额表 MobUserGuideFormModel :移动新手向导 QueryListModel :查询模型 ReportQueryListModel :报表数据源 KMModel :知识库模型 |
| 6 | fparentid | 父对象 | varchar | 36 |  | √ | ' ' | [表单元数据 bos_formmeta](../mdl_files/bos_formmeta.md) |
| 7 | fisv | 开发商标识 | varchar | 50 |  | √ | ' ' | 开发商标识 |
| 8 | finheritpath | 继承路径 | varchar | 300 |  | √ | ' ' | 继承路径 |
| 9 | fbizappid | 应用id | varchar | 36 |  | √ | ' ' | 应用id |
| 10 | fcreatedate | 创建日期 | timestamp | 0 |  |  | LOCALTIMESTAMP | 创建日期 |
| 11 | fmasterid | 原页面id | varchar | 36 |  | √ | ' ' | 原页面id |
| 12 | ftype | 表单类型 | bpchar | 1 |  | √ | '0' | 表单类型,枚举: |
| 13 | fmodifydate | 修改日期 | timestamp | 0 |  |  | null | 修改日期 |
| 14 | fisextended | 报表是否允许扩展 | bpchar | 1 |  | √ | '1' | 报表是否允许扩展 |
| 15 | fnumber | 编码 | varchar | 36 |  | √ | ' ' | 编码 |
| 16 | fisvsign | fisvsign | varchar | 255 |  | √ | ' ' |  |
| 17 | fentityid | 实体元数据 | varchar | 36 |  | √ | ' ' | [实体元数据 bos_entitymeta](../mdl_files/bos_entitymeta.md) |
| 18 | ftimestamp | ftimestamp | int8 | 64 |  | √ | 0 |  |
| 19 | fdata | fdata | text | 0 |  |  | null |  |
| 20 | findustry | 行业 | int8 | 64 |  | √ | 0 | [行业信息 bos_devp_industry](../devportal_files/bos_devp_industry.md) |
| 21 | fenabled | 是否启用 | bpchar | 1 |  | √ | '1' | 是否启用 |
| 22 | fistemplate | 模板 | bpchar | 1 |  | √ | '0' | 模板 |
| 23 | fversion | 版本 | int8 | 64 |  | √ | 0 | 版本 |

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

## 表单元数据-多语言表 t_meta_formdesign_l

- **表名称：** 表单元数据-多语言表
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
