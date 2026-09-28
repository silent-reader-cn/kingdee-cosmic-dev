# 存贷款产品维护-ifm_ldproduct

## 存贷款产品维护-分表 t_cfm_financingvarieties_p

- **表名称：** 存贷款产品维护-分表
- **表名：** t_cfm_financingvarieties_p

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | ffloatrate | 浮动利率 | bpchar | 1 |  | √ | '0' | 浮动利率 |
| 3 | fcategory | 类别 | varchar | 80 |  | √ | ' ' | 类别,枚举: C :定期存款 D :通知存款 E :短期贷款 F :中长期贷款 G :长期贷款 |
| 4 | fratesignbp | 利率浮动基点（BP） | varchar | 80 |  | √ | ' ' | 利率浮动基点（BP）,枚举: add :加 subtract :减 |
| 5 | freferrateid | 参考利率 | int8 | 64 |  | √ | 0 | [参考利率表 tbd_referrate](../fbd_files/tbd_referrate.md) |
| 6 | frateproductid | 参考利率 | int8 | 64 |  | √ | 0 | [参考利率表 tbd_referrate](../fbd_files/tbd_referrate.md) |
| 7 | fservicecategory | 金融服务项目 | varchar | 80 |  | √ | ' ' | 金融服务项目,枚举: B :贷款 A :定期存款 C :通知存款 |
| 8 | fbiztype | fbiztype | varchar | 80 |  | √ | ' ' |  |
| 9 | fratefloatpoints | 整数 | int8 | 64 |  | √ | 0 | 整数 |
| 10 | feffectivedate | 制单日期 | timestamp | 0 |  |  | null | 制单日期 |
| 11 | fproductterm | 产品期限 | varchar | 80 |  | √ | ' ' | 产品期限,枚举: - :活期 on :O/N day :1D week :1W twoWeek :2W threeWeek :3W month :1M twoMonth :2M season :3M fourMonth :4M fiveMonth :5M hyear :6M sevenMonth :7M eightMonth :8M nineMonth :9M tenMonth :10M elevenMonth :11M oneYear :1Y twoYear :2Y threeYear :3Y fourYear :4Y fiveYear :5Y |
| 12 | ffloatpoints | 利率浮动点数（BP） | int8 | 64 |  | √ | 0 | 利率浮动点数（BP） |
| 13 | frateprice | 利率挂牌价格(%) | varchar | 80 |  | √ | ' ' | 利率挂牌价格(%) |
| 14 | fbasis | 利率转换天数 | varchar | 80 |  | √ | ' ' | 利率转换天数,枚举: Actual_360 :360 Actual_365 :365 |
| 15 | fproductprice | 利率挂牌价格% | varchar | 80 |  | √ | ' ' | 利率挂牌价格% |
| 16 | fcurrencyid | 币种 | int8 | 64 |  | √ | 0 | [币种 bd_currency](../base_files/bd_currency.md) |
| 17 | fratesign | 利率浮动基点（BP） | varchar | 80 |  | √ | ' ' | 利率浮动基点（BP）,枚举: add :加 subtract :减 |
| 18 | fratetype | 利率类型 | varchar | 30 |  | √ | ' ' | 利率类型,枚举: fixed :固定利率 float :浮动利率 agree :协议利率 |
| 19 | fpricenum | 利率挂牌价格% | numeric | 23 | 10 | √ | 0 | 利率挂牌价格% |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_cfm_financingvarieties_p |  | fcategory |
| 2 | pk_t_cfm_financingvarieties_p |  | fid |

---

## 存贷款产品维护-多语言表 t_cfm_financingvarieties_l

- **表名称：** 存贷款产品维护-多语言表
- **表名：** t_cfm_financingvarieties_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 产品名称 | varchar | 255 |  | √ | ' ' | 产品名称 |
| 3 | fcomment | 备注 | varchar | 255 |  | √ | ' ' | 备注 |
| 4 | ffullname | ffullname | varchar | 255 |  | √ | ' ' |  |
| 5 | flocaleid | flocaleid | varchar | 30 |  | √ | ' ' | localeid |
| 6 | fpkid | fpkid | varchar | 30 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_cfm_financingvarieties_l_pkey |  | fpkid |
| 2 | idx_t_cfm_financingvarieties_l |  | fid,flocaleid |

---

## 存贷款产品维护-主表 t_cfm_financingvarieties

- **表名称：** 存贷款产品维护-主表
- **表名：** t_cfm_financingvarieties

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fiswtdk | fiswtdk | bpchar | 1 |  | √ | '0' |  |
| 3 | fisleaf | fisleaf | bpchar | 1 |  | √ | '1' |  |
| 4 | fdescrible | 描述 | varchar | 255 |  | √ | ' ' | 描述 |
| 5 | fdisabledate | 禁用日期 | timestamp | 0 |  |  | null | 禁用日期 |
| 6 | fispreset | fispreset | bpchar | 1 |  | √ | '0' |  |
| 7 | fmodifytime | 最后更新时间 | timestamp | 0 |  |  | null | 最后更新时间 |
| 8 | fstatus | 数据状态 | varchar | 30 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 9 | fcredittype | 授信类别 | int8 | 64 |  | √ | 0 | [授信类别 cfm_credittype](../creditm_files/cfm_credittype.md) |
| 10 | fbiztype | 业务种类 | varchar | 80 |  | √ | ' ' | 业务种类,枚举: cfm :融资品种 ifm :存贷款产品 |
| 11 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 12 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 13 | fenablerid | 启用人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 14 | ffinsource | ffinsource | varchar | 30 |  | √ | ' ' |  |
| 15 | fmodifierid | 最后更新人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 16 | fname | 产品名称 | varchar | 255 |  | √ | ' ' | 产品名称 |
| 17 | fcenterid | 结算中心 | int8 | 64 |  | √ | 0 | [金融机构 bd_finorginfo](../basedata_files/bd_finorginfo.md) |
| 18 | floanterm | floanterm | varchar | 50 |  | √ | ' ' |  |
| 19 | fparentid | fparentid | int8 | 64 |  | √ | 0 |  |
| 20 | fcomment | fcomment | varchar | 255 |  | √ | ' ' |  |
| 21 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 22 | ffullname | ffullname | varchar | 255 |  | √ | ' ' |  |
| 23 | flongnumber | flongnumber | varchar | 80 |  | √ | ' ' |  |
| 24 | fenabledate | 启用日期 | timestamp | 0 |  |  | null | 启用日期 |
| 25 | fdisablerid | 禁用人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 26 | flevel | flevel | int8 | 64 |  | √ | 0 |  |
| 27 | fenable | 使用状态 | varchar | 30 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 28 | fnumber | 产品编码 | varchar | 80 |  | √ | ' ' | 产品编码 |
| 29 | fcreditratio | fcreditratio | int4 | 32 |  | √ | 0 |  |
| 30 | fperpetualbond | fperpetualbond | bpchar | 1 |  | √ | '0' |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_cfm_financingvarieties_pkey |  | fid |
| 2 | idx_t_cfm_finvarieties_se |  | fstatus,fenable |
