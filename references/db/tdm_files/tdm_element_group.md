# 元素设置-tdm_element_group

## 元素设置-多语言表 t_tdm_element_info_l

- **表名称：** 元素设置-多语言表
- **表名：** t_tdm_element_info_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 元素名称 | varchar | 500 |  | √ | ' ' | 元素名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 18 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_tdm_element_info_l_0 |  | fid,flocaleid |
| 2 | t_tdm_element_info_l_pkey |  | fpkid |

---

## 元素设置-主表 t_tdm_element_info

- **表名称：** 元素设置-主表
- **表名：** t_tdm_element_info

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fjson | 存储公式 | varchar | 510 |  | √ | ' ' | 存储公式 |
| 3 | fgroupid | fgroupid | int8 | 64 |  | √ | 0 |  |
| 4 | ftimedeviationdirection | 时间偏移方向 | varchar | 100 |  | √ | ' ' | 时间偏移方向,枚举: + :向前 |
| 5 | fdescribe | 描述 | varchar | 510 |  | √ | ' ' | 描述 |
| 6 | fisvariable | 是否变量 | bpchar | 1 |  | √ | ' ' | 是否变量 |
| 7 | ffieldid | 字段id | varchar | 100 |  | √ | ' ' | 字段id |
| 8 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 9 | fstatus | 数据状态 | varchar | 30 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 10 | ffilterjson | ffilterjson | varchar | 100 |  | √ | ' ' |  |
| 11 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 12 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 13 | ftimedeviationtype | 计算周期 | varchar | 100 |  | √ | ' ' | 计算周期,枚举: 1 :月度 2 :季度 3 :半年度 4 :年度 |
| 14 | fpreset | 系统预设 | bpchar | 1 |  | √ | ' ' | 系统预设,枚举: 1 :是 0 :否 |
| 15 | ftaxareagroup | 税收辖区 | int8 | 64 |  | √ | 0 | [税收辖区 bastax_taxareagroup](../basedata_files/bastax_taxareagroup.md) |
| 16 | fformula | 表达式 | varchar | 2000 |  | √ | ' ' | 表达式 |
| 17 | fbottom | 是否底层 | bpchar | 1 |  | √ | ' ' | 是否底层 |
| 18 | ftimedeviationcount | 元素计算偏移月份数 | varchar | 100 |  | √ | ' ' | 元素计算偏移月份数,枚举: 0 :0 1 :1 2 :2 3 :3 4 :4 5 :5 6 :6 7 :7 8 :8 9 :9 10 :10 11 :11 12 :12 |
| 19 | frisktimedeviationtype | 风险运行时间偏移 | varchar | 50 |  | √ | ' ' | 风险运行时间偏移,枚举: 0 :本期 1 :上年同期 2 :上期 |
| 20 | ftaxtype | 税种 | int8 | 64 |  | √ | 0 | [税种 bd_taxcategory](../basedata_files/bd_taxcategory.md) |
| 21 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 22 | ftypevalue | 比例类型值 | bpchar | 1 |  | √ | ' ' | 比例类型值 |
| 23 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 24 | ftableid | ftableid | varchar | 100 |  | √ | ' ' |  |
| 25 | fformulaname | 表达式名称（已废弃） | varchar | 510 |  | √ | ' ' | 表达式名称（已废弃） |
| 26 | fdraftpurpose | 底稿用途 | varchar | 50 |  | √ | ' ' | 底稿用途,枚举: nssb :纳税申报 sjjt :税金计提 sbjtThan :计提与申报比对 |
| 27 | fgathercount | 汇总取数 | bpchar | 1 |  | √ | '0' | 汇总取数 |
| 28 | ftimedeviation | 时间偏移 | varchar | 100 |  | √ | ' ' | 时间偏移 |
| 29 | fautorefresh | 自动刷新 | bpchar | 1 |  | √ | ' ' | 自动刷新 |
| 30 | ftype | 元素分类 | int8 | 64 |  | √ | 0 | [元素类型 tdm_element_type](../tdm_files/tdm_element_type.md) |
| 31 | fenable | 使用状态 | varchar | 30 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 2 :保存 |
| 32 | fformula_tag | fformula_tag | text | 0 |  |  | null |  |
| 33 | fnumber | 编码 | varchar | 60 |  | √ | ' ' | 编码 |
| 34 | fjson_tag | 存储公式_详情 | text | 0 |  |  | null | 存储公式_详情 |
| 35 | fformulaname_tag | fformulaname_tag | text | 0 |  |  | null |  |
| 36 | fdatatype | 取数方式 | varchar | 30 |  | √ | 'END' | 取数方式,枚举: END :周期内最后一月 START :周期内第一月 CUMULATIVE :截止当前周期本年累计 SUM :本周期合计 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_t_tdm_element_info |  | fnumber |
| 2 | t_tdm_element_info_pkey |  | fid |
