# 取数规则配置-tctsa_tjsjb_rule_config

## 单据体-子表 t_tctsa_tjsjb_access_djt

- **表名称：** 单据体-子表
- **表名：** t_tctsa_tjsjb_access_djt

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fdatasourcetext | 数据源 | text | 0 |  |  | null | 数据源 |
| 3 | frecheck | 是否复合 | varchar | 50 |  | √ | ' ' | 是否复合,枚举: 0 :否 1 :是 |
| 4 | fdatasourcejson | 数据源 | varchar | 510 |  | √ | ' ' | 数据源 |
| 5 | fdatasourcejson_tag | 数据源_详情 | text | 0 |  |  | null | 数据源_详情 |
| 6 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 7 | faccessobject | 取数对象 | varchar | 50 |  | √ | ' ' | 取数对象,枚举: tctb_tjsjb :统计税金表 tctsa_provision_tjsjb :计提表 |
| 8 | faccessfield | 取数字段 | varchar | 50 |  | √ | ' ' | 取数字段,枚举: org :税务组织 type :申报表类型 skssqq :税款所属期起 skssqz :税款所属期止 bqybtse :本期应补（退）税额 taxtype :税种 hsorg :核算组织 fcstaxitems :房产税税目 sbbid :申报表id formno :申报表编号 yhstaxitems :印花税税目 yssr :应税收入 nsrmc :纳税人名称 datatype :数据来源 jmse :减免税额 fsl :税负率 ynse :应纳税额 yzse :预征税额 sjsj :实缴金额 jkdate :缴款时间 |
| 9 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_tctsa_tjsjb_access_djt |  | fentryid |
| 2 | idx_tjsjb_access_djt |  | fid |

---

## 取数规则配置-主表 t_tctsa_tjsjb_rule_config

- **表名称：** 取数规则配置-主表
- **表名：** t_tctsa_tjsjb_rule_config

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fname | 名称 | varchar | 50 |  | √ | ' ' | 名称 |
| 3 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 4 | finvaliddate | 失效日期 | timestamp | 0 |  |  | null | 失效日期 |
| 5 | fbusinesssource | 业务来源 | varchar | 50 |  | √ | ' ' | 业务来源,枚举: 0 :纳税申报 1 :事项填报 2 :计提底稿 3 :税金计提单 4 :海外纳税申报 |
| 6 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 7 | feffectdate | 生效日期 | timestamp | 0 |  |  | null | 生效日期 |
| 8 | fdraftpurpose | 底稿用途 | varchar | 50 |  | √ | ' ' | 底稿用途,枚举: nssb :纳税申报 sjjt :税金计提 |
| 9 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 10 | fyhstaxitems | 税目 | int8 | 64 |  | √ | 0 | 印花税-税目及税率 tpo_tcsd_taxrate |
| 11 | fstatus | 数据状态 | varchar | 50 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 12 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 13 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 14 | ftype | 申报表类型 | varchar | 36 |  | √ | ' ' | [模板类型 tctb_template_type](../tctb_files/tctb_template_type.md) |
| 15 | ftaxareagroup | 税收辖区 | int8 | 64 |  | √ | 0 | [税收辖区 bastax_taxareagroup](../basedata_files/bastax_taxareagroup.md) |
| 16 | ffcstaxitems | 税目 | int8 | 64 |  | √ | 0 | 房产税和城镇土地税-税目及税率 tpo_tcret_taxrate |
| 17 | fenable | 使用状态 | varchar | 50 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 18 | ftaxitemsname | 税目名称 | varchar | 50 |  | √ | ' ' | 税目名称 |
| 19 | fnumber | 编号 | varchar | 30 |  | √ | ' ' | 编号 |
| 20 | ftaxtype | 税种 | int8 | 64 |  | √ | 0 | [税种 bd_taxcategory](../basedata_files/bd_taxcategory.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_tjsjb_rule_config |  | fnumber |
| 2 | pk_tctsa_tjsjb_rule_config |  | fid |

---

## 取数规则配置-多语言表 t_tctsa_tjsjb_rule_config_l

- **表名称：** 取数规则配置-多语言表
- **表名：** t_tctsa_tjsjb_rule_config_l

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
| 1 | pk_tctsa_tjsjb_rule_config_l |  | fpkid |
| 2 | idx_tjsjb_rule_config_l_0 |  | fid,flocaleid |
