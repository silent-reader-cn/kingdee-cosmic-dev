# 打印模板-bos_printtemplate

## 打印模板-主表 t_meta_formdesign

- **表名称：** 打印模板-主表
- **表名：** t_meta_formdesign

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | varchar | 36 |  | √ | ' ' | id |
| 2 | fmodifierid | fmodifierid | varchar | 36 |  | √ | ' ' |  |
| 3 | fsubsysid | fsubsysid | int8 | 64 |  | √ | 0 |  |
| 4 | fisinherit | fisinherit | bpchar | 1 |  | √ | '1' |  |
| 5 | fmodeltype | 模型类型 | varchar | 50 |  | √ | ' ' | 模型类型,枚举: |
| 6 | fparentid | fparentid | varchar | 36 |  | √ | ' ' |  |
| 7 | fisv | fisv | varchar | 50 |  | √ | ' ' |  |
| 8 | finheritpath | 继承路径 | varchar | 300 |  | √ | ' ' | 继承路径 |
| 9 | fbizappid | fbizappid | varchar | 36 |  | √ | ' ' |  |
| 10 | fcreatedate | fcreatedate | timestamp | 0 |  |  | LOCALTIMESTAMP |  |
| 11 | fmasterid | fmasterid | varchar | 36 |  | √ | ' ' |  |
| 12 | ftype | ftype | bpchar | 1 |  | √ | '0' |  |
| 13 | fmodifydate | fmodifydate | timestamp | 0 |  |  | null |  |
| 14 | fisextended | fisextended | bpchar | 1 |  | √ | '1' |  |
| 15 | fnumber | 编码 | varchar | 36 |  | √ | ' ' | 编码 |
| 16 | fisvsign | fisvsign | varchar | 255 |  | √ | ' ' |  |
| 17 | fentityid | 实体元数据 | varchar | 36 |  | √ | ' ' | 实体元数据 bos_entitymeta |
| 18 | ftimestamp | ftimestamp | int8 | 64 |  | √ | 0 |  |
| 19 | fdata | fdata | text | 0 |  |  | null |  |
| 20 | findustry | findustry | int8 | 64 |  | √ | 0 |  |
| 21 | fenabled | fenabled | bpchar | 1 |  | √ | '1' |  |
| 22 | fistemplate | fistemplate | bpchar | 1 |  | √ | '0' |  |
| 23 | fversion | fversion | int8 | 64 |  | √ | 0 |  |

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

## 打印模板-多语言表 t_meta_formdesign_l

- **表名称：** 打印模板-多语言表
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
