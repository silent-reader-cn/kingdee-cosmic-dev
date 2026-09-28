# 财报指标库-dfa_quota_info

## 上级指标(归因)-多选基础资料表 t_dfa_dupont_quota

- **表名称：** 上级指标(归因)-多选基础资料表
- **表名：** t_dfa_dupont_quota

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fbasedataid | fbasedataid | int8 | 64 |  | √ | 0 | [财报指标库 dfa_quota_info](../dfa_files/dfa_quota_info.md) |
| 3 | fpkid | fpkid | int8 | 64 |  | √ | 0 | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_dfa_dupont_quota_fk |  | fid |
| 2 | pk_dfa_dupont_quota |  | fpkid |

---

## 财报指标库-主表 t_dfa_quota_info

- **表名称：** 财报指标库-主表
- **表名：** t_dfa_quota_info

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fgroupid | 分组 | int8 | 64 |  | √ | 0 | [财报指标分类目录 dfa_quota_type](../dfa_files/dfa_quota_type.md) |
| 3 | fbelongingindicatzjtx | fbelongingindicatzjtx | int8 | 64 |  | √ | 0 |  |
| 4 | fmodifytime1 | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 5 | fquotaapply | fquotaapply | varchar | 50 |  | √ | ' ' |  |
| 6 | fcalculationbasis | 计算依据 | varchar | 50 |  | √ | ' ' | 计算依据,枚举: 0 :标准报表项目 3 :财报指标 4 :对标业务模板 5 :全部 |
| 7 | fclassificationindicatiba | fclassificationindicatiba | varchar | 50 |  | √ | ' ' |  |
| 8 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 9 | foperationtype | foperationtype | varchar | 50 |  | √ | ' ' |  |
| 10 | fformularule | 表达式 | varchar | 500 |  | √ | ' ' | 表达式 |
| 11 | fisportraitmeterhead | fisportraitmeterhead | bpchar | 1 |  | √ | '0' |  |
| 12 | fcreatetime1 | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 13 | fisportraittrendchart | fisportraittrendchart | bpchar | 1 |  | √ | '0' |  |
| 14 | findicatorscenario | findicatorscenario | varchar | 50 |  | √ | ' ' |  |
| 15 | fbelongingindicatcfa | fbelongingindicatcfa | int8 | 64 |  | √ | 0 |  |
| 16 | fname | 指标名称 | varchar | 50 |  |  | ' ' | 指标名称 |
| 17 | fclassificationindicatzjtx | fclassificationindicatzjtx | varchar | 50 |  | √ | ' ' |  |
| 18 | ffourclassification | ffourclassification | varchar | 50 |  | √ | ' ' |  |
| 19 | fsecondbasicdata | 二级分类基础资料 | int8 | 64 |  | √ | 0 | [财报指标分类目录 dfa_quota_type](../dfa_files/dfa_quota_type.md) |
| 20 | fdidcquota | fdidcquota | int8 | 64 |  | √ | 0 |  |
| 21 | fvaluetype | 值类型 | varchar | 50 |  | √ | ' ' | 值类型,枚举: 0 :文本 1 :布尔值 2 :数值 3 :小数 4 :整数 5 :日期 6 :长日期 |
| 22 | fnotcalculate | 不计算情形 | varchar | 50 |  | √ | ' ' | 不计算情形,枚举: 0 :分母为0 2 :分母为负数 1 :分子为负数 |
| 23 | fisenable | 启用 | bpchar | 1 |  | √ | '1' | 启用 |
| 24 | fbelongingindicatiba | fbelongingindicatiba | int8 | 64 |  | √ | 0 |  |
| 25 | frptgroup | frptgroup | varchar | 50 |  | √ | ' ' |  |
| 26 | fenable | 使用状态 | varchar | 50 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 27 | fformulatranslation | 表达式描述 | varchar | 255 |  |  | ' ' | 表达式描述 |
| 28 | fproject | fproject | int8 | 64 |  | √ | 0 |  |
| 29 | fnumber | 编码 | varchar | 30 |  | √ | ' ' | 编码 |
| 30 | fisindustryranking | fisindustryranking | bpchar | 1 |  | √ | '0' |  |
| 31 | ftranexpression | 表达式译文 | varchar | 500 |  | √ | ' ' | 表达式译文 |
| 32 | fisdefault | 系统预设 | bpchar | 1 |  | √ | '1' | 系统预设 |
| 33 | fmodeltype | fmodeltype | varchar | 50 |  | √ | ' ' |  |
| 34 | findustryaverage | findustryaverage | varchar | 50 |  | √ | ' ' |  |
| 35 | fbusinessrelation | 业务相关性 | varchar | 50 |  | √ | ' ' | 业务相关性,枚举: 0 :正相关 1 :负相关 |
| 36 | fformulatranslation_tag | 表达式描述_详情 | text | 0 |  |  | null | 表达式描述_详情 |
| 37 | fsinglequarter | 是否单期间指标 | varchar | 50 |  | √ | ' ' | 是否单期间指标,枚举: 0 :是 1 :否 |
| 38 | fstatus | 数据状态 | varchar | 50 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 39 | fstatisticalmethod | fstatisticalmethod | varchar | 50 |  | √ | ' ' |  |
| 40 | fishardindicators | fishardindicators | varchar | 50 |  | √ | ' ' |  |
| 41 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 42 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 43 | fcreater | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 44 | fsecondclassification | 二级分类 | varchar | 50 |  | √ | ' ' | 二级分类 |
| 45 | findicatormeaning | 指标含义 | varchar | 500 |  |  | ' ' | 指标含义 |
| 46 | ffourbasicdata | ffourbasicdata | int8 | 64 |  | √ | 0 |  |
| 47 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 48 | fcompindicators | 关联大陆上市公司指标 | int8 | 64 |  | √ | 0 | [全球股票指标 global_stock_metric](../dfa_files/global_stock_metric.md) |
| 49 | ffirstclassification | 一级分类 | varchar | 50 |  | √ | ' ' | 一级分类 |
| 50 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 51 | freportvaluetype | freportvaluetype | varchar | 50 |  | √ | ' ' |  |
| 52 | fmodifier1 | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 53 | fshowrow | 显示顺序 | int8 | 64 |  | √ | 0 | 显示顺序 |
| 54 | ffirstbasicdata | 一级分类基础资料 | int8 | 64 |  | √ | 0 | [财报指标分类目录 dfa_quota_type](../dfa_files/dfa_quota_type.md) |
| 55 | fdatasources | 数据来源 | varchar | 50 |  | √ | ' ' | 数据来源,枚举: 0 :公式计算 1 :大数据库 2 :公式计算、大数据库 3 :其他 |
| 56 | faccuracy | 显示精度 | varchar | 50 |  | √ | ' ' | 显示精度,枚举: 0 :0位小数 1 :2位小数 |
| 57 | foscompindicators | 关联海外上市公司指标 | int8 | 64 |  | √ | 0 | [全球股票指标 global_stock_metric](../dfa_files/global_stock_metric.md) |
| 58 | fisindustryprosperity | fisindustryprosperity | bpchar | 1 |  | √ | '0' |  |
| 59 | fthirdclassification | 三级分类 | varchar | 50 |  | √ | ' ' | 三级分类 |
| 60 | fmetadatacode | fmetadatacode | varchar | 50 |  | √ | ' ' |  |
| 61 | fshowname | 指标显示名称 | varchar | 50 |  |  | ' ' | 指标显示名称 |
| 62 | fisportraittrendchartyoy | fisportraittrendchartyoy | bpchar | 1 |  | √ | '0' |  |
| 63 | fyear | 参数N | int8 | 64 |  |  | null | 参数N |
| 64 | fadapttoroles | fadapttoroles | varchar | 50 |  | √ | ' ' |  |
| 65 | fclassificationindicatcfa | fclassificationindicatcfa | varchar | 50 |  | √ | ' ' |  |
| 66 | funits | 单位 | varchar | 50 |  | √ | ' ' | 单位,枚举: 0 :% 1 :元 2 :天 3 :次 4 :无 5 :个 6 :元/人 7 :年 8 :倍 |
| 67 | fthirdbasicdata | 三级分类基础资料 | int8 | 64 |  | √ | 0 | [财报指标分类目录 dfa_quota_type](../dfa_files/dfa_quota_type.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_dfa_quota_info |  | fid |
| 2 | idx_dfa_quota_info_m0 |  | fmasterid |

---

## 财报指标库-多语言表 t_dfa_quota_info_l

- **表名称：** 财报指标库-多语言表
- **表名：** t_dfa_quota_info_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 指标名称 | varchar | 80 |  |  | ' ' | 指标名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_dfa_quota_info_l_0 |  | fid,flocaleid |
| 2 | pk_dfa_quota_info_l |  | fpkid |
