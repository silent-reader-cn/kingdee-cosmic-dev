# 导入导出个性化设置数据-bos_impt_user_config_data

## 导入导出个性化设置数据-主表 t_bas_import_user_config

- **表名称：** 导入导出个性化设置数据-主表
- **表名：** t_bas_import_user_config

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 3 | fname | 名称 | varchar | 500 |  | √ | ' ' | 名称 |
| 4 | fexportautoline | 导出自动换行 | varchar | 50 |  | √ | ' ' | 导出自动换行 |
| 5 | fcomment | fcomment | varchar | 500 |  | √ | ' ' |  |
| 6 | fmonitorenable | 文本7 | varchar | 50 |  | √ | 'false' | 文本7 |
| 7 | fcreatetime | 创建时间 | timestamp | 0 |  | √ | LOCALTIMESTAMP | 创建时间 |
| 8 | fbizobject | 业务对象 | varchar | 36 |  | √ | ' ' | [主实体对象 bos_entityobject](../mdl_files/bos_entityobject.md) |
| 9 | fuser | 用户 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 10 | fexportalllogdata | fexportalllogdata | varchar | 50 |  | √ | ' ' |  |
| 11 | fexport_alllogdata | 导出Excel全量数据 | varchar | 50 |  | √ | ' ' | 导出Excel全量数据 |
| 12 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 13 | fstatus | 数据状态 | bpchar | 1 |  | √ | 'Z' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 14 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 15 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 16 | fexportmultilang | 导出多语言 | varchar | 1024 |  | √ | ' ' | 导出多语言 |
| 17 | fexportsummaryline | 导出合计行 | varchar | 50 |  | √ | ' ' | 导出合计行 |
| 18 | fexportautofillsuperinfo | 导出自动填充上级信息 | varchar | 255 |  | √ | ' ' | 导出自动填充上级信息 |
| 19 | fexportatt | 导出附件 | varchar | 50 |  | √ | ' ' | 导出附件 |
| 20 | fenable | 使用状态 | bpchar | 1 |  | √ | '0' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 21 | fexportimg | 导出图片 | varchar | 50 |  | √ | ' ' | 导出图片 |
| 22 | fnumber | 编码 | varchar | 50 |  | √ | ' ' | 编码 |
| 23 | fexportcsv | 导出csv | varchar | 50 |  | √ | ' ' | 导出csv |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_bas_import_user_config |  | fid |
| 2 | t_bas_import_user_config_index |  | fbizobject,fuser |

---

## 导入导出个性化设置数据-多语言表 t_bas_import_user_config_l

- **表名称：** 导入导出个性化设置数据-多语言表
- **表名：** t_bas_import_user_config_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 500 |  | √ | ' ' | 名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_bas_import_user_config_l |  | fpkid |
| 2 | idx_bas_import_user_config_l |  | fid,flocaleid |
