# 元素（旧）-t_tdm_element_info

## 元素（旧）-多语言表 t_tdm_element_info_l

- **表名称：** 元素（旧）-多语言表
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

## 元素（旧）-主表 t_tdm_element_info

- **表名称：** 元素（旧）-主表
- **表名：** t_tdm_element_info

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fjson | 存储公式 | varchar | 510 |  | √ | ' ' | 存储公式 |
| 3 | fgroupid | 分组 | int8 | 64 |  | √ | 0 | [元素类型 tdm_element_type](../tdm_files/tdm_element_type.md) |
| 4 | ftimedeviationdirection | 时间偏移方向 | varchar | 100 |  | √ | ' ' | 时间偏移方向 |
| 5 | fdescribe | 描述 | varchar | 510 |  | √ | ' ' | 描述 |
| 6 | fisvariable | 是否变量 | bpchar | 1 |  | √ | ' ' | 是否变量 |
| 7 | ffieldid | ffieldid | varchar | 100 |  | √ | ' ' |  |
| 8 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 9 | fstatus | 数据状态 | varchar | 30 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 10 | ffilterjson | ffilterjson | varchar | 100 |  | √ | ' ' |  |
| 11 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 12 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 13 | ftimedeviationtype | 时间偏移跨度 | varchar | 100 |  | √ | ' ' | 时间偏移跨度 |
| 14 | fpreset | 是否预置 | bpchar | 1 |  | √ | ' ' | 是否预置 |
| 15 | ftaxareagroup | ftaxareagroup | int8 | 64 |  | √ | 0 |  |
| 16 | fformula | fformula | varchar | 2000 |  | √ | ' ' |  |
| 17 | fbottom | 是否底层 | bpchar | 1 |  | √ | ' ' | 是否底层 |
| 18 | ftimedeviationcount | 时间偏移量 | varchar | 100 |  | √ | ' ' | 时间偏移量 |
| 19 | frisktimedeviationtype | frisktimedeviationtype | varchar | 50 |  | √ | ' ' |  |
| 20 | ftaxtype | ftaxtype | int8 | 64 |  | √ | 0 |  |
| 21 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 22 | ftypevalue | 比例类型值 | bpchar | 1 |  | √ | ' ' | 比例类型值 |
| 23 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 24 | ftableid | ftableid | varchar | 100 |  | √ | ' ' |  |
| 25 | fformulaname | fformulaname | varchar | 510 |  | √ | ' ' |  |
| 26 | fdraftpurpose | fdraftpurpose | varchar | 50 |  | √ | ' ' |  |
| 27 | fgathercount | 汇总取数 | bpchar | 1 |  | √ | '0' | 汇总取数 |
| 28 | ftimedeviation | 时间偏移 | varchar | 100 |  | √ | ' ' | 时间偏移 |
| 29 | fautorefresh | 自动刷新 | bpchar | 1 |  | √ | ' ' | 自动刷新 |
| 30 | ftype | 元素类型 | int8 | 64 |  | √ | 0 | [元素类型 tdm_element_type](../tdm_files/tdm_element_type.md) |
| 31 | fenable | 使用状态 | varchar | 30 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 2 :保存 |
| 32 | fformula_tag | fformula_tag | text | 0 |  |  | null |  |
| 33 | fnumber | 编码 | varchar | 60 |  | √ | ' ' | 编码 |
| 34 | fjson_tag | 存储公式_详情 | text | 0 |  |  | null | 存储公式_详情 |
| 35 | fformulaname_tag | fformulaname_tag | text | 0 |  |  | null |  |
| 36 | fdatatype | fdatatype | varchar | 30 |  | √ | 'END' |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_t_tdm_element_info |  | fnumber |
| 2 | t_tdm_element_info_pkey |  | fid |
