# 税码服务结果表-bdtaxr_taxcode_result

## 单据体-子表 t_bdtaxr_taxcode_detail

- **表名称：** 单据体-子表
- **表名：** t_bdtaxr_taxcode_detail

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fintervalstartdate | 区间开始日期 | timestamp | 0 |  |  | null | 区间开始日期 |
| 3 | fintervalenddate | 区间结束日期 | timestamp | 0 |  |  | null | 区间结束日期 |
| 4 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 5 | ftaxbaseamount | 对应税基 | numeric | 23 | 10 | √ | 0 | 对应税基 |
| 6 | ftaxcodetype | 税码结果类型 | int8 | 64 |  | √ | 0 | [税码明细结果类型 bastax_code_detailstype](../bastax_files/bastax_code_detailstype.md) |
| 7 | fresultsource | 结果来源 | varchar | 36 |  | √ | ' ' | [主实体对象 bos_entityobject](../mdl_files/bos_entityobject.md) |
| 8 | fdays | 交集期间天数 | int8 | 64 |  | √ | 0 | 交集期间天数 |
| 9 | fenddate | 失效日期 | timestamp | 0 |  |  | null | 失效日期 |
| 10 | fsumintervalamount | 各区间税额合计 | numeric | 23 | 10 | √ | 0 | 各区间税额合计 |
| 11 | ftaxratetype | 税率类型 | int8 | 64 |  | √ | 0 | [税率类型 bd_taxratetype](../basedata_files/bd_taxratetype.md) |
| 12 | ftotaldays | 总天数 | int8 | 64 |  | √ | 0 | 总天数 |
| 13 | fresultnumber | 结果编码 | varchar | 120 |  | √ | ' ' | 结果编码 |
| 14 | fstartdate | 生效日期 | timestamp | 0 |  |  | null | 生效日期 |
| 15 | fresultname | 结果名称 | varchar | 200 |  | √ | ' ' | 结果名称 |
| 16 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 17 | fproportion | 总天数占比 | numeric | 23 | 10 | √ | 0 | 总天数占比 |
| 18 | fresultid | 结果id | varchar | 200 |  | √ | ' ' | 结果id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_bdtaxr_taxcode_detail_fk |  | fid |
| 2 | pk_bdtaxr_taxcode_detail |  | fentryid |

---

## 子单据体-子表 t_bdtaxr_taxcode_sdetail

- **表名称：** 子单据体-子表
- **表名：** t_bdtaxr_taxcode_sdetail

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fintervalamount | 适用税基 | numeric | 23 | 10 | √ | 0 | 适用税基 |
| 2 | fintervaltaxrate | 适用税率 | numeric | 23 | 10 | √ | 0 | 适用税率 |
| 3 | fintervaltaxamount | 各区间税额 | numeric | 23 | 10 | √ | 0 | 各区间税额 |
| 4 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 5 | fdetailid | fdetailid | int8 | 64 |  | √ | 0 | id |
| 6 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |
| 7 | finterval | 区间 | varchar | 200 |  | √ | ' ' | 区间 |
| 8 | fintervaljson | 区间json | varchar | 255 |  | √ | ' ' | 区间json |
| 9 | fintervaljson_tag | 区间json_详情 | text | 0 |  |  | null | 区间json_详情 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fdetailid | fdetailid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_bdtaxr_taxcode_sdetail |  | fdetailid |
| 2 | idx_bdtaxr_taxcode_sdetail_fk |  | fentryid |

---

## 税码服务结果表-主表 t_bdtaxr_taxcode_result

- **表名称：** 税码服务结果表-主表
- **表名：** t_bdtaxr_taxcode_result

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fdraftid | 底稿编制id | int8 | 64 |  | √ | 0 | 底稿编制id |
| 3 | ftaxamount | 税额 | numeric | 23 | 10 | √ | 0 | 税额 |
| 4 | ftemplateid | 模板id | int8 | 64 |  | √ | 0 | 模板id |
| 5 | forgid | 税务组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 6 | ftaxcode | 税码 | int8 | 64 |  | √ | 0 | [税码 bastax_taxcode](../bastax_files/bastax_taxcode.md) |
| 7 | fskssqq | 所属税期起 | timestamp | 0 |  |  | null | 所属税期起 |
| 8 | fdraftpurpose | 底稿用途 | varchar | 50 |  | √ | ' ' | 底稿用途,枚举: nssb :纳税申报 sjjt :税金计提 |
| 9 | ftaxationsys | 税收制度 | int8 | 64 |  | √ | 0 | [税收制度 bd_taxationsys](../basedata_files/bd_taxationsys.md) |
| 10 | fcreatedate | 创建日期 | timestamp | 0 |  |  | null | 创建日期 |
| 11 | fdatastatus | 数据状态 | varchar | 50 |  | √ | ' ' | 数据状态,枚举: 0 :临时数据 1 :正式数据 |
| 12 | fskssqz | 所属税期止 | timestamp | 0 |  |  | null | 所属税期止 |
| 13 | ftaxareagroup | 税收辖区 | int8 | 64 |  | √ | 0 | [税收辖区 bastax_taxareagroup](../basedata_files/bastax_taxareagroup.md) |
| 14 | freportkey | 报表项key | varchar | 200 |  | √ | ' ' | 报表项key |
| 15 | fcreater | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 16 | ftaxtype | 税种 | int8 | 64 |  | √ | 0 | [税种 bd_taxcategory](../basedata_files/bd_taxcategory.md) |
| 17 | fsplitstartdate | 分割区间开始日期 | timestamp | 0 |  |  | null | 分割区间开始日期 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_bdtaxr_taxcode_result |  | fid |
| 2 | idx_bdtaxr_tcresult_cont |  | forgid,ftemplateid,ftaxationsys,ftaxtype,freportkey |

---

## 单据体-多语言表 t_bdtaxr_taxcode_detail_l

- **表名称：** 单据体-多语言表
- **表名：** t_bdtaxr_taxcode_detail_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 2 | fresultname | 结果名称 | varchar | 200 |  | √ | ' ' | 结果名称 |
| 3 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |
| 4 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_bdtaxr_taxcode_detail_l_0 |  | fentryid,flocaleid |
| 2 | pk_bdtaxr_taxcode_detail_l |  | fpkid |
