# 产品目录-bd_productsummary

## 产品目录-主表 t_bd_productsummary

- **表名称：** 产品目录-主表
- **表名：** t_bd_productsummary

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fhistory_name | 曾用名 | varchar | 255 |  | √ | ' ' | 曾用名 |
| 3 | ffulfillment_center | 履行中心 | varchar | 255 |  | √ | ' ' | 履行中心 |
| 4 | fproduct_code | COA产品编码 | varchar | 255 |  | √ | ' ' | COA产品编码 |
| 5 | fenglish_description | 英文描述 | varchar | 255 |  | √ | ' ' | 英文描述 |
| 6 | fchinese_description | 中文描述 | varchar | 255 |  | √ | ' ' | 中文描述 |
| 7 | fsubstitute_offering | 替代产品 | varchar | 255 |  | √ | ' ' | 替代产品 |
| 8 | fsub_category | Offering子类型 | varchar | 255 |  | √ | ' ' | Offering子类型 |
| 9 | ftl9000 | TL9000 | varchar | 255 |  | √ | ' ' | TL9000 |
| 10 | fmodifytime | 最后更新时间 | timestamp | 0 |  |  | null | 最后更新时间 |
| 11 | foffering_model | 产品型号 | varchar | 255 |  | √ | ' ' | 产品型号 |
| 12 | fchinese_classification_l | 分类标签中文 | varchar | 255 |  | √ | ' ' | 分类标签中文 |
| 13 | fstatus | 数据状态 | varchar | 30 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 14 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 15 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 16 | fcompany_brand | 公司品牌 | varchar | 255 |  | √ | ' ' | 公司品牌 |
| 17 | fproduct_brand | 产品品牌 | varchar | 255 |  | √ | ' ' | 产品品牌 |
| 18 | fproduct_sequence_code | 产品序列号 | varchar | 255 |  | √ | ' ' | 产品序列号 |
| 19 | fproduct_type | 产品类型 | varchar | 255 |  | √ | ' ' | 产品类型 |
| 20 | fecosystem | 生态体系 | varchar | 255 |  | √ | ' ' | 生态体系 |
| 21 | fproduct_lifespan | 产品寿命 | numeric | 23 | 10 | √ | 0.0000000000 | 产品寿命 |
| 22 | fmodifierid | 最后修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 23 | fcategory | 产品类型 | varchar | 10 |  | √ | ' ' | 产品类型,枚举: Offering :Offering |
| 24 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 25 | fproduct_series_symbol | 产品系列标识 | varchar | 255 |  | √ | ' ' | 产品系列标识 |
| 26 | fbenefit_project | 受益项目 | varchar | 255 |  | √ | ' ' | 受益项目 |
| 27 | fexternal_model | 外部型号 | varchar | 255 |  | √ | ' ' | 外部型号 |
| 28 | foffering_source | Offering来源 | varchar | 255 |  | √ | ' ' | Offering来源 |
| 29 | flifecyle | 生命周期 | varchar | 255 |  | √ | ' ' | 生命周期 |
| 30 | fqualified_software | 退税软件 | int8 | 64 |  | √ | 0 | [即征即退软件 bd_levyrefund](../basedata_files/bd_levyrefund.md) |
| 31 | fenglish_classification_l | 分类标签英文 | varchar | 255 |  | √ | ' ' | 分类标签英文 |
| 32 | fmanaged_by_version | 版本管理 | bpchar | 1 |  | √ | '0' | 版本管理 |
| 33 | foffering_category | Offering类型 | varchar | 255 |  | √ | ' ' | Offering类型 |
| 34 | fexposed_to_internet | 互联网联接 | varchar | 255 |  | √ | ' ' | 互联网联接 |
| 35 | fsubstituteofferingdate | 替代产品生效日期 | timestamp | 0 |  |  | null | 替代产品生效日期 |
| 36 | fparent | 父节点 | int8 | 64 |  | √ | 0 | [产品分类 bd_productgroup](../basedata_files/bd_productgroup.md) |
| 37 | fenable | 使用状态 | bpchar | 1 |  | √ | '1' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 38 | fnumber | Offering编码 | varchar | 30 |  | √ | ' ' | Offering编码 |
| 39 | fmanufacturing_entity | 制造主体 | varchar | 255 |  | √ | ' ' | 制造主体 |
| 40 | fname_standard | 命名标准 | varchar | 255 |  | √ | ' ' | 命名标准 |
| 41 | fsolution_type | 解决方案类型 | varchar | 255 |  | √ | ' ' | 解决方案类型 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | ids_t_bd_productsummary_number |  | fnumber |
| 2 | pk_t_bd_productsummary |  | fid |

---

## 产品目录-多语言表 t_bd_productsummary_l

- **表名称：** 产品目录-多语言表
- **表名：** t_bd_productsummary_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | Offering名称 | varchar | 255 |  | √ | ' ' | Offering名称 |
| 3 | fmkt_name | 市场传播名 | varchar | 255 |  | √ | ' ' | 市场传播名 |
| 4 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 5 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_bd_productsummary_l |  | fpkid |
| 2 | idx_t_bd_productsummary_l_fid |  | fid,flocaleid |
