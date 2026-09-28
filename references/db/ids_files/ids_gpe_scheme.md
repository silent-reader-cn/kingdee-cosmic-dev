# 预测模型方案-ids_gpe_scheme

## 预测模型方案-主表 t_ids_gpe_scheme

- **表名称：** 预测模型方案-主表
- **表名：** t_ids_gpe_scheme

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fdimfieldname | 预测对象维度字段 | varchar | 512 |  | √ | ' ' | 预测对象维度字段 |
| 3 | fstatic_reals | 静态数值变量 | varchar | 512 |  | √ | ' ' | 静态数值变量,枚举: |
| 4 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 5 | fstatus | 数据状态 | bpchar | 1 |  | √ | 'A' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 6 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 7 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 8 | fconfig | 方案配置 | varchar | 255 |  | √ | ' ' | 方案配置 |
| 9 | ftime_var_unknown_reals | 时变未知数值变量 | varchar | 512 |  | √ | ' ' | 时变未知数值变量,枚举: |
| 10 | fvalidationlength | 验证集周期数 | int4 | 32 |  | √ | 0 | 验证集周期数 |
| 11 | ftimefieldname | 预测时间字段 | varchar | 100 |  | √ | ' ' | 预测时间字段 |
| 12 | fname | 名称 | varchar | 50 |  | √ | ' ' | 名称 |
| 13 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 14 | ftimegranularity | 预测时间粒度 | varchar | 50 |  | √ | ' ' | 预测时间粒度,枚举: fyear :年 fhalf_year :半年 fquarter :季度 fmonth :月 fweek :周 fdate :日 |
| 15 | ffuturedataset | 未来数据集 | int8 | 64 |  | √ | 0 | [数据集 ids_gpe_dataset](../ids_files/ids_gpe_dataset.md) |
| 16 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 17 | ftime_var_unknown_cateory | 时变未知分类变量 | varchar | 512 |  | √ | ' ' | 时变未知分类变量,枚举: |
| 18 | fpredictlength | 预测长度 | int4 | 32 |  | √ | 0 | 预测长度 |
| 19 | fstatic_category | 静态分类变量 | varchar | 512 |  | √ | ' ' | 静态分类变量,枚举: |
| 20 | fpreobjfieldname | 预测对象字段 | varchar | 512 |  | √ | ' ' | 预测对象字段 |
| 21 | fpredictstartdate | 预测起始日期 | timestamp | 0 |  |  | null | 预测起始日期 |
| 22 | fdataset | 数据集 | int8 | 64 |  | √ | 0 | [数据集 ids_gpe_dataset](../ids_files/ids_gpe_dataset.md) |
| 23 | ftime_var_known_reals | 时变已知数值变量 | varchar | 512 |  | √ | ' ' | 时变已知数值变量,枚举: |
| 24 | ftime_var_known_category | 时变已知分类变量 | varchar | 512 |  | √ | ' ' | 时变已知分类变量,枚举: |
| 25 | ftargetfieldname | 预测目标字段 | varchar | 512 |  | √ | ' ' | 预测目标字段 |
| 26 | fconfig_tag | 方案配置_详情 | text | 0 |  |  | null | 方案配置_详情 |
| 27 | fenable | 使用状态 | bpchar | 1 |  | √ | '0' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 28 | falgorithm | 预测算法 | varchar | 2000 |  | √ | ' ' | 预测算法,枚举: arima :ARIMA prophet :Prophet linearregression :LinearRegression xgbregressor :XGBRegressor tft :Temporal Fusion Transformer nhits :N-HiTS |
| 29 | fnumber | 编码 | varchar | 80 |  | √ | ' ' | 编码 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_ids_gpe_scheme_name |  | fname |
| 2 | pk_t_ids_gpe_scheme |  | fid |

---

## 预测模型方案-多语言表 t_ids_gpe_scheme_l

- **表名称：** 预测模型方案-多语言表
- **表名：** t_ids_gpe_scheme_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 50 |  | √ | ' ' | 名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_ids_gpe_scheme_l |  | fpkid |
| 2 | idx_ids_gpe_scheme_l_fname |  | fname |
