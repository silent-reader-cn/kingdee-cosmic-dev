# 实体列表-bos_devpn_entitylist

## 实体列表-主表 t_meta_entitydesign

- **表名称：** 实体列表-主表
- **表名：** t_meta_entitydesign

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | varchar | 36 |  | √ | ' ' | id |
| 2 | fsubsysid | fsubsysid | int8 | 64 |  | √ | 0 |  |
| 3 | fmodeltype | 模型类型 | varchar | 50 |  | √ | ' ' | 模型类型,枚举: |
| 4 | fparentid | 父对象 | varchar | 36 |  | √ | ' ' | [实体元数据 bos_entitymeta](../mdl_files/bos_entitymeta.md) |
| 5 | fisv | fisv | varchar | 50 |  | √ | ' ' |  |
| 6 | finheritpath | finheritpath | varchar | 300 |  | √ | ' ' |  |
| 7 | fbizappid | 应用id | varchar | 36 |  | √ | ' ' | [业务应用实体 bos_devportal_bizapp](../mdl_files/bos_devportal_bizapp.md) |
| 8 | fcreatedate | fcreatedate | timestamp | 0 |  |  | LOCALTIMESTAMP |  |
| 9 | fmasterid | fmasterid | varchar | 36 |  | √ | ' ' |  |
| 10 | ftype | 类型 | bpchar | 1 |  | √ | '0' | 类型,枚举: |
| 11 | fmodifydate | 修改日期 | timestamp | 0 |  |  | null | 修改日期 |
| 12 | fnumber | 编码 | varchar | 36 |  | √ | ' ' | 编码 |
| 13 | ftimestamp | ftimestamp | int8 | 64 |  | √ | 0 |  |
| 14 | fdata | fdata | text | 0 |  |  | null |  |
| 15 | findustry | findustry | int8 | 64 |  | √ | 0 |  |
| 16 | fenabled | fenabled | bpchar | 1 |  | √ | '1' |  |
| 17 | fistemplate | fistemplate | bpchar | 1 |  | √ | '0' |  |
| 18 | fversion | fversion | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_meta_entitydesign_pkey |  | fid |
| 2 | t_meta_entitydesign_fnumber_key |  | fnumber |
| 3 | idx_meta_entdesign_masterid |  | fmasterid |

---

## 实体列表-多语言表 t_meta_entitydesign_l

- **表名称：** 实体列表-多语言表
- **表名：** t_meta_entitydesign_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | varchar | 36 |  | √ | ' ' |  |
| 2 | fname | 名称 | varchar | 200 |  | √ | ' ' | 名称 |
| 3 | fnumber | fnumber | varchar | 36 |  | √ | ' ' |  |
| 4 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 5 | fdata | fdata | text | 0 |  |  | null |  |
| 6 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_meta_entitydesign_l_fid_flocaleid_key |  | fid,flocaleid |
| 2 | idx_meta_entitydsgn_l_fid |  | fid,flocaleid |
| 3 | idx_meta_entitydsgn_l_number |  | fnumber,flocaleid |
| 4 | t_meta_entitydesign_l_fnumber_flocaleid_key |  | fnumber,flocaleid |
| 5 | t_meta_entitydesign_l_pkey |  | fpkid |
